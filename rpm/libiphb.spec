Name:       libiphb
Summary:    API for IP Heartbeat service
Version:    1.2.7
Release:    0
License:    LGPLv2+
URL:        https://git.sailfishos.org/mer-core/libiphb
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.24
BuildRequires:  pkgconfig(dbus-1)  >= 1.8
BuildRequires:  pkgconfig(dsme) >= 0.65.0
BuildRequires:  pkgconfig(mce) >= 1.12.3

%description
This package contains C API for using IP Heartbeat service.


%package devel
Summary:    Development files for IP Heartbeat service
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains C headers for the IP Heartbeat API.


%package tests
Summary:    Tests package for IP Heartbeat service
Requires:   %{name} = %{version}-%{release}

%description tests
Tests package to test IP Heartbeat functionality.


%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.


%prep
%autosetup -n %{name}-%{version}

%build
unset LD_AS_NEEDED
./verify_version.sh
chmod a+x autogen.sh
./autogen.sh
chmod a+x configure

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
AUTHORS INSTALL README NEWS ChangeLog

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libiphb.so.*
%license COPYING

%files devel
%defattr(-,root,root,-)
%attr(644,root,root)%{_includedir}/iphbd/*
%{_libdir}/libiphb.so
%{_libdir}/pkgconfig/libiphb.pc

%files tests
%defattr(-,root,root,-)
/opt/tests/%{name}-tests

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
