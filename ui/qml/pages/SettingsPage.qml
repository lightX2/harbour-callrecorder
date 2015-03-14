/*
    Call Recorder for SailfishOS
    Copyright (C) 2014-2015 Dmitriy Purgin <dpurgin@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

import QtQuick 2.0
import Sailfish.Silica 1.0

Page {
    id: settingsPage

    SilicaListView {
        id: settingsView

        anchors.fill: parent

        header: PageHeader {
            title: qsTr('Settings')
        }

        model: ListModel {
            ListElement {
                title: 'Recording Daemon'
                img: 'qrc:/images/icon-m-daemon.png'
                target: 'Daemon.qml'
            }

            ListElement {
                title: 'Storage'
                img: 'qrc:/images/icon-m-sdcard.png'
                target: 'Storage.qml'
            }

            ListElement {
                title: 'Audio Settings'
                img: 'qrc:/images/icon-m-recording.png'
                target: 'AudioSettings.qml'
            }
        }

        delegate: ListItem {
            id: delegate

            contentHeight: content.height

            Row {
                id: content

                width: parent.width
                height: Theme.itemSizeSmall

                anchors.left: parent.left
                anchors.leftMargin: Theme.paddingLarge

                anchors.right: parent.right
                anchors.rightMargin: Theme.paddingLarge

                spacing: Theme.paddingLarge

                Image {
                    id: icon

                    height: parent.height

                    source: img

                    verticalAlignment: Image.AlignVCenter

                    fillMode: Image.Pad
                }

                Label {
                    id: label

                    text: title

                    height: parent.height

                    verticalAlignment: Text.AlignVCenter
                }
            }

            onClicked: {
                pageStack.push('settings/' + target)
            }

        }
    }
}
