---
title: WSCC Portable
date: 2016-05-29T04:51:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/wscc-portable/
categories:
  - LocalSoftware
---
<!--more-->

### Description:

Being in the IT field, you will no doubt end up working on Windows boxes for various issues. Many administrators have an arsenal of tools that they use, but over time, you may end up like me and narrow these down to a select few tools. One tool I use often is called &#8220;[WSCC or Windows System Control Center](http://www.kls-soft.com/wscc/)&#8221; which is essentially a combination of the Windows System Internals Suite and Nirsoft Utilities combined. The tool is portable and supports command line parameters. It's much faster and more efficient to use command line tools than GUI's.

### How To Use This Program:

1. You can download and run this program just as any other portable application, but I added mine as an entry on [QuickCliq](http://apathysoftworks.com/software/quickcliq) with a shortcut key of F1 for a one-click launch.

2. Once it's installed, go to the applications options and navigate to the network tab => check the &#8220;include new software&#8221; and take note of the two live urls on the Software tab:

   - [http://live.sysinternals.com/](https://live.sysinternals.com/)  
   - [http://www.nirsoft.net/panel/](http://www.nirsoft.net/panel/)

3. You can call any of these applications from any computer's run line (Win+R) meaning:

   - `Win+R + http://live.sysinternals.com/autoruns.exe` = Launches the autoruns application (or downloads it so you can run it)  
   - `Win+R + http://www.nirsoft.net/panel/bluescreenview.exe` = Launches the bluescreenview application

### Examples:

1. Process Explorer => A GUI application that shows information on running processes much more in-depth then the Windows Task Manager.

2. Autoruns => A GUI application to manage startup entries.

3. DiskToVHD- Converts a physical computer to a vhd. It can be set to auto run for a home-made backup solution.

4. PsFiles- Shows which files on your system are opened remotely. This could be good for a file server pending a reboot.

5. TCPView => Shows all active TCP/UDP connections and allows you to close them in a GUI.

6. ProcessMonitor => Records events in real time. Use to replicate an issue for an error you are unsure of.

7. BlueScreenView- Analyze crash files to find out what happened. You could also run WinCrashReport to analyze what went wrong prior to the crash.

8. FolderChangesView- Used to monitor a directory for any add, modify, and deletes.

9. LastActivityView => Shows all tasks a user did by compiling various information in reporting.

10. Wireless Network Watcher- Performs a network scan of all devices on your network.

11. ProduKey => Shows your Windows Product key.

12. Even though WSCC comes with [PS Tools](https://technet.microsoft.com/en-us/sysinternals/pstools.aspx), I usually download them and copy them to my `C:\Windows\System32` location. Here is where you can find them. Of these tools, PSExec is my most used. For example:

   ```powershell
   # To Run Remote .BAT file:
   copy c:\scripts\test.bat \\ServerComputerName\c$\scripts\test.bat  
   psexec \\ServerComputerName "C:\scripts\test.bat"
   # To Run Remote .EXE file:
   copy c:\scripts\test.exe \\ServerComputerName\c$\scripts\test.exe  
   psexec \\ServerComputerName "C:\scripts\test.exe"
   ```

