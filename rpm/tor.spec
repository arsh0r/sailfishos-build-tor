Name:       tor
Version:    0.3.5.7
Release:    1%{?dist}
Group:      System Environment/Daemons
License:    BSD
Summary:    Anonymizing overlay network for TCP
URL:        https://www.torproject.org

Source0:    https://www.torproject.org/dist/tor-%{version}.tar.gz
Source1:    https://www.torproject.org/dist/tor-%{version}.tar.gz.asc

BuildRoot: %{_tmppath}/build-root-%{name}
Prefix: /usr
Provides: tor

Requires: openssl
Requires: zlib

%description
The Tor network is a group of volunteer-operated servers that allows people to
improve their privacy and security on the Internet. Tor's users employ this
network by connecting through a series of virtual tunnels rather than making a
direct connection, thus allowing both organizations and individuals to share
information over public networks without compromising their privacy. Along the
same line, Tor is an effective censorship circumvention tool, allowing its
users to reach otherwise blocked destinations or content. Tor can also be used
as a building block for software developers to create new communication tools
with built-in privacy features.

This package contains the Tor software that can act as either a server on the
Tor network, or as a client to connect to the Tor network.

%changelog
* Sat Jul 14 2018 Marcel Härry <mh+fedora@scrit.ch> - 0.3.3.9-1
- update to latest upstream stable release 0.3.3.9 (#1581512)

%prep
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" RLOG_LIBS="--static" \
./configure --enable-static-libevent --with-libevent-dir=/usr/local --prefix=%{prefix} --mandir=%{_mandir}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install-strip

cd $RPM_BUILD_ROOT

find . -type d -fprint $RPM_BUILD_DIR/file.list.%{name}.dirs
find . -type f -fprint $RPM_BUILD_DIR/file.list.%{name}.files.tmp
sed '/\/man\//s/$/.gz/g' $RPM_BUILD_DIR/file.list.%{name}.files.tmp > $RPM_BUILD_DIR/file.list.%{name}.files
find . -type l -fprint $RPM_BUILD_DIR/file.list.%{name}.libs
sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' $RPM_BUILD_DIR/file.list.%{name}.dirs > $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.files >> $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.libs >> $RPM_BUILD_DIR/file.list.%{name}

%clean
case "$RPM_BUILD_ROOT" in build-root-*) rm -rf $RPM_BUILD_ROOT ;; esac
rm -f $RPM_BUILD_DIR/file.list.%{name}
rm -f $RPM_BUILD_DIR/file.list.%{name}.libs
rm -f $RPM_BUILD_DIR/file.list.%{name}.files
rm -f $RPM_BUILD_DIR/file.list.%{name}.files.tmp
rm -f $RPM_BUILD_DIR/file.list.%{name}.dirs

%define _unpackaged_files_terminate_build 0 
##%files -f file.list.%{name}
%files
%{_bindir}/tor
%{_bindir}/tor-gencert
%{_bindir}/tor-resolve
%dir %{_datadir}/tor
%{_datadir}/tor/geoip
%{_datadir}/tor/geoip6

%defattr(-,root,root,0755)
