Summary:	VIC - the UCB/LBNL video conferencing tool
Summary(pl.UTF-8):   VIC - narzędzie do konferencji wideo z UCB/LBNL
Name:		vic
Version:	2.8
Release:	0.1
License:	BSD
Group:		Applications/Multimedia
Source0:	ftp://ftp.ee.lbl.gov/conferencing/vic/%{name}src-%{version}.tar.gz
# Source0-md5:	1f9ae3fbf8e9e47e6539c0621964542d
Patch0:		%{name}-config.patch
Patch1:		%{name}-fix.patch
URL:		http://www-nrg.ee.lbl.gov/vic/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VIC - the UCB/LBNL video conferencing tool.

%description -l pl.UTF-8
VIC - narzędzie do konferencji wideo z UCB/LBNL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure
%{__make} all h261_play \
	CCOPT="%{rpmcflags}" STATIC=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install vic h261_play histtolut $RPM_BUILD_ROOT%{_bindir}
install vic.1 h261_play.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README html/{*.html,*.gif}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
