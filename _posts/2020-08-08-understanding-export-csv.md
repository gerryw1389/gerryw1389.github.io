---
title: Understanding Export-CSV
date: 2020-08-08T11:10:16-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/08/understanding-export-csv
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

[Reddit post](https://www.reddit.com/r/PowerShell/comments/i60zrs/issues_understanding_exportcsv/):

So I'm working on [sds](https://docs.microsoft.com/en-us/schooldatasync/csv-files-for-school-data-sync) and trying to upload CSV's and I ran into something I cannot figure out: Why does this work?

   ```powershell
   Import-Csv 'C:\scripts\section.csv' | Select-Object * | Export-Csv -Path "c:/scripts/section3.csv" -NoTypeInformation
   ```

But this doesn't?

   ```powershell
   $sectionCsv = Import-Csv 'C:\scripts\section.csv'
   $tempCSV = $sectionCsv | 
      Select-Object -Property "SIS ID","School SIS ID","Section Name","Section Number","Term SIS ID","Term Name","Term StartDate","Term EndDate","Course SIS ID","Course Name","Course Number","Course Description","Status"
   Export-Csv -InputObject $tempCSV -Path "c:/scripts/section2.csv" -NoTypeInformation
   ```

When I say it doesn't, I mean that it is giving me a 1kb file:

   ```escape
   "Count","Length","LongLength","Rank","SyncRoot","IsReadOnly","IsFixedSize","IsSynchronized"
   "25169","25169","25169","1","System.Object[]","False","True","False"
   ```

I tried googling and found a few examples like [this](https://stackoverflow.com/questions/19450616/export-csv-exports-length-but-not-name) but I still cannot understand. In vscode, if I type `tempCSV`, I get a list of all the records like one would expect. Why cannot export-csv this object which is of type `Selected.System.Management.Automation.PSCustomObject` ? Does it have to just be a `PSCustomObject`?

To be clear I'm only trying to learn as the one liner solves the issue but trying to see why I cannot grasp such a simple concept. Another thing I have tried is:

   ```powershell
   $csvPath = Get-Childitem 'C:/scripts'
   foreach ( $csv in $csvPath)
   {
      $tempCsv = Import-Csv $($csv.fullname)
      $columnNames = $tempcsv | get-member -MemberType "NoteProperty"

      $list = @()
      foreach ( $column in $($columnNames.Name))
      {
         $list += $column
      }
      $export = $tempCSV | Select-Object -Property $list
      
      $params = @{
         "InputObject"       = $export
         "Path"              = ( "c:/scripts/" + $($csv.name) )
         "Encoding"          = "ascii"
         "NoTypeInformation" = $True
      }
      Export-Csv @params
   }
   ```

Again, this exports the 1kb file instead the whole CSV. If I check `$export` in debug, it lists the 5,000 records I would expect to see in the final CSV. Lastly, the reason I'm doing this is because I have a series of CSVs I have built manually and they work fine, but I want a 'clean' CSV with quotes around each row so I'm doing this. The one liner produces this, but it irks me because I'm not a huge fan of piping because I want to understand. Ideally the solution will `import-csv`, get all the columns that are not built in (NoteProperties and not regular properties or methods), and export it to a new CSV. Thanks!

### To Resolve:

1. [Answer](https://stackoverflow.com/questions/38772645/powershell-piped-input-to-export-csv-different-from-inputobject) per [u/Jantu01](https://www.reddit.com/user/Jantu01/)

   - Perfect! `one.csv` and `three.csv` are the same, thank you much!

   ```powershell
   $a = Get-Process | Select-Object -first 5 -Property "name"
   $a | Export-CSV -Path 'c:\scripts\one.csv' -NoTypeInformation

   New-Item -Itemtype "file" -Path 'c:\scripts\three.csv' -Value 'something' -Force | Out-Null
   #$a = Get-Process | Select-Object -first 5
   # System.Diagnostics.Process

   #get-member -InputObject $a
   # System.Object[]

   # Works!
   $a | ForEach-Object -Begin { 
      Clear-Content 'c:\scripts\three.csv' 
   } -Process {
      Export-CSV -InputObject $_ -Path 'c:\scripts\three.csv' -Append -NoTypeInformation
   }
   ```

   - And:

   ```powershell
   $a = Get-Process | Select-Object -first 5 -Property "name"
   $a | Export-CSV -Path 'c:\scripts\one.csv' -NoTypeInformation

   New-Item -Itemtype "file" -Path 'c:\scripts\three.csv' -Value 'something' -Force | Out-Null
   #$a = Get-Process | Select-Object -first 5
   # System.Diagnostics.Process

   #get-member -InputObject $a
   # System.Object[]

   # Works!
   $a | ForEach-Object -Begin { 
      Clear-Content 'c:\scripts\three.csv' 
   } -Process {
      Export-CSV -InputObject $_ -Path 'c:\scripts\three.csv' -Append -NoTypeInformation
   }
   ```

2. Another good answer from [u/MadWithPowerShell](https://www.reddit.com/user/MadWithPowerShell/):

   ```escape
   Export-CSV is specifically designed as a pipeline command. Parameter -InputObject is not intended to be used explicitly, and not with the entire array of objects at one time. It is designed to get the items in the array one at a time, through the pipeline.

   This:

   $TempCSV | Export-CSV

   NOT this:

   Export-CSV -InputObject $TempCSV

   Sort-Object, Where-Object, Whatever-Object, etc., are similarly pipeline commands. They all have the -InputObject parameter, but they are all designed to only work as expected when input objects are passed to them through the pipeline, not explicitly.
   ```
