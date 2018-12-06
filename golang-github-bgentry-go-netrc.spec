# https://github.com/bgentry/go-netrc
%global goipath         github.com/bgentry/go-netrc
%global commit          9fd32a8b3d3d3f9d43c341bfe098430e07609480

%global common_description %{expand:
A Golang package for reading and writing netrc files. This package can parse
netrc files, make changes to them, and then serialize them back to netrc
format, while preserving any whitespace that was present in the source file.}

%gometa

Name:           golang-github-bgentry-go-netrc
Version:        0
Release:        0.6%{?dist}
Summary:        A netrc file parser for the Go programming language
# Detected licences
# - Expat License at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20181112git9fd32a8
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20140422git9fd32a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20140422git9fd32a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0-0.3.20140422git9fd32a8
- Add commit date to release.

* Fri Aug 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0-0.2.git9fd32a8
- Fix summary line.
- Add documentation to subpackage.

* Sun May 15 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-0.1.git9fd32a8
- Initial package
