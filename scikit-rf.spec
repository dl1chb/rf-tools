# Created by pyp2rpm-3.3.2
%global pypi_name scikit-rf

Name:           python-%{pypi_name}
Version:        0.14.9
Release:        1%{?dist}
Summary:        Object Oriented Microwave Engineering

License:        new BSD
URL:            http://www.scikit-rf.org
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3-future
BuildRequires:  python3-ipython
BuildRequires:  python3-matplotlib
BuildRequires:  python3-numpy
BuildRequires:  python3-pandas
BuildRequires:  python3-scipy
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-nbsphinx

%description
 sckit-rf is an open source approach to RF/Microwave engineering implemented in
the Python programming language.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-future
Requires:       python3-ipython
Requires:       python3-matplotlib
Requires:       python3-numpy
Requires:       python3-pandas
Requires:       python3-scipy
Requires:       python3-six
%description -n python3-%{pypi_name}
 sckit-rf is an open source approach to RF/Microwave engineering implemented in
the Python programming language.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%{python3_sitearch}/apps
%{python3_sitearch}/skrf
%{python3_sitearch}/scikit_rf-%{version}-py?.?.egg-info


%changelog
* Sun Apr 21 2019 Christopher Beck <beckus@beckus.eu> - 0.14.9-1
- changed BuildRequires and Requires to fedora packages
* Sun Apr 21 2019 Christopher Beck <beckus@beckus.eu> - 0.14.9-1
- Initial package.
