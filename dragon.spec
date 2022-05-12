%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	A simple video player for KDE
Name:		dragon
Epoch:		3
Version:	22.04.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.kde.org/applications/multimedia/dragonplayer/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Phonon4Qt5)

%description
Dragon Player is a multimedia player where the focus is on simplicity,
instead of features. Dragon Player does one thing, and only one thing,
which is playing multimedia files. It's simple interface is designed not
to get in your way and instead empower you to simply play multimedia
files.

%files -f dragon.lang -f dragonplayer.lang
%config %{_sysconfdir}/xdg/dragonplayerrc
%{_bindir}/dragon
%{_libdir}/qt5/plugins/kf5/parts/dragonpart.so
%{_datadir}/applications/org.kde.dragonplayer.desktop
%{_datadir}/kservices5/ServiceMenus/*
%{_datadir}/kservices5/*.desktop
%{_datadir}/solid/actions/*.desktop
%{_datadir}/metainfo/org.kde.dragonplayer.appdata.xml
%{_datadir}/icons/*/*/*/*
%{_mandir}/man1/dragon.1*

#------------------------------------------------------------------------------

%prep
%setup -q -n dragon-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang dragon --with-man
%find_lang dragonplayer --with-html
