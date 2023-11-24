---
title: 'PS: Compare Files'
date: 2016-05-30T06:33:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ps-compare-files/
tags:
  - Windows
tags:
  - Scripting-Powershell
  - FileSystem
---
<!--more-->

### Description:

Many administrators create baselines for systems when they are working and then take snapshots afterwards to compare. Follow these steps to compare files in PS.

### To Resolve:

1. Let's use Processes for example. We will compare current processes with a &#8220;baseline&#8221; test (a snapshot of when the system was stable).

   ```powershell
   Get-Process | Export-Clixml C:\Procs.Xml
   ```

2. Open a few &#8220;notepad.exe&#8221; instances. Now run:

   ```powershell
   Compare-Object (Import-Clixml C:\Procs.Xml) | (Get-Process)
   ```

3. Type:

   ```powershell
   Compare-Object (Import-Clixml C:\Procs.Xml) (Get-Process) -Property Name
   ```

4. Use the above steps to compare just about anything in Powershell. CliXML is preferred because it holds the most properties similar to an object.

5. Another example:

   ```powershell
   # Shows same between 1 and 2  
   # This shows all the servers that are the same between the vuln.txt and prod.txt.  
   Compare-Object -ReferenceObject $( Get-Content "c:\_gwill\temp\vuln.txt" ) -DifferenceObject $( Get-Content "c:\_gwill\temp\prod.txt" ) -IncludeEqual -ExcludeDifferent

   # Shows what is in 2 that is not in 1.  
   # Shows all the servers that are in prod.txt, but not in vuln.txt

   Compare-Object -ReferenceObject $( Get-Content "c:\_gwill\temp\vuln.txt" ) -DifferenceObject $( Get-Content "c:\_gwill\temp\prod.txt" ) |
   Where-Object -Property SideIndicator -eq '=>'

   # Shows what is in 1 that is not in two  
   # Shows all the servers that are in vuln.txt, but not in prod.txt

   Compare-Object -ReferenceObject $( Get-Content "c:\_gwill\temp\vuln.txt" ) -DifferenceObject $( Get-Content "c:\_gwill\temp\prod.txt" ) |
   Where-Object -Property SideIndicator -eq '<='
   ```