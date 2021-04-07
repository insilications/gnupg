#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x528897B826403ADA
#
Name     : gnupg
Version  : 2.3.0
Release  : 65
URL      : https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.3.0.tar.bz2
Source0  : https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.3.0.tar.bz2
Source1  : https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.3.0.tar.bz2.sig
Summary  : zlib compression library
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 NCSA
Requires: gnupg-bin = %{version}-%{release}
Requires: gnupg-data = %{version}-%{release}
Requires: gnupg-info = %{version}-%{release}
Requires: gnupg-libexec = %{version}-%{release}
Requires: gnupg-license = %{version}-%{release}
Requires: gnupg-locales = %{version}-%{release}
Requires: gnupg-man = %{version}-%{release}
Requires: pcsc-lite
Requires: pinentry
BuildRequires : bzip2-dev
BuildRequires : libassuan-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-extras
BuildRequires : libksba-dev
BuildRequires : libusb-dev
BuildRequires : npth-dev
BuildRequires : pcsc-lite
BuildRequires : pinentry
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(zlib)
Patch1: 0001-Warn-on-use-of-insecure-3DES-algo.patch

%description
The GNU Privacy Guard 2
=========================
Version 2.3 (devel)
* INTRODUCTION

%package bin
Summary: bin components for the gnupg package.
Group: Binaries
Requires: gnupg-data = %{version}-%{release}
Requires: gnupg-libexec = %{version}-%{release}
Requires: gnupg-license = %{version}-%{release}

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
Requires: gnupg-man = %{version}-%{release}
Requires: gnupg-info = %{version}-%{release}

%description doc
doc components for the gnupg package.


%package info
Summary: info components for the gnupg package.
Group: Default

%description info
info components for the gnupg package.


%package libexec
Summary: libexec components for the gnupg package.
Group: Default
Requires: gnupg-license = %{version}-%{release}

%description libexec
libexec components for the gnupg package.


%package license
Summary: license components for the gnupg package.
Group: Default

%description license
license components for the gnupg package.


%package locales
Summary: locales components for the gnupg package.
Group: Default

%description locales
locales components for the gnupg package.


%package man
Summary: man components for the gnupg package.
Group: Default

%description man
man components for the gnupg package.


%prep
%setup -q -n gnupg-2.3.0
cd %{_builddir}/gnupg-2.3.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617831457
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --disable-rpath
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1617831457
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnupg
cp %{_builddir}/gnupg-2.3.0/COPYING %{buildroot}/usr/share/package-licenses/gnupg/4bc05f7560e1e3ced08b71c93f10abe9e702c3ee
cp %{_builddir}/gnupg-2.3.0/COPYING.CC0 %{buildroot}/usr/share/package-licenses/gnupg/754becb73f3b288d7d8a62d8927a334cd38ac10b
cp %{_builddir}/gnupg-2.3.0/COPYING.GPL2 %{buildroot}/usr/share/package-licenses/gnupg/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/gnupg-2.3.0/COPYING.LGPL21 %{buildroot}/usr/share/package-licenses/gnupg/ac1b58bbd5bc11cacb7205718d620156ffd57c7e
cp %{_builddir}/gnupg-2.3.0/COPYING.LGPL3 %{buildroot}/usr/share/package-licenses/gnupg/bf58811df8e4261d540cc1872f42011872ca8f54
cp %{_builddir}/gnupg-2.3.0/COPYING.other %{buildroot}/usr/share/package-licenses/gnupg/366d4e13a65adbfd0f7972f4c8dc9891692e92e5
cp %{_builddir}/gnupg-2.3.0/tests/gpgscm/LICENSE.TinySCHEME %{buildroot}/usr/share/package-licenses/gnupg/ca474fc88304aab05401b27d158b3f9e0c1ffae6
%make_install
%find_lang gnupg2
## install_append content
ln -s gpg %{buildroot}/usr/bin/gpg2
## install_append end

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
/usr/bin/gpg-card
/usr/bin/gpg-connect-agent
/usr/bin/gpg-wks-client
/usr/bin/gpg-wks-server
/usr/bin/gpg2
/usr/bin/gpgconf
/usr/bin/gpgparsemail
/usr/bin/gpgscm
/usr/bin/gpgsm
/usr/bin/gpgsplit
/usr/bin/gpgtar
/usr/bin/gpgv
/usr/bin/kbxutil
/usr/bin/watchgnupg

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
%defattr(0644,root,root,0755)
%doc /usr/share/doc/gnupg/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/gnupg.info
/usr/share/info/gnupg.info-1
/usr/share/info/gnupg.info-2
/usr/share/info/gnupg.info-3

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gpg-check-pattern
/usr/libexec/gpg-pair-tool
/usr/libexec/gpg-preset-passphrase
/usr/libexec/gpg-protect-tool
/usr/libexec/gpg-wks-client
/usr/libexec/keyboxd
/usr/libexec/scdaemon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnupg/366d4e13a65adbfd0f7972f4c8dc9891692e92e5
/usr/share/package-licenses/gnupg/4bc05f7560e1e3ced08b71c93f10abe9e702c3ee
/usr/share/package-licenses/gnupg/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/gnupg/754becb73f3b288d7d8a62d8927a334cd38ac10b
/usr/share/package-licenses/gnupg/ac1b58bbd5bc11cacb7205718d620156ffd57c7e
/usr/share/package-licenses/gnupg/bf58811df8e4261d540cc1872f42011872ca8f54
/usr/share/package-licenses/gnupg/ca474fc88304aab05401b27d158b3f9e0c1ffae6

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dirmngr-client.1
/usr/share/man/man1/gpg-agent.1
/usr/share/man/man1/gpg-card.1
/usr/share/man/man1/gpg-check-pattern.1
/usr/share/man/man1/gpg-connect-agent.1
/usr/share/man/man1/gpg-preset-passphrase.1
/usr/share/man/man1/gpg-wks-client.1
/usr/share/man/man1/gpg-wks-server.1
/usr/share/man/man1/gpg.1
/usr/share/man/man1/gpgconf.1
/usr/share/man/man1/gpgparsemail.1
/usr/share/man/man1/gpgsm.1
/usr/share/man/man1/gpgtar.1
/usr/share/man/man1/gpgv.1
/usr/share/man/man1/scdaemon.1
/usr/share/man/man1/watchgnupg.1
/usr/share/man/man7/gnupg.7
/usr/share/man/man8/addgnupghome.8
/usr/share/man/man8/applygnupgdefaults.8
/usr/share/man/man8/dirmngr.8

%files locales -f gnupg2.lang
%defattr(-,root,root,-)

