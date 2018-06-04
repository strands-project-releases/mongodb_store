Name:           ros-indigo-mongodb-log
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS mongodb_log package

Group:          Development/Libraries
License:        GPLv2
URL:            http://ros.org/wiki/mongodb_log
Source0:        %{name}-%{version}.tar.gz

Requires:       python-pymongo
Requires:       ros-indigo-libmongocxx-ros
Requires:       ros-indigo-mongodb-store
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
BuildRequires:  openssl-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-libmongocxx-ros
BuildRequires:  ros-indigo-mongodb-store
BuildRequires:  ros-indigo-rosgraph
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostopic
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf

%description
The mongodb_log package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jun 04 2018 Marc Hanheide <marc@hanheide.net> - 0.4.2-0
- Autogenerated by Bloom

* Tue May 29 2018 Marc Hanheide <marc@hanheide.net> - 0.4.1-0
- Autogenerated by Bloom

* Wed May 23 2018 Marc Hanheide <marc@hanheide.net> - 0.4.0-0
- Autogenerated by Bloom

* Wed May 02 2018 Marc Hanheide <marc@hanheide.net> - 0.3.8-1
- Autogenerated by Bloom

* Wed May 02 2018 Marc Hanheide <marc@hanheide.net> - 0.3.8-0
- Autogenerated by Bloom

* Fri Sep 15 2017 Marc Hanheide <marc@hanheide.net> - 0.3.6-1
- Autogenerated by Bloom

* Fri Jun 23 2017 Marc Hanheide <marc@hanheide.net> - 0.1.30-1
- Autogenerated by Bloom

* Mon Jun 19 2017 Marc Hanheide <marc@hanheide.net> - 0.1.29-1
- Autogenerated by Bloom

* Wed Nov 09 2016 Marc Hanheide <marc@hanheide.net> - 0.1.28-1
- Autogenerated by Bloom

* Tue Nov 01 2016 Marc Hanheide <marc@hanheide.net> - 0.1.27-1
- Autogenerated by Bloom

* Tue Feb 23 2016 Marc Hanheide <marc@hanheide.net> - 0.1.22-1
- Autogenerated by Bloom

* Wed Oct 28 2015 Marc Hanheide <marc@hanheide.net> - 0.1.18-0
- Autogenerated by Bloom

* Tue Aug 04 2015 Marc Hanheide <marc@hanheide.net> - 0.1.16-0
- Autogenerated by Bloom

* Mon Feb 09 2015 Marc Hanheide <marc@hanheide.net> - 0.1.12-1
- Autogenerated by Bloom

* Thu Nov 06 2014 Marc Hanheide <marc@hanheide.net> - 0.1.6-1
- Autogenerated by Bloom

* Wed Oct 29 2014 Marc Hanheide <marc@hanheide.net> - 0.1.4-0
- Autogenerated by Bloom

* Tue Oct 21 2014 Marc Hanheide <marc@hanheide.net> - 0.1.3-1
- Autogenerated by Bloom

* Tue Oct 21 2014 Marc Hanheide <marc@hanheide.net> - 0.1.3-0
- Autogenerated by Bloom

* Tue Oct 21 2014 Marc Hanheide <marc@hanheide.net> - 0.1.2-0
- Autogenerated by Bloom

* Fri Oct 17 2014 Marc Hanheide <marc@hanheide.net> - 0.1.1-0
- Autogenerated by Bloom

* Thu Oct 16 2014 Marc Hanheide <marc@hanheide.net> - 0.1.0-0
- Autogenerated by Bloom

* Thu Oct 09 2014 Marc Hanheide <marc@hanheide.net> - 0.0.5-1
- Autogenerated by Bloom

* Thu Oct 09 2014 Marc Hanheide <marc@hanheide.net> - 0.0.5-0
- Autogenerated by Bloom

* Sat Sep 13 2014 Marc Hanheide <marc@hanheide.net> - 0.0.4-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Marc Hanheide <marc@hanheide.net> - 0.0.3-0
- Autogenerated by Bloom

