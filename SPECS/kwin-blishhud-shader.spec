Name:           kwin-blishhud-shader
Version:        0.1.0
Release:        1%{?dist}
Summary:        KWin BlishHUD Shader
License:        MIT
URL:            https://github.com/FloFri/kwin-blishhud-shader
Source0:        kwin-blishhud-shader-%{version}.tar.gz

BuildArch:      x86_64

%description
A KWin shader for BlishHUD.

%prep
%autosetup -p1

%build
mkdir build
pushd build
cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release
make %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib64/qt6/plugins/kwin/effects/plugins
mkdir -p %{buildroot}/usr/share/kwin/shaders
install -Dm0755 build/bin/kwin/effects/plugins/kwin_effect_blishhud_shader.so %{buildroot}/usr/lib64/qt6/plugins/kwin/effects/plugins/kwin-blishhud-shader.so
install -Dm0755 data/transparent_black_core.frag %{buildroot}/usr/share/kwin/shaders/transparent_black_core.frag

%files
%{_libdir}/qt6/plugins/kwin/effects/plugins/kwin-blishhud-shader.so
%{_datadir}/kwin/shaders/transparent_black_core.frag

%changelog
* Mon Oct 30 2023 Your Name <your.email@example.com> - 0.1.0-1
- Initial package build.