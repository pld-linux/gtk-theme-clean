%define  ver     @VERSION@
%define  rel     1
%define  prefix  /usr

Summary: Clean - A gtk+ theme engine
Name: gtk-clean-theme
Version: %ver
Release: %rel
Group: Misc
Copyright: GPL
Source: http://progen.dynodns.net/dengen/CleanTheme/gtk-clean-theme-%{ver}.tar.gz
Url: http://progen.dynodns.net/dengen/CleanTheme/
BuildRoot: /var/tmp/clean-%{PACKAGE_VERSION}-root
Docdir: %{prefix}/doc

Requires: gtk+ >= 1.2

%description
A clean, blue gtk theme.

%prep
%setup

%build

%ifarch alpha
  CFLAGS="$RPM_OPT_FLAGS" ./configure --host=alpha-redhat-linux --prefix=%prefix
%else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix 
%endif

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Tue Apr 18 1999 Vincent Harvey <vharvey@mcs.net>
- I made an rpm spec. I am not the author though, Dwight Engen <dengen40@yahoo.com>

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README COPYING 

%{prefix}/share/themes/Clean/gtk/gtkrc
%{prefix}/share/themes/Clean/ICON.png
%{prefix}/share/themes/Clean/README.html

%{prefix}/lib/gtk/themes/engines/*
