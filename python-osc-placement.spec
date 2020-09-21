%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global library osc-placement
%global module osc_placement
%global with_doc 1

Name:       python-%{library}
Version:    2.1.0
Release:    1%{?dist}
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

%package -n python3-%{library}
Summary:    OpenStackClient plugin for the Placement service
%{?python_provide:%python_provide python2-%{library}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-setuptools
BuildRequires:  git

BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-subunit
BuildRequires:  python3-testrepository
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-keystoneauth1 >= 3.3.0
BuildRequires:  python3-openstackclient
BuildRequires:  python3-osc-lib >= 1.2.0
BuildRequires:  python3-stestr
BuildRequires:  python3-oslo-utils >= 3.37.0

Requires:   python3-pbr >= 2.0.0
Requires:   python3-six >= 1.10.0
Requires:   python3-keystoneauth1 >= 3.3.0
Requires:   python3-osc-lib >= 1.2.0
# We currently don't have 3.16.0, so setting >= 3.10.0
Requires:   python3-simplejson >= 3.16.0
Requires:   python3-oslo-utils >= 3.37.0

%description -n python3-%{library}
OpenStackClient plugin for the Placement service.

This is an OpenStackClient plugin, that provides CLI for the Placement service.
Python API binding is not implemented - Placement API consumers are encouraged
to use the REST API directly, CLI is provided only for convenience of users.


%package -n python3-%{library}-tests
Summary:    OpenStackClient plugin for the Placement service tests
Requires:   python3-%{library} = %{version}-%{release}

Requires:   python3-mock
Requires:   python3-oslotest
Requires:   python3-subunit
Requires:   python3-testrepository
Requires:   python3-stestr
Requires:   python3-openstackclient

%description -n python3-%{library}-tests
OpenStackClient plugin for the Placement service tests

This package contains the test files.


%if 0%{?with_doc}
%package -n python-%{library}-doc
Summary:    OpenStackClient plugin for the Placement service documentation

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme
BuildRequires: python3-cliff

%description -n python-%{library}-doc
OpenStackClient plugin for the Placement service.

This package contains the documentation.
%endif

%prep
%autosetup -n %{library}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
export PYTHONPATH=.
sphinx-build -W -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
export PYTHON=%{__python3}
stestr-3 run

%files -n python3-%{library}
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.egg-info
%exclude %{python3_sitelib}/%{module}/tests

%files -n python3-%{library}-tests
%license LICENSE
%{python3_sitelib}/%{module}/tests

%if 0%{?with_doc}
%files -n python-%{library}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
* Mon Sep 21 2020 RDO <dev@lists.rdoproject.org> 2.1.0-1
- Update to 2.1.0

