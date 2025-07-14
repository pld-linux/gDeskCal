Summary:	A cute little eye-candy and quite useful calendar
Summary(pl.UTF-8):	Mały, przyciągający oko i użyteczny kalendarz
Name:		gDeskCal
Version:	0.57.1
Release:	6
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/%{name}-%(echo %{version} | tr . _).tar.gz
# Source0-md5:	c2c1de1046e9026558c51e90fe6f8a9e
Source1:	%{name}.desktop
Patch0:		%{name}-locale_path.patch
Patch1:		%{name}-ewmh.patch
Patch2:		%{name}-evolution.patch
URL:		http://www.pycage.de/software_gdeskcal.html
Requires:	python-pygtk-gtk >= 1.99.16
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cute little eye-candy and quite useful calendar for your desktop.

%description -l pl.UTF-8
Mały, przyciągający oko i użyteczny kalendarz dla pulpitu.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

mv locale/{no,nb}

%build
%py_comp code
%py_ocomp code

find {data,code,skins} -name "*.py" -exec rm -f '{}' ';'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/gdeskcal,%{_desktopdir}}

install gdeskcal $RPM_BUILD_ROOT%{_bindir}/gdeskcal.bin
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -a data code skins $RPM_BUILD_ROOT%{_datadir}/gdeskcal
cp -a locale $RPM_BUILD_ROOT%{_datadir}

cat > $RPM_BUILD_ROOT%{_bindir}/gdeskcal << EOF
#!/bin/sh
PYTHONPATH=%{_datadir}/gdeskcal
export PYTHONPATH

exec gdeskcal.bin
EOF

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS AUTHORS README*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gdeskcal
%{_desktopdir}/*.desktop
