Name:           ros-indigo-mongodb-store-msgs
Version:        0.1.6
Release:        1%{?dist}
Summary:        ROS mongodb_store_msgs package

Group:          Development/Libraries
License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-message-runtime
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation

%description
The mongodb_store_msgs package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Nov 06 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.6-1
- Autogenerated by Bloom

* Wed Oct 29 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.4-0
- Autogenerated by Bloom

* Tue Oct 21 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.2-0
- Autogenerated by Bloom

* Tue Oct 21 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.3-0
- Autogenerated by Bloom

* Tue Oct 21 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.3-1
- Autogenerated by Bloom

* Fri Oct 17 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.1-0
- Autogenerated by Bloom

* Thu Oct 16 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.0-0
- Autogenerated by Bloom

* Thu Oct 09 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.0.5-1
- Autogenerated by Bloom

* Thu Oct 09 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.0.5-0
- Autogenerated by Bloom

* Sat Sep 13 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.0.4-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.0.3-0
- Autogenerated by Bloom

