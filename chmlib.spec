%define	major	0
%define	libname	%mklibname chm %{major}
%define devname %mklibname -d chm

Summary:	A library for dealing with Microsoft ITSS/CHM format files
Name:		chmlib
Version:	0.40
Release:	16
License:	GPLv2
Group:		System/Libraries
Url:		http://www.jedrea.com/chmlib/
Source0:	http://www.jedrea.com/chmlib/%{name}-%{version}.tar.bz2
Patch1:		chmlib-0.37-morearchs.patch
Provides:	libchm-bin

%description
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.
Right now, it is a very simple library, but sufficient for dealing with
all of the .chm files I've come across. Due to the fairly well-designed
indexing built into this particular file format, even a small library
is able to gain reasonably good performance indexing into ITSS archives.

Code runs on Linux, Windows, Solaris, and Irix.

%package -n	%{libname}
Summary:	A library for dealing with Microsoft ITSS/CHM format files
Group:		System/Libraries

%description -n	%{libname}
This package contains the shared library for %{name}.

%package -n	%{devname}
Summary:	A library for dealing with Microsoft ITSS/CHM format files
Group:		Development/Other
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{_lib}chm-static-devel

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%patch1 -p0 -b .more_archs

%build
%configure2_5x \
	--enable-static \
	--enable-examples

export CFLAGS="%{optflags} -DCHM_MT -DCHM_USE_PREAD -DCHM_USE_IO64 -L.libs"
export LDFLAGS="%{ldflags} -lpthread" 

%make

%install
install -d %{buildroot}{%{_libdir},%{_includedir}}
%makeinstall_std

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libchm.so.%{major}*

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
