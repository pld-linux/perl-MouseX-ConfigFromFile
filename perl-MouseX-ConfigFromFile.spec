#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	MouseX
%define	pnam	ConfigFromFile
Summary:	MouseX::ConfigFromFile - An abstract Mouse role for setting attributes from a configfile
Summary(pl.UTF-8):	MouseX::ConfigFromFile - abstrakcyjna rola Mouse do ustawiania atrybutów z pliku konfiguracyjnego
Name:		perl-MouseX-ConfigFromFile
Version:	0.05
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MASAKI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f6dc7f738085611949510c07301402ca
URL:		http://search.cpan.org/dist/MouseX-ConfigFromFile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MouseX::Types::Path::Class) >= 0.05
BuildRequires:	perl-Mouse
BuildRequires:	perl(Any::Moose) >= 0.05
BuildRequires:	perl(Test::UseAllModules)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an abstract role which provides an alternate constructor for
creating objects using parameters passed in from a configuration file.
The actual implementation of reading the configuration file is left to
concrete subroles.

It declares an attribute configfile and a class method
new_with_config, and requires that concrete roles derived from it
implement the class method get_config_from_file.

Attributes specified directly as arguments to new_with_config
supercede those in the configfile.

%description -l pl.UTF-8
MouseX::ConfigFromFile - abstrakcyjna rola Mouse do ustawiania atrybutów z pliku konfiguracyjnego

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MouseX/*.pm
%{_mandir}/man3/*
