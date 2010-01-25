%define upstream_name    Config-Model-OpenSsh
%define upstream_version 1.210

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    OpenSsh configuration files editor and API
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build)
BuildRequires: perl(Config::Model)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/config-edit-ssh
%{_bindir}/config-edit-sshd
%{_mandir}/man1/config-edit-ssh.1*
%{_mandir}/man1/config-edit-sshd.1*
%{_mandir}/man3/*
%{perl_vendorlib}/Config
