---
title: 'PS: Why I Use My Template For Logging'
date: 2017-09-24T05:04:43+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/09/ps-why-I-use-my-template-for-logging/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Logging is an essential function for scripting because it not only can display text to a screen, but it records times that scripts have ran and their associated output. I found a couple examples from the Microsoft Script Center and have since incorporated them into my [PS Template Script](https://github.com/gerryw1389/powershell/blob/main/Other/templates/_current-template-w-logging.ps1).

### To Resolve:

1. So going by template script:

   - So in the `Begin {}` block of all my scripts I write a functions called `Start-Log`, `Write-Log`, and `Stop-Log`. 
   - These simply create a folder in the script's running directory called `PSLogs` and then writes a logfile which is a transaction of the script
   - Under this folder you get `yyyy-mm-dd-function-name.log` files for each time you run a script.
   - If it runs more than once in the same day, you see them in a single file. Different days will produce new files.

2. Within the script I use `Write-Log` which is actually just using `Write-Verbose` but since `Verbose` is forced to be on at the beginning of the script, they will be written to the logfile. The power of these functions come from `Start-Transcript` and `Stop-Transcript` as it will record EVERYTHING that happens during the script, even terminating errors! This avoids the need for complex `If.. then` statements for logging!

3. Getting more technical:
   - The `Start-Log` function will create the `PSLogs` directory and the logfile. If it is over 10MB it will clear it.
   - The `Write-Log` function has two parameters - `InputObject` and `Color`. Input object works just like `Write-Output` in that you can pass objects and it will expand them out. Color is statically set to `Green` but you can change that if you wish.
   - The `Stop-Log` is kinda complicated. It stops the transcript and then takes the logfile and parses it and cleans it up.
   - The reason for the complicated clean up is that it takes output that normally looks like this:

   ```escape
   **********************
   Windows PowerShell transcript start
   Start time: 20200323065436
   Username: computerName\Gerry
   RunAs User: computerName\Gerry
   Configuration Name: 
   Machine: computerName (Microsoft Windows NT 10.0.18362.0)
   Host Application: PowerShell.exe -noexit -command Set-Location 'C:\scripts'
   Process ID: 2916
   PSVersion: 5.1.18362.628
   PSEdition: Desktop
   PSCompatibleVersions: 1.0, 2.0, 3.0, 4.0, 5.0, 5.1.18362.628
   BuildVersion: 10.0.18362.628
   CLRVersion: 4.0.30319.42000
   WSManStackVersion: 3.0
   PSRemotingProtocolVersion: 2.3
   SerializationVersion: 1.1.0.1
   **********************
   Transcript started, output file is C:\scripts\PSLogs\2020-03-23-Test2.log
   VERBOSE: 2020-03-23 06:54:36 AM: hello
   VERBOSE: 2020-03-23 06:54:36 AM: Function completed on computerName
   VERBOSE: 2020-03-23 06:54:36 AM: ####################</Function>####################
   **********************
   Windows PowerShell transcript end
   End time: 20200323065436
   **********************
   **********************
   Windows PowerShell transcript start
   Start time: 20200323065600
   Username: computerName\Gerry
   RunAs User: computerName\Gerry
   Configuration Name: 
   Machine: computerName (Microsoft Windows NT 10.0.18362.0)
   Host Application: PowerShell.exe -noexit -command Set-Location 'C:\scripts'
   Process ID: 2916
   PSVersion: 5.1.18362.628
   PSEdition: Desktop
   PSCompatibleVersions: 1.0, 2.0, 3.0, 4.0, 5.0, 5.1.18362.628
   BuildVersion: 10.0.18362.628
   CLRVersion: 4.0.30319.42000
   WSManStackVersion: 3.0
   PSRemotingProtocolVersion: 2.3
   SerializationVersion: 1.1.0.1
   **********************
   Transcript started, output file is C:\scripts\PSLogs\2020-03-23-Test2.log
   VERBOSE: 2020-03-23 06:56:00 AM: hello
   VERBOSE: 2020-03-23 06:56:00 AM: Function completed on computerName
   VERBOSE: 2020-03-23 06:56:00 AM: ####################</Function>####################
   **********************
   Windows PowerShell transcript end
   End time: 20200323065600
   **********************
   **********************
   Windows PowerShell transcript start
   Start time: 20200323065603
   Username: computerName\Gerry
   RunAs User: computerName\Gerry
   Configuration Name: 
   Machine: computerName (Microsoft Windows NT 10.0.18362.0)
   Host Application: PowerShell.exe -noexit -command Set-Location 'C:\scripts'
   Process ID: 2916
   PSVersion: 5.1.18362.628
   PSEdition: Desktop
   PSCompatibleVersions: 1.0, 2.0, 3.0, 4.0, 5.0, 5.1.18362.628
   BuildVersion: 10.0.18362.628
   CLRVersion: 4.0.30319.42000
   WSManStackVersion: 3.0
   PSRemotingProtocolVersion: 2.3
   SerializationVersion: 1.1.0.1
   **********************
   Transcript started, output file is C:\scripts\PSLogs\2020-03-23-Test2.log
   VERBOSE: 2020-03-23 06:56:03 AM: hello
   VERBOSE: 2020-03-23 06:56:03 AM: Function completed on computerName
   VERBOSE: 2020-03-23 06:56:03 AM: ####################</Function>####################
   **********************
   Windows PowerShell transcript end
   End time: 20200323065603
   **********************
   ```

   - ... And makes it look like this:

   ```escape
   2020-03-23 09:33:41 AM: ##########<Start Function>##########
   2020-03-23 09:33:41 AM: Function started on computerName
   2020-03-23 09:33:41 AM: hello
   2020-03-23 09:33:41 AM: hello
   2020-03-23 09:33:41 AM: Function completed on computerName
   2020-03-23 09:33:41 AM: ###########<End Function>###########
   2020-03-23 09:34:00 AM: ##########<Start Function>##########
   2020-03-23 09:34:00 AM: Function started on computerName
   2020-03-23 09:34:00 AM: hello
   2020-03-23 09:34:00 AM: hello
   2020-03-23 09:34:00 AM: Function completed on computerName
   2020-03-23 09:34:00 AM: ###########<End Function>###########
   ```

   - I'm wondering if this is the basis for the `-UseMinimalHeader` [switch](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.host/start-transcript?view=powershell-7#parameters) in PS7? O_o

4. You could skip most of this logging non sense if you wish and use the redirect method:

   ```powershell
   Powershell.Exe -Noprofile -File Test.Ps1 > Test.Log
   ```

   - This has been tested to record Write-Error, Write-Warning, and just about any other console output PS spits out.

