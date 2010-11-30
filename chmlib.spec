Name: chmlib
Version: 0.40
Release: %mkrel 4
License: GPL
Group: System/Libraries
Summary: A library for dealing with Microsoft ITSS/CHM format files
URL: http://www.jedrea.com/chmlib/
Source0: http://www.jedrea.com/chmlib/%{name}-%{version}.tar.bz2
Patch1: chmlib-0.37-morearchs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%defattr(-,root,root)
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
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.la

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
%defattr(-,root,root)
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
rm -rf %{buildroot}
install -d %{buildroot}{%{_libdir},%{_includedir}}
%makeinstall_std
install -m644 src/.libs/libchm.a %{buildroot}%{_libdir}/libchm.a

%clean
rm -rf %{buildroot}

