---
title: Using AutoIT With Powershell
date: 2016-06-04T04:07:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/using-autoit-with-powershell-for-total-automation/
categories:
  - LocalSoftware
---
<!--more-->

### Description:

[AutoIT](https://www.autoitscript.com/site/) is a neat freeware you can download and install that automates the button click of GUIs within Windows. I'm really new to it so I'm not sure all the features, but I have noticed this:

1. It's super easy to create a script: Open notepad, type a few commands from the references below and save as .au3. Double click to run.

2. It's super easy to convert a script into an executable. Right click => compile. When combined with a powershell script converted to an exe, it outputs a single encrypted exe that you can then push to clients for a quick PS script without messing with anything.

   - I decided to test it using my [uninstall/reinstall custom ClickOnce application powershell script](https://automationadmin.com/2016/12/ps-clickonce-app-uninstall-reinstall/)

### To Resolve:

1. First, on my computer I put the "click-once-uninstall-reinstall.ps1" in a folder on my C:scripts directory.

2. Created a new blank .au3 script with the folling commands

   ```escape
   Run("reinstall.exe")  
   WinWaitActive("applicationName Maintenance")  
   Send("OK")  
   WinWaitActive("Application Install Security Warning")  
   Send("I")
   ```

3. Since I had already converted the script to an executable called "reinstall.exe", I just right clicked on the script and selected "compile 32bit" for compatibility reasons and it spit out a new exe that I could then run on any computer to fully automate the uninstall/reinstall of our custom app.

4. If you don't feel like converting your .ps1's to exe's, you can simply use the program to launch powershell the traditional way (since it simulates keyboard keys), and just push over the executable with your script and it will still automate the install. The commands to do this will be like:

   ```escape
   Send("#r")  
   Send("powershell.exe -windowstyle hidden -executionpolicy bypass -File C:\scripts\click-once-uninstall-reinstall.ps1")  
   Send("{ENTER}")  
   WinWaitActive("<application> Maintenance")  
   Send("OK")  
   WinWaitActive("Application Install => Security Warning")  
   Send("I")
   ```


2. After creating the script, just right click and "compile 32bit". It will generate a .exe you can push over with your .ps1 and run it automatically.

   - If you go this route, make sure your script is always in the path that you call it from. For example, I created a folder called "_" on the root of my C: that I push over to client via LogMeIn Rescue. Inside it has a .ps1 file and a exe. I just double click on the exe and it calls the PS script for the back end work and the AutoIT executable waits and presses the GUI buttons for the front end work.

   - I'm a really new to this, but I assume you can use the program to also get rid of GUI windows altogether or just use a PS UI module and not even mess with AutoIT but it was still a learning experience worth posting. In the references, I noticed a blog where someone used the AutoIT app itself inside Powershell to automate some builds, might be interesting as well.

### References:

["AutoIt"](https://www.autoitscript.com/autoit3/docs/)  
["Automated Machine Builds with PowerShell and AutoIT"](http://muegge.com/blog/automated-machine-builds-with-powershell-and-autoit/)  