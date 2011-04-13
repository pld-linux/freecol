
%define		_status	alpha2

%include	/usr/lib/rpm/macros.java
Summary:	Open source Colonization clone
Summary(pl.UTF-8):	Klon gry Colonization o otwartych źródłach
Name:		freecol
Version:	0.10.0
Release:	0.%{_status}.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/freecol/%{name}-%{version}-%{_status}-src.zip
# Source0-md5:	5327b5e1f07759bff6de2f4daf8c5787
Source1:	%{name}.sh
Source2:	%{name}.desktop
URL:		http://www.freecol.org/
BuildRequires:	ant-nodeps
BuildRequires:	higlayout
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	miglayout
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	higlayout
Requires:	java-commons-cli
Requires:	jre >= 1.4
Requires:	jre-X11
Requires:	miglayout
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FreeCol team aims to create an Open Source version of Colonization
(released under the GPL).

%description -l pl.UTF-8
Celem zespołu FreeCol jest stworzenie otwartej wersji gry Colonization
(wydanej na licencji GPL).

%prep
%setup -q -n %{name}

%build
required_jars="higlayout miglayout-swing"
export CLASSPATH=$(build-classpath $required_jars)
%ant

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/freecol,%{_desktopdir},%{_pixmapsdir},%{_javadir}}

install FreeCol.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/freecol

# install freecol specific cortado library
install jars/cortado-0.6.0.jar $RPM_BUILD_ROOT%{_javadir}/
ln -s  cortado-0.6.0.jar $RPM_BUILD_ROOT%{_javadir}/cortado-fc.jar

cp -a data/* $RPM_BUILD_ROOT%{_datadir}/freecol/
install %SOURCE2 $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/freecol
%{_datadir}/freecol
%{_javadir}/%{name}.jar
%{_javadir}/cortado-0.6.0.jar
%{_javadir}/cortado-fc.jar
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
