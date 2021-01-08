---
title: 'PS: Build A Path Dynamically'
date: 2018-05-27T03:23:34+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/ps-build-a-path-dynamically/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

So just for learning purposes, I wanted to create a function that creates all directories leading up to a path if you just pass a path's name as a parameter. We all know that adding a &#8220;-Force&#8221; to New-Item will do this for you, but still…

### To Resolve:

1. First, we want to create a path:

```powershell
$Path = "HKCU:\SOFTWARE\Microsoft\Office\15.0\Outlook\AutoDiscover"
```

2. Next, split it into parts. This is important because paths will have different levels. For example, C:\scripts\mydir is two levels deep and c:\scripts\mydir\hello\world is four levels deep. We want the function to be able to dynamically create these directories for us.

```powershell
$PathList = $Path -split '\\'
```

3. Next, we want to initiate an array to put each into:

```powershell
$NewPath = ''
```

4. Now we create a loop to create the directories

```powershell
foreach ($p in $PathList) 
{
    $NewPath += "$p\"
    if (-not(Test-Path $NewPath)) 
    {
        New-Item -ItemType Directory -Path $NewPath | Out-Null
    }
}
```

NOTE: What this loop does is add each part of the path, $p, into the $NewPath array. It then creates that part of the path if it doesn't exist already. So the first iteration will create &#8220;HKCU:&#8221; but this obviously exists so it will skip to the next one &#8220;HKCU:\SOFTWARE&#8221; and so on until it has stepped through all directories.