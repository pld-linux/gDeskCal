Summary:	A cute little eye-candy and quite useful calendar
Summary(pl):	Ma³y, przyci±gaj±cy oko i u¿yteczny kalendarz
Name:		gDeskCal
Version:	0.55
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/%{name}-%(echo %{version} | tr . _).tar.gz
# Source0-md5:	1bcc83b703292eefd9daa690a2c91985
Source1:	%{name}.desktop
Patch0:		%{name}-locale_path.patch
URL:		http://www.pycage.de/software_gdeskcal.html
Requires:	python-pygtk-gtk >= 1.99.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cute little eye-candy and quite useful calendar for your desktop.

%description -l pl
Ma³y, przyci±gaj±cy oko i u¿yteczny kalendarz dla pulpitu.

%prep
%setup -q
%patch -p1

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

%py_comp $RPM_BUILD_ROOT%{_datadir}/gdeskcal
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/gdeskcal

find  $RPM_BUILD_ROOT%{_datadir}/gdeskcal -name "*.py" -exec rm -f {} \;

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS AUTHORS README*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gdeskcal
%{_desktopdir}/*
