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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains a theme for Beamer which is referenced as "Cuerna"
inside beamer and has four basic colour themes. The title page shows
rectangles that represent the Fibonacci sequence, and spiral is drawn on
top of the rectangles. Besides that the rest of the graphic elements in
the slides are scarce to keep it clean

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-cuerna
%dir %{_datadir}/texmf-dist/source/latex/beamertheme-cuerna
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-cuerna
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-cuerna/pictures
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-cuerna/README
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-cuerna/beamertheme-cuerna.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-cuerna/pictures/bluesimplex.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-cuerna/pictures/bluesimplexexample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-cuerna/pictures/brickexample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-cuerna/pictures/defaultexample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-cuerna/pictures/lettuceexample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-cuerna/template.tex
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-cuerna/beamertheme-cuerna.dtx
%doc %{_datadir}/texmf-dist/source/latex/beamertheme-cuerna/beamertheme-cuerna.ins
%{_datadir}/texmf-dist/tex/latex/beamertheme-cuerna/beamercolorthemeCuerna.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-cuerna/beamercolorthemebluesimplex.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-cuerna/beamercolorthemebrick.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-cuerna/beamercolorthemelettuce.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-cuerna/beamerinnerthemeCuerna.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-cuerna/beamerouterthemeCuerna.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-cuerna/beamerthemeCuerna.sty
