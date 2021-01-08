---
title: 'PS: Compare Large Sets'
date: 2018-04-30T04:39:10+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/ps-compare-large-sets/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

So I found some code on [/r/powershell](https://reddit.com/r/powershell) the other day, and went over it to let it sink in. This is how you would go about comparing large sets using Hashtables from two or more arrays.

### To Resolve:

1. Code:

   ```powershell
   Write-Host "Testing Hashtable array compare"
   Measure-Command 
   {
      $Array1 = 1..9999 # Reference Array counting 1 to 9999
      $Array2 = 2..9998 # Difference Array counting 2 to 9998
      #If my code works you'll get back 2 missing values
      $Hash = @{} # Hashtable created from the difference array
      #This builds our hastable, we're looking through the array and mapping the values and keys to $Hash
      # hashtables can't have duplicate keys the IF -not checks to make sure it doesn't exist already
      $Array2 | ForEach-Object -Process { IF (-not $Hash.ContainsKey($_))
         {
               $Hash.Add($_, "") # the value you add here doesn't matter, I like to do "" but you can easily to "some value", "Bob", or "Jim"
         }} 
      Write-Host "$(Get-Date -Format u) | Checking for missing Values..."
      $missing = @() # empty array to put our difference into
      ForEach ($item in $Array1)
      {
         IF ($Hash.ContainsKey($item))
         {
               #Do Nothing
         }
         ELSE
         {
               Write-Host "Array 2 Missing Value: $item"
               $missing += $item
         }
      }
      write-host "Found : $($missing.Count) missing items"
   } | 
   Format-table TotalMilliseconds 

   Write-Host "Testing Where-Object Array Compare"
   Measure-Command 
   {
      $Array1 = 1..9999 # Reference Array counting 1 to 9999
      $Array2 = 2..9998 # Difference Array counting 2 to 9998
      #If my code works you'll get back 2 missing values
      Write-Host "$(Get-Date -Format u) | Checking for missing Values..."
      $missing = $Array1 | ? {$_ -notin $Array2}
      write-host "Found : $($missing.Count) missing items"
   } | 
   Format-table TotalMilliseconds
   ```

2. The gist is:

   - You create two arrays.

   - You create an empty hashtable and fill it with the values of array 2. Remember that hashtables use the &#8220;key=value&#8221; setup. So we are setting each value in the array as the KEY to the hashtable and setting its associated value as whatever we want. I just used an empty string &#8221;, but as I commented, you can call this &#8220;bob&#8221;, &#8220;jim&#8221; or &#8220;whatever&#8221;. At this point you have a hashtable called `$Hash @{ 2=''; 3=''; 4=''}` ... and so on to 9998.

   - Now we create an empty array called $missing = @()

   - Loop through each item in Array 1 and if the Hashtable contains the item, do nothing. If it doesn't contain the item, add it to the array in step &#8220;c&#8221;.

   - As you can see in the Measure-Command results, it is much faster to use this method instead of the &#8220;Where-Object compare&#8221;.