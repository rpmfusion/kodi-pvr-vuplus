%global commit 25c4883e7c73c71d77fd32c8e33284ed5f081287
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170419

%global kodi_addon pvr.vuplus
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        2.4.10
Release:        1%{?dist}
Summary:        Kodi's VuPlus client addon

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  platform-devel
BuildRequires:  tinyxml-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
Kodi's frontend for VU+/Enigma2 based settop boxes. Supports streaming of live
TV & recordings, EPG, timers.


%prep
%autosetup -n %{kodi_addon}-%{commit}

cp -p %{SOURCE1} .


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%license gpl-2.0.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Fri Apr 28 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:2.4.10-1
- Update to latest stable release for Kodi 17

* Sat Jul 23 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.11.13-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.10.7-1
- Initial RPM release
