Name: redfish-finder 
Version: 0.4
Release: %autorelease
Summary: Utility for parsing SMBIOS information and configuring canonical BMC access
BuildArch: noarch

License: GPL-2.0-or-later
URL: https://github.com/nhorman/redfish-finder
Source: %url/archive/V%{version}/%{name}-%{version}.tar.gz

# Fix shabang python interpreter: https://github.com/nhorman/redfish-finder/commit/59fc5f964bf6971da552d059520d7798fccbd4fc
Patch0: redfish-finder-python3.patch

# Fix parsing HostConfig for DHCP: https://github.com/nhorman/redfish-finder/commit/581327fd45351dd53c06a26517bb7f92e19d8f31
Patch1: hostconfig-dhcp-parse.patch

BuildRequires: systemd-rpm-macros

Requires: python3
Requires: NetworkManager
Requires: dmidecode

%description
Scans Smbios information for type 42 management controller information, and uses
that to configure the appropriate network interface so that the BMC is
canonically accessible via the host name redfish-localhost

%prep
%autosetup

%build
#noop here

%install
install -D -p -m 0755 redfish-finder %{buildroot}/%{_bindir}/redfish-finder
install -D -p -m 0644 redfish-finder.1 %{buildroot}/%{_mandir}/man1/redfish-finder.1
install -D -p -m 0644 ./redfish-finder.service %{buildroot}/%{_unitdir}/redfish-finder.service

%post
%systemd_post redfish-finder.service

%preun
%systemd_preun redfish-finder.service

%postun
%systemd_postun_with_restart redfish-finder.service


%files
%doc README.md
%license COPYING
%{_bindir}/redfish-finder
%{_mandir}/man1/redfish-finder.1.*
%{_unitdir}/redfish-finder.service

%changelog
%autochangelog
