# revision 20408
# category Package
# catalog-ctan /fonts/jamtimes
# catalog-date 2009-11-07 09:52:42 +0000
# catalog-license other-free
# catalog-version 1.12
Name:		texlive-jamtimes
Version:	1.12
Release:	1
Summary:	Expanded Times Roman fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/jamtimes
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jamtimes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jamtimes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers LaTeX support for the expanded Times Roman
font, which has been used for many years in the Journal
d'Analyse Mathematique. Mathematics support is based on the
Belleek fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/jamtimes/jtm.map
%{_texmfdistdir}/fonts/tfm/public/jamtimes/blsy.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmb7tv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmb8cv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmb8rv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmb8tv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbc7tv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbc8tv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbi7me.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbi7tv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbi8cv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbi8rv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbi8tv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbo7tv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbo8cv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbo8rv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmbo8tv.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr7tc.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr7te.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr7tw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr7ye.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr7yoe.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr8cc.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr8ce.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr8cw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr8rc.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr8re.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr8rw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr8tc.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr8te.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmr8tw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmrc7te.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmrc7tw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmrc8te.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmrc8tw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmri7me.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmri7te.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmri7tw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmri7ze.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmri8ce.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmri8cw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmri8re.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmri8rw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmri8te.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmri8tw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmro7te.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmro7tw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmro8ce.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmro8cw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmro8re.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmro8rw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmro8te.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/jtmro8tw.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/ptmb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/ptmbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/ptmr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/ptmri8a.tfm
%{_texmfdistdir}/fonts/tfm/public/jamtimes/rblmi.tfm
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmb7tv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmb8cv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmb8tv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmbc7tv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmbc8tv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmbi7me.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmbi7tv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmbi8cv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmbi8tv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmbo7tv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmbo8cv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmbo8tv.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmr7tc.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmr7te.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmr7tw.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmr7ye.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmr8cc.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmr8ce.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmr8cw.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmr8tc.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmr8te.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmr8tw.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmrc7te.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmrc7tw.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmrc8te.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmrc8tw.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmri7me.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmri7te.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmri7tw.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmri8ce.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmri8cw.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmri8te.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmri8tw.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmro7te.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmro7tw.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmro8ce.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmro8cw.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmro8te.vf
%{_texmfdistdir}/fonts/vf/public/jamtimes/jtmro8tw.vf
%{_texmfdistdir}/tex/latex/jamtimes/jamtimes.sty
%{_texmfdistdir}/tex/latex/jamtimes/omljtm.fd
%{_texmfdistdir}/tex/latex/jamtimes/omsjtm.fd
%{_texmfdistdir}/tex/latex/jamtimes/ot1jtm.fd
%{_texmfdistdir}/tex/latex/jamtimes/t1jtm.fd
%{_texmfdistdir}/tex/latex/jamtimes/ts1jtm.fd
%doc %{_texmfdistdir}/doc/latex/jamtimes/README
%doc %{_texmfdistdir}/doc/latex/jamtimes/jamtimes.bib
%doc %{_texmfdistdir}/doc/latex/jamtimes/jamtimes.dtx
%doc %{_texmfdistdir}/doc/latex/jamtimes/jamtimes.ins
%doc %{_texmfdistdir}/doc/latex/jamtimes/jamtimes.pdf
%doc %{_texmfdistdir}/doc/latex/jamtimes/mathsample.pdf
%doc %{_texmfdistdir}/doc/latex/jamtimes/mathsample.tex
%doc %{_texmfdistdir}/doc/latex/jamtimes/mathsample_ps.pdf
%doc %{_texmfdistdir}/doc/latex/jamtimes/textsample.pdf
%doc %{_texmfdistdir}/doc/latex/jamtimes/textsample.tex
%doc %{_texmfdistdir}/doc/latex/jamtimes/textsample_ps.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
