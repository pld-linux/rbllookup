Summary:	Check given IP/Host presence in RBLs.
Summary(pl):	Sprawdzenie obecno¶ci adresu IP/Hosta w bazach RBL.
Name:		rbllookup
Version:	0.0.1.1
Release:	0.1
License:	GPL
Group:		Applications/Console
Source0:	http://dl.sourceforge.net/rbllookup/%{name}-%{version}.tar.bz2
# Source0-md5:	fc0a64bd160a45bc69b6f9a13e7d7d42
URL:		http://rbllookup.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check given IP/Host presence in 106 RBLs. Now, you don't have to check
a lot www sites, just run this script in console.

%description -l pl
Za pomoc± tego programu mo¿liwe jest odpytanie 106 baz RBL o podany z
linii poleceñ adres.

%prep
%setup -q -c -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install rbl.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README INSTALL TODO NOTES
%attr(755,root,root) %{_bindir}/*
