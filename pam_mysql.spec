Summary:	PAM module for auth UNIX users using MySQL data base
Name:		pam_mysql
Version:	0.7
Release:	0.16.rc1%{?dist}
Epoch:		1
License:	GPLv2+
Group:		System Environment/Base
Source0:	http://dl.sf.net/pam-mysql/%{name}-%{version}RC1.tar.gz
Patch0:		pam_mysql-0.7RC1-resps-segfault.patch
Patch1:		pam_mysql-0.7RC1-first-pass.patch
Patch2:		pam_mysql-0.7RC1-scrambled.patch
Patch3:         pam_mysql-0.7RC1-sha256.patch
URL:		http://sf.net/projects/pam-mysql/
BuildRequires:  pam-devel mysql-devel cyrus-sasl-devel pkgconfig openssl-devel
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:	pam

%description
Pam_mysql aims to provide a backend neutral means of authenticating
users against an MySQL database.

%prep
%setup -q -n %{name}-%{version}RC1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure \
  --with-openssl \
  --with-pam-mods-dir=/%{_lib}/security \
  --enable-static=no \
  --with-cyrus-sasl2

make %{?_smp_mflags}

mv CREDITS CREDITS.lame
iconv -f latin1 -t utf-8 -o CREDITS CREDITS.lame
touch -r README CREDITS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog COPYING CREDITS NEWS README
/%{_lib}/security/pam_mysql.so

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-0.16.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-0.15.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-0.14.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-0.13.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 10 2011 Paul P. Komkoff Jr <i@stingr.net> 1:0.7-0.12.rc1
- make_scrambled_password fix (bz#709534)

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1:0.7-0.11.rc1.2
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-0.10.rc1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1:0.7-0.9.rc1.2
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-0.8.rc1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7-0.7.rc1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Manuel "lonely wolf" Wolfshant <wolfy@nobugconsulting.ro> 0.7-0.6.rc1.2
- rebuild for mysql-5.1 (libmysqlclient.so.15)

* Fri Jan 16 2009 Manuel "lonely wolf" Wolfshant <wolfy@nobugconsulting.ro> 0.7-0.6.rc1.1
- rebuild for newer openssl

* Fri Oct 3 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.7-0.6.rc1
- Fix bz#465186 (credits go to: Philippe Troin)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:0.7-0.5.rc1.2
- Autorebuild for GCC 4.3

* Wed Jan 23 2008 lonely wolf <wolfy at fedoraproject dot org> - 0.7-0.4.rc1.2
- BR: pkgconfig, openssl-devel
- preserve timestamp of CREDITS

* Sat Jan 19 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.7-0.4.rc1.1
- more packaging fixes and one segfault bugfix

* Thu Jan 9 2008 lonely wolf <wolfy at fedoraproject dot org> - 0.7-0.3.rc1.1
- couple of fixes

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 0.7-0.2.rc1
- Rebuild for deps

* Fri Oct 19 2007 Paul P. Komkoff Jr <i@stingr.net> - 0.7-0.1.rc1
- pick up the package
- new upstream RC

* Wed Sep 06 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.6.2-4
- Rebuild for FC6

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.6.2-3
- Rebuild for Fedora Extras 5

* Fri Nov 13 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.6.2-2
- Fixed build on x86_64

* Fri Nov 13 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.6.2-1
- Upstream update
- Fixed versioning scheme

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Mar 28 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.50-5
- Added zlib-devel to BuildRequires

* Wed Mar 23 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.50-4
- Fixed build on x86_64

* Wed Mar 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.50-3
- Removed explicit Requires
- Removed Polish Summary and Description

* Tue Mar 15 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.50-2
- Bump release to 2
- Added Requires

* Fri Jan  7 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0:0.50-1.iva.0
- Retooled spec file for FC3
