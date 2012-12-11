Name:           yahqtzee
Version:        2009.10
Summary:        A dice game written in C++ with Qt 4
Release:        %mkrel 2
License:        GPL
Group:          Graphical desktop/KDE
URL:            http://www.qt-apps.org/content/show.php/YahQtzee?content=88126
Source0:        http://prdownloads.sourceforge.net/88126-yahtzee-%version.tar.gz
Patch0:         88126-yahtzee-2009.02-fix-desktopfile.patch
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildRequires:  qt4-devel

%description
A dice game written in C++ with Qt 4. 

%files
%defattr(-,root,root)
%_gamesdatadir/yahtzee
%_gamesbindir/yahtzee
%_datadir/applications/yahtzee.desktop
%_iconsdir/yahtzee.png

#-----------------------------------------------------------------------------

%prep
%setup -q -n yahtzee
%patch0 -p1

%build

qmake yahtzee.pro

%make


%install
rm -rf %buildroot
%__mkdir -p  %buildroot%_gamesdatadir/yahtzee
%__cp yahtzee %buildroot%_gamesdatadir/yahtzee/
%__cp *.qm  %buildroot%_gamesdatadir/yahtzee/

%__mkdir -p %buildroot%_gamesdatadir/yahtzee/images
%__cp images/* %buildroot%_gamesdatadir/yahtzee/images

%__mkdir -p %buildroot%_gamesbindir 
ln -s %_gamesdatadir/yahtzee/yahtzee %buildroot%_gamesbindir

%__mkdir -p %buildroot%_datadir/applications
%__cp desktop/yahtzee.desktop %buildroot%_datadir/applications/yahtzee.desktop

%__mkdir -p %buildroot%_iconsdir
%__cp desktop/yahtzee.png %buildroot%_iconsdir/yahtzee.png

%clean
rm -rf %{buildroot}



%changelog
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 2009.10-2mdv2010.0
+ Revision: 446277
- rebuild

* Wed Mar 04 2009 Antoine Ginies <aginies@mandriva.com> 2009.10-1mdv2009.1
+ Revision: 348480
- update to latest release available

* Tue Jan 13 2009 Nicolas Lécureuil <neoclust@mandriva.org> 2009.02-1mdv2009.1
+ Revision: 329217
- New upstream version

* Sat Dec 13 2008 Nicolas Lécureuil <neoclust@mandriva.org> 2008.50-2mdv2009.1
+ Revision: 313942
- Bump release

* Sat Dec 13 2008 Nicolas Lécureuil <neoclust@mandriva.org> 2008.50-1mdv2009.1
+ Revision: 313940
- Fix Summary
- import yahqtzee


