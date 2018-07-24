Summary:	A program to manipulate Intel microcode update collections
Summary(pl.UTF-8):	Program do operowania na zbiorach uaktualnień mikrokodu Intela
Name:		iucode-tool
Version:	2.3.1
Release:	1
License:	GPL v2+
Group:		Base
Source0:	http://http.debian.net/debian/pool/contrib/i/iucode-tool/%{name}_%{version}.orig.tar.xz
# Source0-md5:	63b33cc0ea1f8c73b443412abbf39d6f
URL:		https://gitlab.com/iucode-tool/iucode-tool
ExclusiveArch:	%{ix86} %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iucode_tool is a program to manipulate microcode update collections
for Intel(R) i686 and X86-64 system processors, and prepare them for
use by the Linux kernel.

%description -l en.UTF-8
iucode_tool is a program to manipulate microcode update collections
for Intel® i686 and X86-64 system processors, and prepare them for use
by the Linux kernel.

%description -l pl.UTF-8
iucode_tool to program do operowania na zbiorach uaktualnień dla
procesorów Intela rodziny i686 i X86-64 oraz przygotowywania ich do
użycia przez jądro Linuksa.

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
%doc AUTHORS CONTRIBUTING ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/iucode_tool
%{_mandir}/man8/iucode_tool.8*
