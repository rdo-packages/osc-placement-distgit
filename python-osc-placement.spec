# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global library osc-placement
%global module osc_placement

Name:       python-%{library}
Version:    XXX
Release:    XXX
Summary:    OpenStackClient plugin for the Placement service
License:    ASL 2.0
URL:        https://github.com/openstack/osc-placement

Source0:    http://tarballs.openstack.org/%{library}/%{library}-%{upstream_version}.tar.gz

BuildArch:  noarch

%description
OpenStackClient plugin for the Placement service

This is an OpenStackClient plugin, that provides CLI for the Placement service.
Python API binding is not implemented - Placement API consumers are encouraged
to use the REST API directly, CLI is provided only for convenience of users.

%package -n python%{pyver}-%{library}
Summary:    OpenStackClient plugin for the Placement service
%{?python_provide:%python_provide python2-%{library}}

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr >= 2.0.0
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  git

BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-subunit
BuildRequires:  python%{pyver}-testrepository
BuildRequires:  python%{pyver}-six >= 1.10.0
BuildRequires:  python%{pyver}-keystoneauth1 >= 3.3.0
BuildRequires:  python%{pyver}-osc-lib >= 1.2.0

Requires:   python%{pyver}-pbr >= 2.0.0
Requires:   python%{pyver}-six >= 1.10.0
Requires:   python%{pyver}-keystoneauth1 >= 3.3.0
Requires:   python%{pyver}-osc-lib >= 1.2.0

%description -n python%{pyver}-%{library}
OpenStackClient plugin for the Placement service.

This is an OpenStackClient plugin, that provides CLI for the Placement service.
Python API binding is not implemented - Placement API consumers are encouraged
to use the REST API directly, CLI is provided only for convenience of users.


%package -n python%{pyver}-%{library}-tests
Summary:    OpenStackClient plugin for the Placement service tests
Requires:   python%{pyver}-%{library} = %{version}-%{release}

Requires:   python%{pyver}-mock
Requires:   python%{pyver}-oslotest
Requires:   python%{pyver}-subunit
Requires:   python%{pyver}-testrepository

%description -n python%{pyver}-%{library}-tests
OpenStackClient plugin for the Placement service tests

This package contains the test files.


%package -n python-%{library}-doc
Summary:    OpenStackClient plugin for the Placement service documentation

BuildRequires: python%{pyver}-sphinx
BuildRequires: python%{pyver}-oslo-sphinx

%description -n python-%{library}-doc
OpenStackClient plugin for the Placement service.

This package contains the documentation.

%prep
%autosetup -n %{library}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%{pyver_build}

# generate html docs
%{pyver_bin} setup.py build_sphinx
# remove the sphinx-build-%{pyver} leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{pyver_install}

%check
export PYTHON=%{pyver_bin}
%{pyver_bin} setup.py test

%files -n python%{pyver}-%{library}
%license LICENSE
%{pyver_sitelib}/%{module}
%{pyver_sitelib}/%{module}-*.egg-info
%exclude %{pyver_sitelib}/%{module}/tests

%files -n python%{pyver}-%{library}-tests
%license LICENSE
%{pyver_sitelib}/%{module}/tests

%files -n python-%{library}-doc
%license LICENSE
%doc doc/build/html README.rst

%changelog
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/osc-placement/commit/?id=fc563d37bceac78f053772e8822717bc7006a92f
