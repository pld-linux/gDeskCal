
Summary:	A cute little eye-candy and quite useful calendar
Name:		gDeskCal
Version:	0.52
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/%{name}-%(echo %{version} | tr .  _).tar.gz
# Source0-md5:	039a0e7ccd2c17b27802f4e60b415e79
Source1:	%{name}.desktop
URL:		http://www.pycage.de/software_gdeskcal.html
Requires:	python-pygtk-gtk >= 1.99.16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cute little eye-candy and quite useful calendar for your desktop.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/gdeskcal,%{_desktopdir}}

install gdeskcal $RPM_BUILD_ROOT%{_bindir}/gdeskcal.bin
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -a data code skins $RPM_BUILD_ROOT%{_datadir}/gdeskcal/
cp -a locale $RPM_BUILD_ROOT%{_datadir}

cat > $RPM_BUILD_ROOT%{_bindir}/gdeskcal << EOF
#!/bin/sh
PYTHONPATH=%{_datadir}/gdeskcal
export PYTHONPATH

exec gdeskcal.bin
EOF

%py_comp $RPM_BUILD_ROOT%{_datadir}/gdeskcal
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/gdeskcal

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS AUTHORS README*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gdeskcal
%{_desktopdir}/*
