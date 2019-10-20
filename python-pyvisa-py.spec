# Created by pyp2rpm-3.3.2
%global pypi_name pyvisa-py

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Python VISA bindings for GPIB, RS232, and USB instruments

License:        MIT License
URL:            https://github.com/pyvisa/pyvisa-py
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/PyVISA-py-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyvisa) >= 1.8
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
PyVISA-py A PyVISA backend that implements a large part of the "Virtual
Instrument Software Architecture" (VISA_) in pure Python (with the help of some
nice cross platform libraries python packages!). Description --PyVISA started
as wrapper for the NI-VISA library and therefore you need to install National
Instruments VISA library in your system. This works most of the time, for most
people....

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(pyvisa) >= 1.8
%description -n python3-%{pypi_name}
PyVISA-py A PyVISA backend that implements a large part of the "Virtual
Instrument Software Architecture" (VISA_) in pure Python (with the help of some
nice cross platform libraries python packages!). Description --PyVISA started
as wrapper for the NI-VISA library and therefore you need to install National
Instruments VISA library in your system. This works most of the time, for most
people....

%package -n python-%{pypi_name}-doc
Summary:        pyvisa-py documentation
%description -n python-%{pypi_name}-doc
Documentation for pyvisa-py

%prep
%autosetup -n PyVISA-py-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/pyvisa_py-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sun Oct 06 2019 Christopher Beck <beckus@beckus.eu> - 0.3.1-1
- Initial package.