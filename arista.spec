%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

Summary:	An easy to use multimedia transcoder for the GNOME Desktop
Name:		arista
Version:	0.9.3
Release:	%mkrel 2
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
Requires:	python-gstreamer
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

# Generates .pyc / .pyo
%{__rm} -f %{buildroot}%{py_puresitedir}/%{name}/*.pyc
%python_compile_opt
%python_compile
install %{name}/*.pyc %{name}/*.pyo %{buildroot}%{py_puresitedir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README
%{_bindir}/%{name}*
%{py_puresitedir}/%{name}*.egg-info
%{py_puresitedir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
