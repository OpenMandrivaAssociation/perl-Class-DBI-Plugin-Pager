%define upstream_name    Class-DBI-Plugin-Pager
%define upstream_version 0.561

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	Paged queries for CDBI
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Class::Accessor::Chained::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::DBI)
BuildRequires:	perl(Data::Page)
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(Test::Exception)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Adds a pager method to your class that can query using SQL::Abstract
where clauses, and limit the number of rows returned to a specific subset.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Class/DBI/Plugin/*
%{_mandir}/*/*

