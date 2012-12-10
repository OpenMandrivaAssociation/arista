%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

Summary:	An easy to use multimedia transcoder for the GNOME Desktop
Name:		arista
Version:	0.9.7
Release:	%mkrel 1
License:	LGPLv2+
Group:		Video
Url:		http://programmer-art.org/projects/arista-transcoder
Source:		http://programmer-art.org/media/releases/arista-transcoder/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:      noarch
BuildRequires:	python-devel
Requires:	python-dbus
Requires:	pygtk2.0
Requires:	gnome-python-gconf
Requires:	gstreamer0.10-python
Requires:	gstreamer0.10-ffmpeg
Requires:	gstreamer0.10-plugins-base
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-plugins-bad
Requires:	gstreamer0.10-plugins-ugly


%description
An easy to use multimedia transcoder for the GNOME Desktop. Arista 
focuses on being easy to use by making the complex task of encoding 
for various devices simple. Pick your input, pick your target device, 
choose a file to save to and go. 

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}

rm -f %{buildroot}%{_datadir}/locale/templates/arista.pot %{buildroot}%{_prefix}/lib/nautilus/extensions-2.0/python/arista-nautilus.py

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS LICENSE
%{_bindir}/%{name}*
%{py_puresitedir}/%{name}*.egg-info
%{py_puresitedir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/nautilus-python/extensions/arista-nautilus.py


%changelog
* Wed Sep 28 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.7-1mdv2012.0
+ Revision: 701732
- New version: 0.9.7

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.9.5-2mdv2011.0
+ Revision: 592381
- rebuild for python 2.7

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 0.9.5-1mdv2011.0
+ Revision: 582961
- New version 0.9.5

* Thu Dec 03 2009 Jérôme Brenier <incubusss@mandriva.org> 0.9.3-3mdv2010.1
+ Revision: 472992
+ rebuild (emptylog)

* Thu Dec 03 2009 Jérôme Brenier <incubusss@mandriva.org> 0.9.3-2mdv2010.1
+ Revision: 472924
- fix Requires

* Wed Dec 02 2009 Jérôme Brenier <incubusss@mandriva.org> 0.9.3-1mdv2010.1
+ Revision: 472625
- add specfile and source
- Created package structure for arista.

