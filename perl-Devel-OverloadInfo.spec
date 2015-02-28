#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Devel
%define		pnam	OverloadInfo
%include	/usr/lib/rpm/macros.perl
Summary:	Devel::OverloadInfo - introspect overloaded operators
Name:		perl-Devel-OverloadInfo
Version:	0.002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bff186962739cd63d303061f2da038b1
URL:		http://search.cpan.org/dist/Devel-OverloadInfo/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-Package-Stash >= 0.14
BuildRequires:	perl-Sub-Identify
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::OverloadInfo returns information about overloaded operators for
a given class (or object), including where in the inheritance
hierarchy the overloads are declared and where the code implementing
it is.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Devel/OverloadInfo.pm
%{_mandir}/man3/*
