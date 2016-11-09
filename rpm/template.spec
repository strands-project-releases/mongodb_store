Name:           ros-indigo-mongodb-store-msgs
Version:        0.1.28
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
* Wed Nov 09 2016 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.28-1
- Autogenerated by Bloom

* Tue Nov 01 2016 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.27-1
- Autogenerated by Bloom

* Tue Feb 23 2016 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.22-1
- Autogenerated by Bloom

* Wed Oct 28 2015 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.18-0
- Autogenerated by Bloom

* Tue Aug 04 2015 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.16-0
- Autogenerated by Bloom

* Mon Feb 09 2015 Nick Hawes <n.a.hawes@cs.bham.ac.uk> - 0.1.12-1
- Autogenerated by Bloom

