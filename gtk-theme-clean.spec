Summary:	Clean - A GTK+ theme engine
Summary(pl.UTF-8):   Clean - motyw do GTK+
Name:		gtk-theme-clean
Version:	0.4
Release:	6
License:	GPL
Group:		Themes/GTK+
Source0:	http://progen.dynodns.net/dengen/cleantheme/clean-theme-gtk-%{version}.tar.gz
# Source0-md5:	46bbd81d66882348746693b48c08d3a1
URL:		http://progen.dynodns.net/dengen/cleantheme/index.html
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2
Obsoletes:	gtk-clean-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A clean, blue GTK+ theme.

%description -l pl.UTF-8
Clean - motyw do GTK+.

%prep
%setup -q -n gtk-clean-theme

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
