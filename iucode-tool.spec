Summary:	A program to manipulate Intel microcode update collections
Name:		iucode-tool
Version:	2.2
Release:	1
License:	GPL v2+
Group:		Base
URL:		https://gitlab.com/iucode-tool/iucode-tool
Source0:	http://http.debian.net/debian/pool/contrib/i/iucode-tool/%{name}_%{version}.orig.tar.xz
# Source0-md5:	f6cc22c89b66e4f1ff87af36197cdfaa
ExclusiveArch:	%{ix86} x86_64

%description
iucode_tool is a program to manipulate microcode update collections
for Intel® i686 and X86-64 system processors, and prepare them for use
by the Linux kernel.

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
