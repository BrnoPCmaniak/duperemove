Name:    duperemove
Version: 0.10
Release: 1%{?dist}
Summary: Simple tool for finding duplicated extents and submitting them for deduplication
URL:     https://github.com/markfasheh/duperemove
Source0: https://github.com/markfasheh/duperemove/archive/v0.10.tar.gz
License: GPLv2

BuildRequires: glib2-devel
BuildRequires: sqlite-devel >= 3

Requires: kernel >= 3.13
Requires: sqlite

%description
Simple tool for finding duplicated extents and submitting them for
deduplication. When given a list of files it will hash their contents on
a block by block basis and compare those hashes to each other, finding
and categorizing blocks that match each other. Duperemove can submit
those extents for deduplication using the Linux kernel extent-same ioctl.

%prep
%autosetup -n duperemove-0.10

%build
%make_build

%install
%make_install PREFIX=/usr MANDIR=%{_mandir}

%files
%doc README.md
%license LICENSE LICENSE.xxhash
%{_sbindir}/*
%{_mandir}/man8/*

%changelog
* Fri Jul 28 2017 Filip Dobrovolny <brnopcman@gmail.com> - 0.10-1
- Initial packaging.
