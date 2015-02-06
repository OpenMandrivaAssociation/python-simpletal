%define srcname SimpleTAL

Name:           python-simpletal
Version:        5.1
Release:        2

Summary:        An XML based template processor for TAL, TALES and METAL specifications

Group:          System/Libraries
License:        BSD
URL:            http://www.owlfish.com/software/simpleTAL/index.html
Source0:        http://www.owlfish.com/software/simpleTAL/downloads/SimpleTAL-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel

%description
SimpleTAL is a stand alone Python implementation of the TAL, TALES and METAL 
specifications used in Zope to power HTML and XML templates.


%prep
%setup -q -n %{srcname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}



%files
%defattr(-,root,root,-)
%doc Changes.txt LICENSE.txt README.txt examples/
%dir %{python_sitelib}/simpletal
%{python_sitelib}/simpletal/*.py
%{python_sitelib}/SimpleTAL-%{version}-py*.egg-info



%changelog
* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 4.3-1mdv2011.0
+ Revision: 636248
- update to new version 4.3

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 4.2-2mdv2011.0
+ Revision: 591782
- Rebuild

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 4.2-1mdv2010.1
+ Revision: 489193
- update to new version 4.2

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 4.1-3mdv2010.0
+ Revision: 442485
- rebuild

* Fri Dec 26 2008 Crispin Boylan <crisb@mandriva.org> 4.1-2mdv2009.1
+ Revision: 319400
- Rebuild for python2.6

* Thu Dec 04 2008 Crispin Boylan <crisb@mandriva.org> 4.1-1mdv2009.1
+ Revision: 309952
- Fix summary
- Based on redhat package
- create python-simpletal


