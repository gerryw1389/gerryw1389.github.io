---
title: 'PS: Removing Backticks'
date: 2018-02-24T03:19:23+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/02/ps-removing-backticks/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

So lately I have been going over my code and trying to remove backticks. That is because, although they work, they can cause a script to fail with a simple space character is placed after them. The way to do this has often been to place objects in hash tables instead. So now I follow this setup for hash tables and arrays:

### To Resolve:

1. Hashtables go in four steps => initialize, populate, call the function, and then clear the variable. You will see this often with my [SetReg](https://automationadmin.com/2018/01/ps-helper-functions/) function for example:

   ```powershell
   $Params = @{}
   $Params.Path= "HKCU:\Some\Path"
   $Params.Name = "Category"
   $Params.Value = "1"
   $Params.Type = "DWORD"
   }
   SetReg @Params
   Clear-Variable -Name Params
   ```

   - To test a value

   ```powershell
   if( $Params.Value -eq 1 ){...}
   #For Example from the hash table above:
   If ($Params.Path -eq "HKCU:\Some\Path")
   {
   Write-Output "Path is correct
   }
   ```

   - To remove a key:

   ```powershell
   $Params.remove("Value")
   # For example:
   $Params.Remove("Path")
   # After this, $Params will still have the "Name", "Value", and "Type" properties - just not Path.
   # For more reading, see my references below
   ```

2. Arrays:

   ```powershell
   # For short arrays (less than 100 items)
   $Array = @()
   ForEach ($Item in $Collection)
   {
   $Array += $Item
   }

   # For more than 100 items:
   $Array = [System.Collections.ArrayList]@()
   ForEach ($Item in $Collection)
   {
   [void]$Array.Add("something")
   }
   $Array.clear()
   ```

### References:

["Bye Bye Backtick: Natural Line Continuations in PowerShell "](https://get-powershellblog.blogspot.com/2017/07/bye-bye-backtick-natural-line.html?m=1)

["Hashtable as a collection of properties"](https://kevinmarquette.github.io/2016-11-06-powershell-hashtable-everything-you-wanted-to-know-about/#hashtable-as-a-collection-of-properties)