%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name core

Name: cutefish-%{component_name}
Version: 0.7
Release: 2%{?dist}
License: GPLv3
Summary: System components, backend, and session files for Cutefish Desktop

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: polkit-devel polkit-qt5-1-devel libSM-devel
BuildRequires: pkgconfig(xorg-libinput)
BuildRequires: libXcursor-devel
BuildRequires: xcb-util-devel xcb-util-image-devel xcb-util-keysyms-devel libXtst-devel
BuildRequires: libxcb-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: qt5-qtbase-devel qt5-qtx11extras-devel qt5-qttools-devel qt5-qtdeclarative-devel qt5-qtquickcontrols2-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: fishui-devel
BuildRequires: xorg-x11-drv-synaptics-devel
BuildRequires: libX11-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kidletime-devel
BuildRequires: xorg-x11-server-devel
Requires: pulseaudio-daemon
Requires: fishui

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: https://gitlab.ultramarine-linux.org/dist-pkgs/cutefish-desktop/-/raw/master/patches/cutefish-core/0001-change-default-wallpaper.patch

%description
System components, backend, and session files for the Cutefish Desktop

%prep
%setup -qn %{component_name}-%{version}
%patch0 -p1

%build
%{set_build_flags}
mkdir build
pushd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd

%files
%{_bindir}/chotkeys
%{_bindir}/cupdatecursor
%{_bindir}/cutefish-cpufreq
%{_bindir}/cutefish-polkit-agent
%{_bindir}/cutefish-powerman
%{_bindir}/cutefish-screen-brightness
%{_bindir}/cutefish-session
%{_bindir}/cutefish-settings-daemon
%{_bindir}/cutefish-shutdown
%{_bindir}/cutefish-xembedsniproxy
%{_datadir}/cutefish-polkit-agent
%{_datadir}/cutefish-settings-daemon
%{_datadir}/cutefish-shutdown
%{_datadir}/xsessions/cutefish-xsession.desktop
%{_sysconfdir}/xdg/autostart/cutefish-polkit-agent.desktop
%{_bindir}/cutefish-gmenuproxy
%{_bindir}/cutefish-notificationd
%{_bindir}/cutefish-sddm-helper
/usr/lib/systemd/user/cutefish-gmenuproxy.service
%{_datadir}/cutefish-notificationd/
%{_datadir}/polkit-1/actions/com.cutefish*
%{_sysconfdir}/cutefish