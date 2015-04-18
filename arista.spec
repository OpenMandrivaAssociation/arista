%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

Summary:	An easy to use multimedia transcoder for the GNOME Desktop
Name:		arista
Version:	0.9.7
Release:	2
License:	LGPLv2+
Group:		Video
Url:		http://programmer-art.org/projects/arista-transcoder
Source:		http://programmer-art.org/media/releases/arista-transcoder/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:	python2-devel
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
python2 setup.py build

%install
python2 setup.py install --root %{buildroot}

rm -f %{buildroot}%{_datadir}/locale/templates/arista.pot %{buildroot}%{_prefix}/lib/nautilus/extensions-2.0/python/arista-nautilus.py

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS LICENSE
%{_bindir}/%{name}*
%{py2_puresitedir}/%{name}*.egg-info
%{py2_puresitedir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/nautilus-python/extensions/arista-nautilus.py

