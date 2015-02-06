Summary:	An avahi plugin for gmpc
Name:		gmpc-avahi
Version:	0.20.0
Release:	4
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//gmpc-plugins-avahi
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	libxml2-devel
BuildRequires:	libavahi-glib-devel
BuildRequires:	libavahi-client-devel
BuildRequires:	gmpc-devel >= 0.15.98
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	intltool
Requires:	gmpc

%description
An avahi plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/avahiplugin.so


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-2mdv2011.0
+ Revision: 610902
- rebuild

* Mon Apr 05 2010 Funda Wang <fwang@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 531603
- update to new version 0.20.0

* Sat Dec 26 2009 Funda Wang <fwang@mandriva.org> 0.19.0-1mdv2010.1
+ Revision: 482400
- BR intltool
- New version 0.19.0

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 0.18.0-1mdv2010.0
+ Revision: 379380
- New version 0.18.0

* Mon Dec 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.17.0-1mdv2009.1
+ Revision: 321123
- update to new version 0.17.0

* Wed Dec 03 2008 Funda Wang <fwang@mandriva.org> 0.16.0-1mdv2009.1
+ Revision: 309572
- move plugins

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - fix file list
    - update to new version 0.16.0

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.15.5.0-3mdv2009.0
+ Revision: 246270
- rebuild

* Wed Jan 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.15.5.0-1mdv2008.1
+ Revision: 160346
- add spec file
- add source
- Created package structure for gmpc-avahi.

