---
title: 'Command Prompt: Hardware Commands'
date: 2016-06-02T20:39:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/command-prompt-hardware-commands/
tags:
  - Windows
  - SysAdmin
tags:
  - OneLiners-CMD
  - Scripting-CMD
---
<!--more-->

### Description:

The following commands can be ran from the Windows Command Prompt

### To navigate the filesystem:

   ```powershell
   :: To Rename a File
   ren filename newFilename

   :: To Move a file
   move -y filename new location

   :: To Copy a file
   copy filename newFilename

   :: To change where you are in a file system through a terminal program
   :: changes a directory. "" is root, "." is current directory, and ".." is one directory up (without quotes)
   :: cd Directory
   :: Example:
   cd c:\users\gerry\Documents\WindowsPowershell
   ```

### To Get A Service Tag From A Computer:

   ```powershell
   wmic bios get serialnumber
   ```

### To Check A Drive For Physical Errors:

   ```powershell
   chkdsk

   :: Fixes the errors found
   chkdsk /x
   ```

### To Find Strings In A Directory:

   ```powershell
   :: findstr /d:[directory] /m [string] [files]
   :: Where files is the file type. Example: 
   C:> findstr /s /d:c:\windows /m mp3 *
   ```

### To Link A Directory To Another Drive (SymLink):

   ```powershell
   :: This creates a folder called "notes" at your current location and links it to a folder called "notes" at "z:\google\backup\notes"
   mklink /d notes z:\google\backup\notes
   ```

### To Take Control of a File / Folder:

   ```powershell
   takeown (filename)

   :: To Take Control of A Directory:
   takeown /f (foldername) /r /d y

   :: Example batch script that takes a "CSC" folder and deletes it:
   cd c:\Windows
   takeown /f csc /r /a /d y > NUL
   icacls csc /grant Administrators:(F) /t /l /q
   cd csc
   del * /S /Q
   cd c:\windows
   rmdir /S /Q "C:\Windows\CSC\"
   ```

### To Shutdown A Computer:

   ```powershell
   :: Default 60 seconds shutdown =  /s is poweroff /r is reboot
   shutdown

   :: To reboot in 2 seconds where r=reboot, f=force, and t=time
   shutdown -r -f -t 2 

   :: Aborts a shutdown
   shutdown -a 

   :: Initiates a shutdown on remote computers in the same network. 
   :: You will choose them from a list and tell them what to do in a drop down menu. 
   :: NOTE: You have to have administrative rights on their machines to do this.
   shutdown -i
   ```

### To Find Out the Last Time A Computer Was Rebooted:

   ```powershell
   :: # Make sure to use the quotations around "Time".
   systeminfo | Find "Time"

   :: The "Statistics Since" line will have the last boot time.
   net statistics workstation

   :: Works on workstations too.
   net statistics server
   ```

### To Disable Hibernation:

   ```powershell
   powercfg.exe -h off
   ```

### To Format A Drive:

   ```powershell
   :: Where the first "f" is the drive letter you want to format.
   format f: /fs:NTFS /p:2
   ```

### To Get System Info:

   ```powershell
   systeminfo
   ```

### To Find Computer Name Information:

   ```powershell
   :: Displays the name of the computer
   hostname

   :: Displays Domain name / User name
   whoami
   ```

### To Check Your OS Version:

   ```powershell
   :: Huge amounts of info, one of my favorite commands!
   msinfo32

   :: Same
   dxdiag

   :: Another way to see info
   wmic os get Caption,CSDVersion /value
   ```

### To Show The Domain Name:

   ```powershell
   echo %userdomain%
   net config workstation
   ```