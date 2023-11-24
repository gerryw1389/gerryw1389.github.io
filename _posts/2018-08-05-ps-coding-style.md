---
title: 'PS: Coding Style'
date: 2018-08-05T07:04:41+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/08/ps-coding-style/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

When it comes to Powershell, there are two main styles that people will follow (actually three, but the third is just like one of them):

### To Resolve:

1. Styles:

   - OTBS

   ```powershell
   function Get-Noun {
      end {
         if($Wide) {
               Get-Command | Sort-Object Noun -Unique | Format-Wide Noun
         } else {
               Get-Command | Sort-Object Noun -Unique | Select-Object -Expand Noun
         }
      }
   }
   ```

   - Stroustup: Same as OTBS but will place &#8220;else&#8221; in a new line.

   - Allman

   ```powershell
   function Get-Noun
   {
      end
      {
         if($Wide)
         {
               Get-Command | Sort-Object Noun -Unique | Format-Wide Noun
         }
         else
         {
               Get-Command | Sort-Object Noun -Unique | Select-Object -Expand Noun
         }
      }
   }
   ```


### References

["Where to put braces #24"](https://github.com/PoshCode/PowerShellPracticeAndStyle/issues/24)  
["PowerShellPracticeAndStyle"](https://github.com/PoshCode/PowerShellPracticeAndStyle/blob/master/Style-Guide/Code-Layout-and-Formatting.md)