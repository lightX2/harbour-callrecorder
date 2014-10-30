harbour-callrecorder
====================

Native call recorder for Jolla's SailfishOS.

**This is application requires the latest opt-in SailfishOS update (update9, SailfishOS 1.1). If you are unsure, wait for its general availability.**

**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [harbour-callrecorder](#user-content-harbour-callrecorder)
	- [Requirements](#user-content-requirements)
	- [Installation from OpenRepos](#user-content-installation-from-openrepos)
	- [Installation from RPM](#user-content-installation-from-rpm)
	- [Installation from sources](#user-content-installation-from-sources)
	- [Usage](#user-content-usage)
		- [Storage](#user-content-storage)
		- [Audio Format](#user-content-audio-format)
		- [Call Recorder UI](#user-content-call-recorder-ui)
			- [Start page -- Events](#user-content-start-page----events)
			- [Details Page](#user-content-details-page)
			- [About Page](#user-content-about-page)
	- [Known Issues](#user-content-known-issues)
		- [Moving call to speaker when the number is still dialled](#user-content-moving-call-to-speaker-when-the-number-is-still-dialled)
		- [Switching from loudspeaker to earpiece may cause 500ms lack in the recording (doesn't affect the call itself)](#user-content-switching-from-loudspeaker-to-earpiece-may-cause-500ms-lack-in-the-recording-doesnt-affect-the-call-itself)
	- [Troubleshooting](#user-content-troubleshooting)
		- [The calls are not recorded](#user-content-the-calls-are-not-recorded)
		- [The UI application shows white screen](#user-content-the-ui-application-shows-white-screen)
	- [FAQ](#user-content-faq)
		- [Does it require developer mode?](#user-content-does-it-require-developer-mode)
	- [Contacts](#user-content-contacts)

##Requirements

* SailfishOS 1.1 or later
* Allowance for unrusted software installation

##Installation from OpenRepos

1. Install Warehouse application from [OpenRepos](https://openrepos.net/content/basil/warehouse-sailfishos)
2. Search for 'Call Recorder' in Warehouse
3. Install it.

##Installation from RPM

1. Enable untrusted software installation at Settings -> Untrusted software.
2. Download the latest version RPM package which is located at https://dpurgin.github.io/. This page is best accessed from your Jolla device. The package you need *doesn't* say `debuginfo` or `debugsource` in its name.
3. If you have downloaded the package with the Jolla Browser, go to Settings -> Transfers and tap on the downloaded package, it prompts for installation after a while.
4. Tap on `Install` when prompted.
5. After installation is successful, a notification appears.
6. Make sure `Call Recorder` has appeared in the list of applications.
7. Make a call and check if the recording has appeared in `Call Recorder` application. If it hasn't, go to Troubleshooting section.

You don't need to have the UI application running all the time to have your calls recorded. They always are as soon as the service is enabled. 

##Installation from sources

This section assumes you are familiar with SailfishOS SDK and able to deploy your own project to a device. The project was developed and tested with SDK version 1407.

1. Clone the project from master branch or a tag to a directory of your choice. The master branch will always contain compilable bleeding edge code.
2. Open harbour-callrecorder.pro in SailfishOS SDK, configure the project to use armv7hl and i486 targets.
3. Run qmake, build, deploy. 

Luckily, all the dependencies should be resolved and downloaded automatically by the SDK. If not, just follow the error messages.

##Usage

The harbour-callrecorder is designed for unattended usage. Once properly installed, it records every GSM call you make or receive. The UI application doesn't need to be run to make this happen. Moreover, think of UI application as the way to access recorded calls only.

###Storage

Data generated by the application is stored at writable location under `/home/nemo/.local/share/kz.dpurgin/harbour-callrecorder/` (further referred to as `$DATA`).

All the recordings made by the daemon are stored at `$DATA/data`. Currently, there's no way to rebase the archive except making a symlink in this location. 

List of recordings with their properties is stored in a database at `$DATA/callrecorder.db`. Please refer to `libcallrecorder/database.cpp`, `Database::Database()` for database structure.

###Audio Format
The recordings are currently encoded to FLAC, 44.1 kHz, mono, 16-bit LE, compression level 8. These settings are hardcoded and subject to change in future. 

###Call Recorder UI

This application is a simple front-end for accessing the recordings which were made since the installation and property configuring harbour-callrecorder.

####Start page -- Events

This is a list of all the recordings made by the call recording daemon. Each list item contains call type marker (incoming/outgoing), caller/callee ID, date and time, recording duration and file size. Tap on item gets to Details page. 

Pull-down menu provides access to About page.

####Details Page

This page allows to listen to the recording. Player is situated in the lower part of the page. If an error occured, player is replaced with textual error description. The recording can be seeked through using the progress bar above the Play button.

####About Page

Pretty self-explanatory. Click on the button at the bottom to view short license notice. Full license text is installed to `/usr/share/harbour-callrecorder/LICENSE`.

##Known Issues

###Moving call to speaker when the number is still dialled

If the call is started and put on speaker before the other party takes the call, the call remains on speaker during dialing tones but goes back to earpiece as soon as the other party takes the call, although the speaker icon remains highlit. 

**Workaround**

Tap on the speaker icon twice to get it back to speaker *or* move the call to speaker after the other party takes the call.

###Switching from loudspeaker to earpiece may cause 500ms lack in the recording (doesn't affect the call itself)

This is due to asynchronous nature of PulseAudio events and internals of call recording process. It just needs some time to decide if the sound card really should go to other mode.

**Workaround**

None. Should be treated more as a feature. The 500ms switch time may change to lower values in future based on user experience.

###The other party is not recorded if the call is on headphones or bluetooth

Unfortunately this feature is still WIP.

**Workaround**

None. Do not reroute calls except to loudspeaker, if possible.

**There has been a report on TMO that BT switching works fine and the call gets recorded**

##Troubleshooting

### The calls are not recorded

Please check if the service is enabled and running. You will need the Terminal application. Issue the following command in terminal (mind 'd' at the end and you don't need to enter $ sign, it's already there):

```
$ systemctl --user status harbour-callrecorderd
```

If the output looks like this (mind `disabled` at the second line):

```
harbour-callrecorderd.service - Call Recorder Daemon
   Loaded: loaded (/usr/lib/systemd/user/harbour-callrecorderd.service; disabled)
   Active: inactive (dead)
```

then try (mind `d` at the end):

```
$ systemctl --user enable harbour-callrecorderd
$ systemctl --user start harbour-callrecorderd
```

If the service is up and running, it should say something like this:

```
harbour-callrecorderd.service - Call Recorder Daemon
   Loaded: loaded (/usr/lib/systemd/user/harbour-callrecorderd.service; enabled)
   Active: active (running) since Mon 2014-10-27 00:02:12 ALMT; 19s ago
 Main PID: 1136 (harbour-callrec)
   CGroup: /user.slice/user-100000.slice/user@100000.service/harbour-callrecorderd.service
           └─1136 /usr/bin/harbour-callrecorderd
```

### The UI application shows white screen

Check if you have SailfishOS 1.1 (Settings -> Sailfish OS updates).

##FAQ

###Does it require developer mode?
Generally, no. If you run into trouble, you might need the Terminal application to diagnose. 

#Contacts
If you have any questions not covered by this file, please contact me at <dpurgin@gmail.com>
