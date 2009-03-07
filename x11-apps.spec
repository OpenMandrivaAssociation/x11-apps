Name: x11-apps
Version: 1.0.0
Release: %mkrel 9
Summary: X11 apps
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
License: MIT
Requires: bitmap
Requires: ico
Requires: oclock
Requires: xbiff
Requires: xcalc
Requires: xclipboard
Requires: xclock
Requires: xedit
Requires: xeyes
Requires: xfd
Requires: xfontsel
Requires: xgc
Requires: xload
Requires: xlogo
Requires: xman
Requires: xmag
Requires: xmessage
Requires: xwd
Requires: xwud

%description
X11 apps

%files
%defattr(-,root,root)
