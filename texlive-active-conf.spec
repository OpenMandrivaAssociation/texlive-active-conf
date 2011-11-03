# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/conferences/active-conf
# catalog-date 2008-05-24 14:41:17 +0200
# catalog-license lppl
# catalog-version 0.3a
Name:		texlive-active-conf
Version:	0.3a
Release:	1
Summary:	Class for typesetting ACTIVE conference papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/conferences/active-conf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/active-conf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/active-conf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/active-conf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Active-conf is a class for typesetting papers for the Active
conference on noise and vibration control. It is initially
intended for the 2006 conference in Adelaide, Australia. The
class is based on article with more flexible front-matter, and
can be customised for conferences in future years with a header
file.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
