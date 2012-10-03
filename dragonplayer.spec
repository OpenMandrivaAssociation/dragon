Name:		dragonplayer
Version: 4.9.2
Release: 1
Epoch:		3
Summary:	A simple video player for KDE 4
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org/applications/multimedia/dragonplayer/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/dragon-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
Requires:	kdebase4-runtime
Conflicts:	kdemultimedia4-core < 3:4.5.71
Conflicts:	kmix < 3:4.8.95

%description
Dragon Player is a multimedia player where the focus is on simplicity,
instead of features. Dragon Player does one thing, and only one thing,
which is playing multimedia files. It's simple interface is designed not
to get in your way and instead empower you to simply play multimedia
files.

%files
%{_kde_bindir}/dragon
%{_kde_appsdir}/dragonplayer
%{_kde_appsdir}/solid/actions/dragonplayer-opendvd.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_mandir}/man1/*
%{_kde_libdir}/kde4/dragonpart.so
%{_kde_applicationsdir}/dragonplayer.desktop
%{_kde_services}/ServiceMenus/dragonplayer_*
%{_kde_services}/dragonplayer_part.desktop
%{_kde_configdir}/dragonplayerrc
%{_kde_docdir}/HTML/en/dragonplayer

#------------------------------------------------------------------------------

%prep
%setup -q -n dragon-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

