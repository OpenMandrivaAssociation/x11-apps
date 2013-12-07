Name:		x11-apps
Version:	1.0.0
Release:	18
Summary:	X11 apps
Group:		Development/X11
BuildArch:	noarch
License:	MIT
Requires:	bitmap
Requires:	ico
Requires:	oclock
Requires:	xbiff
Requires:	xcalc
Requires:	xclipboard
Requires:	xclock
Requires:	xedit
Requires:	xeyes
Requires:	xfd
Requires:	xfontsel
Requires:	xgc
Requires:	xload
Requires:	xlogo
Requires:	xman
Requires:	xmag
Requires:	xmessage
Requires:	xwd
Requires:	xwud

%description
X11 apps.

%files



%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-12mdv2011.0
+ Revision: 671110
- mass rebuild

* Fri Dec 10 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.0-11mdv2011.0
+ Revision: 620449
- Rebuild for 2011.0

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-10mdv2010.1
+ Revision: 524360
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.0-9mdv2009.1
+ Revision: 351432
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-8mdv2009.0
+ Revision: 225938
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdv2008.1
+ Revision: 179662
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Remove applications that must have xprint support (xmore crashes if not
      compiled with, and xpr is an x printer interface as the name says).
      Also updates license to MIT and remove a few other known broken applications.

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdv2008.0
+ Revision: 75594
- rebuild


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Wed May 17 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-17 19:00:32 (27556)
- adding packager tag

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

