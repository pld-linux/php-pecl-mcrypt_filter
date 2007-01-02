%define		_modname	mcrypt_filter
%define		_status		beta
Summary:	%{_modname} - applies mcrypt symmetric encryption using stream filters
Summary(pl):	%{_modname} - symetryczne szyfrowanie za pomoc± filtrów strumieni
Name:		php-pecl-%{_modname}
Version:	0.1.0
Release:	6
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	f0648aa92b518bfacc0c0be9e86d6bc9
URL:		http://pecl.php.net/package/mcrypt_filter/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Creates mcrypt.* and mdecrypt.* class of filters for inline symmetric
encryption and decryption.

In PECL status of this extension is: %{_status}.

%description -l pl
To rozszerzenie tworzy klasy filtrów mcrypt.* i mdecrypt.* do
symetrycznego szyfrowania i odszyfrowywania strumieni.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
