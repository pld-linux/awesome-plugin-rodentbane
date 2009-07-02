%define		rel 20090623
Summary:	An awesome plugin that allow to manipulate mouse cursor using keyboard
Summary(pl.UTF-8):	Wtyczka awesome pozwalająca używać kursora myszy przy uzyciu klawiatury
Name:		awesome-plugin-rodentbane
Version:	0
Release:	0.%{rel}.1
License:	WTFPL
Group:		X11/Window Managers
## git clone git://git.glacicle.com/awesome/rodentbane.git
Source0:	rodentbane.lua
Requires:	awesome-plugin-awful
Requires:	awesome-plugin-beautiful
Requires:	xdotool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rodentbane is an implementation of keynav in a lua module for awesome.
It allows for rapid control of the mouse cursor using just the
keyboard, and can speed up your workflow significantly. It is mean to
be used in situations where regular window manager and application
bindings will not suffice, and you absolutely have to use a click
event. (Think flash objects inside webpages) It is not meant as a
full-blown replacement for using the mouse, for that, you will need to
set keybindings and use programs that support full keyboard control
(such as awesome, of course).

%description -l pl.UTF-8
Rodentable jest implementacją idei "keynav" w module jeżyka lua dla
zarządcy okien awesome. Wtyczka ta pozwala szybko i efektywnie
posługiwać się kursorem myszy korzystając tylko z klawiatury, co może
znacząco usprawnić pracę z komputerem. Rodentable pozwala obejść się
bez myszy nawet w aplikacjach w których pewne akcje nie są normalnie
dostępne z poziomu klawiatury. Przykładem mogą tu być objekty flash na
stronach www. Rodentable nie zastępuje jednak w pełni myszy. Czasem
wygodniej jest używać aplikacji, która może być w całości kontrolowana
z poziomu klawiatury (takiej jak na przykład zarządca okien awesome).

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib
install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/awesome/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/rodentbane.lua
