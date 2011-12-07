## Makefile.am -- an automake template for a Makefile.in file
## EPSON ESC/P-R Printer Driver for Linux
## Copyright (C) 2000-2008 AVASYS CORPORATION.
## Copyright (C) Seiko Epson Corporation 2000-2008.
##  This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110, USA.

cupsfilterdir = $(CUPS_FILTER_DIR)
cupsfilter_PROGRAMS = \
	epson-escpr \
	epson-escpr-wrapper

epson_escpr_wrapper_CFLAGS = \
	-DCUPS_FILTER_NAME=\"epson-escpr\" \
	-DCUPS_FILTER_PATH=\"$(CUPS_FILTER_DIR)\"
epson_escpr_wrapper_SOURCES = \
	wrapper.c

epson_escpr_CFLAGS = \
	-I$(top_srcdir)/lib \
	-DPAPER_PATH=\"$(pkgdatadir)/paper_list.csv\"
epson_escpr_SOURCES = \
	filter.c \
	libprtX.h \
	debug.c debug.h \
	pips.h \
	pipsDef.h \
	optBase.h \
	str.c str.h \
	err.c err.h \
	csv.c csv.h \
	mem.c mem.h \
	def.h

epson_escpr_LDADD = \
	$(top_builddir)/lib/libescpr.la
