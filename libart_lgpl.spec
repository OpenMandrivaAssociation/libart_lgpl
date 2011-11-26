%define lib_major 2

%define lib_name %mklibname art_lgpl %{lib_major}
%define develname %mklibname -d art_lgpl

Summary: Library for high-performance 2D graphics
Name: libart_lgpl
Version: 2.3.21
Release: 5
License: LGPL
Group: System/Libraries
URL: http://www.levien.com/libart/
Source0: http://ftp.gnome.org/pub/GNOME/sources/libart_lgpl/%{name}-%{version}.tar.bz2

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

%package -n %{develname}
Summary:	%{summary}
Group:		Development/GNOME and GTK+
Requires:   %{lib_name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d art_lgpl 2

%description -n %{develname}
This is the LGPL'd component of libart.  Libart is a library for 
high-performance 2D graphics. All functions needed for
running the Gnome canvas, and for printing support, will be going in
here. The GPL'd component will be getting various enhanced functions
for specific applications.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la

%multiarch_binaries %{buildroot}%{_bindir}/libart2-config

%multiarch_includes %{buildroot}%{_includedir}/libart-2.0/libart_lgpl/art_config.h

%files -n %{lib_name}
%{_libdir}/libart_lgpl_2.so.%{lib_major}*

%files -n %{develname}
%{_bindir}/*-config
%{multiarch_bindir}/libart2-config
%{_includedir}/*
%dir %{multiarch_includedir}/libart-2.0
%dir %{multiarch_includedir}/libart-2.0/libart_lgpl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

