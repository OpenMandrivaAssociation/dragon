%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	A simple video player for KDE
Name:		dragon
Epoch:		3
Version:	15.08.3
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.kde.org/applications/multimedia/dragonplayer/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)

%description
Dragon Player is a multimedia player where the focus is on simplicity,
instead of features. Dragon Player does one thing, and only one thing,
which is playing multimedia files. It's simple interface is designed not
to get in your way and instead empower you to simply play multimedia
files.

%files
%config %{_sysconfdir}/xdg/dragonplayerrc
%{_datadir}/appdata/dragonplayer.appdata.xml
%{_bindir}/dragon
%{_libdir}/qt5/plugins/dragonpart.so
%{_datadir}/applications/org.kde.dragonplayer.desktop
%{_datadir}/kservices5/ServiceMenus/*
%{_datadir}/kservices5/*.desktop
%{_datadir}/kxmlgui5/dragonplayer
%{_datadir}/solid/actions/*.desktop
%{_datadir}/icons/*/*/*/*
%{_mandir}/man1/dragon.1*
%doc %{_docdir}/HTML/en/dragonplayer

#------------------------------------------------------------------------------

%prep
%setup -q -n dragon-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
