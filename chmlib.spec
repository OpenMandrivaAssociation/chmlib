Name: chmlib
Version: 0.40
Release: 7
License: GPL
Group: System/Libraries
Summary: A library for dealing with Microsoft ITSS/CHM format files
URL: http://www.jedrea.com/chmlib/
Source0: http://www.jedrea.com/chmlib/%{name}-%{version}.tar.bz2
Patch1: chmlib-0.37-morearchs.patch
Provides: libchm-bin

%description
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.
Right now, it is a very simple library, but sufficient for dealing with
all of the .chm files I've come across. Due to the fairly well-designed
indexing built into this particular file format, even a small library
is able to gain reasonably good performance indexing into ITSS archives.

Code runs on Linux, Windows, Solaris, and Irix.

%files
%defattr(-,root,root)
%_bindir/*

#----------------------------------------------------------------------

%define	major 0
%define	libname %mklibname chm %{major}

%package -n	%{libname}
Summary:	A library for dealing with Microsoft ITSS/CHM format files
Group:		System/Libraries
Provides:	libchm = %{version}-%{release}

%description -n	%{libname}
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.
Right now, it is a very simple library, but sufficient for dealing with
all of the .chm files I've come across. Due to the fairly well-designed
indexing built into this particular file format, even a small library
is able to gain reasonably good performance indexing into ITSS archives.

%files -n %{libname}
%{_libdir}/libchm.so.%{major}*

#----------------------------------------------------------------------

%define libnamedev %mklibname -d chm

%package -n	%{libnamedev}
Summary: A library for dealing with Microsoft ITSS/CHM format files
Group: Development/Other
Provides: %{name}-devel = %{version}
Provides: libchm-devel = %{version}
Requires: %{libname} = %{version}
Obsoletes: %{mklibname -d chm 0}

%description -n %{libnamedev}
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.
Right now, it is a very simple library, but sufficient for dealing with
all of the .chm files I've come across. Due to the fairly well-designed
indexing built into this particular file format, even a small library
is able to gain reasonably good performance indexing into ITSS archives.

%files -n %{libnamedev}
%{_includedir}/*.h
%{_libdir}/*.so

#----------------------------------------------------------------------

%define libnamedevstat %mklibname -d -s chm

%package -n	%{libnamedevstat}
Summary: A library for dealing with Microsoft ITSS/CHM format files
Group: Development/Other
Provides: %{name}-static-devel = %{version}
Provides: libchm-static-devel = %{version}
Requires: %{libnamedev} = %{version}
Obsoletes: %{mklibname -d chm 0}

%description -n %{libnamedevstat}
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.
Right now, it is a very simple library, but sufficient for dealing with
all of the .chm files I've come across. Due to the fairly well-designed
indexing built into this particular file format, even a small library
is able to gain reasonably good performance indexing into ITSS archives.

%files -n %{libnamedevstat}
%{_libdir}/*.a

#----------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch1 -p0 -b .more_archs

%build
%configure2_5x \
	--enable-examples

export CFLAGS="%{optflags} -DCHM_MT -DCHM_USE_PREAD -DCHM_USE_IO64 -L.libs"
export LDFLAGS="%{ldflags} -lpthread" 

%make

%install
install -d %{buildroot}{%{_libdir},%{_includedir}}
%makeinstall_std
install -m644 src/.libs/libchm.a %{buildroot}%{_libdir}/libchm.a



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.40-5mdv2011.0
+ Revision: 663372
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.40-4mdv2011.0
+ Revision: 603829
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.40-3mdv2010.1
+ Revision: 518989
- rebuild

* Wed Jul 29 2009 Helio Chissini de Castro <helio@mandriva.com> 0.40-2mdv2010.0
+ Revision: 404419
- Reduce insanity in package build
- Make proper libnames obsoleting old devel with soname
- Enable examples that provides usefull utilities

* Sun Jun 21 2009 Oden Eriksson <oeriksson@mandriva.com> 0.40-1mdv2010.0
+ Revision: 387945
- 0.40
- rediffed P0

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.39-4mdv2009.1
+ Revision: 316515
- it's %%{ldflags}, not %%{rpmldflags}

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.39-3mdv2009.0
+ Revision: 220571
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.39-2mdv2008.1
+ Revision: 136304
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 0.39-2mdv2008.0
+ Revision: 75829
- Rebuild


* Thu Jan 25 2007 Götz Waschk <waschk@mandriva.org> 0.39-1mdv2007.0
+ Revision: 113083
- new version
- unpack patch

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org> 0.38-2mdv2007.0
+ Revision: 53042
- rebuild
- Import chmlib

* Fri Jul 21 2006 Emmanuel Andry <eandry@mandriva.org> 0.38-1mdv2007.0
- 0.38
- better url
- url for source

* Thu Jun 08 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.37.4-3mdv2007.0
- fix P1 to fix build on other archs (based on PLD's patch)

* Thu Apr 20 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.37.4-2mdk
- patch1: fix ppc build

* Thu Mar 23 2006 Lenny Cartier <lenny@mandriva.com> 0.37.4-1mdk
- 0.37.4

* Thu Oct 27 2005 Götz Waschk <waschk@mandriva.org> 0.37-1mdk
- fix build
- New release 0.37

* Sat Sep 10 2005 Götz Waschk <waschk@mandriva.org> 0.36-1mdk
- drop patch
- New release 0.36

* Fri Apr 22 2005 Oden Eriksson <oeriksson@mandriva.com> 0.35-2mdk
- added P0 from debian to make it compile on x86_64
- used different make flags

* Fri Jul 30 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.35-1mdk
- 0.35
- compile with $RPM_OPT_FLAGS
- cosmetics

* Wed Jun 02 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.33-1mdk
- 0.33
- bzip2 source
- remove patch0, use make macro instead

