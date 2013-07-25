%define upstream_name    Config-Model-OpenSsh
%define upstream_version 1.228

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.228
Release:	1

Summary:	OpenSsh configuration files editor and API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/Config-Model-OpenSsh-1.228.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Config::Model) >= 2.17.0
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(Log::Log4perl) >= 1.110.0
BuildRequires:	perl(Module::Build) >= 0.360.100
BuildRequires:	perl(Mouse::Meta::Attribute::Custom::Trait::Hash)
BuildRequires:	perl(MouseX::StrictConstructor)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::File::Contents)
BuildRequires:	perl(Test::Memory::Cycle)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
This module provides a configuration model for OpenSsh. Then Config::Model
provides a graphical editor program for _/etc/ssh/sshd_config_ and
_/etc/ssh/ssh_config_. See the config-edit-sshd manpage and the
config-edit-ssh manpage for more help.

This module and Config::Model can also be used to modify safely the content
for _/etc/ssh/sshd_config_, _/etc/ssh/ssh_config_ or _~/.ssh/config_ from
Perl programs.

Once this module is installed, you can run (as root, but please backup
/etc/X11/xorg.conf before):

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
rm -f t/pod.t
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc ChangeLog LICENSE META.yml MYMETA.yml README TODO demo
%{_mandir}/man3/*
%{perl_vendorlib}/Config


