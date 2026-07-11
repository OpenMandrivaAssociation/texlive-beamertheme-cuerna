%global tl_name beamertheme-cuerna
%global tl_revision 42161

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A beamer theme with 4 colour palettes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-cuerna
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-cuerna.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-cuerna.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-cuerna.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains a theme for Beamer which is referenced as "Cuerna"
inside beamer and has four basic colour themes. The title page shows
rectangles that represent the Fibonacci sequence, and spiral is drawn on
top of the rectangles. Besides that the rest of the graphic elements in
the slides are scarce to keep it clean

