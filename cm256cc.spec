Name:           cm256cc
Version:        1.0.5
Release:        1%{?dist}
Summary:        some dependency from SDRangel

License:        GPLv3
URL:            https://github.com/f4exb/cm256cc
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  cmake gcc-c++ pkgconfig fftw-devel libusb-devel qt5-qtbase-devel qt5-qtmultimedia-devel qt5-qttools-devel boost-devel pulseaudio-libs-devel alsa-lib-devel mesa-libGL
Requires:       fftw libusb qt5-qtbase qt5-qtmultimedia qt5-qttools boost pulseaudio alsa-lib mesa-libGL

%description

%global debug_package %{nil}

%prep
%autosetup


%build
mkdir %{_builddir}/build && cd %{_builddir}/build && cmake -Wno-dev -DCMAKE_INSTALL_PREFIX=/opt/sdrangel/cm256cc %{_builddir}/%{name}-%{version}
%make_build


%install
rm -rf $RPM_BUILD_ROOT
cd %{_builddir}/build && %make_install


%files
/opt/sdrangel/cm256cc
#%license add-license-file-here
#%doc add-docs-here



%changelog
* Mon Apr 22 2019 Christopher Beck <beckus@beckus.eu>
- modified so that it builds
* Sun Apr 21 2019 Christopher Beck <beckus@beckus.eu>
- Initial generation
