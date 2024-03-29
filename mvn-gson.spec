#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-gson
Version  : 2.2.4
Release  : 6
URL      : https://repo1.maven.org/maven2/com/google/code/gson/gson/2.2.4/gson-2.2.4.jar
Source0  : https://repo1.maven.org/maven2/com/google/code/gson/gson/2.2.4/gson-2.2.4.jar
Source1  : https://repo1.maven.org/maven2/com/google/code/gson/gson-parent/2.7/gson-parent-2.7.pom
Source2  : https://repo1.maven.org/maven2/com/google/code/gson/gson-parent/2.8.5/gson-parent-2.8.5.pom
Source3  : https://repo1.maven.org/maven2/com/google/code/gson/gson/2.2.4/gson-2.2.4.pom
Source4  : https://repo1.maven.org/maven2/com/google/code/gson/gson/2.3.1/gson-2.3.1.jar
Source5  : https://repo1.maven.org/maven2/com/google/code/gson/gson/2.3.1/gson-2.3.1.pom
Source6  : https://repo1.maven.org/maven2/com/google/code/gson/gson/2.7/gson-2.7.jar
Source7  : https://repo1.maven.org/maven2/com/google/code/gson/gson/2.7/gson-2.7.pom
Source8  : https://repo1.maven.org/maven2/com/google/code/gson/gson/2.8.5/gson-2.8.5.jar
Source9  : https://repo1.maven.org/maven2/com/google/code/gson/gson/2.8.5/gson-2.8.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-gson-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-gson package.
Group: Data

%description data
data components for the mvn-gson package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.2.4
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.2.4/gson-2.2.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson-parent/2.7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson-parent/2.7/gson-parent-2.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson-parent/2.8.5
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson-parent/2.8.5/gson-parent-2.8.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.2.4
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.2.4/gson-2.2.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.3.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.3.1/gson-2.3.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.3.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.3.1/gson-2.3.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.7
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.7/gson-2.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.7
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.7/gson-2.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.8.5
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.8.5/gson-2.8.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.8.5
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/google/code/gson/gson/2.8.5/gson-2.8.5.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/google/code/gson/gson-parent/2.7/gson-parent-2.7.pom
/usr/share/java/.m2/repository/com/google/code/gson/gson-parent/2.8.5/gson-parent-2.8.5.pom
/usr/share/java/.m2/repository/com/google/code/gson/gson/2.2.4/gson-2.2.4.jar
/usr/share/java/.m2/repository/com/google/code/gson/gson/2.2.4/gson-2.2.4.pom
/usr/share/java/.m2/repository/com/google/code/gson/gson/2.3.1/gson-2.3.1.jar
/usr/share/java/.m2/repository/com/google/code/gson/gson/2.3.1/gson-2.3.1.pom
/usr/share/java/.m2/repository/com/google/code/gson/gson/2.7/gson-2.7.jar
/usr/share/java/.m2/repository/com/google/code/gson/gson/2.7/gson-2.7.pom
/usr/share/java/.m2/repository/com/google/code/gson/gson/2.8.5/gson-2.8.5.jar
/usr/share/java/.m2/repository/com/google/code/gson/gson/2.8.5/gson-2.8.5.pom
