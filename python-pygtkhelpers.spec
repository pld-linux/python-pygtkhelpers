%define 	module	pygtkhelpers
Summary:	Library to assist the building of PyGTK applications
Name:		python-%{module}
Version:	0.4.3
Release:	1
License:	Other
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/pygtkhelpers/%{module}-%{version}.tar.gz
# Source0-md5:	1e2493dbbfed4042d35552b383f7a7cc
URL:		http://pypi.python.org/pypi/pygtkhelpers/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyGTKHelpers is a library to assist the building of PyGTK
applications. It is intentionally designed to be non-frameworky, and
blend well with your particular style of PyGTK development.

PyGTKHelpers provides a number of widespread features including: View
delegation, MVC, mixed GtkBuilder/Python views, widget proxying,
signal auto-connection, object-base lists and trees, a number of
helper widgets, utility functions for assisting creating new GObject
types, unit testing helpers and utilities to help debug PyGTK
applications.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt PKG-INFO
%dir %{py_sitescriptdir}/pygtkhelpers
%{py_sitescriptdir}/pygtkhelpers/*.py[co]
%dir %{py_sitescriptdir}/pygtkhelpers/debug
%{py_sitescriptdir}/pygtkhelpers/debug/*.py[co]
%dir %{py_sitescriptdir}/pygtkhelpers/ui
%{py_sitescriptdir}/pygtkhelpers/ui/*.py[co]
%dir %{py_sitescriptdir}/pygtkhelpers/ui/objectlist
%{py_sitescriptdir}/pygtkhelpers/ui/objectlist/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pygtkhelpers*.egg-info
%endif
