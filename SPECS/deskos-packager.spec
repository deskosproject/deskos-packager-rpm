Name:           deskos-packager
Version:        0.1.1
Release:        1%{?dist}
Summary:        Tools and files necessary for building DeskOS packages
Group:          Applications/Productivity

License:        GPLv3+
URL:            https://deskosproject.org
Source0:        COPYING
Source1:        dbs-koji.conf
Source2:        deskos-7-x86_64.cfg

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
%{__install} -m 0644 %{SOURCE1} %{buildroot}/etc/koji.conf.d/dbs-koji.conf

%{__mkdir_p} %{buildroot}/%{_bindir}
ln -sf %{_bindir}/koji %{buildroot}%{_bindir}/dbs

%{__mkdir_p} %{buildroot}/etc/mock/
%{__install} -m 0644 %{SOURCE2} %{buildroot}/etc/mock/deskos-7-x86_64.cfg

%files
%defattr(-,root,root,-)
%doc COPYING
%config /etc/koji.conf.d/dbs-koji.conf
%config /etc/mock/deskos-7-x86_64.cfg
%{_bindir}/dbs

%changelog
* Mon Sep 19 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1.1-1
- Changed serverca and url

* Mon Sep 12 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1.0-1
- Initial release
