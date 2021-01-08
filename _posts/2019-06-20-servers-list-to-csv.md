---
title: Servers List To CSV
date: 2019-06-20T00:54:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/servers-list-to-csv/
categories:
  - SysAdmin
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

One of the main things you will do with powershell is this workflow:

- Take this text file which has a list of servers listed one server per line
- and...
- Run this process on each of them remotely and give me the results
- Results should be put in a CSV or ran as jobs (this will have to be a different post)

For this post you may want to pull up [Test-PSRemoting](https://github.com/gerryw1389/powershell/blob/main/gwNetworking/Public/Test-PSRemoting.ps1) to see what I'm talking about. This is how you go about doing this:

### To Resolve:
 
1. So many of my functions have parameters that start off like

   ```powershell
   Param
   (
   [Parameter(Mandatory = $true, ValueFromPipeline = $true, ValueFromPipelineByPropertyName = $true, Position = 0)]   
   [ValidateScript( {(Test-Path $_) -and ((Get-Item $_).Extension -eq ".txt")})]
   [String]$FilePath,

   [Parameter(Mandatory = $false, Position = 2)]
   [String]$OutFile
   )
   ```

2. This just means that you will use `$FilePath` as the source text file and `$OutFile` as the CSV export.

3. How it usually works is later in the script you will see:

   ```powershell
   $servers = Get-Content $FilePath

   $CSV = [System.Collections.Generic.List[PSObject]]@()
   $Intro = 'Server,ServerSharePath,ShareSizeInGB' # Enter column names

   Foreach ($server in $Servers)
   {
      # Do some code to populate the variables below for THIS server.
      $CSVline = $Server + ',' + $ServerSharePath + ',' + $ShareSizeInGB
      # Add this server to the CSV
      [void]$CSV.Add($CSVLine)
   }

   If ( $OutFile -ne '' )
   {
      $CSV | Out-File $Outfile -Encoding ascii
   }
   Else
   {
      $CSV
   }
   ```

4. The way this reads is:
 
   - Take the contents in the source file and store them in variable `$servers` as an array
   - Create a list object that will eventually be our CSV; Write the first line (header)
   - For each server in the list, add a line to the CSV that gets the details we want.
   - At the end of the script, you will have an object `$CSV` which you can optionally pipe out to a file, or just write to a log (not shown above but used quite a bit in my [github functions](https://github.com/gerryw1389/powershell/).

   NOTE: Many scripters are violently against storing all this data in memory and dumping it in the end. They say 'it defeats the purpose of the pipeline' and will instead use other methods, that is fine! I don't really care what people like, I like to use what I know works and works for me. That is not to say this is wrong AT ALL because many agree it works fine, it's just some may instead say to write those objects to the pipeline. To each their own. I will say though that if you are running thousands of objects, then yes - find another method. The most servers I ever run against is less than 500 and I never see Powershell using more than a couple GB of memory.
   {: .notice--success}
