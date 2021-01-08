---
title: 'PS: Forcing Preferences'
date: 2018-02-07T00:22:49+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/02/ps-forcing-preferences/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

So I've been watching the 90 part Don Jones series on CBT Nuggets on Powershell and one thing he is always saying is &#8220;Don't assume what the user will use your script for… don't force your preferences on other people&#8221; like comments. Well if you ever stumble upon my script and have issues with my setup, here are somethings you can do to fix.

### To Resolve:

1. So in the `Begin {}` block of all my scripts I write a functions called `Start-Log`, `Write-Log`, and `Stop-Log`. These simply create a folder in the script's running directory called `PSLogs` and then writes a logfile which is a transaction of the script, it actually looks really good! But... but.. maybe you don't want it - that's fine. Do this:
   - Comment out `Start-Log` in the begin block and `Stop-log` in the end block.
   - Rename `Write-Log` to `Write-output`.

2. This should fix most scripts, but you might have to see if `-Color` was ever passed as I sometimes use that as well.

3. If you wanted to make logging optional like [here](https://github.com/gerryw1389/powershell/blob/main/Other/templates/old-template-w-logging-optional.ps1), you would have to do something like:

   ```powershell
   Begin
      {       
         If ($($Logfile.Length) -gt 1)
         {
               $EnabledLogging = $True
         }
         Else
         {
               $EnabledLogging = $False
         }
         
         
         Filter Timestamp
         {
               "$(Get-Date -Format "yyyy-MM-dd hh:mm:ss tt"): $_"
         }

         If ($EnabledLogging)
         {
               # Create parent path and logfile if it doesn't exist
               $Regex = '([^\\]*)$'
               $Logparent = $Logfile -Replace $Regex
               If (!(Test-Path $Logparent))
               {
                  New-Item -Itemtype Directory -Path $Logparent -Force | Out-Null
               }
               If (!(Test-Path $Logfile))
               {
                  New-Item -Itemtype File -Path $Logfile -Force | Out-Null
               }
      
               # Clear it if it is over 10 MB
               $Sizemax = 10
               $Size = (Get-Childitem $Logfile | Measure-Object -Property Length -Sum) 
               $Sizemb = "{0:N2}" -F ($Size.Sum / 1mb) + "Mb"
               If ($Sizemb -Ge $Sizemax)
               {
                  Get-Childitem $Logfile | Clear-Content
                  Write-Verbose "Logfile has been cleared due to size"
               }
               # Start writing to logfile
               Start-Transcript -Path $Logfile -Append 
               Write-Output "####################<Script>####################"
               Write-Output "Script Started on $env:COMPUTERNAME" | TimeStamp
         }
      }
      
      Process
      {   
         Try
         {
               
               
               # Script      
               # Here
      

         }
         Catch
         {
               Write-Error $($_.Exception.Message)
         }
      }

      End
      {
         If ($EnableLogging)
         {
               Write-Output "Script Completed on $env:COMPUTERNAME" | TimeStamp
               Write-Output "####################</Script>####################"
               Stop-Transcript
         }
   ```

