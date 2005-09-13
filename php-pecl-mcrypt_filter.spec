%define		_modname	mcrypt_filter
%define		_status		beta

Summary:	%{_modname} - applies mcrypt symmetric encryption using stream filters
Summary(pl):	%{_modname} - symetryczne szyfrowanie za pomoc± filtrów strumieni
Name:		php-pecl-%{_modname}
Version:	0.1.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	f0648aa92b518bfacc0c0be9e86d6bc9
URL:		http://pecl.php.net/package/mcrypt_filter/
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

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
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
