---
title: 'PS: Get Text Between Two Lines'
date: 2019-04-09T15:23:11+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/ps-get-text-between-two-lines/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

Use this to get all text between two lines in a text file.

### To Resolve:

1. One way:

   ```powershell
   $file = Get-Content C:\scripts\text.txt
   # get the line numbers of text you want to extract from. For example, lines 1 and 32
   # remember to subtract 1 because indexes start at 0
   $inner = $file[0]
   $outer = $file[31]

   # now we use the readcount property which is an int to loop through all the lines between and add to an array - $array
   $array = @()
   for ($i = ($inner.ReadCount); $i -lt ($outer.ReadCount - 1); $i++)
   {
   $array += $file[$i]
   }
   # $array now contains all lines between your start and end points!
   ```

2. Another way

   ```powershell
   # this will return all lines that don't match a specific pattern.
   $results = Select-String -Pattern '\*\*\*' -NotMatch -AllMatches C:\scripts\file.txt

   # you can then loop through $results[$i].line to see the values and put them in an array.
   $array = @()
   for ($i = 0; $i -lt $results.Length; $i++)
   { 
      $array += $results[$i].Line
   }
   ```

3. For example, in my "clean transcripts" section of my logging functions:

   ```powershell
   # Now we will clean up the transcript file as it contains filler info that needs to be removed...
   $Transcript = Get-Content $Logfile -raw

   # Create a tempfile
   $TempFile = $PSScriptRoot + "\PSLogs\temp.txt"
   New-Item -Path $TempFile -ItemType File | Out-Null

   # Get all the matches for PS Headers and dump to a file
   $Transcript | 
      Select-String '(?smi)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*([\S\s]*?)\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*' -AllMatches | 
      ForEach-Object {$_.Matches} | 
      ForEach-Object {$_.Value} | 
      Out-File -FilePath $TempFile -Append

   # Compare the two and put the differences in a third file
   $m1 = Get-Content -Path $Logfile
   $m2 = Get-Content -Path $TempFile
   $all = Compare-Object -ReferenceObject $m1 -DifferenceObject $m2 | Where-Object -Property Sideindicator -eq '<='
   $Array = [System.Collections.Generic.List[PSObject]]@()
   foreach ($a in $all)
   {
      [void]$Array.Add($($a.InputObject))
   }
   $Array = $Array -replace 'VERBOSE: ', ''

   Remove-Item -Path $Logfile -Force
   Remove-Item -Path $TempFile -Force
   # Finally, put the information we care about in the original file and discard the rest.
   $Array | Out-File $Logfile -Append -Encoding ASCII
   ```

