# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-callrecorder

# >> macros
%define __provides_exclude_from ^%{_datadir}/.*$
%define __requires_exclude ^libarchive|libcontactcache-qt5|libcallrecorder|libqtpulse|libnemocontacts.*$
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Call Recorder for SailfishOS
Version:    0.7.1
Release:    5
Group:      Applications/Communications
License:    GPLv3
URL:        https://github.com/dpurgin/harbour-callrecorder
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-callrecorder.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   qt5-qtmultimedia-plugin-audio-pulseaudio
Requires:   qt5-qtmultimedia-plugin-mediaservice-gstmediaplayer
Requires:   nemo-qml-plugin-dbus-qt5
BuildRequires:  pkgconfig(Qt5Contacts)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Versit)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(qofono-qt5)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(mce)
BuildRequires:  pkgconfig(mlocale5)
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(qtcontacts-sqlite-qt5-extensions) >= 0.2.1
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  nemo-qml-plugin-dbus-qt5
BuildRequires:  qtcontacts-sqlite-qt5
BuildRequires:  desktop-file-utils
BuildRequires:  libsailfishapp-devel

%description
Native call recorder for SailfishOS


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
%post
echo "Reloading systemd..."
systemctl-user daemon-reload

# install
if [ $1 = 1 ]; then
    echo "Enabling service..."
    mkdir -p /home/nemo/.config/systemd/user/post-user-session.target.wants
    chown --recursive nemo:nemo /home/nemo/.config/systemd

    systemctl-user enable harbour-callrecorderd

    echo "Starting service..."
    systemctl-user start harbour-callrecorderd
# upgrade
elif [ $1 = 2 ]; then
    echo "Starting service..."
    chown --recursive nemo:nemo /home/nemo/.config/systemd
    systemctl-user try-restart harbour-callrecorderd
fi
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

# >> uninstall pre
%preun

#uninstall
if [ $1 = 0 ]; then
    echo "Stopping service..."
    systemctl-user stop harbour-callrecorderd
fi
# << uninstall pre

%files
%defattr(-,root,root,-)
%attr(755,-,-) %{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_libdir}/systemd/user/%{name}d.service
# >> files
# << files
