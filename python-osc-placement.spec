%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

# Python3 support in OpenStack starts with version 3.5,
# which is only in Fedora 24+
%if 0%{?fedora} >= 24
%global with_python3 1
%endif


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

%package -n python2-%{library}
Summary:    OpenStackClient plugin for the Placement service
%{?python_provide:%python_provide python2-%{library}}

BuildRequires:  python2-devel
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python-setuptools
BuildRequires:  git

BuildRequires:  python2-mock
BuildRequires:  python2-oslotest
BuildRequires:  python2-subunit
BuildRequires:  python2-openstackclient
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-keystoneauth1 >= 3.3.0
BuildRequires:  python2-osc-lib >= 1.2.0

Requires:   python2-pbr >= 2.0.0
Requires:   python2-six >= 1.10.0
Requires:   python2-keystoneauth1 >= 3.3.0
Requires:   python2-osc-lib >= 1.2.0

%description -n python2-%{library}
OpenStackClient plugin for the Placement service.

This is an OpenStackClient plugin, that provides CLI for the Placement service.
Python API binding is not implemented - Placement API consumers are encouraged
to use the REST API directly, CLI is provided only for convenience of users.


%package -n python2-%{library}-tests
Summary:    OpenStackClient plugin for the Placement service tests
Requires:   python2-%{library} = %{version}-%{release}

Requires:   python2-mock
Requires:   python2-oslotest
Requires:   python2-subunit
Requires:   python2-openstackclient

%description -n python2-%{library}-tests
OpenStackClient plugin for the Placement service tests

This package contains the test files.


%package -n python-%{library}-doc
Summary:    OpenStackClient plugin for the Placement service documentation

BuildRequires: python2-sphinx
BuildRequires: python2-oslo-sphinx

%description -n python-%{library}-doc
OpenStackClient plugin for the Placement service.

This package contains the documentation.

%if 0%{?with_python3}
%package -n python3-%{library}
Summary:    OpenStackClient plugin for the Placement service
%{?python_provide:%python_provide python3-%{library}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-setuptools
BuildRequires:  git

BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-subunit
BuildRequires:  python3-openstackclient
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-keystoneauth1 >= 3.3.0
BuildRequires:  python3-osc-lib >= 1.2.0

Requires:   python3-pbr >= 2.0.0
Requires:   python3-six >= 1.10.0
Requires:   python3-keystoneauth1 >= 3.3.0
Requires:   python3-osc-lib >= 1.2.0

%description -n python3-%{library}
OpenStackClient plugin for the Placement service

This is an OpenStackClient plugin, that provides CLI for the Placement service.
Python API binding is not implemented - Placement API consumers are encouraged
to use the REST API directly, CLI is provided only for convenience of users.


%package -n python3-%{library}-tests
Summary:    OpenStackClient plugin for the Placement service tests
Requires:   python3-%{library} = %{version}-%{release}

Requires:   python3-mock
Requires:   python3-oslotest
Requires:   python3-subunit
Requires:   python3-openstackclient

%description -n python3-%{library}-tests
OpenStackClient plugin for the Placement service tests

This package contains the test files.

%endif # with_python3


%description
OpenStackClient plugin for the Placement service

This is an OpenStackClient plugin, that provides CLI for the Placement service.
Python API binding is not implemented - Placement API consumers are encouraged
to use the REST API directly, CLI is provided only for convenience of users.


%prep
%autosetup -n %{library}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif


%check
%if 0%{?with_python3}
%{__python3} setup.py test
rm -rf .testrepository
%endif
%{__python2} setup.py test

%files -n python2-%{library}
%license LICENSE
%{python2_sitelib}/%{module}
%{python2_sitelib}/%{module}-*.egg-info
%exclude %{python2_sitelib}/%{module}/tests

%files -n python2-%{library}-tests
%license LICENSE
%{python2_sitelib}/%{module}/tests

%files -n python-%{library}-doc
%license LICENSE
%doc doc/build/html README.rst

%if 0%{?with_python3}
%files -n python3-%{library}
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.egg-info
%exclude %{python3_sitelib}/%{module}/tests

%files -n python3-%{library}-tests
%license LICENSE
%{python3_sitelib}/%{module}/tests
%endif # with_python3

%changelog
