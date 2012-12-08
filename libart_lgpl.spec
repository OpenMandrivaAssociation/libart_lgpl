%define lib_major 2

%define lib_name %mklibname art_lgpl %{lib_major}
%define develname %mklibname -d art_lgpl

Summary:	Library for high-performance 2D graphics
Name:		libart_lgpl
Version:	2.3.21
Release:	7
License:	LGPL
Group:		System/Libraries
URL:		http://www.levien.com/libart/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libart_lgpl/%{name}-%{version}.tar.bz2

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
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d art_lgpl 2} < 2.3.21

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

%multiarch_binaries %{buildroot}%{_bindir}/libart2-config

%multiarch_includes %{buildroot}%{_includedir}/libart-2.0/libart_lgpl/art_config.h

%files -n %{lib_name}
%{_libdir}/libart_lgpl_2.so.%{lib_major}*

%files -n %{develname}
%{_bindir}/*-config
%{multiarch_bindir}/libart2-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Sat Nov 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.3.21-5
+ Revision: 733660
- added back multiarch workaround of a double line
- rebuild
- disabled static build
- removed .la files
- removed defattr
- removed old ldconfig scriptlets
- removed clean section
- cleaned up spec
- removed mkrel & BuildRoot

* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 2.3.21-4
+ Revision: 661985
- update fiel list

  + Oden Eriksson <oeriksson@mandriva.com>
    - multiarch fixes

* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 2.3.21-3
+ Revision: 660595
- fix multiarch usage

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.21-2mdv2011.0
+ Revision: 602520
- rebuild

* Thu Apr 01 2010 Götz Waschk <waschk@mandriva.org> 2.3.21-1mdv2010.1
+ Revision: 530672
- update to new version 2.3.21

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.20-5mdv2010.1
+ Revision: 520750
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.3.20-4mdv2010.0
+ Revision: 425515
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.3.20-3mdv2009.0
+ Revision: 222501
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.3.20-2mdv2008.1
+ Revision: 170944
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix spacing at top of description

* Wed Jan 30 2008 Götz Waschk <waschk@mandriva.org> 2.3.20-1mdv2008.1
+ Revision: 160181
- new version
- drop patch
- new devel name
- spec file cleanup

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2.3.19-3mdv2008.1
+ Revision: 150451
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Thu Mar 01 2007 Götz Waschk <waschk@mandriva.org> 2.3.19-2mdv2007.0
+ Revision: 130304
- fix header for C++

* Wed Feb 28 2007 Götz Waschk <waschk@mandriva.org> 2.3.19-1mdv2007.1
+ Revision: 127077
- new version

* Mon Feb 26 2007 Götz Waschk <waschk@mandriva.org> 2.3.18-1mdv2007.1
+ Revision: 125968
- new version

* Sun Feb 18 2007 Götz Waschk <waschk@mandriva.org> 2.3.17-5mdv2007.1
+ Revision: 122418
- rebuild

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.3.17-4mdv2007.1
+ Revision: 108674
- Import libart_lgpl

* Sun Jan 14 2007 G�tz Waschk <waschk@mandriva.org> 2.3.17-4mdv2007.1
- rebuild

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.3.17-4mdk
- Rebuild

* Sat Jul 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.3.17-3mdk
- fix provides on x86_64

* Mon Jan 31 2005 G�tz Waschk <waschk@linux-mandrake.com> 2.3.17-2mdk
- multiarch support

* Fri Jan 21 2005 Goetz Waschk <waschk@linux-mandrake.com> 2.3.17-1mdk
- New release 2.3.17

* Sat Jul 17 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.3.16-2mdk
- spec fixes

