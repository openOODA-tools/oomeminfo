Name:           oomeminfo
Version:        0.1.0
Release:        1%{?dist}
Summary:        Parses /proc/meminfo to report HugePages, Dirty pages, and ZRAM status.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomeminfo
Source0:        oomeminfo-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomeminfo is a sovereign, capability-bounded DETAILED RAM written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomeminfo
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomeminfo-uninstall

%files
/usr/bin/oomeminfo
/usr/bin/oomeminfo-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
