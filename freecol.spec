Summary:	Open source Colonization clone
Summary(pl.UTF-8):	Klon gry Colonization o otwartych źródłach
Name:		freecol
Version:	0.7.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/freecol/%{name}-%{version}-src.tar.gz
# Source0-md5:	254576cbfada1f20535e641feb2b38f0
Source1:	%{name}.sh
Source2:	%{name}.desktop
URL:		http://www.freecol.org/
BuildRequires:	ant-nodeps
BuildRequires:	higlayout
BuildRequires:	jdk >= 1.4
Requires:	higlayout
Requires:	jre >= 1.4
Requires:	jre-X11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FreeCol team aims to create an Open Source version of Colonization
(released under the GPL).

%description -l pl.UTF-8
Celem zespoły FreeCol jest stworzenie otwartej wersji gry Colonization
(wydanej na licencji GPL).

%prep
%setup -q -n %{name}

%build
CLASSPATH="$(build-classpath higlayout)"
JAVA_HOME=%{java_home}
export CLASSPATH JAVA_HOME
%ant

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/freecol,%{_desktopdir}}

install FreeCol.jar $RPM_BUILD_ROOT%{_datadir}/freecol/FreeCol.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/freecol

cp -ar data/* $RPM_BUILD_ROOT%{_datadir}/freecol/
install %SOURCE2 $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/freecol
%{_datadir}/freecol
%{_desktopdir}/%{name}.desktop
