Summary:	Open source Colonization clone
Summary(pl):	Klon gry Colonization o otwartych ¼ród³ach
Name:		freecol
Version:	0.5.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/freecol/%{name}-%{version}-src.tar.gz
# Source0-md5:	fa33b91c291665dc94382afcfc4be69a
Source1:	%{name}.sh
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
#rm -rf jars
#sed -i -e /Class-Path/d src/MANIFEST.MF

%build
CLASSPATH=$(build-classpath higlayout)
JAVA_HOME=%{java_home}
export CLASSPATH JAVA_HOME
%{ant} -Dnojars -Dnodata fullpackage

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 644 FreeCol.jar \
	$RPM_BUILD_ROOT%{_datadir}/games/freecol/FreeCol.jar
install -Dpm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/freecol

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/freecol
%{_datadir}/games/freecol
