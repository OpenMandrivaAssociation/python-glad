%global srcname glad

Name:           python-%{srcname}
Version:        2.0.2
Release:        1
Summary:        Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator
# Mostly MIT, ASL 2.0 for Khronos and EGL specifications/headers.
License:        MIT and ASL 2.0
URL:            https://github.com/Dav1dde/glad
Source0:        https://files.pythonhosted.org/packages/source/g/glad/glad-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
Requires:       python3dist(setuptools)

%description
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.


%package -n     %{srcname}
Summary:        %{summary}

Requires:       python3dist(glad)

%description -n %{srcname}
Glad uses the official Khronos-XML specs to generate a GL/GLES/EGL/GLX/WGL
Loader made for your needs.

%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Fix shebang
sed -i -e '/^#!\//, 1d' %{srcname}/__main__.py

%build
%py_build

%install
%py_install

%files -n %{srcname}
%{_bindir}/glad

%files
%{python_sitelib}/%{srcname}
%{python_sitelib}/%{srcname}-%{version}-py%{python_version}.egg-info
