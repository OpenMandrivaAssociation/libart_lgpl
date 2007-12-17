%define mdkversion		%(perl -pe '/(\\d+)\\.(\\d)\\.?(\\d)?/; $_="$1$2".($3||0)' /etc/mandriva-release)

%define lib_major 2

%if %mdkversion > 900
%define lib_name %mklibname art_lgpl %{lib_major}
%else 
%define lib_name libart_lgpl%{lib_major}
%endif

Summary: Libart is a library for high-performance 2D graphics
Name: libart_lgpl
Version: 2.3.19
Release: %mkrel 2
Source0: http://ftp.gnome.org/pub/GNOME/sources/libart_lgpl/%{name}-%{version}.tar.bz2
# fix header use with C++ (merged upstream)
Patch: libart_lgpl-2.3.19-extern-c.patch
License: LGPL
URL: http://www.levien.com/libart/
Group: System/Libraries

%description
This is the LGPL'd component of libart.  Libart is a library for 
high-performance 2D graphics. All functions needed for
running the Gnome canvas, and for printing support, will be going in
here. The GPL'd component will be getting various enhanced functions
for specific applications.

%package -n %{lib_name}
Summary:	%{summary}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{lib_name}

This is the LGPL'd component of libart.  Libart is a library for 
high-performance 2D graphics. All functions needed for
running the Gnome canvas, and for printing support, will be going in
here. The GPL'd component will be getting various enhanced functions
for specific applications.

%package -n %{lib_name}-devel
Summary:	%{summary}
Group:		Development/GNOME and GTK+
Provides:	art_lgpl-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:   pkgconfig >= 0.8
Requires:   %{lib_name} = %{version}-%{release}


%description -n %{lib_name}-devel

This is the LGPL'd component of libart.  Libart is a library for 
high-performance 2D graphics. All functions needed for
running the Gnome canvas, and for printing support, will be going in
here. The GPL'd component will be getting various enhanced functions
for specific applications.


%prep
%setup -q
%patch -p1 -b .extern-c

%build

%if %mdkversion <= 1000
#we don't use libtool 1.5 yet
%define __libtoolize /bin/true
%endif

%if %mdkversion >= 900
%configure2_5x
%else
%configure
%endif

%make

%install
rm -rf $RPM_BUILD_ROOT

%if %mdkversion >= 900
%makeinstall_std
%else
%makeinstall
%endif
%multiarch_binaries %buildroot%_bindir/*-config
%multiarch_includes %buildroot%_includedir/libart-2.0/libart_lgpl/art_config.h

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_bindir}/*-config
%{_bindir}/*/libart2-config
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


