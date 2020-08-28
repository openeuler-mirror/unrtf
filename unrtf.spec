Name:       unrtf
Summary:    RTF (Rich Text Format) to other formats converter
Version:    0.21.9
Release:    1
License:    GPLv3+
URL:        https://www.gnu.org/software/unrtf/unrtf.html
Source0:    http://ftp.gnu.org/gnu/unrtf/unrtf-%{version}.tar.gz
# http://hg.savannah.gnu.org/hgweb/unrtf/rev/3b16893a6406
Patch0001:           0001-Replace-all-instances-of-sprintf-with-snprintf-and-a.patch
BuildRequires:       gcc   automake
%description
UnRTF is a command-line program written in C which converts documents in
Rich Text Format (.rtf) to HTML, LaTeX, troff macros, and RTF itself.
Converting to HTML, it supports a number of features of Rich Text Format:
    * Changes in the text's font, size, weight (bold), and slant (italic)
    * Underlines and strikethroughs
    * Partial support for text shadowing, outlining, embossing, or engraving
    * Capitalizations
    * Superscripts and subscripts
    * Expanded and condensed text
    * Changes in the foreground and background colors
    * Conversion of special characters to HTML entities

%prep
%autosetup -p1

%build
./bootstrap
%configure
make %{?_smp_mflags}

%install
%make_install

%check
make check

%files
%doc README ChangeLog COPYING AUTHORS NEWS
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/%{name}/

%changelog
* Mon Aug 3 2020 fanjiachen <fanjiachen3@huawei.com> - 0.21.9-1
- package init
