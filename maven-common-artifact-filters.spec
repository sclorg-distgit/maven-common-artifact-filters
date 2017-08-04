%{?scl:%scl_package maven-common-artifact-filters}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-common-artifact-filters
Version:        3.0.1
Release:        2.2%{?dist}
Summary:        Maven Common Artifact Filters
License:        ASL 2.0
URL:            http://maven.apache.org/shared/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

Patch0:         0001-Remove-Maven-3.0-specific-code.patch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  %{?scl_prefix}mvn(org.easymock:easymock)
BuildRequires:  %{?scl_prefix}mvn(org.eclipse.aether:aether-api)
BuildRequires:  %{?scl_prefix}mvn(org.eclipse.aether:aether-util)

%description
A collection of ready-made filters to control inclusion/exclusion of artifacts
during dependency resolution.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
This package contains javadoc for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q
%patch0 -p1

# We don't want to support legacy Maven versions (older than 3.1)
%pom_remove_dep org.sonatype.sisu:
%pom_remove_dep org.sonatype.aether:
find -name SonatypeAether\*.java -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 3.0.1-2.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 3.0.1-2.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 02 2016 Michael Simacek <msimacek@redhat.com> - 3.0.1-1
- Update to upstream version 3.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0-0.1.20151012svn1708080
- Update to upstream 3.0 snapshot (svn revision 1708080)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 gil cattaneo <puntogil@libero.it> 1.4-15
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-13
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-12
- Fix unowned directory

* Thu Aug 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11
- Migrate from easymock 1 to easymock 3
- Resolves: rhbz#1002476

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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
