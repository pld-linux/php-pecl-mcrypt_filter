%define		php_name	php%{?php_suffix}
%define		modname	mcrypt_filter
%define		status		beta
Summary:	%{modname} - applies mcrypt symmetric encryption using stream filters
Summary(pl.UTF-8):	%{modname} - symetryczne szyfrowanie za pomocą filtrów strumieni
Name:		%{php_name}-pecl-%{modname}
Version:	0.1.0
Release:	8
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	f0648aa92b518bfacc0c0be9e86d6bc9
URL:		http://pecl.php.net/package/mcrypt_filter/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Provides:	php(%{modname}) = %{version}
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Creates mcrypt.* and mdecrypt.* class of filters for inline symmetric
encryption and decryption.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
To rozszerzenie tworzy klasy filtrów mcrypt.* i mdecrypt.* do
symetrycznego szyfrowania i odszyfrowywania strumieni.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
