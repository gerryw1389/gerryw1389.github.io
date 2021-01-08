---
title: How To Launch Console As System User
date: 2018-11-23T17:56:55+00:00
author: gerryw1389
layout: single
classes: wide
classes: wide
permalink: /2018/11/how-to-launch-console-as-system-user/
categories:
  - Windows
---
<!--more-->

### Description:

Despite how cool it sounds &#8220;Ya! Running as the highest privileged user on the system!&#8221;, I can count on my hands how often I've ever had to run a Powershell or CMD prompt as system. Even then, it was to just clear credential manager or something quick. Regardless of why, here is how you can go about getting a `NTAuthority\System` prompt:

### To Resolve:

1. Most common, download PSExec:

   ```powershell
   Start-Process -FilePath cmd.exe -Verb Runas -ArgumentList '/k C:\SysinternalsSuite\PsExec.exe -i -s powershell.exe'
   ```

   - This assumes you have the psexec executable in the `c:\sysinternalssuite` directory. This will give you an interactive SYSTEM prompt.

2. If you want to use the "all native" route, you can use task scheduler to run a script as system:  

   - Open Task Scheduler (`taskschd.msc`)  
   - Create a Basic Task  
   - Set a trigger (for example, "One time")  
   - Set the start time (Synchronize across time zones = UTC)  
   - Start a program
   - Program/script: `%SystemRoot%\syswow64\WindowsPowerShell\v1.0\powershell.exe`
   - Add arguments (optional): `–NoProfile –ExecutionPolicy Bypass –File C:\Demo\Get-CurrentUser.ps1`
   - Get-CurrentUser.ps1:

   ```powershell
   [PSCustomObject]@{
      'env:USERNAME' = $env:USERNAME
      'whoami' = whoami.exe
      'GetCurrent' = [Security.Principal.WindowsIdentity]::GetCurrent().Name
   } | Format-List | Out-File -FilePath C:\demo\whoami.txt
   ```

   - Check the box "Open the Properties dialog for this task when I click Finish"  
   - Change user to `SYSTEM` and configure for the OS of this machine (in my case it is Windows 10)  
   - I didn't checked the box &#8220;Run with highest privileges&#8221; in this case as not needed but sometimes you could need that enabled.

3. After it runs: If I check the content of `C:\demo\whoami.txt`, I see that the script successfully ran under the context of `NT AUTHORITY\SYSTEM`. As we can see, the current user was indeed `NT AUTHORITY\SYSTEM` (`the variable $env:USERNAME will show as MACHINE$`).

### References:

["Powershell Tip #53: Run PowerShell as SYSTEM (NT AUTHORITY\SYSTEM)"](http://powershell-guru.com/powershell-tip-53-run-powershell-as-system/)  

