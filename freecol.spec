Summary:	Open source Colonization clone
Summary(pl):	Klon gry Colonization o otwartych ¼ród³ach
Name:		freecol
Version:	0.5.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/freecol/%{name}-%{version}-src.tar.gz
# Source0-md5:	6b0b94da77a8cb0f671e1f3d392bcf89
Source1:	%{name}.sh
Patch0:		%{name}-no_taskdefs.patch
URL:		http://www.freecol.org/
BuildRequires:	ant
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

%description -l pl
Celem zespo³y FreeCol jest stworzenie otwartej wersji gry Colonization
(wydanej na licencji GPL).

%prep
%setup -q -n %{name}
%patch0 -p1

%build
CLASSPATH="$(build-classpath higlayout)"
JAVA_HOME=%{java_home}
export CLASSPATH JAVA_HOME
%ant -Dnojars -Dnodata fullpackage

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 644 FreeCol.jar \
	$RPM_BUILD_ROOT%{_datadir}/games/freecol/FreeCol.jar
install -Dpm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/freecol

install -d $RPM_BUILD_ROOT%{_datadir}/freecol
cp -ar data/* $RPM_BUILD_ROOT%{_datadir}/freecol/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/freecol
%{_datadir}/games/freecol
%{_datadir}/freecol
