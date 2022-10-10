---
title: 'Keyboard Shortcuts and Run Commands => Use Them!'
date: 2016-05-27T22:21:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/keyboard-shortcuts-and-run-commands-use-them/
categories:
  - SysAdmin
  - Windows
---
<!--more-->

### Description:

Please, please, please refer to this page often! Keyboard shortcuts are not only useful for getting things done faster, but often represent a sense of professionalism when working with customers. Many times when I remote in or sit in front of a computer and start running run commands or command prompt commands, the end user will compliment me saying &#8220;finally, someone who knows what they are doing!&#8221; 

I would start by creating a spreadsheet of all the commands (manually type them so you can start to memorize them), and then create a most used list to reference often. Print a small page and keep in your cubicle or take it with you if you are an onsite technician => you won't regret it!


### To Resolve:

1. First, my favorite Run Commands:

   - `mstsc` - Used to remote to other machines inside and outside of your network. For a full list of switches, see [here](http://technet.microsoft.com/en-us/library/cc753907.aspx).

     - `mstsc /f` - Enters a RDP session in full screen.  
     - `mstsc /admin` - Enters a RDP session as a console session. Note this used to be mstsc /console. See [here](http://blogs.msdn.com/b/rds/archive/2007/12/17/changes-to-remote-administration-in-windows-server-2008.aspx) for details.

   - `compmgmt.msc` => Computer Management => Used to many common tasks, works best if the computer is on a workgroup. It brings up Users and Computers (`lusrmgr.msc`), Device Manager (`devmgmt.msc`), Event Viewer (`eventvwr.msc`), Services (`services.msc`), and others. If the computer is on a domain, you will need to use the &#8220;Administrative Tools&#8221; on the DC to other tasks such as adding, deleting, or modifying users/ groups in AD (Active Directory).

   - `resmon` => Resource Monitor => Lets you see in real time what the status is of the CPU, Memory, Disk, and Network in more details that your common Task Manager (taskmgr).

2. Okay, now the list of Run Commands: (Keyboard Keys: [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) + *command from below* )

   |Application Launched| Command|
   |:---:|:---:|
   |Add/ Remove Programs|appwiz.cpl|
   |Action Center/ Security Center Alerts|wscui.cpl|
   |Admin Tools|control admintools|
   |Command Prompt|cmd|
   |Computer Management|compmgmt.msc|
   |Control Panel|control|
   |Device Manager|devmgmt.msc|
   |Firewall Properties|firewall.cpl|
   |Folder Properties|control folders|
   |Group Policy Editor|gpedit.msc|
   |Power Settings|powercfg.cpl|
   |Internet Properties|inetcpl.cpl|
   |Local Security Settings|secpol.msc|
   |Local Users and Groups|lusrmgr.msc|
   |Microsoft Management Console|mmc|
   |Network Connections|ncpa.cpl|
   |Disk Cleanup|cleanmgr.exe|
   |Paint|mspaint|
   |Power Options|powercfg.cpl|
   |Notepad|notepad|
   |Registry Editor|regedit|
   |Remote Desktop Connection|mstsc|
   |Scheduled Tasks|control schedtasks|
   |System Configuration Monitor|msconfig|
   |System Info|dxdiag|
   |System Info (my preference)|msinfo32|
   |System Properties|sysdm.cpl|
   |Resultant Set Of Policies|rsop.msc|
   |Devices and Printers|control printers|
   |Folder Properties|control folders|
   |Windows Updates|control update, wuapp (w7)|
   |AD Domains and Trusts|domain.msc|
   |Active Directory Management|admgmt.msc|
   |AD Sites and Services|dssite.msc|
   |AD Users and Computers|dsa.msc|
   |ADSI Edit|adsiedit.msc|
   |Authorization manager|azman.msc|
   |Certification Authority Management|certsrv.msc|
   |Certificate Templates|certtmpl.msc|
   |Cluster Administrator|cluadmin.exe|
   |Computer Management|compmgmt.msc|
   |Component Services|comexp.msc|
   |Configure Your Server|cys.exe|
   |Device Manager|devmgmt.msc|
   |DHCP Management|dhcpmgmt.msc|
   |Disk Defragmenter|dfrg.msc|
   |Disk Manager|diskmgmt.msc|
   |Distributed File System|dfsgui.msc|
   |DNS Management|dnsmgmt.msc|
   |Event Viewer|eventvwr.msc|
   |Indexing Service Management|ciadv.msc|
   |IP Address Manager|ipaddrmgmt.msc|
   |Licensing Manager|llsmgr.exe|
   |Local Certificates Management|certmgr.msc|
   |Local Group Policy Editor|gpedit.msc|
   |Local Security Settings Manager|secpol.msc|
   |Local Users and Groups Manager|lusrmgr.msc|
   |Network Load balancing|nlbmgr.exe|
   |Performance Monitor|perfmon.msc|
   |PKI Viewer|pkiview.msc|
   |Public Key Management|pkmgmt.msc|
   |Quality of Service Control Management|acssnap.msc|
   |Remote Desktop|tsmmc.msc|
   |Remote Storage Administration|rsadmin.msc|
   |Removable Storage|ntmsmgr.msc|
   |Removable Storage Operator Requests|ntmsoprq.msc|
   |Routing and Remote Access Manager|rrasmgmt.msc|
   |Resultant Set of Policy|rsop.msc|
   |Schema management|schmmgmt.msc|
   |Services Management|services.msc|
   |Shared Folders|fsmgmt.msc|
   |SID Security Migration|sidwalk.msc|
   |Telephony Management|tapimgmt.msc|
   |Terminal Server Configuration|tscc.msc|
   |Terminal Server Licensing|licmgr.exe|
   |Terminal Server Manager|tsadmin.exe|
   |Terminal Services RDP|mstsc|
   |Terminal Services RDP to Console|mstsc /v:[server] /console|
   |UDDI Services Managment|uddi.msc|
   |Windows Management Instumentation|wmimgmt.msc|
   |WINS Server Manager|winsmgmt.msc|

3. With the new Settings app, there is even more:

   | Setting Name| Run Command|
   |:---:|:---:|
   | Settings home page | ms-settings:|
   | Display| ms-settings:display |
   | Night light  | ms-settings:nightlight |
   | Notifications & actions  | ms-settings:notifications |
   | Power & sleep| ms-settings:powersleep |
   | Battery| ms-settings:batterysaver  |
   | Battery usage by app  | ms-settings:batterysaver-usagedetails |
   | Battery Saver settings| ms-settings:batterysaver-settings  |
   | Storage| ms-settings:storagesense  |
   | Save locations  | ms-settings:savelocations |
   | Change how we free up space | ms-settings:storagepolicies  |
   | Tablet mode  | ms-settings:tabletmode |
   | Multitasking | ms-settings:multitasking  |
   | Projecting to this PC | ms-settings:project |
   | Remote Desktop  | ms-settings:remotedesktop |
   | Shared experiences | ms-settings:crossdevice|
   | About  | ms-settings:about|
   | Bluetooth & other devices| ms-settings:bluetooth  |
   | Connected devices  | ms-settings:connecteddevices |
   | Printers & scanners| ms-settings:printers|
   | Mouse  | ms-settings:mousetouchpad |
   | Touchpad  | ms-settings:devices-touchpad |
   | Typing | ms-settings:typing  |
   | Pen & Windows Ink  | ms-settings:pen  |
   | AutoPlay  | ms-settings:autoplay|
   | USB | ms-settings:usb  |
   | Phone  | ms-settings:mobile-devices|
   | Add a phone  | ms-settings:mobile-devices-addphone|
   | Status | ms-settings:network-status|
   | Cellular & SIM  | ms-settings:network-cellular |
   | Wi-Fi  | ms-settings:network-wifi  |
   | Wi-Fi Calling| ms-settings:network-wificalling |
   | Manage known networks | ms-settings:network-wifisettings|
   | Ethernet  | ms-settings:network-ethernet |
   | Dial-up| ms-settings:network-dialup|
   | VPN | ms-settings:network-vpn|
   | Airplane mode| ms-settings:network-airplanemode|
   | Mobile hotspot  | ms-settings:network-mobilehotspot  |
   | Data usage| ms-settings:datausage  |
   | Proxy  | ms-settings:network-proxy |
   | Background| ms-settings:personalization-background|
   | Colors | ms-settings:colors  |
   | Lock screen  | ms-settings:lockscreen |
   | Themes | ms-settings:themes  |
   | Start  | ms-settings:personalization-start  |
   | Taskbar| ms-settings:taskbar |
   | Apps & features | ms-settings:appsfeatures  |
   | Manage optional features | ms-settings:optionalfeatures |
   | Default apps | ms-settings:defaultapps|
   | Offline maps | ms-settings:maps |
   | Apps for websites  | ms-settings:appsforwebsites  |
   | Video playback  | ms-settings:videoplayback |
   | Your info | ms-settings:yourinfo|
   | Email & app accounts  | ms-settings:emailandaccounts |
   | Sign-in options | ms-settings:signinoptions |
   | Access work or school | ms-settings:workplace  |
   | Family & other people | ms-settings:otherusers |
   | Sync your settings | ms-settings:sync |
   | Date & time  | ms-settings:dateandtime|
   | Region & language  | ms-settings:regionlanguage|
   | Speech | ms-settings:speech  |
   | Game bar  | ms-settings:gaming-gamebar|
   | Game DVR  | ms-settings:gaming-gamedvr|
   | Broadcasting | ms-settings:gaming-broadcasting |
   | Game Mode | ms-settings:gaming-gamemode  |
   | TruePlay  | ms-settings:gaming-trueplay  |
   | Xbox Networking | ms-settings:gaming-xboxnetworking  |
   | Narrator  | ms-settings:easeofaccess-narrator  |
   | Magnifier | ms-settings:easeofaccess-magnifier |
   | High contrast| ms-settings:easeofaccess-highcontrast |
   | Closed captions | ms-settings:easeofaccess-closedcaptioning|
   | Keyboard  | ms-settings:easeofaccess-keyboard  |
   | Mouse  | ms-settings:easeofaccess-mouse  |
   | Other options| ms-settings:easeofaccess-otheroptions |
   | Talk to Cortana | ms-settings:cortana |
   | Permissions & History | ms-settings:cortana-permissions |
   | Notifications| ms-settings:cortana-notifications  |
   | More details | ms-settings:cortana-moredetails |
   | Cortana Language| ms-settings:cortana-language |
   | General| ms-settings:privacy |
   | Location  | ms-settings:privacy-location |
   | Camera | ms-settings:privacy-webcam|
   | Microphone| ms-settings:privacy-microphone  |
   | Motion | ms-settings:privacy-motion|
   | Notifications| ms-settings:privacy-notifications  |
   | Speech, inking, & typing | ms-settings:privacy-speechtyping|
   | Account info | ms-settings:privacy-accountinfo |
   | Contacts  | ms-settings:privacy-contacts |
   | Calendar  | ms-settings:privacy-calendar |
   | Call history | ms-settings:privacy-callhistory |
   | Email  | ms-settings:privacy-email |
   | Tasks  | ms-settings:privacy-tasks |
   | Messaging | ms-settings:privacy-messaging|
   | Radios | ms-settings:privacy-radios|
   | Other devices| ms-settings:privacy-customdevices  |
   | Feedback & diagnostics| ms-settings:privacy-feedback |
   | Background apps | ms-settings:privacy-backgroundapps |
   | App diagnostics | ms-settings:privacy-appdiagnostics |
   | Automatic file downloads | ms-settings:privacy-automaticfiledownloads  |
   | Windows Update  | ms-settings:windowsupdate |
   | Check for updates  | ms-settings:windowsupdate-action|
   | Update history  | ms-settings:windowsupdate-history  |
   | Restart options | ms-settings:windowsupdate-restartoptions |
   | Advanced options| ms-settings:windowsupdate-options  |
   | Delivery Optimization | ms-settings:delivery-optimization  |
   | Windows Defender| ms-settings:windowsdefender  |
   | Backup | ms-settings:backup  |
   | Troubleshoot | ms-settings:troubleshoot  |
   | Recovery  | ms-settings:recovery|
   | Activation| ms-settings:activation |
   | Find My Device  | ms-settings:findmydevice  |
   | For developers  | ms-settings:developers |
   | Windows Hello| ms-settings:signinoptions-launchfaceenrollment |
   | Windows Insider Program  | ms-settings:windowsinsider|
   | Mixed reality| ms-settings:holographic|
   | Audio and speech| ms-settings:holographic-audio|
   | Accounts  | ms-settings:surfacehub-accounts |
   | Team Conferencing  | ms-settings:surfacehub-calling  |
   | Team device management| ms-settings:surfacehub-devicemanagement  |
   | Session cleanup | ms-settings:surfacehub-sessioncleanup |
   | Welcome screen  | ms-settings:surfacehub-welcome  |


4. Common Windows Keyboard Shortcuts:

   |Shortcut To| Keyboard Combo|
   |:---:|:---:|
   |Run|Win + R|
   |Task Manager|Ctrl + Shift + Esc|
   |Browse Through Open Windows|Alt + Tab|
   |Closes Selected Window|Alt + F4|
   |Deletes Item without Recycle Bin|Shift + Delete|
   |Finds any File or Folder|Win + F|
   |Locks The Computer|Win + L|
   |Maximizes All Minimized Windows|Win + Shift + M|
   |Maximizes Selected Window|Alt + Space + X|
   |Minimizes Selected Window|Alt + Space + N|
   |Minimizes/ Maximizes All Windows|Win + D / Win + D (do it twice)|
   |Move Through the Tabs In Dialog Box|Ctrl + Tab|
   |My Computer|Win + E|
   |Properties of Highlighted Item|Alt + Enter|
   |System Properties|Win + Pause/ Break|

5. Windows 10 keyboard shortcuts:

   |Shortcut To| Keyboard Combo|
   |:---:|:---:|
   | Open or close Start. | Windows logo key   |
   | Open Action center.  | Windows logo key+A |
   | Set focus in the notification area.  | Windows logo key+B |
   | Open the charms menu.| Windows logo key+Shift + C |
   | Display and hide the desktop.| Windows logo key+D |
   | Display and hide the date and time on the desktop.   | Windows logo key+Alt + D   |
   | Open File Explorer.  | Windows logo key+E |
   | Open Feedback Hub and take a screenshot. | Windows logo key+F |
   | Open Game bar when a game is open.   | Windows logo key+G |
   | Start dictation. | Windows logo key+H |
   | Open Settings.   | Windows logo key+I |
   | Set focus to a Windows tip when one is available.| Windows logo key+J |
   | Open the Connect quick action.   | Windows logo key+K |
   | Lock your PC or switch accounts. | Windows logo key+L |
   | Minimize all windows.| Windows logo key+M |
   | Lock device orientation. | Windows logo key+O |
   | Choose a presentation display mode.  | Windows logo key+P |
   | Open Quick Assist.   | Windows logo key + Ctrl + Q|
   | Open the Run dialog box. | Windows logo key+R |
   | Open search. | Windows logo key+S |
   | Take a screenshot of part of your screen.| Windows logo key+Shift + S |
   | Cycle through apps on the taskbar.   | Windows logo key+T |
   | Open Ease of Access Center.  | Windows logo key+U |
   | Cycle through notifications. | Windows logo key+Shift + V |
   | Open the Quick Link menu.| Windows logo key+X |
   | Switch input between Windows Mixed Reality and your desktop. | Windows logo key + Y   |
   | Show the commands available in an app in full-screen mode.   | Windows logo key+Z |
   | Open emoji panel.| Windows logo key + period (.) or semicolon (;) |
   | Temporarily peek at the desktop. | Windows logo key+comma |
   | Display the System Properties dialog box.| Windows logo key+Pause |
   | Search for PCs (if you're on a network). | Windows logo key+Ctrl + F  |
   | Restore minimized windows on the desktop.| Windows logo key+Shift + M |
   | Open the desktop and start the app pinned to the taskbar in the position indicated by the number. If the app is already running, switch to that app. | Windows logo key+number|
   | Open the desktop and start a new instance of the app pinned to the taskbar in the position indicated by the number.  | Windows logo key+Shift + number|
   | Open the desktop and switch to the last active window of the app pinned to the taskbar in the position indicated by the number.  | Windows logo key+Ctrl + number |
   | Open the desktop and open the Jump List for the app pinned to the taskbar in the position indicated by the number.   | Windows logo key+Alt + number  |
   | Open the desktop and open a new instance of the app located at the given position on the taskbar as an administrator.| Windows logo key+Ctrl + Shift + number |
   | Open Task view.  | Windows logo key+Tab   |
   | Maximize the window. | Windows logo key+Up arrow  |
   | Remove current app from screen or minimize the desktop window.   | Windows logo key+Down arrow|
   | Maximize the app or desktop window to the left side of the screen.   | Windows logo key+Left arrow|
   | Maximize the app or desktop window to the right side of the screen.  | Windows logo key+Right arrow   |
   | Minimize all except the active desktop window (restores all windows on second stroke).   | Windows logo key+Home  |
   | Stretch the desktop window to the top and bottom of the screen.  | Windows logo key+Shift + Up arrow  |
   | Restore/minimize active desktop windows vertically, maintaining width.   | Windows logo key+Shift + Down arrow|
   | Move an app or window in the desktop from one monitor to another.| Windows logo key+Shift + Left arrow or Right arrow |
   | Switch input language and keyboard layout.   | Windows logo key + Spacebar|
   | Change to a previously selected input.   | Windows logo key + Ctrl + Spacebar |
   | Turn on Narrator.| Windows logo key+Ctrl + Enter  |
   | Open Magnifier.  | Windows logo key + Plus (+)|
   | Begin IME reconversion.  | Windows logo key+forward slash (/) |
   | Open shoulder taps.  | Windows logo key + Ctrl + V|
   | Wake PC from blank or black screen   | Windows logo key + Ctrl + Shift + B|

6. Chrome

   |Shortcut To| Keyboard Combo|
   |:---:|:---:|
   |This will pin a tab so that it is always open, even if you close other windows|Right Click Tab – Pin Tab|
   |Reloads a page and force reloads a page respectively|Ctrl+R/ Ctrl+Shift+R|
   |Navigate back and forwards between tabs|Alt+Left/Alt+Right|
   |Jump to top or bottom of a page|Home/End|
   |Everyones favorite, Find|Ctrl+F|
   |Opens a new tab or page|Ctrl+T/ Ctrl+N|
   |Opens a new tab with a web address instead of overriding the current tab|Enter web address + (Alt+Enter)|
   |Close a tab or a window of tabs|Ctrl+F4/Ctrl+Shift+F4|
   |New private mode window|Ctrl+Shift+N|
   |Re-open a previously closed tab|Ctrl+Shift+T|
   |Jumps straight to the address bar|Ctrl+L|
   |Opens in a new tab|Ctrl+Shift+Click on a hyperlink|
   |Jumps straight to that tab|Ctrl+Tab Number (left to right)|
   |Allows you to browse as a guest|Ctrl+Shift+M|
   |Allows you to toggle bookmarks on/off|Ctrl+Shift+B|
   |Opens a webpage as source|Ctrl+U|
   |Allows you to scroll down on a page|Spacebar|

### Reference:

["The Always Up-to-Date Power User's Guide to Chrome"](http://lifehacker.com/5867446/the-always-up-to-date-power-users-guide-to-chrome#shortcuts)

