%global pkg_name maven-common-artifact-filters
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:          %{?scl_prefix}%{pkg_name}
Version:       1.4
Release:       11.9%{?dist}
Summary:       Maven Common Artifact Filters
License:       ASL 2.0
Url:           http://maven.apache.org/shared/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
BuildArch:     noarch

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix_java_common}easymock
BuildRequires: %{?scl_prefix}maven-shared
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}plexus-containers-container-default
BuildRequires: %{?scl_prefix}maven-test-tools
BuildRequires: %{?scl_prefix}maven-plugin-testing-harness


%description
A collection of ready-made filters to control inclusion/exclusion of artifacts
during dependency resolution.

%package javadoc
Summary:       Javadoc for %{pkg_name}

%description javadoc
This package contains javadoc for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

# Maven 2 -> Maven 3
%pom_remove_dep :maven-project
%pom_add_dep org.apache.maven:maven-core
%pom_add_dep org.apache.maven:maven-compat
%pom_xpath_set "pom:dependency[pom:groupId[text()='org.apache.maven']]/pom:version" 3.0.4

# Workaround for rhbz#911365
%pom_add_dep aopalliance:aopalliance::test
%pom_add_dep cglib:cglib::test
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.4-11.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.4-11.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4-11
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-10
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Apr 11 2013 Michal Srb <msrb@redhat.com> - 1.4-9
- Enable tests again, they don't cause any trouble anywhere

* Thu Apr 11 2013 Michal Srb <msrb@redhat.com> - 1.4-8
- Run tests only in Fedora

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7
- Build with xmvn
- Bring back BR on maven-shared

* Mon Feb 18 2013 Tomas Radej <tradej@redhat.com> - 1.4-6
- Removed B/R on maven-shared (unnecessary + blocking maven-shared retirement)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Nov 22 2012 gil <puntogil@libero.it> 1.4-3
- resolves rhbz#879363 (NOTICE file is not installed with javadoc package)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 08 2012 gil cattaneo <puntogil@libero.it> 1.4-1
- initial rpm
