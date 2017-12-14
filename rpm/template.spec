Name:           ros-kinetic-mongodb-log
Version:        0.3.7
Release:        0%{?dist}
Summary:        ROS mongodb_log package

Group:          Development/Libraries
License:        GPLv2
URL:            http://ros.org/wiki/mongodb_log
Source0:        %{name}-%{version}.tar.gz

Requires:       python-pymongo
Requires:       ros-kinetic-libmongocxx-ros
Requires:       ros-kinetic-mongodb-store
Requires:       ros-kinetic-rosgraph
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rostopic
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
BuildRequires:  openssl-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-libmongocxx-ros
BuildRequires:  ros-kinetic-mongodb-store
BuildRequires:  ros-kinetic-rosgraph
BuildRequires:  ros-kinetic-roslib
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-rostopic
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf

%description
The mongodb_log package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Dec 14 2017 Marc Hanheide <marc@hanheide.net> - 0.3.7-0
- Autogenerated by Bloom

* Fri Sep 15 2017 Marc Hanheide <marc@hanheide.net> - 0.3.6-0
- Autogenerated by Bloom

