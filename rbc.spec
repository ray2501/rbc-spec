#
# spec file for package rbc
#

Name:           rbc
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  libX11-6
Requires:       tcl
Requires:       tk
License:        BSD 3-Clause
Group:          Development/Libraries/Tcl
Version:        0.1.1
Release:        0
Summary:        Refactored BLT Components
BuildRoot:      %{_tmppath}/rbc-%{version}-build
URL:            https://github.com/apnadkarni/rbctoolkit
Source0:        rbc-%{version}.tar.gz
Patch0:         configure.patch

%description
RBC is an extension to the Tk toolkit. It has BLT's vector, graph,
barchart, stripchart, winop, and eps components.

Now it is alpha release.

%package devel-static
Summary:        Development files for statically link RBC toolkit.
Group:          Development/Libraries/Tcl
Requires:       %{name} = %{version}

%description devel-static
This package holds the development files for statically linking RBC toolkit.

%prep
%setup -q -n rbc
%patch0

%build
autoconf
CFLAGS="%optflags -fno-strict-aliasing" \
%configure \
	--with-tcl=%_libdir \
	--with-tk=%_libdir
make

%install
make DESTDIR=%{buildroot} pkglibdir=%tclscriptdir/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README license.terms ChangeLog
%{_libdir}/librbc0.1.1.so
%tclscriptdir/%{name}%{version}

%files devel-static
%defattr(-,root,root,-)
/usr/include/rbcStubLib.c
%{_libdir}/librbcstub0.1.1.a

