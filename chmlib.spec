%define	name	chmlib
%define	version	0.39
%define	release	%mkrel 3

%define	oname	chm
%define	major	0
%define	libname	%mklibname %{oname} %{major}

Summary:	A library for dealing with Microsoft ITSS/CHM format files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Source0:	http://freshmeat.net/redir/chmlib/22229/url_tgz/%{name}-%{version}.tar.bz2
Patch1:		chmlib-0.37-morearchs.patch
URL:		http://freshmeat.net/redir/chmlib/22229/url_homepage/chmlib
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Provides:	%{name} = %{version}-%{release}
Provides:	lib%{oname} = %{version}-%{release}

%description -n	%{libname}
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.
Right now, it is a very simple library, but sufficient for dealing with
all of the .chm files I've come across. Due to the fairly well-designed
indexing built into this particular file format, even a small library
is able to gain reasonably good performance indexing into ITSS archives.

%package -n	%{libname}-devel
Summary:	A library for dealing with Microsoft ITSS/CHM format files
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{oname}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{libname}-devel
CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.
Right now, it is a very simple library, but sufficient for dealing with
all of the .chm files I've come across. Due to the fairly well-designed
indexing built into this particular file format, even a small library
is able to gain reasonably good performance indexing into ITSS archives.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .more_archs

%build
%configure2_5x
%make CFLAGS="%{optflags} -DCHM_MT -DCHM_USE_PREAD -DCHM_USE_IO64 -L.libs" \
    LDFLAGS="%{rpmldflags} -lpthread" CC="%{__cc}" LD="%{__cc}"

%install
rm -rf %{buildroot}
install -d %{buildroot}{%{_libdir},%{_includedir}}
%makeinstall_std
install -m644 src/.libs/libchm.a %{buildroot}%{_libdir}/libchm.a
#gw broken symlink
ln -sf libchm.so.0.0.0 %{buildroot}%{_libdir}/libchm.so

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la



