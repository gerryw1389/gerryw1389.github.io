---
title: 'PS: Helper Functions'
date: 2018-01-12T11:42:12+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/01/ps-helper-functions/
tags:
  - Windows
tags:
  - Scripting-Powershell
  - Powershell-Designing
  - Powershell-Modules
---
<!--more-->

### Description:

Helper functions are functions that are used in modules that are not meant to be used as a public function, but rather a &#8220;helper&#8221;. These go under the folder `Private` at the root of your module and you call them into scripts like:

   ```powershell
   Begin
   {
      If (-not (Test-path "$PSScriptRoot\..\Private\helpers.psm1"))
      {
         Import-Module $PSScriptRoot\..\Private\helpers.psm1"
      }
   }
   ```

You place that in the `Begin {}` block of your functions to call helper functions. And because your modules root psm1 file ignores that directory, you never see these functions get imported when you do `Import-Module yourModuleName`.

### To Resolve:

1. I have made a couple of these over the years but have since just placed these functions into my [template](https://github.com/gerryw1389/powershell/blob/main/Other/templates/_current-template-w-logging.ps1) since I don't always distribute modules completely and instead usually prefer self-contained scripts.

2. [Older helper function with logging functions](https://github.com/gerryw1389/powershell/blob/main/Other/templates/old-helpers-w-logging.psm1)

3. [Older helper function with Event log logging functions](https://github.com/gerryw1389/powershell/blob/main/Other/templates/old-helpers-w-eventlog.psm1)