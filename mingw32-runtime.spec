%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

Name:           mingw32-runtime
Version:        3.15.2
Release:        %mkrel 3
Summary:        MinGW Windows cross-compiler runtime

License:        Public Domain
Group:          Development/Other
URL:            http://www.mingw.org/
Source0:        http://dl.sourceforge.net/sourceforge/mingw/mingwrt-%{version}-mingw32-src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 39-3
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-w32api

# Once this is installed, mingw32-bootstrap (binary bootstrapper) is no
# longer needed.
Obsoletes:      mingw32-runtime-bootstrap


%description
MinGW Windows cross-compiler runtime, base libraries.


%prep
%setup -q -n mingwrt-%{version}-mingw32


%build
MINGW32_CFLAGS="%{_mingw32_cflags} -I%{_mingw32_includedir}"
%{_mingw32_configure}
%{_mingw32_make}


%install
rm -rf $RPM_BUILD_ROOT

%{_mingw32_makeinstall}

# make install places these in nonstandard locations, so move them.
mkdir -p $RPM_BUILD_ROOT%{_mingw32_docdir}
mv $RPM_BUILD_ROOT%{_mingw32_prefix}/doc/* $RPM_BUILD_ROOT%{_mingw32_docdir}/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_mingw32_bindir}/*
%{_mingw32_docdir}/*
%{_mingw32_includedir}/*
%{_mingw32_libdir}/*
%{_mingw32_mandir}/man3/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.15.2-3mdv2011.0
+ Revision: 620357
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 3.15.2-2mdv2010.0
+ Revision: 439933
- rebuild

* Tue Feb 17 2009 Jérôme Soyer <saispo@mandriva.org> 3.15.2-1mdv2009.1
+ Revision: 341484
- New upstream release

* Fri Feb 06 2009 Jérôme Soyer <saispo@mandriva.org> 3.15.1-1mdv2009.1
+ Revision: 338047
- import mingw32-runtime


