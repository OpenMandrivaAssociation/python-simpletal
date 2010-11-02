%define srcname SimpleTAL

Name:           python-simpletal
Version:        4.2
Release:        %mkrel 2

Summary:        An XML based template processor for TAL, TALES and METAL specifications

Group:          System/Libraries
License:        BSD
URL:            http://www.owlfish.com/software/simpleTAL/index.html
Source0:        http://www.owlfish.com/software/simpleTAL/downloads/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel

%description
SimpleTAL is a stand alone Python implementation of the TAL, TALES and METAL  specifications  used in Zope to power HTML and XML templates.


%prep
%setup -q -n %{srcname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes.txt LICENSE.txt README.txt examples/
%dir %{python_sitelib}/simpletal
%{python_sitelib}/simpletal/*.py
%{python_sitelib}/SimpleTAL-%{version}-py*.egg-info

