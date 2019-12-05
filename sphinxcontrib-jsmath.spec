#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : sphinxcontrib-jsmath
Version  : 1.0.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/b2/e8/9ed3830aeed71f17c026a07a5097edcf44b692850ef215b161b8ad875729/sphinxcontrib-jsmath-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b2/e8/9ed3830aeed71f17c026a07a5097edcf44b692850ef215b161b8ad875729/sphinxcontrib-jsmath-1.0.1.tar.gz
Source99 : https://files.pythonhosted.org/packages/b2/e8/9ed3830aeed71f17c026a07a5097edcf44b692850ef215b161b8ad875729/sphinxcontrib-jsmath-1.0.1.tar.gz.asc
Summary  : A sphinx extension which renders display math in HTML via JavaScript
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-jsmath-license = %{version}-%{release}
Requires: sphinxcontrib-jsmath-python = %{version}-%{release}
Requires: sphinxcontrib-jsmath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================
===============================
sphinxcontrib-jsmath is a sphinx extension which renders display math in HTML
via JavaScript.

%package license
Summary: license components for the sphinxcontrib-jsmath package.
Group: Default

%description license
license components for the sphinxcontrib-jsmath package.


%package python
Summary: python components for the sphinxcontrib-jsmath package.
Group: Default
Requires: sphinxcontrib-jsmath-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-jsmath package.


%package python3
Summary: python3 components for the sphinxcontrib-jsmath package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sphinxcontrib-jsmath package.


%prep
%setup -q -n sphinxcontrib-jsmath-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554254436
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-jsmath
cp LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-jsmath/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-jsmath/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
