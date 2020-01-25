Summary:	Check given IP/Host presence in RBLs
Summary(pl.UTF-8):	Sprawdzenie obecności adresu IP/Hosta w bazach RBL
Name:		rbllookup
Version:	0.0.1.1
Release:	0.2
License:	GPL
Group:		Applications/Console
Source0:	http://dl.sourceforge.net/rbllookup/%{name}-%{version}.tar.bz2
# Source0-md5:	fc0a64bd160a45bc69b6f9a13e7d7d42
Patch0:		%{name}-usage.patch
URL:		http://rbllookup.sourceforge.net/
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-modules
BuildRequires:	rpm-perlprov
# already in perl-modules in appropriate version
BuildRequires:	perl(Term::ANSIColor)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check given IP/Host presence in 106 RBLs. Now, you don't have to check
a lot of WWW sites, just run this script in console.

%description -l pl.UTF-8
Za pomocą tego programu możliwe jest odpytanie 106 baz RBL o podany z
linii poleceń adres.

%prep
%setup -q -c
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install rbl.pl $RPM_BUILD_ROOT%{_bindir}/rbllookup

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README INSTALL TODO NOTES
%attr(755,root,root) %{_bindir}/*
