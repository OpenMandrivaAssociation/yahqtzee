Name:           yahqtzee
Version:        2008.50
Summary:        A dice game written in C++ with Qt 4
Release:        %mkrel 2
License:        GPL
Group:          Graphical desktop/KDE
URL:            http://www.qt-apps.org/content/show.php/YahQtzee?content=88126
Source0:        http://prdownloads.sourceforge.net/88126-yahtzee-2008-50.tar.gz
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildRequires:  qt4-devel

%description
A dice game written in C++ with Qt 4. 

%files
%defattr(-,root,root)
%_gamesdatadir/yahtzee
%_gamesbindir/yahtzee

#-----------------------------------------------------------------------------

%prep
%setup -q -n yahtzee-2008-50

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
#ln -s %buildroot%_gamesbindir/yahtzees %buildroot%_datadir/yahtzee/yahtzee

%clean
rm -rf %{buildroot}

