---
title: 'PS: Relaunch Script As Admin'
date: 2018-04-30T04:26:56+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/ps-relaunch-script-as-admin/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

The following code can be used to relaunch unelevated scripts as elevated automatically inserting all parameters as required. Admittedly, I don't use this as much as I should and plan to look into this as the need arises.

### To Resolve:

1. Either put these functions in your begin block, dot source them, or put them in a helpers module.

   ```powershell
   # Helper - Test if admin
   function Test-IsAdmin() 
   {
      # Get the current ID and its security principal
      $windowsID = [System.Security.Principal.WindowsIdentity]::GetCurrent()
      $windowsPrincipal = new-object System.Security.Principal.WindowsPrincipal($windowsID)
      # Get the Admin role security principal
      $adminRole = [System.Security.Principal.WindowsBuiltInRole]::Administrator
      # Are we an admin role?
      if ($windowsPrincipal.IsInRole($adminRole))
      {
         $true
      }
      else
      {
         $false
      }
   }

   # Helper - Get UNC path from mapped drive
   function Get-UNCFromPath
   {
      Param
      (
         [Parameter(Position = 0, Mandatory = $true, ValueFromPipeline = $true)][String]$Path
      )
      if ($Path.Contains([io.path]::VolumeSeparatorChar)) 
      {
         $psdrive = Get-PSDrive -Name $Path.Substring(0, 1) -PSProvider 'FileSystem'
         # Is it a mapped drive?
         if ($psdrive.DisplayRoot) 
         {
               $Path = $Path.Replace($psdrive.Name + [io.path]::VolumeSeparatorChar, $psdrive.DisplayRoot)
         }
      }
      return $Path
   }

   # Main Function - Relaunch the script if not admin
   function Invoke-RequireAdmin
   {
      Param
      (
         [Parameter(Position = 0, Mandatory = $true, ValueFromPipeline = $true)][System.Management.Automation.InvocationInfo]$MyInvocation
      )

      if (-not (Test-IsAdmin))
      {
         # Get the script path
         $scriptPath = $MyInvocation.MyCommand.Path
         $scriptPath = Get-UNCFromPath -Path $scriptPath
         # Need to quote the paths in case of spaces
         $scriptPath = '"' + $scriptPath + '"'
         # Build base arguments for powershell.exe
         [string[]]$argList = @('-NoLogo -NoProfile', '-ExecutionPolicy Bypass', '-File', $scriptPath)
         # Add 
         $argList += $MyInvocation.BoundParameters.GetEnumerator() | ForEach-Object {"-$($_.Key)", "$($_.Value)"}
         $argList += $MyInvocation.UnboundArguments
         try
         {    
               Start-Process PowerShell.exe -PassThru -Verb Runas -WorkingDirectory $pwd -ArgumentList $argList
               exit $process.ExitCode
         }
         catch
         {
         }
         exit 1 
      }
   }
   ```

2. Then in your script's begin block, you will just add this one line:

   ```powershell
   Invoke-RequireAdmin $script:MyInvocation
   ```

3. For version 4+, just place the following at the top of  your script => [Source](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_requires?view=powershell-4.0) :

   ```powershell
   #Requires -RunAsAdministrator
   ```