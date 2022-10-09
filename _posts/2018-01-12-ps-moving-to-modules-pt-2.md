---
title: 'PS: Moving To Modules Pt. 2'
date: 2018-01-12T11:43:16+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/01/ps-moving-to-modules-pt-2/
categories:
  - Windows
  - SysAdmin
tags:
  - Scripting-Powershell
  - Powershell-Designing
---
<!--more-->

### Description:

This is a continuation post of [Moving to Modules](https://automationadmin.com/2017/12/ps-moving-to-modules/) I posted earlier. Main thing, I just wanted to go over design in this post. Here is a typical module:  
<img class="alignnone size-full wp-image-4925" src="https://automationadmin.com/assets/images/uploads/2018/01/template.jpg" alt="" width="137" height="226" /> 

A good way to see this is to download one of my Modules off [Github](https://github.com/gerryw1389). From here you can see the folder structure and how I use the modules in a portable fashion (explained below).

### To Resolve:

1. So the modules can be named whatever you want. The first thing you do is create a guid for your template so it can be unique in case you ever post it online. You can use online sites like [GUID Generator](https://www.guidgenerator.com/) or just Powershell: `$GUID = [guid]::NewGuid().ToString() |Clip.exe`

2. Next you can create and edit your template.psd1 file:

   ```powershell
   <#######<ModuleManifest>#######>
   <#######<Header>#######>
   # Name: Module Manifest
   # Date: 2017-03-27
   # Copyright: Gerry Williams
   # License: MIT License (https://opensource.org/licenses/MIT) 
   <#######</Header>#######>
   <#######<Body>#######>

   @{

   # Script module or binary module file associated with this manifest.
   RootModule = 'Template.psm1'

   # Version number of this module.
   ModuleVersion = '1.0'

   # ID used to uniquely identify this module
   GUID = '70802a57-92de-4ebb-bf2f-45bd3a819159'

   # Author of this module
   Author = 'Gerry.Williams'

   # Company or vendor of this module
   #CompanyName = 'Unknown'

   # Copyright statement for this module
   Copyright = '(c) 2017 Gerry Williams. All rights reserved.'

   # Description of the functionality provided by this module
   Description = 'Template module with Powershell functions'

   # Minimum version of the Windows PowerShell engine required by this module
   PowerShellVersion = '3.0'

   # Name of the Windows PowerShell host required by this module
   # PowerShellHostName = ''

   # Minimum version of the Windows PowerShell host required by this module
   # PowerShellHostVersion = ''

   # Minimum version of Microsoft .NET Framework required by this module
   # DotNetFrameworkVersion = ''

   # Minimum version of the common language runtime (CLR) required by this module
   # CLRVersion = ''

   # Processor architecture (None, X86, Amd64) required by this module
   # ProcessorArchitecture = ''

   # Modules that must be imported into the global environment prior to importing this module
   # RequiredModules = @()

   # Assemblies that must be loaded prior to importing this module
   # RequiredAssemblies = @()

   # Script files (.ps1) that are run in the caller's environment prior to importing this module.
   # ScriptsToProcess = @()

   # Type files (.ps1xml) to be loaded when importing this module
   # TypesToProcess = @()

   # Format files (.ps1xml) to be loaded when importing this module
   # FormatsToProcess = ''

   # Modules to import as nested modules of the module specified in RootModule/ModuleToProcess
   # NestedModules = @()

   # Functions to export from this module
   FunctionsToExport = '*'

   # Cmdlets to export from this module
   CmdletsToExport = '*'

   # Variables to export from this module
   VariablesToExport = '*'

   # Aliases to export from this module
   AliasesToExport = '*'

   # DSC resources to export from this module
   # DscResourcesToExport = @()

   # List of all modules packaged with this module
   # ModuleList = @()

   # List of all files packaged with this module
   # FileList = @()

   # Private data to pass to the module specified in RootModule/ModuleToProcess. This may also contain a PSData hashtable with additional module metadata used by PowerShell.
   PrivateData = @{

      PSData = @{

         # Tags applied to this module. These help with module discovery in online galleries.
         # Tags = @()

         # A URL to the license for this module.
         # LicenseUri = ''

         # A URL to the main website for this project.
         # ProjectUri = ''

         # A URL to an icon representing this module.
         # IconUri = ''

         # ReleaseNotes of this module
         # ReleaseNotes = ''

      } # End of PSData hashtable

   } # End of PrivateData hashtable

   # HelpInfo URI of this module
   # HelpInfoURI = ''

   # Default prefix for commands exported from this module. Override the default prefix using Import-Module -Prefix.
   # DefaultCommandPrefix = ''

   }

   <#######</Body>#######>
   <#######</ModuleManifest>#######>
   ```

3. Next you want to create and edit your template.psm1 file. The good thing about this is that it is the same for any module you create:

   ```powershell
   <#######<Module>#######>
   <#######<Header>#######>
   # Name: Module
   # Date: 2018-03-18
   # Copyright: Gerry Williams
   # License: MIT License (https://opensource.org/licenses/MIT) 
   <#######</Header>#######>
   <#######<Body>#######>


   $files = @( Get-ChildItem -Path $PSScriptRoot\Public\*.ps1 -Recurse -ErrorAction SilentlyContinue)
   $files | ForEach-Object `
   { 
      . $_.fullname
   }

   Export-ModuleMember -Function *

   <#######</Body>#######>
   <#######</Module>#######>
   ```

4. Now you create your folders:  
   - Private => This is where private functions go, this is where my [helpers.psm1 file](https://automationadmin.com/2018/01/ps-helper-functions/) lives with helper functions. These will not be exported by the module.  
   - Public => This is where all your .ps1 scripts go. If you do like me, you will make them all advanced functions and the way users will use them is:
     - They will import your module and then just call the function that way => preferred.  
     - For one offs, they can navigate to your Public folder in powershell or Windows Explorer and dot source your script and then call the function from within it.

5. Lastly, in the Public folder, you create functions that use a setup like in [my current Template script](https://github.com/gerryw1389/powershell/blob/main/Other/templates/_current-template-w-logging.ps1)

6. 2018-09-22: Just wanted to add that setting them up this way allows me to pull from Github pretty easily:

   ```powershell
   # Launching scripts from Github
   Write-Output "Launching template script"
   [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"

   $Path = "$Env:UserProfile\Downloads" + "\Temp"
   New-Item -ItemType Directory -Path $Path -Force | Out-Null

   $PrivatePath = $Path + "\Private"
   New-Item -ItemType Directory -Path $PrivatePath -Force | Out-Null
   $Download = "$Path\Private\helpers.psm1"
   $URI = "https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Private/helpers.psm1"
   $Response = Invoke-RestMethod -Method Get -Uri $URI
   $Response | Out-File $Download -Encoding ASCII

   $PublicPath = $Path + "\Public"
   New-Item -ItemType Directory -Path $PublicPath -Force | Out-Null
   $Download = "$Path\Public\set-template.ps1"
   $URI = "https://raw.githubusercontent.com/gerryw1389/powershell/main/gwConfiguration/Public/Set-Template.ps1"
   $Response = Invoke-RestMethod -Method Get -Uri $URI
   $Response | Out-File $Download -Encoding ASCII

   $Batch = $PublicPath + "\set-template.bat"
   $String = @'
   @ECHO OFF
   PowerShell.exe -NoProfile ^
   -Command "& {Start-Process PowerShell.exe -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command ". "%~dpn0.ps1"; Set-Template "' -Verb RunAs}"
   '@
   Write-Output $String | Out-File -LiteralPath $Batch -Encoding ASCII

   Start-Process $Batch -Verb Runas
   cmd /c "pause"
   ```

