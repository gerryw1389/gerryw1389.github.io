---
title: 'PS: Modules'
date: 2016-05-30T05:55:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/powershell-modules/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - Powershell-Modules
---
<!--more-->

### Description:

Powershell comes with many modules installed by default, but many that you can install by running `get-module -listavailable` and then `import-module (moduleName)` from the list. Microsoft has highly encouraged developers for most server admin type software to develop PS modules in order to help admins like me take advantage of this powerful language. Follow these steps to install modules from third party developers.

### To Resolve:

1. First off, after any role or feature that you install on a server OS, there may be some new modules to import after it's installed.

   - Example modules:

   - Veeam Backup and Recovery => Find the Veeam ISO and extract (I used 7zip for this) the &#8220;Backup&#8221; folder. Run the `BPS_x64.msi` to install the PS plugins. To use them, open Veeam and click on Powershell from the File menu. From what I saw, it's not like a module you can import.

   - [Powershell Community Extensions](http://pscx.codeplex.com/releases)

   - [AWS PS Tools](https://aws.amazon.com/powershell/)

### Remoting Into A Server With Modules Installed:

1. One of the greatest things about powershell is remoting. You can have one machine on your LAN with has the newest powershell loaded with as many modules are available and then you can remote into that machine (step 2), and run commands from it instead of having all your machines install the newest PS version and import all the modules/plug ins.

2. Run the following:

   ```powershell
   Enter-Pssession -ComputerName Server01
   Invoke-Command -ComputerName Server01 Get-Module -ListAvailable
   ```

3. Then you can import the modules you want by typing: `import-module (moduleName)`. Note that people tend to do this on the server in their domain with most roles installed.

4. Then you can learn the new commands by typing `get-command -module (moduleName)`. `import-module` is one of the common commands stored in PowerShell Profiles. If you use Powershell a lot, there is a chance that you get annoyed having to dot source your files all the time, follow this setup in order for PS to auto load your favorite functions and modules:

### For AutoImport Functions:

1. Copy all your favorite functions to a folder of your choice. Just put the functions in the file, don't call the functions at the end. Ex: C:\Scripts

2. Navigate to `C:\Users\yourUserName\Documents\WindowsPowershell` and create the following two files if they don't exist: `Microsoft.PowerShell_profile.ps1` and `Microsoft.PowerShellISE_profile.ps1`

3. Set the value of both scripts to be:

   ```powershell
   $files = @( Get-ChildItem -Path c:\scripts -Recurse -Include *.ps1 -ErrorAction SilentlyContinue )
   $files | ForEach-Object { . $_ }
   Write-Output "Custom PowerShell Environment Loaded"
   ```

   - You could put all the functions directly in your profile, but some say that this will cause Powershell to take a long time to load so they choose to follow this method.

### For AutoImport Modules:

1. If you download modules off the internet, most of them will register themselves if they come with an installer. If not, just type: `$psmodulepath` This will return all the paths that Powershell v3+ load modules automatically. If you have a custom module, just put it in one of those paths, just remember that you have to create a folder and filename.psm1 with the EXACT same name for Powershell to auto-import the modules.

2. If you have a directory of modules that you want Powershell to load automatically, run the following commands:

   ```powershell
   $originalpaths = (Get-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Session Manager\Environment' -Name PSModulePath).PSModulePath
   # Add your new path to below after the ;
   $newPath=$originalpaths+';C:\Scripts'
   Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Session Manager\Environment' ' -Name PSModulePath –Value $newPath
   ```

### To Create A Module:

1. Create a folder and name it whatever you want, for example &#8220;gwtoolbox&#8221;. Place this folder in any PS Module path or just add it following the steps above.

2. Inside that folder, create a psm1 file with the same name as the folder. Here is my contents of mine:

   ```powershell
   <#######<Module>#######>
   <#######<Header>#######>
   # Name: Module
   # Date: 2017-03-27
   # Copyright: Gerry Williams
   # License: MIT License (https://opensource.org/licenses/MIT)
   <#######</Header>#######>
   <#######<Body>#######>

   $files = @( Get-ChildItem -Path $PSScriptRoot -Recurse -Include *.ps1 -ErrorAction SilentlyContinue )
   $files | ForEach-Object { . $_ }

   Export-ModuleMember -Function *

   <#######</Body>#######>
   <#######</Module>#######>
   ```

3. Inside that folder, create as many folders and subfolders as you want with all your scripts. Just make sure **NOT** to call the functions within the scripts. Ex:

   - example.ps1:

   ```powershell
   #start#

   function create-folders

   {

   New-Item folder1 -itemtype directory

   New-Item folder2 -itemtype directory

   }

   create-folders # <---- DON'T DO THIS!!

   #end#
   ```

4. That's it! If you wish to share your scripts that you create, just create a module for them first, zip it, and send it to whoever. This is the best way to make script portable and is the default way to share Powershell scripts.