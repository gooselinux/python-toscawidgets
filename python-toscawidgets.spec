# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname ToscaWidgets

Name:           python-toscawidgets
Version:        0.9.8
Release:        1%{?dist}
Summary:        Toolkit to help create widgets for WSGI web apps
Group:          Development/Languages
License:        MIT
URL:            http://toscawidgets.org/
Source0:        http://pypi.python.org/packages/source/T/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel

Requires: python-paste >= 1.1
# Can replace this with python-cjson -- since TG-1 uses simplejson we'll use
# this for now.
Requires: python-simplejson
Requires: python-webob

%description
ToscaWidgets is a web widget toolkit for Python to aid in the creation, 
packaging and distribution of common view elements normally used in the web.

ToscaWidgets is an almost complete rewrite of the widgets package bundled with
TurboGears-1.0. The rewrite's goal was to decouple the widgets package from
CherryPy and TurboGears itself to fit better with TurboGears 2.0 
philosophy which is to partition it's services into independent WSGI 
components for easier mainteinance and reuse in other Python web applications 
or frameworks.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt PKG-INFO
%{python_sitelib}/*


%changelog
* Thu Oct 01 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-1
- 0.9.8 release
- Remove js patch which is now upstream

* Thu Aug 27 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-0.4.dev20090825
- Apply a patch from http://toscawidgets.org/trac/tw/ticket/30
  to fix problems with encoding javascript methods.

* Tue Aug 25 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-0.3.dev20090825
- Update to the latest mercurial snapshot, which fixes the python 2.4
  incompatibilites.

* Mon Aug 24 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-0.2.dev20090822
- Add a couple of patches to get things working on Python2.4

* Sat Aug 22 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-0.1.dev20090822
- Update to a 0.9.8 development snapshot

* Wed Aug 12 2009 Luke Macken <lmacken@redhat.com> - 0.9.7.2-1
- 0.9.7.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Luke Macken <lmacken@redhat.com> - 0.9.7.1-1
- 0.9.7.1
- s/define/global/

* Thu Jun 04 2009 Luke Macken <lmacken@redhat.com> - 0.9.6-1
- Update to 0.9.6

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 0.9.4-1
- Update to 0.9.4

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.3-2
- Rebuild for Python 2.6

* Tue Aug 26 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.3-1
- New upstream.

* Sun Jul 27 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.2-2
- Require python-webob

* Mon Jul 07 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.2-1
- Update to latest release.
- Fixes problem with pages being returned as text/plain.

* Mon Jun 02 2008 Luke Macken <lmacken@redhat.com> - 0.9.1-1
- Update to latest release
- Remove python-paste-script, python-ruledispatch, python-decorator and
  python-decoratortools dependencies.

* Sat May 31 2008 Luke Macken <lmacken@redhat.com> - 0.8.7-1
- Update to latest release.

* Fri May 30 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.6.1-1
- Update to latest release.

* Thu Mar 20 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2-0.3.20080320svn4283
- Update to a snapshot.

* Thu Dec 20 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2-0.2.rc3dev_r3795
- Add Requires

* Wed Dec 19 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2-0.1.rc3dev_r3795
- Inital Fedora Build
