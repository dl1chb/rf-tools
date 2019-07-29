%global commit 4892ebbc04ef57dd6f603d3f4ece253d8c2bd571
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20190729
Name:           liquid-dsp
Version:        1.3.2
Release:        1.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:        Digital Signal Processing Library for Software-Defined Radios

License:        MIT
URL:            http://liquidsdr.org/
Source0:        https://github.com/jgaeddert/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# set soname ourselves as upstream doesn't
#Patch0:         soname-version.patch
# add autotooling as upstream doesn't
#Patch1:         autotools.patch
# fixes ppc64 altivec, other 64-bit problems. Patch by Dan Horák.
# https://github.com/jgaeddert/liquid-dsp/pull/136
#Patch1:         ppc64.patch
BuildRequires:  gcc fftw-libs-single autoconf

%define debug_package %{nil}

%description
Digital signal processing library for software-defined radios

%package -n %{name}-devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-devel
Digital signal processing library for software-defined radios

%prep
%autosetup -p1 -n %{name}-%{commit}
./bootstrap.sh

%build
%configure --exec_prefix=/
%make_build

%check
make check

%install
%make_install
#pushd ${RPM_BUILD_ROOT}/%{_libdir} > /dev/null 2>&1
#chmod a+x libliquid.so
#popd > /dev/null 2>&1

%ldconfig_scriptlets
%files
%license LICENSE
%{_libdir}/libliquid.so
%{_libdir}/libliquid.a


%files -n %{name}-devel
%{_includedir}/liquid/
%{_libdir}/libliquid.so


%changelog
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4.20180806git9658d81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug  15 2018 Matt Domsch <matt@domsch.com> 1.3.1-3.20180806git9658d81
- apply patch fixing ppc64, armv7hl build failures

* Tue Aug  14 2018 Matt Domsch <matt@domsch.com> 1.3.1-2.20180806git9658d81
- remove -faltivec from ppc64le build gcc args

* Tue Aug  7 2018 Matt Domsch <matt@domsch.com> 1.3.1-1.20180806git9658d81
- Initial Fedora packaging
