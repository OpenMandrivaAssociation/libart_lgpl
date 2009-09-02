%define lib_major 2

%define lib_name %mklibname art_lgpl %{lib_major}
%define develname %mklibname -d art_lgpl

Summary: Library for high-performance 2D graphics
Name: libart_lgpl
Version: 2.3.20
Release: %mkrel 4
Source0: http://ftp.gnome.org/pub/GNOME/sources/libart_lgpl/%{name}-%{version}.tar.bz2
License: LGPL
URL: http://www.levien.com/libart/
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

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

%package -n %develname
Summary:	%{summary}
Group:		Development/GNOME and GTK+
Provides:	art_lgpl-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d art_lgpl 2
Requires:   pkgconfig >= 0.8
Requires:   %{lib_name} = %{version}-%{release}


%description -n %develname
This is the LGPL'd component of libart.  Libart is a library for 
high-performance 2D graphics. All functions needed for
running the Gnome canvas, and for printing support, will be going in
here. The GPL'd component will be getting various enhanced functions
for specific applications.


%prep
%setup -q

%build


%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
%multiarch_binaries %buildroot%_bindir/*-config
%multiarch_includes %buildroot%_includedir/libart-2.0/libart_lgpl/art_config.h

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/libart_lgpl_2.so.%{lib_major}*

%files -n %develname
%defattr(-,root,root)
%{_bindir}/*-config
%{_bindir}/*/libart2-config
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


