---
title: 'PS: Logging'
date: 2017-08-12T04:56:42+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/ps-logging/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Logging is essential for anyone who is into scripting. Below are common ways to go about logging:

### To Resolve:

1. Use `Start-Transcript` in your `Begin {}` and `Stop-Transcript` in your `End {}`. This is my preferred method. See my current [Template script](https://github.com/gerryw1389/powershell/blob/main/Other/templates/_current-template-w-logging.ps1). Description [here](https://automationadmin.com/2017/09/ps-why-I-use-my-template-for-logging/).

2. Skip logging by doing `yourScript.ps1 > c:\scripts\log.log`

3. Use multiple `Write-Output "Doing action" | Out-File "c:\scripts\log.log" -Append -Encoding ASCII` but make sure it exists first.

4. Log to the Windows Event Viewer. I used to use this so look at my older module [Event Viewer logging](https://github.com/gerryw1389/powershell/blob/main/Other/templates/old-helpers-w-eventlog.psm1). Assuming you have copied my functions and wanted to write to the eventlog, you would:
    
   - Run your function calling my module in your `Begin {}` block. 
   - You could then run the following to see what was ran:

   ```powershell
   # Find out when a script was started:
   Get-Eventlog -Logname Application -Source $Logfile | Where-Object {$_.Eventid -Eq "10"}

   # Get all the informational events:
   Get-Eventlog -Logname Application -Source $Logfile | Where-Object {$_.Eventid -Eq "20"}

   # Get all the warning events:
   Get-Eventlog -Logname Application -Source $Logfile | Where-Object {$_.Eventid -Eq "30"}

   # Get all the error events:
   Get-Eventlog -Logname Application -Source $Logfile | Where-Object {$_.Eventid -Eq "40"}

   # Get all the error events that exited gracefully:
   Get-Eventlog -Logname Application -Source $Logfile | Where-Object {$_.Eventid -Eq "45"}

   # Get all the script completed successfully events:
   Get-Eventlog -Logname Application -Source $Logfile | Where-Object {$_.Eventid -Eq "50"}

   # To See Events:
   $Events = Get-Eventlog -Logname Application -Source $Logfile
   $Events | Sort -Property Index
   ```

   - The problem with this method was that the event viewer would have issues with certain things. So the Event Viewer doesn't store variables as well as logging does so you have to be creative when you log. For example (assuming you are using the functions in the module [Event Viewer logging](https://github.com/gerryw1389/powershell/blob/main/Other/templates/old-helpers-w-eventlog.psm1):

   ```powershell
   $A = Get-Process

   # Event viewer shows this garbage:
   Processes: System.Diagnostics.Process (AdjustService) System.Diagnostics.Process (ApplicationFrameHost) System.Diagnostics.Process (audiodg) System.Diagnostics.Process (chrome) System.Diagnostics.Process (chrome) System.Diagnostics.Process (chrome) System.Diagnostics.Process (chrome) System.Diagnostics.Process (chrome) System.Diagnostics.Process (chrome) System.Diagnostics.Process (chrome) System.Diagnostics.Process (chrome) System.Diagnostics.Process (chrome) System.Diagnostics.Process (chrome) System.Diagnostics.Process (chrome) System.Diagnostics.Process (conhost) System.Diagnostics.Process (csrss) System.Diagnostics.Process (csrss) System.Diagnostics.Process (cvpnd) System.Diagnostics.Process (dasHost) System.Diagnostics.Process (dllhost) System.Diagnostics.Process (dwm) System.Diagnostics.Process (explorer) System.Diagnostics.Process (explorer) System.Diagnostics.Process (fontdrvhost) System.Diagnostics.Process (fontdrvhost) System.Diagnostics.Process (GfExperienceService) System.Diagnostics.Process (GoogleCrashHandler) System.Diagnostics.Process (GoogleCrashHandler64) System.Diagnostics.Process (googledrivesync) System.Diagnostics.Process (googledrivesync) System.Diagnostics.Process (Greenshot) System.Diagnostics.Process (HeciServer) System.Diagnostics.Process (Idle) System.Diagnostics.Process (igfxCUIService) System.Diagnostics.Process (igfxEM) System.Diagnostics.Process (Jhi_service) System.Diagnostics.Process (LMI_Rescue_srv) System.Diagnostics.Process (LMIGuardianSvc) System.Diagnostics.Process (lsass)
   ```

   - If you just want to store a variable such as $A = Get-Process, you can just type:

   ```powershell
   Log "Processes: $a"
   ```

   - But if you want to access a property of the process like $a.processname, you have to surround it in parenthesis and place an outside dollar sign (called a subExpression):

   ```powershell
   Log "Processes: $($a.processname)"
   ```

   - So now we get this:

   ```powershell
   Processes: AdjustService ApplicationFrameHost audiodg chrome chrome chrome chrome chrome chrome chrome chrome chrome chrome chrome conhost csrss csrss cvpnd dasHost dllhost dwm explorer explorer fontdrvhost fontdrvhost GfExperienceService GoogleCrashHandler GoogleCrashHandler64 googledrivesync googledrivesync Greenshot HeciServer Idle igfxCUIService igfxEM Jhi_service LMI_Rescue_srv LMIGuardianSvc lsass MediaMonkey Memory Compression mqsvc MSASCuiL MsMpEng NisSrv notepad++ notepad++ NvBackend NVDisplay.Container NVDisplay.Container NvNetworkService nvtray OfficeClickToRun ONENOTE PnkBstrA powershell powershell_ise PresentationFontCache qc RAVCpl64 RuntimeBroker SearchFilterHost SearchIndexer SearchProtocolHost SearchUI SecurityHealthService services ShellExperienceHost sihost smartscreen smss SMSvcHost SMSvcHost spoolsv sqlservr sqlwriter Steam SteamService steamwebhelper
   ```

   - So now that we get the Event Viewer logging all of our processes, but why are they all on one line? Well we have to add a new line to each output process:

   ```powershell
   Log "These are your processes: `n$($a -Join [Environment]::Newline)" -Color Yellow

   # Notice the lack of a space after `n. Also if you want to access a property, so:

   Log "These are your processes: `n$($($a.processname) -Join [Environment]::Newline)" -Color Yellow

   # Now it looks right:

   These are your processes:
   AdjustService
   ApplicationFrameHost
   audiodg
   chrome
   chrome
   chrome
   chrome
   chrome
   ```

   - The last thing to touch on is tables. The log file will store these fine, but once again the Event Viewer will need some extra work. I find myself using Out-String quite a bit:

   ```powershell
   $C = Get-Culture | Select-Object *

   $D = Out-String -Inputobject $C -Width 100

   Log "$D"

   # or:

   $F = Out-String -Inputobject (Get-Culture)

   Log "$F"
   ```

5. Outside of plain logging, if you want to trap errors and then log them to a logfile you would do something like:

   ```powershell
   Try
   {
      Do-Something -Erroraction Stop
   }
   Catch
   {
      Write-Output "Error: $($_.Exception.Message)" | Out-File $Logfile -Append -Encoding ASCII
      Write-Error -Message $($_.Exception.Message)
   }
   ```

