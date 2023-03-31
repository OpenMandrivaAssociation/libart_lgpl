%define url_ver %(echo %{version}|cut -d. -f1,2)
#MD the API should technically be added to the pkg names
#but this pkg maybe obsolete

%define major	2
%define libname	%mklibname art_lgpl %{major}
%define devname	%mklibname -d art_lgpl

Summary:	Library for high-performance 2D graphics
Name:		libart_lgpl
Version:	2.3.21
Release:	21
License:	LGPLv2
Group:		System/Libraries
Url:		http://www.levien.com/libart/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libart_lgpl/%{url_ver}/%{name}-%{version}.tar.bz2

%description
This is the LGPL'd component of libart.  Libart is a library for 
high-performance 2D graphics. All functions needed for
running the Gnome canvas, and for printing support, will be going in
here. The GPL'd component will be getting various enhanced functions
for specific applications.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This is the LGPL'd component of libart.  Libart is a library for 
high-performance 2D graphics. All functions needed for
running the Gnome canvas, and for printing support, will be going in
here. The GPL'd component will be getting various enhanced functions
for specific applications.

%package -n %{devname}
Summary:	%{summary}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
autoreconf -fiv

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libart_lgpl_2.so.%{major}*

%files -n %{devname}
%{_bindir}/*-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

