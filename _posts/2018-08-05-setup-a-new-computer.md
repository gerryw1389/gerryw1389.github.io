---
title: Setup A New Computer
date: 2018-08-05T05:31:54+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/08/setup-a-new-computer/
tags:
  - SysAdmin
tags:
  - Tweaks
  - PersonalConfig
---
<!--more-->

### Description:

I will be following these steps to re-image my home computer soon. See my [dot files post](https://automationadmin.com/2022/01/dot-files) for some references to these settings.

### To Resolve:

1. Install [Firefox](https://www.mozilla.org/en-US/firefox/new/).
2. Google [Backup and Sync](https://www.google.com/drive/download/backup-and-sync/). 

   - Create symlink: 

   ```escape
   mkdir c:\_gwill
   cd c:\_gwill
   mklink /d google z:\google
   ```

   - Now launch installer
   - Enter email / Enter password
   - Sign in on web if you have two factor, the screen will just gray out if you use the Authenticator app – Will probably be fixed in a later release.
   - Skip the screen about backing up continuously (although that is what you want to do) – DO NOT CHOOSE a folder here.
   - On the screen where it checks the box to sync google drive, HERE is where you select the folder. If you have a sym link, select that folder.

3. Install apps below:
   - [7zip](https://www.7-zip.org/)
   - [VSCode](https://code.visualstudio.com/)
   - [Greenshot](https://getgreenshot.org/)
   - [Bulk Rename Util](https://www.bulkrenameutility.co.uk/Download.php)
   - [CryptSync](https://tools.stefankueng.com/CryptSync.html)
   - [Everything](https://www.voidtools.com/)
   - [Notepad++](https://notepad-plus-plus.org/download/)
   - [PDF Tools](https://www.pdfill.com/pdf_tools_free.html)
   - PureVPN
   - [NoMacs](https://nomacs.org/) - Image editor
   - [FreeFileSync](https://freefilesync.org/)
   - [Git](https://git-scm.com/download/win)
   - [Teams](https://teams.microsoft.com/downloads)
   - [qBitTorrent](https://www.qbittorrent.org/)
   - [vlc](https://www.videolan.org/vlc/)
   - [Chrome](https://chrome.com)
   - [Veeam Endpoint Backup Free](https://www.veeam.com/windows-endpoint-server-backup-free.html)

4. Install VPN Client for work

5. Configure Veeam Endpoint - Point it to my `Z:\` which will be backed up to encrypted external manually

6. Install Office by logging into O365.
   - Outlook - Turn off all notifications – See [My Outlook Config](https://automationadmin.com/2017/05/my-outlook-config/)

7. NPP Config
   - Settings – Style Configurator – Obsidian theme – Consolas 12 – Enable Global font/ Enable Global font size
   
   - Options:
     - Recent files history = uncheck "don't check at launch"
     - Backup – Uncheck "Remember current session.."
     - Multi-instance = Always in Multi-Instance Mode
     - Misc = Uncheck "enable" under Clickable Link Settings
     - Plugins – dspellchecker – uncheck the "spell check document automatically (ctrl+a)"

8. Firefox config - Sign in and follow [Firefox Config](https://automationadmin.com//2016/10/firefox-config/)

9.  Everything config - Options – Keyboard – Show Window Hotkey: `Ctrl+Alt+Q`

10. Teams config - Click on Initials in top right – Settings – Theme: Dark – check "open application in background"

11. See [Quickcliq config](https://automationadmin.com/2017/07/quickcliq-config/)

12. Install Virtualbox and point to my `G:\`

13. Configure Greenshot
   - Preferences tab - Hotkeys - Clear all and enter `Ctrl+Q` for capture region.
   - Capture tab - Turn off notifications
   - Destination tab - Select only 'Open in Image editor'

1.  VSCode config - See [Vscode Config](https://automationadmin.com/2019/06/vscode-config)

### Configure Windows Itself

1. Run [New Computer Script](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-Template.ps1)

2. Enable WSL - `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`. After installation your Linux distribution will be located at: `%localappdata%\lxss`. I'm not sure but I think you have to then go to the Windows Store and install Ubuntu.

3. Settings – Taskbar – Select which icons appear – Set all to disabled except Backup and Sync

4. Set background to my preferred image

5. Set lockscreen to my preferred image

6. Set mouse to my preferred cursor - [oxy-midnight_meadow](https://www.deviantart.com/lavalon/art/Oxygen-Cursors-76614092)

7. Setup my preferred Powershell profile settings – See [Profile](https://github.com/gerryw1389/misc/blob/main/dot-files/Microsoft.Powershell_profile.ps1)

8. Finally – Set Windows Taskbar: Thunderbird (Portable), VSCode, ConEmu, File Explorer, NPP, Firefox, Teams, Outlook

### Conclusion

1. The following global shortcuts should work:
   - `Ctrl+Q` - Greenshot capture region
   - `Alt+Q` - Quickcliq menu
   - `Ctl+Alt+Q` - Everything menu

2. Pin the following items to the start menu:
   - Powershell
   - Powershell ISE
   - Oracle VirtualBox
   - Ubuntu for Windows