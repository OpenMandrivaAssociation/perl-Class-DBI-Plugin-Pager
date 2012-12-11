%define upstream_name    Class-DBI-Plugin-Pager
%define upstream_version 0.561

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Paged queries for CDBI
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Chained::Fast)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Class::DBI)
BuildRequires:	perl(Data::Page)
BuildRequires:	perl(SQL::Abstract)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
Adds a pager method to your class that can query using SQL::Abstract
where clauses, and limit the number of rows returned to a specific subset.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#%__make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Class/DBI/Plugin/*
%{_mandir}/*/*



%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.561.0-2mdv2011.0
+ Revision: 680795
- mass rebuild

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.561.0-1mdv2011.0
+ Revision: 398795
- rebuild
- using %%perl_convert_version
- fixed source & buildrequires fields

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.561-6mdv2009.0
+ Revision: 241183
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.561-4mdv2008.0
+ Revision: 86106
- rebuild


* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 21:30:38 (56098)
- buildrequires again

* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 21:26:17 (56097)
- fix buildrequires

* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 21:16:14 (56094)
Import perl-Class-DBI-Plugin-Pager

* Sat Apr 08 2006 Arnaud de Lorbeau <devel@mandriva.com> 0.561-1mdk
- Initial MDV RPM

