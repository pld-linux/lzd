Summary:	Simplified decompressor for lzip files
Summary(pl.UTF-8):	Uproszczony dekompresor plików lzip
Name:		lzd
Version:	1.4
Release:	1
License:	Free
Group:		Applications/Archiving
Source0:	http://download.savannah.gnu.org/releases/lzip/lzd/%{name}-%{version}.tar.lz
# Source0-md5:	77539b5bb4ee2eb7cf1ce68ba124a253
URL:		http://savannah.nongnu.org/projects/lzip/
BuildRequires:	libstdc++-devel
BuildRequires:	lzip
BuildRequires:	tar >= 1:1.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lzd is a simplified decompressor for lzip files with an educational
purpose. Studying its source is a good first step to understand how
lzip works. It is not safe to use lzd for any real work.

%description -l pl.UTF-8
Lzd to uproszczony dekompresor plików lzip napisany z myślą o celach
edukacyjnych. Studiowanie jego źródeł to pierwszy krok do zrozumienia,
jak działa lzip. Używanie lzd do rzeczywistych zastosowań nie jest
bezpieczne.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/lzd
