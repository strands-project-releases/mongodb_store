Name:           ros-melodic-mongodb-store
Version:        0.5.2
Release:        0%{?dist}
Summary:        ROS mongodb_store package

Group:          Development/Libraries
License:        MIT
URL:            http://www.ros.org/wiki/mongodb_store
Source0:        %{name}-%{version}.tar.gz

Requires:       mongo-cxx-driver
Requires:       mongodb
Requires:       python-future
Requires:       python-pymongo
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-mongodb-store-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-topic-tools
BuildRequires:  mongo-cxx-driver
BuildRequires:  mongodb
BuildRequires:  openssl-devel
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-mongodb-store-msgs
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-topic-tools

%description
A package to support MongoDB-based storage and analysis for data from a ROS
system, eg. saved messages, configurations etc

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
* Mon Nov 11 2019 Nick Hawes <nickh@robots.ox.ac.uk> - 0.5.2-0
- Autogenerated by Bloom

* Fri Jun 28 2019 Nick Hawes <nickh@robots.ox.ac.uk> - 0.5.1-2
- Autogenerated by Bloom

* Fri Jun 28 2019 Nick Hawes <nickh@robots.ox.ac.uk> - 0.5.1-1
- Autogenerated by Bloom

* Thu Jan 24 2019 Nick Hawes <nickh@robots.ox.ac.uk> - 0.5.0-5
- Autogenerated by Bloom

* Thu Jan 24 2019 Nick Hawes <nickh@robots.ox.ac.uk> - 0.5.0-4
- Autogenerated by Bloom

* Thu Jan 24 2019 Nick Hawes <nickh@robots.ox.ac.uk> - 0.5.0-3
- Autogenerated by Bloom

* Thu Jan 24 2019 Nick Hawes <nickh@robots.ox.ac.uk> - 0.5.0-2
- Autogenerated by Bloom

* Thu Jan 24 2019 Nick Hawes <nickh@robots.ox.ac.uk> - 0.5.0-1
- Autogenerated by Bloom

* Thu Jan 24 2019 Nick Hawes <nickh@robots.ox.ac.uk> - 0.5.0-0
- Autogenerated by Bloom

