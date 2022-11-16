Name:		texlive-ellipse
Version:	39025
Release:	1
Summary:	Draw ellipses and elliptical arcs using the standard LaTeX2e picture environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ellipse
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipse.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipse.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ellipse.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Draw ellipses and elliptical arcs using the standard LaTeX2e
picture environment.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ellipse
%{_texmfdistdir}/tex/latex/ellipse
%doc %{_texmfdistdir}/doc/latex/ellipse

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
