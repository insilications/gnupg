#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6 (dshaw@jabberwocky.com)
#
Name     : gnupg
Version  : 2.1.21
Release  : 24
URL      : ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-2.1.21.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-2.1.21.tar.bz2
Source99 : ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-2.1.21.tar.bz2.sig
Summary  : zlib compression library
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-3.0 LGPL-3.0 NCSA
Requires: gnupg-bin
Requires: gnupg-doc
Requires: gnupg-data
Requires: gnupg-locales
BuildRequires : bzip2-dev
BuildRequires : libassuan-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libksba-dev
BuildRequires : libusb-compat-dev
BuildRequires : npth-dev
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(sqlite3)
Patch1: wakeups.patch

%description
The GNU Privacy Guard 2
=========================
Version 2.1
* INTRODUCTION
GnuPG is a complete and free implementation of the OpenPGP standard
as defined by RFC4880 (also known as PGP).  GnuPG enables encryption
and signing of data and communication, and features a versatile key
management system as well as access modules for public key
directories.

%package bin
Summary: bin components for the gnupg package.
Group: Binaries
Requires: gnupg-data

%description bin
bin components for the gnupg package.


%package data
Summary: data components for the gnupg package.
Group: Data

%description data
data components for the gnupg package.


%package doc
Summary: doc components for the gnupg package.
Group: Documentation

%description doc
doc components for the gnupg package.


%package locales
Summary: locales components for the gnupg package.
Group: Default

%description locales
locales components for the gnupg package.


%prep
%setup -q -n gnupg-2.1.21
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494881567
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
%configure --disable-static --disable-rpath
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1494881567
rm -rf %{buildroot}
%make_install
%find_lang gnupg2
## make_install_append content
ln -s gpg2 %{buildroot}/usr/bin/gpg
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/addgnupghome
/usr/bin/applygnupgdefaults
/usr/bin/dirmngr
/usr/bin/dirmngr-client
/usr/bin/gpg
/usr/bin/gpg-agent
/usr/bin/gpg-connect-agent
/usr/bin/gpg2
/usr/bin/gpgconf
/usr/bin/gpgparsemail
/usr/bin/gpgscm
/usr/bin/gpgsm
/usr/bin/gpgtar
/usr/bin/gpgv2
/usr/bin/kbxutil
/usr/bin/watchgnupg
/usr/libexec/gpg-check-pattern
/usr/libexec/gpg-preset-passphrase
/usr/libexec/gpg-protect-tool
/usr/libexec/gpg-wks-client
/usr/libexec/scdaemon

%files data
%defattr(-,root,root,-)
/usr/share/gnupg/distsigkey.gpg
/usr/share/gnupg/help.be.txt
/usr/share/gnupg/help.ca.txt
/usr/share/gnupg/help.cs.txt
/usr/share/gnupg/help.da.txt
/usr/share/gnupg/help.de.txt
/usr/share/gnupg/help.el.txt
/usr/share/gnupg/help.eo.txt
/usr/share/gnupg/help.es.txt
/usr/share/gnupg/help.et.txt
/usr/share/gnupg/help.fi.txt
/usr/share/gnupg/help.fr.txt
/usr/share/gnupg/help.gl.txt
/usr/share/gnupg/help.hu.txt
/usr/share/gnupg/help.id.txt
/usr/share/gnupg/help.it.txt
/usr/share/gnupg/help.ja.txt
/usr/share/gnupg/help.nb.txt
/usr/share/gnupg/help.pl.txt
/usr/share/gnupg/help.pt.txt
/usr/share/gnupg/help.pt_BR.txt
/usr/share/gnupg/help.ro.txt
/usr/share/gnupg/help.ru.txt
/usr/share/gnupg/help.sk.txt
/usr/share/gnupg/help.sv.txt
/usr/share/gnupg/help.tr.txt
/usr/share/gnupg/help.txt
/usr/share/gnupg/help.zh_CN.txt
/usr/share/gnupg/help.zh_TW.txt
/usr/share/gnupg/sks-keyservers.netCA.pem

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/gnupg/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files locales -f gnupg2.lang
%defattr(-,root,root,-)

