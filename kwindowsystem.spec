#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kwindowsystem
Version  : 5.51.0
Release  : 6
URL      : https://download.kde.org/stable/frameworks/5.51/kwindowsystem-5.51.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.51/kwindowsystem-5.51.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.51/kwindowsystem-5.51.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kwindowsystem-data = %{version}-%{release}
Requires: kwindowsystem-lib = %{version}-%{release}
Requires: kwindowsystem-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libXrender-dev
BuildRequires : libxcb-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : xcb-util-keysyms-dev

%description
# KWindowSystem
Access to the windowing system
## Introduction
Convenience access to certain properties and features of the windowing system.

%package data
Summary: data components for the kwindowsystem package.
Group: Data

%description data
data components for the kwindowsystem package.


%package dev
Summary: dev components for the kwindowsystem package.
Group: Development
Requires: kwindowsystem-lib = %{version}-%{release}
Requires: kwindowsystem-data = %{version}-%{release}
Provides: kwindowsystem-devel = %{version}-%{release}

%description dev
dev components for the kwindowsystem package.


%package lib
Summary: lib components for the kwindowsystem package.
Group: Libraries
Requires: kwindowsystem-data = %{version}-%{release}
Requires: kwindowsystem-license = %{version}-%{release}

%description lib
lib components for the kwindowsystem package.


%package license
Summary: license components for the kwindowsystem package.
Group: Default

%description license
license components for the kwindowsystem package.


%prep
%setup -q -n kwindowsystem-5.51.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539618517
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539618517
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwindowsystem
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kwindowsystem/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/as/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/si/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/te/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kwindowsystem5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kwindowsystem5_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KWindowSystem/KKeyServer
/usr/include/KF5/KWindowSystem/KSelectionOwner
/usr/include/KF5/KWindowSystem/KSelectionWatcher
/usr/include/KF5/KWindowSystem/KStartupInfo
/usr/include/KF5/KWindowSystem/KUserTimestamp
/usr/include/KF5/KWindowSystem/KWindowEffects
/usr/include/KF5/KWindowSystem/KWindowInfo
/usr/include/KF5/KWindowSystem/KWindowSystem
/usr/include/KF5/KWindowSystem/KXMessages
/usr/include/KF5/KWindowSystem/NETWM
/usr/include/KF5/KWindowSystem/config-kwindowsystem.h
/usr/include/KF5/KWindowSystem/fixx11h.h
/usr/include/KF5/KWindowSystem/kkeyserver.h
/usr/include/KF5/KWindowSystem/kkeyserver_x11.h
/usr/include/KF5/KWindowSystem/kmanagerselection.h
/usr/include/KF5/KWindowSystem/kselectionowner.h
/usr/include/KF5/KWindowSystem/kselectionwatcher.h
/usr/include/KF5/KWindowSystem/kstartupinfo.h
/usr/include/KF5/KWindowSystem/kusertimestamp.h
/usr/include/KF5/KWindowSystem/kwindoweffects.h
/usr/include/KF5/KWindowSystem/kwindowinfo.h
/usr/include/KF5/KWindowSystem/kwindowsystem.h
/usr/include/KF5/KWindowSystem/kwindowsystem_export.h
/usr/include/KF5/KWindowSystem/kxmessages.h
/usr/include/KF5/KWindowSystem/netwm.h
/usr/include/KF5/KWindowSystem/netwm_def.h
/usr/include/KF5/KWindowSystem/private/kwindoweffects_p.h
/usr/include/KF5/KWindowSystem/private/kwindowinfo_p.h
/usr/include/KF5/KWindowSystem/private/kwindowsystem_p.h
/usr/include/KF5/KWindowSystem/private/kwindowsystemplugininterface_p.h
/usr/include/KF5/kwindowsystem_version.h
/usr/lib64/cmake/KF5WindowSystem/KF5WindowSystemConfig.cmake
/usr/lib64/cmake/KF5WindowSystem/KF5WindowSystemConfigVersion.cmake
/usr/lib64/cmake/KF5WindowSystem/KF5WindowSystemTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5WindowSystem/KF5WindowSystemTargets.cmake
/usr/lib64/libKF5WindowSystem.so
/usr/lib64/qt5/mkspecs/modules/qt_KWindowSystem.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5WindowSystem.so.5
/usr/lib64/libKF5WindowSystem.so.5.51.0
/usr/lib64/qt5/plugins/kf5/org.kde.kwindowsystem.platforms/KF5WindowSystemWaylandPlugin.so
/usr/lib64/qt5/plugins/kf5/org.kde.kwindowsystem.platforms/KF5WindowSystemX11Plugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwindowsystem/COPYING.LIB
