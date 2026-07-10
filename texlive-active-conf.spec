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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Active-conf is a class for typesetting papers for the Active conference
on noise and vibration control. It is initially intended for the 2006
conference in Adelaide, Australia. The class is based on article with
more flexible front-matter, and can be customised for conferences in
future years with a header file.

