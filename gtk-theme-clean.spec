Summary:	Clean - A gtk+ theme engine
Summary(pl):	Clean - motyw do gtk+
Name:		gtk-clean-theme
Version:	0.4
Release:	4
License:	GPL
Group:		Themes/GTK+
Source0:	http://progen.dynodns.net/dengen/cleantheme/clean-theme-gtk-%{version}.tar.gz
# Source0-md5:	46bbd81d66882348746693b48c08d3a1
URL:		http://progen.dynodns.net/dengen/cleantheme/index.html
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A clean, blue gtk theme.

%description -l pl
Clean - motyw do gtk+.

%prep
%setup -q -n %{name}

%build
cp -f /usr/share/automake/config.sub .
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_datadir}/themes/Clean
%attr(755,root,root) %{_libdir}/gtk/themes/engines/lib*.so
