Name:           ros-jade-mongodb-log
Version:        0.1.17
Release:        0%{?dist}
Summary:        ROS mongodb_log package

Group:          Development/Libraries
License:        GPLv2
URL:            http://ros.org/wiki/mongodb_log
Source0:        %{name}-%{version}.tar.gz

Requires:       libmongo-client-devel
Requires:       mongodb-devel
Requires:       python-pymongo
Requires:       ros-jade-mongodb-store
Requires:       ros-jade-rosgraph
Requires:       ros-jade-roslib
Requires:       ros-jade-rospy
Requires:       ros-jade-rostopic
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
BuildRequires:  libmongo-client-devel
BuildRequires:  mongodb-devel
BuildRequires:  openssl-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-mongodb-store
BuildRequires:  ros-jade-rosgraph
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-rostopic
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf

%description
The mongodb_log package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Sep 01 2015 Marc Hanheide <marc@hanheide.net> - 0.1.17-0
- Autogenerated by Bloom

* Tue Aug 04 2015 Marc Hanheide <marc@hanheide.net> - 0.1.16-0
- Autogenerated by Bloom

