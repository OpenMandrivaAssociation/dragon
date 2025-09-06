#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	A simple video player for KDE
Name:		dragon
Version:	25.08.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://www.kde.org/applications/multimedia/dragonplayer/
%if 0%{?git:1}
Source0:	https://invent.kde.org/multimedia/dragon/-/archive/%{gitbranch}/dragon-%{gitbranchd}.tar.bz2#/dragon-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/dragon-%{version}.tar.xz
%endif

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	pkgconfig(libavcodec)

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%rename plasma6-dragon

%description
Dragon Player is a multimedia player where the focus is on simplicity,
instead of features. Dragon Player does one thing, and only one thing,
which is playing multimedia files. It's simple interface is designed not
to get in your way and instead empower you to simply play multimedia
files.

%files -f %{name}.lang
%{_bindir}/dragon
%{_datadir}/applications/org.kde.dragonplayer.desktop
%{_datadir}/metainfo/org.kde.dragonplayer.appdata.xml
%{_datadir}/icons/*/*/*/*
%{_qtdir}/qml/org/kde/dragon
