Summary:	Clean - A gtk+ theme engine
Summary(pl):	Clean - motyw do gtk+
Name:		gtk-clean-theme
Version:	0.4
Release:	3
License:	GPL
Group:		Themes/Gtk
Source0:	http://progen.dynodns.net/dengen/cleantheme/clean-theme-gtk-%{version}.tar.gz
URL:		http://progen.dynodns.net/dengen/cleantheme/index.html
BuildRequires:	gtk+-devel >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A clean, blue gtk theme.

%description -l pl
Clean - motyw do gtk+.

%prep
%setup -q -n %{name}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/themes/Clean
%attr(755,root,root) %{_libdir}/gtk/themes/engines/lib*.so
