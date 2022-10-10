---
title: Command Prompt Overview
date: 2016-05-30T05:46:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/command-prompt-overview/
categories:
  - SysAdmin
tags:
  - Scripting-CMD
  - OneLiners-CMD
---
<!--more-->

### Description:

The Windows Command Prompt is a command line way to administer Windows systems prior to Windows Powershell. The two most common ways to launch it are:

1. Start (bottom left button on the screen) => Search "cmd" => Then use keyboard Ctrl+Shift+Enter to enter into "Command Prompt (Run As Administrator)" which is an elevated command prompt session. This is most common when your normal user account is unprivileged (which it should be!) and will launch UAC for your to enter credentials to start the process.  

   - While in the shell during an administrative session, you are running as the admin. Don't believe me? Type `whoami` and compare that to a normal Command Prompt session.

2. [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) => `cmd` => press Enter. This will get you an unelevated session and should work for some tasks like commands that get statuses (read only), but will rarely work when you need to make a change to the system (modify / write).  

In addition to the Command Prompt, the preferred administration tool to use in Windows nowadays is Powershell. There are multiple ways to launch it:

1. Start (bottom left button on the screen) => Search "powershell" => Then use keyboard Ctrl+Shift+Enter to enter into "Powershell (Run As Administrator)" which is an elevated command prompt session. This is most common when your normal user account is unprivileged (which it should be!) and will launch UAC for your to enter credentials to start the process.  

   - While in the shell during an administrative session, you are running as the admin. Don't believe me? Type `whoami` and compare that to a normal Command Prompt session.

2. Run (keyboard shortcut `Win` + `R`) => `powershell` => press Enter. This will get you an unelevated session and should work for some tasks like commands that get statuses (read only), but will rarely work when you need to make a change to the system (modify / write).  

3. The popular `Win+X` menu now defaults to Powershell so you can essentially use `Win+x+a` to launch an admin powershell window (`win+x+i` for non-admin) from any modern W10 desktop!

Related, you might want to check out my post on Conemu which combines Command Prompt, Powershell, and WSL (Windows Subsystem for Linux) into a portable program that I consider a must-have!

### To Resolve:

1. Use `Ctrl+C` to Abort a Command = If you have a script running or want to terminate a process, use this shortcut to stop it immediately.

2. View a Command's Results One Page (or Line) at a Time - Just press the space bar to advance by page or press the Enter key to advance one line at a time.

3. Run Command Prompt as an Administrator Automatically- To complete this Command Prompt trick, just create a Command Prompt shortcut on the desktop, enter the shortcut's properties and then select the Run as administrator box located in the Advanced button on the Shortcut tab.

4. Become a Command Prompt Power User with Function Keys  
   - `F1`: Pastes the last executed command (character by character)  
   - `F2`: Pastes the last executed command (up to the entered character)  
   - `F3`: Pastes the last executed command  
   - `F4`: Deletes current prompt text up to the entered character  
   - `F5`: Pastes recently executed commands (does not cycle)  
   - `F6`: Pastes ^Z to the prompt  
   - `F7`: Displays a selectable list of previously executed commands  
   - `F8`: Pastes recently executed commands (cycles)  
   - `F9`: Asks for the number of the command from the F7 list to paste

5. Hack the Prompt Text- Instead of `C:\>`, you can set the prompt to any text you want, have it include the time, the current drive, the Windows version number, you name it. One useful example is `prompt $m$p$g` which will show the full path of a mapped drive in the prompt, alongside the drive letter. You can always execute prompt alone, without options, to return it to its sometimes boring default.

6. Get Help for Any Command - Believe it or not, the help command does not provide help for every Command Prompt command. However, any command can be suffixed with the `/?` option, usually called the help switch, to display detailed information about the command's syntax and often times even some examples.

7. Save a Command's Output to a File - An incredibly useful Command Prompt trick is the use of redirection operators, specifically the `>` and `>>` operators. For example, let's say you're about to post a computer problem to an online forum and you want to provide really accurate information about your computer. An easy way to do that would be to use the systeminfo command with a redirection operator. You might execute `systeminfo > c:\mycomputerinfo.txt` to save the information provided by the `systeminfo` command to a file. You could then attach the file to your forum post.

8. View Your Hard Drive's Entire Directory Structure - Execute `tree` from any directory to see the folder structure under that directory. Tip: With so much information, it's probably a good idea to export the results of the tree command to a file. For example, `tree /a > c:\treeresults.txt`.

9. Customize the Command Prompt Title Bar Text - Execute `title WhateverText` and the Command Prompt's title bar will change immediately. The change won't stick, so the next time you open Command Prompt the title bar will be back to normal. The title command is usually used to help give a custom appearance in script files and batch files.

10. Copy From the Command Prompt- Right -click anywhere in the Command Prompt window and choose Mark. Now, highlight with your left mouse button whatever you'd like to copy. Once your selection is made, press Enter. Now you can paste that information into whatever program you'd like.

11. Open the Command Prompt From Any Location - If you've ever worked in the Command Prompt for very long, you know that it can be really frustrating executing the cd/chdir command over and over again to get to the right directory you want to work from. Luckily, there's a super easy Command Prompt trick that will let you open a Command Prompt window from whatever folder you're viewing in Windows. All you have to do is navigate, in Windows, to the folder you want to start working from in the Command Prompt. Once there, hold down your `Shift key while you right-click anywhere in the folder`. Once the menu pops up, you'll notice an entry that's not usually there: `Open command window here`.

12. Drag and Drop For Easy Path Name Entry - Just navigate to the folder you want the path for in Windows Explorer. Once there, drag the folder or file to the Command Prompt window and let go. Like magic, the full path is inserted, saving you a considerable amount of typing depending on the length and complexity of the path name. Note: Unfortunately, the drag and drop feature does not work in an elevated Command Prompt.

13. Shut Down or Restart Another Computer - The easiest way to shut down a computer remotely is to execute `shutdown /i` from the Command Prompt. Just enter the name of the remote computer (which you can get by running the hostname command on the other PC), choose what you want to do (restart or shutdown), select some other options and then click OK. You can also shut down or restart another computer strictly from the Command Prompt with the shutdown command, without using the Remote Shutdown Dialog.

14. Use Robocopy as a Backup Solution- Just execute `robocopy c:\users\tim\documents f:\backup\documents /copyall /e /r:0 /dcopy:t /mir`, obviously replacing the source and destination folders with whatever you'd like to backup and where. The robocopy command with these options functions identically to an incremental backup software tool, keeping both locations in sync. You don't have the robocopy command if you're using Windows XP or earlier. However, you do have the xcopy command, which can be used to do something very similar: `xcopy c:\users\tim\documents f:\backup\documents /c /d /e /h /i /k /q /r /s /x /y`. No matter which command you choose to use, just create a script file containing the command and schedule it to run in Task Scheduler and you'll have your own custom made backup solution.

15. View Your Computer's Important Network Information - `ipconfig /all`

16. Map a Local Folder Just Like a Network Drive- The `net use` command is used to assign shared drives on a network to your own computer as a drive letter, but did you know there's another command that can be used to do the same thing to any folder on any of your local hard drives? There is and it's called the `subst` command. Just execute the subst command, followed by the path of the folder you wish to appear as a drive. For example, let's say you want your `C:\Windows\Fonts` folder to appear as the `Q:` drive. Just execute `subst q: c:\windows\fonts` and you're set!

17. Access Previously Used Command with the Arrow Keys - Another great Command Prompt trick has to be the use of the keyboard arrow keys to cycle through previously executed commands. The up and down arrow keys cycle through the commands you've entered and the right arrow automatically enters, character by character, the last command you executed.

18. Automatically Complete Commands with Tab Completion - To use tab completion in the Command Prompt, just enter the command and then the portion of the path that you do know, if at all. Then press the tab key over and over to cycle through all of the available possibilities. For example, let's say you want to change directories to some folder in the Windows directory but you're not sure what it's named. Type `cd c:\windows\` and then press tab until you see the folder you're looking for. The results cycle or you can use Shift+Tab to step through the results in reverse.

19. Find a Website's IP Address- Let's use the `nslookup` command to find the IP address of About.com. Just execute `nslookup about.com` and view the result. Make sure you don't confuse any private IP addresses that also show up in the `nslookup` results alongside About.com's public IP address. Another way to find a site's IP address is to use the ping command. Execute ping about.com and then look at the IP address between the brackets in the results shown.

20. Copy & Paste Easier with QuickEdit Mode - Just right-click on the Command Prompt title bar and select Properties. On the Options tab, in the Edit Options section, check the QuickEdit Mode box and then click OK. Enabling QuickEdit Mode is like having Mark enabled all the time so selecting text to copy is really easy. But it also enables an easy way to paste into the Command Prompt: just right click once and whatever is in the clipboard is pasted in the Command Prompt window. Normally, pasting involves right-clicking and selecting Paste.

21. Watch Star Wars Episode IV - Yes, you read that correctly, you can watch an ASCII version of the full Star Wars Episode IV movie right in the Command Prompt window! Just open Command Prompt and execute `telnet towel.blinkenlights.nl`. The movie will start immediately. This isn't a terribly productive use of the Command Prompt, nor is it really a trick of the Command Prompt or any command, but it sure is fun! Note: The telnet command is not enabled by default in Windows 7 or Windows Vista but can be turned on by enabling Telnet Client from Windows Features in the Programs and Features applet in Control Panel. 

### Commonly Used CMD Commands:

|Description|command|
|:---:|:---:|
|Checks A File System and fixes errors|chkdsk /x |
|Defrags the system C Drive|defrag.exe c:|
|Configure IP|ipconfig|
|Displays domain/ username|whoami|
|Name Of Computer|hostname|
|Ping with TraceRoute|pathping 8.8.8.8|
|System File Checker|sfc /scannow|
|Test A Network Connection|ping 8.8.8.8|
|Test A Network Connection|ping server.company.com|
|Traces A Route|tracert|
|Find out the last time the server was rebooted|`systeminfo| Find "Time"`|
|Constant ping to an address|ping -t|
|Use to get serial number to Dell|WMIC BIOS GET SERIALNUMBER|
|IP Configuration – Show more info |ipconfig /all|
|Releases a current IP|ipconfig /release|
|Renews an IP address if on DHCP|ipconfig /renew|

#### For more info on these commands and what they do, go [here](https://technet.microsoft.com/en-us/library/cc772390(v=ws.10).aspx).