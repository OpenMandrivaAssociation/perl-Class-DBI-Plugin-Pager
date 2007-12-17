%define realname Class-DBI-Plugin-Pager
%define name perl-%{realname}
%define version 0.561
%define release %mkrel 4

Summary:	Paged queries for CDBI
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		/%{realname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Data-Page
BuildRequires:	perl-UNIVERSAL-require
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(Class::Accessor::Chained::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(Test::Exception)
BuildArch:	noarch

%description
Adds a pager method to your class that can query using SQL::Abstract
where clauses, and limit the number of rows returned to a specific subset.

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Class/DBI/Plugin/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

