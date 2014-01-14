Summary:	A simple video player for KDE 4
Name:		dragonplayer
Epoch:		3
Version:	4.12.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.kde.org/applications/multimedia/dragonplayer/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/dragon-%{version}.tar.xz

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

%changelog
* Tue Jan 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-1
- New version 4.8.97

* Wed Jul 11 2012 Andrey Bondrov <abondrov@mandriva.org> 3:4.8.95-1
+ Revision: 808890
- imported package dragonplayer

* Tue Jul 10 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.95-1
- Follow upstream and move dragonplayer from kdemultimedia4 to own package
