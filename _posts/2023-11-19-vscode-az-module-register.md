---
title: Vscode Az Module Register Issue
date: 2023-11-19T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/11/vscode-az-module-register
tags:
  - VsCode
  - Powershell
---
<!--more-->

### Description:

When using Windows Powershell 5.1 and only in VSCode, running `import-module az` results in many errors like:

   ```powershell
   Register-AzModule : The type initializer for 'Microsoft.Azure.Commands.Common.AzModule' threw an exception.
   At C:\Users\myuser\Documents\WindowsPowerShell\Modules\Az.Advisor\2.0.0\Az.Advisor.psm1:49 char:13
   ```

Doesn't seem to happen with native powershell console.

### To Resolve:

1. I followed [this issue](https://github.com/PowerShell/vscode-powershell/issues/4594) and [this issue](https://github.com/Azure/azure-powershell/issues/21647) to:

   - Delete all AZ folders in my user Powershell Modules directory.
   - Download and install again => `Install-Module -Name Az -RequiredVersion 9.6.0`

   - Then download the nupkg for Az.Accounts for [`2.12.1`](https://www.powershellgallery.com/packages/Az.Accounts/2.12.1)
   - Extract to the Az.Accounts subfolder under the version number.

1. Now when I run `Import-module az`, it works like in the past. My guess is this will continue to be an issue in the future and should probably switch to Powershell 7.
