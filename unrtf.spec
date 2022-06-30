Name:                unrtf
Summary:             RTF (Rich Text Format) to other formats converter
Version:             0.21.10
Release:             1
License:             GPLv3+
URL:                 https://www.gnu.org/software/unrtf/unrtf.html
Source0:             http://ftp.gnu.org/gnu/unrtf/unrtf-%{version}.tar.gz
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
* Sun Jun 12 2022 YukariChiba <i@0x7f.cc> - 0.21.10-1
- Upgrade version to 0.21.10

* Mon Aug 3 2020 fanjiachen <fanjiachen3@huawei.com> - 0.21.9-1
- package init
