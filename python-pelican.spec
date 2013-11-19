Summary:	Static site generator that supports Markdown and reST syntax
Name:		python-pelican
Version:	3.3.0
Release:	2
License:	GPL v3
Group:		Applications
Source0:	https://github.com/getpelican/pelican/archive/%{version}.tar.gz
# Source0-md5:	00dc4b5b5c843cf3944d9482944353ea
URL:		http://blog.getpelican.com/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-Jinja2
Requires:	python-MarkupSafe
Requires:	python-Pygments
Requires:	python-Unidecode
Requires:	python-blinker
Requires:	python-docutils
Requires:	python-feedgenerator
Requires:	python-pytz
Requires:	python-six
Suggests:	python-Markdown
Suggests:	python-typogrify
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Static site generator that supports Markdown and reST syntax.

%prep
%setup -qn pelican-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.rst README.rst THANKS
%attr(755,root,root) %{_bindir}/pelican*
%dir %{py_sitescriptdir}/pelican
%{py_sitescriptdir}/pelican/*.py[co]
%{py_sitescriptdir}/pelican/tests
%{py_sitescriptdir}/pelican/themes
%{py_sitescriptdir}/pelican/tools
%{py_sitescriptdir}/*.egg-info

