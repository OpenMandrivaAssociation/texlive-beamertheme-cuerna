Name:		texlive-beamertheme-cuerna
Version:	42161
Release:	2
Summary:	A beamer theme with 4 colour palettes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-cuerna
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-cuerna.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-cuerna.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-cuerna.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains a theme for Beamer which is referenced as
"Cuerna" inside beamer and has four basic colour themes. The
title page shows rectangles that represent the Fibonacci
sequence, and spiral is drawn on top of the rectangles. Besides
that the rest of the graphic elements in the slides are scarce
to keep it clean

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/beamertheme-cuerna
%{_texmfdistdir}/tex/latex/beamertheme-cuerna
%doc %{_texmfdistdir}/doc/latex/beamertheme-cuerna

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
