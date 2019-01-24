Name:           ros-melodic-mongodb-log
Version:        0.5.0
Release:        1%{?dist}
Summary:        ROS mongodb_log package

Group:          Development/Libraries
License:        GPLv2
URL:            http://ros.org/wiki/mongodb_log
Source0:        %{name}-%{version}.tar.gz

Requires:       python-pymongo
Requires:       ros-melodic-mongodb-store
Requires:       ros-melodic-rosgraph
Requires:       ros-melodic-roslib
Requires:       ros-melodic-rospy
Requires:       ros-melodic-rostopic
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-tf
BuildRequires:  openssl-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-mongodb-store
BuildRequires:  ros-melodic-rosgraph
BuildRequires:  ros-melodic-roslib
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-rostopic
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-tf

%description
The mongodb_log package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Jan 24 2019 Marc Hanheide <marc@hanheide.net> - 0.5.0-1
- Autogenerated by Bloom

* Thu Jan 24 2019 Marc Hanheide <marc@hanheide.net> - 0.5.0-0
- Autogenerated by Bloom

