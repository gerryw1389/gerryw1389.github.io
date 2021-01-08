---
title: 'PS: Moving To Modules'
date: 2017-12-23T04:17:18+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/ps-moving-to-modules/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - Powershell-Designing
  - Powershell-Modules
---
<!--more-->

### Description:

So I have re-ordered most my scripts into Modules now and set them to follow [this](https://ramblingcookiemonster.github.io/Building-A-PowerShell-Module/) guide.

### To Resolve:

1. Essentially, at the root of your module, you create two folders `Public` and `Private`.

2. Under `Public` you place all your functions in one function per file that will get dot sourced when you import your function using `Import-Module yourModuleName`

3. Under `Private` you place psm1 files that will not get called. Instead, in the public functions, you call the module in your private folder like so:

   ```powershell
   If (-not (Test-path "$PSScriptRoot\..\Private\helpers.psm1"))
   {
      Import-Module $PSScriptRoot\..\Private\helpers.psm1"
   }
   ```

   
4. See [Part 2](https://automationadmin.com/2018/01/ps-moving-to-modules-pt-2/) to see my current setup.