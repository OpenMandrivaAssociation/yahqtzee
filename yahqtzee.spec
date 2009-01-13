Name:           yahqtzee
Version:        2009.02
Summary:        A dice game written in C++ with Qt 4
Release:        %mkrel 1
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
%setup -q -n yahtzee-%version
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

