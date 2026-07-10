%global tl_name active-conf
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3a
Release:	%{tl_revision}.1
Summary:	Class for typesetting ACTIVE conference papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/conferences/active-conf
License:	lppl1.3a
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/active-conf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/active-conf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/active-conf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Active-conf is a class for typesetting papers for the Active conference
on noise and vibration control. It is initially intended for the 2006
conference in Adelaide, Australia. The class is based on article with
more flexible front-matter, and can be customised for conferences in
future years with a header file.

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
%dir %{_datadir}/texmf-dist/doc/latex/active-conf
%dir %{_datadir}/texmf-dist/source/latex/active-conf
%dir %{_datadir}/texmf-dist/tex/latex/active-conf
%dir %{_datadir}/texmf-dist/doc/latex/active-conf/example
%doc %{_datadir}/texmf-dist/doc/latex/active-conf/README
%doc %{_datadir}/texmf-dist/doc/latex/active-conf/active-conf.pdf
%doc %{_datadir}/texmf-dist/doc/latex/active-conf/example/active-example.ltx
%doc %{_datadir}/texmf-dist/doc/latex/active-conf/example/active-header-2006.tex
%doc %{_datadir}/texmf-dist/doc/latex/active-conf/example/header-logo-2006.eps
%doc %{_datadir}/texmf-dist/doc/latex/active-conf/example/header-logo-2006.pdf
%doc %{_datadir}/texmf-dist/source/latex/active-conf/active-conf.dtx
%doc %{_datadir}/texmf-dist/source/latex/active-conf/active-conf.ins
%{_datadir}/texmf-dist/tex/latex/active-conf/active-conf.cls
