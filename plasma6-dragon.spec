%define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	A simple video player for KDE
Name:		plasma6-dragon
Version:	24.01.96
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.kde.org/applications/multimedia/dragonplayer/
%if 0%{?git:1}
Source0:	https://invent.kde.org/multimedia/dragon/-/archive/%{gitbranch}/dragon-%{gitbranchd}.tar.bz2#/dragon-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/dragon-%{version}.tar.xz
%endif

BuildRequires:	cmake
BuildRequires:	ninja
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
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Phonon4Qt6)

%description
Dragon Player is a multimedia player where the focus is on simplicity,
instead of features. Dragon Player does one thing, and only one thing,
which is playing multimedia files. It's simple interface is designed not
to get in your way and instead empower you to simply play multimedia
files.

%files -f dragon.lang -f dragonplayer.lang
%config %{_sysconfdir}/xdg/dragonplayerrc
%{_bindir}/dragon
%{_libdir}/qt6/plugins/kf6/parts/dragonpart.so
%{_datadir}/applications/org.kde.dragonplayer.desktop
%{_datadir}/solid/actions/*.desktop
%{_datadir}/metainfo/org.kde.dragonplayer.appdata.xml
%{_datadir}/icons/*/*/*/*
%{_datadir}/kio/servicemenus/dragonplayer_play_dvd.desktop

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n dragon-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang dragon --with-man
%find_lang dragonplayer --with-html
