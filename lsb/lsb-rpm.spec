# lsb.spec.in -- an rpm spec file templete for LSB package
# Epson Inkjet Printer Driver (ESC/P-R) for Linux
# Copyright (C) Seiko Epson Corporation 2011.
#  This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

%define pkg     epson-inkjet-printer-escpr
%define ver     1.1.0
%define rel     1

# used in RPM macro set for the LSB Driver Development Kit
%define drivername      epson-inkjet-printer-escpr
%define driverstr       epson-inkjet-printer-escpr
%define distribution    LSB
%define manufacturer    EPSON
%define supplier        %{drivername}
%define lsbver          3.2

%define extraversion    -%{rel}lsb%{lsbver}
%define supplierstr     Seiko Epson Corporation


Name: %{pkg}
Version: %{ver}
Release: %{rel}lsb%{lsbver}
Source0: %{name}-%{version}-%{release}.tar.gz
License: GPL
Vendor: Seiko Epson Corporation
URL: http://avasys.jp/english/linux_e/
Packager: Seiko Epson Corporation <linux-epson-inkjet@avasys.jp>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Group: Applications/System
Requires: lsb >= %{lsbver}
Summary: Epson Inkjet Printer Driver (ESC/P-R) for Linux

%description
This software is a filter program used with Common UNIX Printing
System (CUPS) from the Linux. This can supply the high quality print
with Seiko Epson Color Ink Jet Printers.

This product supports only EPSON ESC/P-R printers. This package can be
used for all EPSON ESC/P-R printers.

For detail list of supported printer, please refer to below site:
http://avasys.jp/english/linux_e/

# from RPM macro set for the LSB Driver Development Kit
%install_into_opt

# Packaging settings
%prep
%setup -q

%build
%configure \
        --with-cupsfilterdir=%{_cupsserverbin}/filter \
        --with-cupsppddir=%{_cupsppd}
make pkgdatadir=%{_datadir}

%install
rm -rf %{buildroot}
# Make directories
install -d %{buildroot}%{_cupsserverbin}/filter
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_datadir}
install -d %{buildroot}%{_docdir}
make install-strip DESTDIR=%{buildroot} pkgdatadir=%{_datadir}
install -m 644 README README.ja COPYING AUTHORS NEWS %{buildroot}%{_docdir}
rm -f %{buildroot}%{_libdirglob}/*.a
rm -f %{buildroot}%{_libdirglob}/*.la

# from RPM macro set for the LSB Driver Development Kit
%adjust_ppds

# keep buildroot tree for makelsbpkg.
# after you execute rpmbuild -bb, execute the following commands.
# # makelsbpkg %{name} \
#     --tagfile makelsbpkg-tags.xml \
#     --permfile makelsbpkg-perms.xml \
#     %{buildroot}.BAK
cp -a %{buildroot} %{buildroot}.BAK

# pre/post scripts
%pre
%create_opt_dirs

%post
/sbin/ldconfig
%set_ppd_links
%restart_cups

%postun
/sbin/ldconfig
%not_on_rpm_update
%remove_ppd_links
%restart_cups
%end_not_on_rpm_update

%clean
make clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_prefix}
