Summary:	Game like Nibbles but different - sound tracks
Summary(pl):	Gra w stylu Nibbles, ale inna - podk�ad d�wi�kowy
Name:		heroes-sound-tracks
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/heroes/%{name}-%{version}.tar.bz2
# Source0-md5:	f23313177d7a33b1b2e8c759cfa54310
URL:		http://heroes.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but
includes many graphical improvements and new game features. In it, you
must maneuver a small vehicle around a world and collect powerups
while avoiding obstacles, your opponents' trails, and even your own
trail. Several modes of play are available, including
"get-all-the-bonuses", deathmatch, and "squish-the-pedestrians".
This package containts sound tracks.

%description -l pl
Heroes jest podobny do starych gier "Tron" i "Nibbles", ale zawiera
wiele graficznych ulepsze� i nowe w�asno�ci. W tej grze musisz
manewrowa� ma�ym pojazdem i zbiera� dopalacze, unikaj�c przeszk�d i
�lad�w przeciwnik�w, a nawet swojego w�asnego �ladu. S� dost�pne r�ne
tryby gry, w tym "zbierz-wszystkie-premie", deathmatch oraz
"rozjed�-pieszych".
Pakiet zawiera podk�ad d�wi�kowy.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%{_datadir}/heroes/mod
