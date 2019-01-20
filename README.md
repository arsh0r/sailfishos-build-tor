# Building tor with statically linked libevent for SailfishOS

[Install Platform SDK](https://sailfishos.org/wiki/Platform_SDK_Installation)

[Install SDK Target](https://sailfishos.org/wiki/Platform_SDK_Target_Installation)

Install needed packages:
```
sb2 -t SailfishOS-latest-armv7hl -m sdk-install -R zypper in autoconf automake gettext libtool
sb2 -t SailfishOS-latest-armv7hl -m sdk-install -R zypper in zlib-devel openssl-devel
```

Download and compile libevent-2.1.8-stable (will be linked statically)
```
curl -L -O https://github.com/libevent/libevent/releases/download/release-2.1.8-stable/libevent-2.1.8-stable.tar.gz
tar xzf libevent-2.1.8-stable.tar.gz
cd libevent-2.1.8-stable
sb2 -t SailfishOS-latest-armv7hl -m sdk-build ./configure --disable-shared --enable-static --with-pic
sb2 -t SailfishOS-latest-armv7hl -m sdk-build -R make install
cd ..
```

Download and build package for tor 0.3.5.7
```
curl -L -O https://www.torproject.org/dist/tor-0.3.5.7.tar.gz
tar xzf tor-0.3.5.7.tar.gz 
cd tor-0.3.5.7
sb2 -t SailfishOS-latest-armv7hl -m sdk-build ./configure --enable-static-libevent --with-libevent-dir=/usr/local
```
copy rpm directory from this repository
```
mb2 -t SailfishOS-latest-armv7hl build
```
