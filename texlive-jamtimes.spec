%global tl_name jamtimes
%global tl_revision 20408

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.12
Release:	%{tl_revision}.1
Summary:	Expanded Times Roman fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/jamtimes
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jamtimes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jamtimes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers LaTeX support for the expanded Times Roman font,
which has been used for many years in the Journal d'Analyse
Mathematique. Mathematics support is based on the Belleek fonts.

