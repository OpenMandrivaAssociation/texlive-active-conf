Name:		texlive-active-conf
Version:	15878
Release:	2
Summary:	Class for typesetting ACTIVE conference papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/conferences/active-conf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/active-conf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/active-conf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/active-conf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Active-conf is a class for typesetting papers for the Active
conference on noise and vibration control. It is initially
intended for the 2006 conference in Adelaide, Australia. The
class is based on article with more flexible front-matter, and
can be customised for conferences in future years with a header
file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/active-conf/active-conf.cls
%doc %{_texmfdistdir}/doc/latex/active-conf/README
%doc %{_texmfdistdir}/doc/latex/active-conf/active-conf.pdf
%doc %{_texmfdistdir}/doc/latex/active-conf/example/active-example.ltx
%doc %{_texmfdistdir}/doc/latex/active-conf/example/active-header-2006.tex
%doc %{_texmfdistdir}/doc/latex/active-conf/example/header-logo-2006.eps
%doc %{_texmfdistdir}/doc/latex/active-conf/example/header-logo-2006.pdf
#- source
%doc %{_texmfdistdir}/source/latex/active-conf/active-conf.dtx
%doc %{_texmfdistdir}/source/latex/active-conf/active-conf.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
