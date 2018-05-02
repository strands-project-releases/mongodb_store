#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Provides a service to store ROS message objects in a mongodb database in JSON.
"""

import rospy
import actionlib
import pymongo
import os
import shutil
import subprocess
from mongodb_store_msgs.msg import  MoveEntriesAction, MoveEntriesFeedback
from datetime import *


import mongodb_store.util
MongoClient = mongodb_store.util.import_MongoClient()

class Replicator(object):
    def __init__(self):

        # don't start up until master is there
        use_daemon = rospy.get_param('mongodb_use_daemon', False)


        if use_daemon:
            self.master_db_host = rospy.get_param('mongodb_host')
            self.master_db_port = rospy.get_param('mongodb_port')        
            is_daemon_alive = mongodb_store.util.check_connection_to_mongod(self.master_db_host, self.master_db_port)
            if not is_daemon_alive:
                raise Exception("No Daemon?")
        else:
            if not mongodb_store.util.wait_for_mongo():
                raise Exception("No Datacentre?")
            self.master_db_host = rospy.get_param('mongodb_host')
            self.master_db_port = rospy.get_param('mongodb_port')        
        
        # this is just a test, connections are remade every call for long-running processes
        master, extras = self.make_connections()
        if master is None:
            raise Exception("No master datacentre found using mongodb_host and mongodb_port")

        self.server = actionlib.SimpleActionServer('move_mongodb_entries', MoveEntriesAction, self.move_entries, False)
        self.server.register_preempt_callback(self.do_cancel)
        self.restore_process = None
        self.dump_process = None
        self.server.start()
        self.dump_path = rospy.get_param("~replicator_dump_path", '/tmp/mongodb_replicator')
        rospy.loginfo("Replicator node dumping to %s" % self.dump_path)

        self.make_path()
        self.remove_path()


    def make_path(self):        
        if not os.path.isdir(self.dump_path):
            os.makedirs(self.dump_path) 
        elif not os.access(self.dump_path, os.W_OK):
            raise Exception('Cannot write to dump path: %s' % self.dump_path)
        
    def remove_path(self):
        shutil.rmtree(self.dump_path)

    def make_connections(self):
        master = None
        try:
            master = MongoClient(self.master_db_host, self.master_db_port)
        except pymongo.errors.ConnectionFailure, e:
            rospy.logwarn('Could not connect to master datacentre at %s:%s' % (mongodb_host, mongodb_port))
            return None, None


        extras = rospy.get_param('mongodb_store_extras', [])
        extra_clients = []
        for extra in extras:
            try:
                extra_clients.append(MongoClient(extra[0], extra[1]))
            except pymongo.errors.ConnectionFailure, e:
                rospy.logwarn('Could not connect to extra datacentre at %s:%s' % (extra[0], extra[1]))


        rospy.loginfo('Replicating content from %s:%s to a futher %s datacentres', self.master_db_host, self.master_db_port, len(extra_clients))

        return master, extra_clients

    def move_entries(self, goal):

        # create place to put temp stuf
        self.make_path()
        
        # don't use the connections, just sanity check their existence
        master, extras = self.make_connections()
        
        if len(extras) == 0:
            rospy.logwarn('No datacentres to move to, not performing move')
            self.server.set_aborted()    
            return 

        completed = []
        feedback = MoveEntriesFeedback(completed=completed)
        
        less_time_time = rospy.get_rostime() - goal.move_before

        for collection in goal.collections.data:                    
            self.do_dump(collection, master, less_time_time, db=goal.database)

        self.do_restore(extras, db=goal.database)

        if goal.delete_after_move:  
            for collection in goal.collections.data:                    
                self.do_delete(collection, master, less_time_time, db=goal.database)

        # clean up
        self.remove_path()

        if self.server.is_preempt_requested():
            self.server.set_preempted()
        else:
            self.server.set_succeeded()

    def do_restore(self, extras, db='message_store'):       
        # restore collection to extras
        for extra in extras:            
            if self.server.is_preempt_requested():
                break
            rest_args = ['mongorestore',  '--host',  extra.host, '--port',  str(extra.port), self.dump_path]
            self.restore_process = subprocess.Popen(rest_args)
            self.restore_process.wait()


    def do_delete(self, collection, master, less_time_time=None, db='message_store'):       
        coll = master[db][collection]
        spec = None
        if less_time_time is not None:
            spec = {"_meta.inserted_at": { "$lt": datetime.utcfromtimestamp(less_time_time.to_sec())}}
        coll.remove(spec)



    def do_dump(self, collection, master, less_time_time=None, db='message_store'):       
        # dump collection

        # print 'dumping ', collection

        args = ['mongodump',  '--host',  master.host, '--port',  str(master.port), '--db', db, '--collection', collection, '-o', self.dump_path]

        if less_time_time is not None:
            # match only objects with an insterted data less than this
            args.append('--query')
            args.append('{ \"_meta.inserted_at\": { $lt: new Date(%s)}}' % (less_time_time.secs * 1000))

        # print args

        self.dump_process = subprocess.Popen(args)
        self.dump_process.wait()


    def do_cancel(self):
        if self.restore_process is not None and self.restore_process.poll() is None:
            rospy.loginfo("mongorestore process is being terminated...")
            self.restore_process.terminate()
        if self.dump_process is not None and self.dump_process.poll() is None:
            rospy.loginfo("mongodump process is being terminated...")
            self.dump_process.terminate()
        if self.restore_process is not None:
            self.restore_process.wait()
        if self.dump_process is not None:
            self.dump_process.wait()

if __name__ == '__main__':
    rospy.init_node("mongodb_replicator")

    store = Replicator()
    
    rospy.spin()
