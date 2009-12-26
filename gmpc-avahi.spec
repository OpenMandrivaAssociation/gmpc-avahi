Summary:	An avahi plugin for gmpc
Name:		gmpc-avahi
Version:	0.19.0
Release:	%mkrel 1
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
An avahi plugin for gmpc.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/avahiplugin.la
%{_libdir}/gmpc/plugins/avahiplugin.so
