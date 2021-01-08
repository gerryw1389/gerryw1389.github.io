---
title: 'PS: Intro Commands'
date: 2016-06-02T20:50:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/ps-intro-commands/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

These are entry level Powershell Commands and how the language works:

NOTE: Almost all command prompt commands work just as well in Powershell. Search the &#8220;batch&#8221; label to see examples of them.

### Syntax

1. Cmdlets are small scripts that follow a dash-separated verb-noun convention such as &#8220;Get-Process&#8221;. Similar Verbs with Different Actions:

   - New- Creates a new resource  
   - Set- Modifies an existing resource  
   - Get- Retrieves an existing resource  
   - Read- Gets information from a source, such as a file  
   - Find- Used to look for an object  
   - Search- Used to create a reference to a resource  
   - Start- (asynchronous) begin an operation, such as starting a process  
   - Invoke- (synchronous) perform an operation such as running a command

2. Parameters: Each verb-noun named cmdlet may have many parameters to control cmdlet functionality.

3. Objects: The output of most cmdlets are objects that can be passed to other cmdlets and further acted upon. This becomes important in pipelining cmdlets.

   - <img class="alignnone size-full wp-image-689" src="https://automationadmin.com/assets/images/uploads/2016/09/ps-entry-commands.png" alt="ps-entry-commands" width="434" height="446" srcset="https://automationadmin.com/assets/images/uploads/2016/09/ps-entry-commands.png 434w, https://automationadmin.com/assets/images/uploads/2016/09/ps-entry-commands-292x300.png 292w" sizes="(max-width: 434px) 100vw, 434px" />
   - More [here](https://ramblingcookiemonster.wordpress.com/2012/09/07/powershell-cheat-sheet/)

### Useful Cmdlets (and aliases)

#### To Get a directory listing (ls, dir, gci):

   ```powershell
   Get-ChildItem
   ```

#### To Copy a file (cp, copy, cpi):

   ```powershell
   Copy-Item src.txt dst.txt
   ```

#### To Move a file (mv, move, mi):

   ```powershell
   Move-Item src.txt dst.txt
   ```

#### To Find text within a file:

   ```powershell
   Select-String –path c:users*.txt –pattern password
   ls -r c:users -file | % {Select-String -path $_ -pattern password}
   ```

#### To Display file contents (cat, type, gc):

   ```powershell
   Get-Content file.txt
   ```

#### To Get present directory (pwd, gl):

   ```powershell
   Get-Location
   ```

#### To Get a process listing (ps, gps):

   ```powershell
   Get-Process
   ```

#### To Get a service listing:

   ```powershell
   Get-Service
   ```

#### To Format output of a command (Format-List):

   ```powershell
   ls | Format-List –property name
   ```

#### To Paginating output:

   ```powershell
   ls –r | Out-Host -paging
   ```

#### To Get the SHA1 hash of a file:

   ```powershell
   Get-FileHash -Algorithm SHA1 file.txt
   ```

#### To Export output to CSV:

   ```powershell
   Get-Process | Export-Csv procs.csv
   ```

### Pipelining, Loops, and Variables

#### To Pipe A cmdlet's output to another cmdlet:

   ```powershell
   Get-Process | Format-List –property name
   ```

#### To Use ForEach-Object in the pipeline (alias %):

   ```powershell
   ls *.txt | ForEach-Object {cat $_}
   ```

#### To Use Where-Object condition (alias where or ?):

   ```powershell
   Get-Process | Where-Object {$_.name –eq "notepad"}
   ```

#### To Generating ranges of numbers and looping:

   ```powershell
   1..10 | ForEach-Object{ New-Item -Name "$psitem.txt" -ItemType File} # creates 10 text files
   1..10 | % {echo "Hello!"} # writes "Hello!" 10 times
   ```

#### To Creating and list variables:

   ```powershell
   $tmol = 42
   ls variable:
   ```

#### To See An Example of passing cmdlet output down pipeline:

   ```powershell
   dir | group extension | sort
   Get-Service dhcp | Stop-Service -PassThru | Set-Service -StartupType Disabled
   ```

#### To Give A Choice

   ```powershell
   $OUPathValidate = $true
   While ($OUPathValidate) 
   {
      $OUPath = Read-Host 'INTERN/EXTERN'
      If ($OUPath.ToUpper() -eq 'INTERN') 
      {
         $OUPath = 'OU=Intern,OU=Users,OU=Zero,DC=int,DC=zero,DC=com'
         $OUPathValidate = $false
      } 
      ElseIf ($OUPath.ToUpper() -eq 'EXTERN')
      {
         $OUPath = 'OU=Extern,OU=Users,OU=Zero,DC=int,DC=zero,DC=com'
         $OUPathValidate = $false
      }
      Else 
      {
         Write-Host 'That is not a valid input, please use INTERN or EXTERN'
      }
   }
   ```

#### To Trap Errors

   ```powershell
   # Run your code with the ErrorVariable switch. Remember to just use a string as the name, no $ required
   Get-ChildItem $path | Move-Item -Destination $newlocation -ErrorVariable fileErrors

   # Your exceptions are now here
   $fileErrors

   # or:
   [System.Collections.ArrayList]$MoveItemErrors = @()
   $ItemsToMove = Get-ChildItem $path
   foreach ($item in $ItemsToMove) {
      try {
         $item | Move-item -Destination $newlocation -ErrorAction Stop
      }
      catch {
         $null = $MoveItemErrors.Add($_)
      }
   }
   ```

#### To Create A Hashtable:

   ```powershell
   $Params = @{
      'Path' = "HKCU:\Some\Path"
      'Name' = "Category"
      'Value' = "1" 
      'Type' = "DWORD"
   }
   SetReg @Params | Out-Null
   ```

#### To Use Arrays => Use lists instead where appropriate

   ```powershell
   $Array = [System.Collections.Generic.List[PSObject]]@()
   foreach ($I in $Items) 
   { 
   [void]$Array.Add($Item) 
   }
   ```

#### To See If A Switch Was Used

   ```powershell
   If ([Bool]($MyInvocation.BoundParameters.Keys -match 'Recurse')) { # Parameter 'Recurse' was used } Else { # Parameter 'Recurse' was NOT used }
   ```

#### To Learn to Use #Requires Statements

   ```powershell
   #Requires -Version <N>[.<n>]
   #Requires -PSSnapin <PSSnapin-Name> [-Version <N>[.<n>]]
   #Requires -Modules { <Module-Name> | <Hashtable> }
   #Requires -PSEdition <PSEdition-Name>
   #Requires -ShellId <ShellId>
   #Requires -RunAsAdministrator
   ```

#### To Pause A Script

   ```powershell
   Function Stop-Script 
   {
   Write-Output "Press Any Key To Continue ..."
   $Host.Ui.Rawui.Readkey("Noecho,Includekeydown") | Out-Null
   }
   # or
   cmd /c "pause"
   ```

#### To Set Param Blocks

   ```powershell
   # If in PS ISE, just use Ctrl+J!!
   # If not, something like
   [Cmdletbinding()]
      Param
      (
         [Parameter(Mandatory=$true, ValueFromPipeline=$true, ValueFromPipelineByPropertyName=$true, Position=0)]
         [String[]]$RegistryKey,
         
         [Parameter(Mandatory=$true, Position=1)]
         [String]$Username
      )
   ```

