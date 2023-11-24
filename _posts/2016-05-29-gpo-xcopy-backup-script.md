---
title: 'GPO: XCopy Backup Script'
date: 2016-05-29T04:26:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gpo-xcopy-backup-script/
tags:
  - WindowsServer
tags:
  - GroupPolicy
  - Backup
---
<!--more-->

### Description:

In an Active Directory environment, create a script similiar to this to backup user's desktop and `My Documents` folders:

Logon and Logoff Scripts will need to be in the following folders:

   - `C:\Windows\System32\GroupPolicy\UserScripts\Logoff` 
   - `C:\Windows\System32\GroupPolicy\UserScripts\Logon`

While Startup and Shutdown Scripts will need to be in these folders:

   - `C:\Windows\System32\GroupPolicy\MachineScripts\Shutdown` 
   - `C:\Windows\System32\GroupPolicy\MachineScripts\Startup`

### To Resolve:

1. Save the following as a batch script and place it in the OU for whichever users you want to backup. They need to have write access to said directory:

   ```escape
   xcopy C:\Users\%username%\Documents\* \\fileserver\users\%username%\My Documents /D /E /Y /I
   ```


   - D = Copies source files changed on or after the specified date only. If you do not include a MM-DD-YYYY value, xcopy copies all Source files that are newer than existing Destination files. This command-line option allows you to update files that have changed.
   - E = Copies all subdirectories, even if they are empty. Use /e with the /s and /t command-line options. /t
   - Y = Suppresses prompting to confirm that you want to overwrite an existing destination file.
   - I = If Source is a directory or contains wildcards and Destination does not exist, xcopy assumes Destination specifies a directory name and creates a new directory. Then, xcopy copies all specified files into the new directory. By default, xcopy prompts you to specify whether Destination is a file or a directory.

2. The alternative is to create a public/ private shares on the fileserver and have a script that maps drives on login. Explain to users that what is not saved in those drives is not backed up.

3. Now we need to set this up to auto launch on login through a GPO. There seems to be confusion between using a logon script on ADUC instead of GPO, I'm here to tell you that GPO works much better. Follow these next steps.

4. On the domain controller, open &#8220;Group Policy Management&#8221; and navigate to the OU needed. I always do IT computers first because I work in a 3 man IT Dept so the path was ForestDomains(DomainName)CorporateEmployeesITEmployees&#8221; => Then create a new GPO and link it there. I called it &#8220;Test\_Logon\_Script&#8221;

5. Now you right click and &#8220;Edit&#8221; the script. Go to User ConfigurationPoliciesWindows SettingsScripts(Logon/Logoff). Double click on Logon. These next steps are counter-intuitive so pay attention.

6. Find your batch script from step one and copy it. Then with the GPO open, select the &#8220;Show Files&#8221; button and paste it into that directory. You will then need to cancel out of the Login page and go back in to it. You should not have to navigate any directories, but instead click on your script directly. In the white box with script names, there should be NO DIRECTORIES, just the file name of the script.

   - I had initially copied and pasted from C:Scripts and the script failed to start. I copied and pasted to the directory and it worked. Read the guide in the references for clarification. Done.

7. Before moving to PowerShell, I did get Robocopy working pretty good. Copy and paste this into the batch file mentioned above, it will create a public backup for all users:

   ```escape
   cd c:\windows\system32  
   robocopy C:\Users\%username%\Documents \\fileserver\userbackups\Backups\%username%\Documents /mir /z /e /R:10 /W:10 /mt:4  
   robocopy C:\Users\%username%\Desktop \\fileserver\userbackups\Backups\%username%\Desktop /mir /z /e /R:10 /W:10 /mt:4  
   robocopy C:\Users\%username%\Favorites \\fileserver\userbackups\Backups\%username%\Favorites /mir /z /e /R:10 /W:10 /mt:4  
   robocopy C:\Users\%username%\Pictures \\fileserver\userbackups\Backups\%username%\Pictures /mir /z /e /R:10 /W:10 /mt:4
   ```

   - Since I do not use those folders, but my own personal folder, I just created a batch file and a &#8220;simple task&#8221; in `taskschd.msc`:

   ```escape
   cd c:\windows\system32  
   robocopy C:\_gwill Z:\Backups\gerry.williams\_gwill /mir /z /e /R:10 /W:10 /mt:4
   ```

   - I set it to run every day at 5 am.

8. I'm looking into something like [this](https://blogs.technet.microsoft.com/heyscriptingguy/2012/02/23/use-powershell-to-back-up-modified-files-to-the-network) instead 

### References:

["How do I map user accounts and directories to a server or NAS?"](http://superuser.com/questions/730494/how-do-i-map-user-accounts-and-directories-to-a-server-or-nas)  
["Setting up a Logon Script through GPO in Windows Server 2008"](https://www.petri.com/setting-up-logon-script-through-gpo-windows-server-2008)