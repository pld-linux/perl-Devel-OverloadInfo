#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Devel
%define		pnam	OverloadInfo
Summary:	Devel::OverloadInfo - introspect overloaded operators
Summary(pl.UTF-8):	Devel::OverloadInfo - obserwacja przeciążonych operatorów
Name:		perl-Devel-OverloadInfo
Version:	0.007
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3dfb74ac00c25bcd8581e402fa414e19
URL:		https://metacpan.org/release/Devel-OverloadInfo
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-Package-Stash >= 0.14
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::OverloadInfo returns information about overloaded operators for
a given class (or object), including where in the inheritance
hierarchy the overloads are declared and where the code implementing
it is.

%description -l pl.UTF-8
Devel::OverloadInfo zwraca informacje o przeciążonych operatorach dla
danej klasy (lub obiektu), włącznie z umiejscowieniem deklaracji
przeciążenia w hierarchii dziedziczenia oraz kodu z implementacją.

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
%{_mandir}/man3/Devel::OverloadInfo.3pm*
