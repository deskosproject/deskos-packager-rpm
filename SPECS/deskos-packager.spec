Name:           deskos-packager
Version:        0.2.0
Release:        1%{?dist}
Summary:        Tools and files necessary for building DeskOS packages
Group:          Applications/Productivity

License:        GPLv3+
URL:            https://deskosproject.org
Source0:        COPYING
Source1:        deskos.conf
Source2:        deskos-7-x86_64.cfg
Source3:        RPM-GPG-KEY-DeskOS-7

Requires:       curl
Requires:       koji
Requires:       mock
Requires:       openssh-clients
Requires:       redhat-rpm-config
Requires:       rpm-build
Requires:       rpmdevtools
Requires:       rpmlint

BuildArch:      noarch

%description
Tools to help set up a DeskOS packaging environment

%prep
cp %{SOURCE0} .

%build
# Nothing here

%install
%{__mkdir_p} %{buildroot}/etc/koji.conf.d/
%{__install} -m 0644 %{SOURCE1} %{buildroot}/etc/koji.conf.d/deskos.conf

%{__mkdir_p} %{buildroot}/%{_bindir}
ln -sf %{_bindir}/koji %{buildroot}%{_bindir}/koji-deskos

%{__mkdir_p} %{buildroot}/etc/mock/
%{__install} -m 0644 %{SOURCE2} %{buildroot}/etc/mock/deskos-7-x86_64.cfg

%{__mkdir_p} %{buildroot}/etc/pki/mock/
%{__install} -m 0644 %{SOURCE3} %{buildroot}/etc/pki/mock/RPM-GPG-KEY-DeskOS-7

%files
%defattr(-,root,root,-)
%doc COPYING
%config /etc/koji.conf.d/deskos.conf
%config /etc/mock/deskos-7-x86_64.cfg
%config /etc/pki/mock/RPM-GPG-KEY-DeskOS-7
%{_bindir}/koji-deskos

%changelog
* Mon Nov 14 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.2.0-1
- Use koji-deskos as binary name instead of dbs
- Change mock root to deskos-7-x86_64
- Add the DeskOS repo to mock

* Mon Sep 19 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1.1-1
- Changed serverca and url

* Mon Sep 12 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1.0-1
- Initial release
