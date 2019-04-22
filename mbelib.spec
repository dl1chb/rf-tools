Name:           mbelib
Version:        1.3.0
Release:        1%{?dist}
Summary:        some dependency from SDRangel

License:        GPLv3
URL:            https://github.com/szechyjs/mbelib
# to get the sources for this, clone the git repo and checkout the tag v1.3.0, name the foler mbelib-1.3.0
# then, create the tarball in you SOURCES-directory using tar cfj mbelib-1.3.0.tar.bz2 mbelib-1.3.0
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  cmake gcc-c++ pkgconfig fftw-devel libusb-devel qt5-qtbase-devel qt5-qtmultimedia-devel qt5-qttools-devel boost-devel pulseaudio-libs-devel alsa-lib-devel mesa-libGL
Requires:       fftw libusb qt5-qtbase qt5-qtmultimedia qt5-qttools boost pulseaudio alsa-lib mesa-libGL

%description

%global debug_package %{nil}

%prep
%autosetup


%build
mkdir %{_builddir}/build && cd %{_builddir}/build && cmake -Wno-dev -DCMAKE_INSTALL_PREFIX=/opt/sdrangel/mbelib %{_builddir}/%{name}-%{version}
%make_build


%install
rm -rf $RPM_BUILD_ROOT
cd %{_builddir}/build && %make_install


%files
/opt/sdrangel/mbelib
#%license add-license-file-here
#%doc add-docs-here



%changelog
* Mon Apr 22 2019 Christopher Beck <beckus@beckus.eu>
- Initial generation
