---
title: 'PS: Hardware Commands'
date: 2016-06-02T21:02:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/ps-hardware-commands/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

These commands have to do with the filesystem, services, ext:

NOTE: Almost all command prompt commands work just as well in Powershell. Search the [Scripting-CMD](https://automationadmin.com/tags/#scripting-cmd) label to see examples of them.
{: .notice--success}

#### To Create A Text File of All Files Older Than 6 Months Old:

   ```powershell
   dir | where-object {$_.LastWriteTime -lt (get-date).addmonths(-6)} | out-file c:blah.txt
   ```

#### To Create A New Folder:

   ```powershell
   New-Item -Path . -Name Windowspowershell -Itemtype Directory 
   # Or you could do the old fashion way by typing mkdir WindowsPowerShell or md WindowsPowerShell
   ```

#### To Read the Contents of A Text File Within PS:

   ```powershell
   Get-Content text.txt
   ```

#### To Re-Write Certain Words In A Text File:

   ```powershell
   (Get-Content Example.Txt) | Foreach-Object {$_ -Replace "Warning", "Caution"} | Set-Content Example-Revised.Txt
   ```

#### To compress multi line strings:

   ```powershell
   $ex = @"
   This
   Is
   Text
   On
   Multiple
   Lines
   "@

   # join all lines as one long string:
   $2 = $ex.Replace("`r`n","")
   $2
   # join all lines with a comma as one long string:
   $3 = $ex.replace("`r`n", ",")
   $3
   ThisIsTextOnMultipleLines
   This,Is,Text,On,Multiple,Lines
   ```

#### To convert to a string:

   ```powershell
   $1 = get-process
   $2 = $1 | out-string -Stream
   # now you can access each object as a line by the index number
   $2[3]
   10060     756   212536      23096              3080   0 AdjustService
   ```

   List All Files You Have Modified Today:

   ```powershell
   Dir | Where-Object {$_.LastWriteTime -ge [DateTime]::Today}
   ```

### Services, Event Logs, and Processes:

#### To Create A Web Page Of Latest 5 Events In System Log:

   ```powershell
   Get-Eventlog -Logname System -Newest 5 | Select -Property Eventid, Timewritten, Message | Sort Timewritten -Descending | Convertto-Html | Out-File C:Error.Htm
   ```

#### To Get The Highest Running Processes:

   ```powershell
   # Replace 900 With Whatever Cutoff You Want.
   Get-Process | Where Handles -Gt 900 | Sort Handles -Descending
   ```

#### To Get A List of All Critical Events From A Group of Computers Listed At `Servers.Txt`:  
   - NOTE: You must have enabled remoting on these computers for this to work.

   ```powershell
   Invoke-Command -Computername (Get-Content C:\Servers.Txt) -Scriptblock {Get-Eventlog -Logname System | Where {$_Leveldisplayname -Eq "Critical"}}
   ```

#### To See If Your Computer Shutdown Unexpectedly:

   ```powershell
   Get-Eventlog -Log System –Newest 1000 | Where-Object {$_.Eventid –Eq '1074'} | Format-Table Machinename, Username, Timegenerated –Autosize
   ```

#### To Get Free Disk Space For Drive `C:`:

   ```powershell
   Get-Ciminstance Win32_Logicaldisk -Filter "Deviceid='C:'" | Select @{N='Freegb' ; E={$_.Freespace / 1gb -As [Int]}}
   ```

#### To Get All Running Services On A Local Machine:

   ```powershell
   Get-Service | Where {$_.Status -Eq "Running"}
   ```

#### To Shutdown A Remote Computer:

   ```powershell
   Stop-Computer –Computer Computername –Credential # Computername\Accountname
   ```

#### To Create A Web Page of All Services That Are Set To Start Automatically But Are Not Running:

   ```powershell
   Get-Wmiobject -Class Win32_Service | Where { $_.State -Ne 'Running' -And $_.Startmode -Eq 'Auto' } | Convertto-Html | Out-File Serviceerrors.Html
   ```

#### To See If A Specific Windows Upate is installed:

   ```powershell
   Get-Hotfix -Id Kb2862152
   ```

### How To Expand With Powershell:

#### To Find The Last Boot Time of A Computer:

   ```powershell
   (Get-Date) - (Get-CimInstance Win32_operatingSystem).Lastbootuptime
   ```

#### To Get The Last Boot Time For A Remote Computer:

   ```powershell
   Get-Wmiobject -Class Win32_Operatingsystem -Namespace Rootcimv2 -Computer (Computername)| Select __Server,@{Label='Lastbootuptime';Expression={$_.Converttodatetime($_.Lastbootuptime)} }
   ```

#### To Get The Last Boot Time For A Remote Computer AND Change ColumnName __SERVER To ComputerName AND Export To A CSV:

   ```powershell
   Get-Wmiobject -Class Win32_Operatingsystem -Namespace Rootcimv2 -Computer (Computername) | Select @{Label='ComputerName' ;E={$_.__Server}},@{Label='Lastbootuptime' ;Expression={$_.Converttodatetime($_.Lastbootuptime)} } | Export-Csv Lastboottime.Csv
   ```

### File System:

#### To Rename Files In Bulk:

   ```powershell
   Get-Childitem "C:\_Gwill\Scripts" | Rename-Item -Newname { $_.Name -Replace ".Txt",".Ps1″ }
   ```

#### To Change The File Extension Of All .Jpeg Files To .Jpg

   ```powershell
   Get-Childitem *.Jpeg | Rename-Item -Newname { $_.Name -Replace ".Jpeg",".Jpg" }
   ```

#### To Append A File Extension:

   ```powershell
   Dir | Rename-Item -Newname { $_.Name +".Jpg" }
   ```

#### To Rename Files With Customizable Increasing Number:

   ```powershell
   Dir *.Jpg | Foreach-Object -Begin { $Count=1 } -Process { Rename-Item $_ -Newname "Image$Count.Jpg"; $Count++ }
   ```

#### To Get The Parent Path Of A Directory:

   ```powershell
   $a = "c:\users\test"
   $b = $a.Split("\")[-1]
   $c = $a.TrimEnd($b)
   ```

#### To Set Filters For Queries:

   ```powershell
   Filter FileSizeBelow($size)
   {
   If ($_.length -le $size)
   {
   $_
   }
   }

   # Create 10 MB File:
   $path = "c:\_gwill\test.txt"
   $file = [io.file]::Create($path)
   $file.SetLength(10mb)
   $file.Close()

   # Create 10 KB File:
   $path = "c:\_gwill\test2.txt"
   $file = [io.file]::Create($path)
   $file.SetLength(10kb)
   $file.Close()

   # Should see test.txt but not test2.txt:
   Get-Childitem c:\_gwill | FileSizeBelow 200kb

   # See all files less than 100 MB:
   Get-Childitem -Recurse C:\_gwill | Where-Object { !$_.PSIsContainer } | FileSizeBelow 100mb
   ```

#### To Clear Log File If Larger Than 10 MB:

   ```powershell
   $Dir = "C:\Scripts\script.log"
   $SizeMax = 10
   $Size = (Get-ChildItem $Dir | Measure-Object -Property Length -Sum)
   $SizeMb=$size.sum / 1MB
   if ($sizeMb -ge $sizeMax)
   {
   Get-ChildItem $Dir | Clear-Content
   }
   ```

#### To Compare Files

   ```powershell
   Compare-Object -ReferenceObject ( Get-Content "c:\_gwill\prod.txt" ) -DifferenceObject ( Get-Content "c:\_gwill\prod2.txt" ) | 
   Where-Object -Property SideIndicator -eq '=>'

   Compare-Object -ReferenceObject ( Get-Content "c:\_gwill\prod.txt" ) -DifferenceObject ( Get-Content "c:\_gwill\prod2.txt" ) | 
   Where-Object -Property SideIndicator -eq '<='
   ```

#### To Set Everyone Full Permissions For A File

   ```powershell
   Function Set-Permissions($File)
   {
   $Acl = Get-Acl $File
   $Accessrule= New-Object System.Security.Accesscontrol.Filesystemaccessrule("Everyone", "Fullcontrol", "Allow")
   $Acl.Setaccessrule($Accessrule)
   $Acl | Set-Acl $File
   }
   ```

#### To See Logfile (Place At End Of Script):

   ```powershell
   $Input = Read-Host "Would You Like To See The Script's Log? (Y)Yes Or (N)No"
   If($Input -Eq 'Y')
   {
   Invoke-Item $Logfile
   }
   Else
   {
   Exit
   }
   ```

#### To Clean Strings (In This Case { And } Are Removed):

   ```powershell
   "{636d9115-E54e-4673-B992-B51a8f8ddc8b}".Replace('{',").Replace('}',")
   ```

#### To Take Ownership Files:

   ```powershell
   Function Set-Ownership($File)
   {
   # The Takeown.Exe File Should Already Exist In Win7 – Win10
   Try
   {
   & Takeown /f $File
   }
   Catch
   {
   Write-Output "Failed To Take Ownership Of $File"
   }
   }
   ```

#### To Get All Files Where $User Is Owner:

   ```powershell
   Get-Childitem -Recurse C:\ | Get-Acl | Where {$_.Owner -Match "Gerry.Williams" }
   ```

#### To Take Ownership Of Registry Keys:

   ```powershell
   Function Takeown-Registry($Key)
   {
   # Todo Does Not Work For All Root Keys Yet
   Switch ($Key.Split('\')[0])
   {
   "Hkey_Classes_Root"
   {
   $Reg = [Microsoft.Win32.Registry]::Classesroot
   $Key = $Key.Substring(18)
   }
   "Hkey_Current_User"
   {
   $Reg = [Microsoft.Win32.Registry]::Currentuser
   $Key = $Key.Substring(18)
   }
   "Hkey_Local_Machine"
   {
   $Reg = [Microsoft.Win32.Registry]::Localmachine
   $Key = $Key.Substring(19)
   }
   }
   # Get Administrator Group
   $Admins = New-Object System.Security.Principal.Securityidentifier("S-1-5-32-544")
   $Admins = $Admins.Translate([System.Security.Principal.Ntaccount])

   # Set Owner
   $Key = $Reg.Opensubkey($Key, "Readwritesubtree", "Takeownership")
   $Acl = $Key.Getaccesscontrol()
   $Acl.Setowner($Admins)
   $Key.Setaccesscontrol($Acl)

   # Set Fullcontrol
   $Acl = $Key.Getaccesscontrol()
   $Rule = New-Object System.Security.Accesscontrol.Registryaccessrule($Admins, "Fullcontrol", "Allow")
   $Acl.Setaccessrule($Rule)
   $Key.Setaccesscontrol($Acl)
   }
   ```

#### To Give Admins Full Control Of A Folder:

   ```powershell
   Function Takeown-File($Path)
   {
   Takeown.Exe /A /F $Path
   $Acl = Get-Acl $Path

   # Get Administraor Group
   $Admins = New-Object System.Security.Principal.Securityidentifier("S-1-5-32-544")
   $Admins = $Admins.Translate([System.Security.Principal.Ntaccount])

   # Add Nt Authority\System
   $Rule = New-Object System.Security.Accesscontrol.Filesystemaccessrule($Admins, "Fullcontrol", "None", "None", "Allow")
   $Acl.Addaccessrule($Rule)

   Set-Acl -Path $Path -Aclobject $Acl
   }
   ```

#### To Take Control Of A Folder (Requires Takeown-File):

   ```powershell
   Function Takeown-Folder($Path)
   {
   Takeown-File $Path
   Foreach ($Item In Get-Childitem $Path)
   {
   If (Test-Path $Item -Pathtype Container)
   {
   Takeown-Folder $Item.Fullname
   }
   Else
   {
   Takeown-File $Item.Fullname
   }
   }
   }
   ```

#### To Elevate A Process:

   ```powershell
   Function Elevate-Privileges
   {
   Param($Privilege)
   $Definition = @"
   Using System;
   Using System.Runtime.Interopservices;

   Public Class Adjpriv {
   [Dllimport("Advapi32.Dll", Exactspelling = True, Setlasterror = True)]
   Internal Static Extern Bool Adjusttokenprivileges(Intptr Htok, Bool Disall, Ref Tokpriv1luid Newst, Int Len, Intptr Prev, Intptr Rele);

   [Dllimport("Advapi32.Dll", Exactspelling = True, Setlasterror = True)]
   Internal Static Extern Bool Openprocesstoken(Intptr H, Int Acc, Ref Intptr Phtok);

   [Dllimport("Advapi32.Dll", Setlasterror = True)]
   Internal Static Extern Bool Lookupprivilegevalue(String Host, String Name, Ref Long Pluid);

   [Structlayout(Layoutkind.Sequential, Pack = 1)]
   Internal Struct Tokpriv1luid {
   Public Int Count;
   Public Long Luid;
   Public Int Attr;
   }

   Internal Const Int Se_Privilege_Enabled = 0x00000002;
   Internal Const Int Token_Query = 0x00000008;
   Internal Const Int Token_Adjust_Privileges = 0x00000020;

   Public Static Bool Enableprivilege(Long Processhandle, String Privilege) {
   Bool Retval;
   #### Tokpriv1luid Tp;
   Intptr Hproc = New Intptr(Processhandle);
   Intptr Htok = Intptr.Zero;
   Retval = Openprocesstoken(Hproc, Token_Adjust_Privileges | Token_Query, Ref Htok);
   Tp.Count = 1;
   Tp.Luid = 0;
   Tp.Attr = Se_Privilege_Enabled;
   Retval = Lookupprivilegevalue(Null, Privilege, Ref Tp.Luid);
   Retval = Adjusttokenprivileges(Htok, False, Ref Tp, 0, Intptr.Zero, Intptr.Zero);
   Return Retval;
   }
   }
   "@
   $Processhandle = (Get-Process -Id $Pid).Handle
   $Type = Add-Type $Definition -Passthru
   $Type[0]::Enableprivilege($Processhandle, $Privilege)
   }
   ```

#### To Force Create A Directory:

   ```powershell
   Function Force-Mkdir($Path)
   {
   If (!(Test-Path $Path))
   {
   New-Item -Itemtype Directory -Force -Path $Path
   }
   }
   ```

#### To Send Clipboard Contents To Desktop:

   ```powershell
   Function Send-ClipToDesktop
   {

   Function Get-Clipboard
   {
   [CmdletBinding(ConfirmImpact = 'None', SupportsShouldProcess = $false)] # to support -OutVariable and -Verbose
   param ()

   Add-Type -AssemblyName System.Windows.Forms
   if ([threading.thread]::CurrentThread.ApartmentState.ToString() -eq 'STA')
   {
   Write-Verbose 'STA mode: Using [Windows.Forms.Clipboard] directly.'
   # To be safe, we explicitly specify that Unicode (UTF-16) be used – older platforms may default to ANSI.
   [System.Windows.Forms.Clipboard]::GetText([System.Windows.Forms.TextDataFormat]::UnicodeText)
   }
   else
   {
   Write-Verbose 'MTA mode: Using a [System.Windows.Forms.TextBox] instance for clipboard access.'
   $tb = New-Object System.Windows.Forms.TextBox
   $tb.Multiline = $true
   $tb.Paste()
   $tb.Text
   }
   }

   Get-Clipboard | Out-File Passwords.txt
   Copy-Item Passwords.txt -Destination $env:userprofile\Desktop\Passwords.txt
   }
   ```

#### To Place Input To Keyboard (Essentially clip.exe in a nutshell):

   ```powershell
   Function Set-Clipboard
   {
   Add-Type -AssemblyName System.Windows.Forms
   $In = @($Input)

   $Out = If ($In.Length -Eq 1 -And $In[0] -Is [String])
   {
   $In[0]
   }
   Else
   {
   $In | Out-String
   }

   If ($Out)
   {
   [Windows.Forms.Clipboard]::Settext($Out);
   }
   Else
   {
   # Input Is Nothing, Therefore Clear The Clipboard
   [Windows.Forms.Clipboard]::Clear();
   }
   }

   # "Blah" | Set-Clipboard
   ```

#### To Convert CSV To JSON:

   ```powershell
   # This assumes that your CSV file has three columns, one for Name, one for SessionValues, and one for UserAgent
   $Query = @{}
   Import-Csv -Path $Path | ForEach-Object {
      $Properties = @{}
      $Properties['Client_Session'] = @($_.SessionValues)
      $Properties['ebanner_HTTP'] = @($_.UserAgent)

      $Query[$_.Name] = @{
         Properties = $Properties
      }
   }

   <#
   example output:
      {
      "10.0.12.77":  {
                        "properties":  {
                                             "client_session":  [
                                                                  "10.0.12.77 10.0.31.214 23/TCP",
                                                                  "10.0.31.214 10.0.12.77 23/TCP"
                                                               ],
                                             "ebanner_http":  [
                                                                  "Super Secret HTTP Agent 1.0"
                                                            ]
                                       }
                     }
   }
   #>
   ```

#### To Disable/Enable Touchscreen:

   ```powershell
   Get-PnpDevice | Where-Object {$_.FriendlyName -like '*touch screen*'} | Disable-PnpDevice -Confirm:$false
   Start-Sleep -Seconds 3
   Get-PnpDevice | Where-Object {$_.FriendlyName -like '*touch screen*'} | Enable-PnpDevice -Confirm:$false
   ```

#### To Create/Send Shortcuts To The Desktop:

   ```powershell
   Write-Output "Setting IE 64bit"
   $Targetfile = "C:\Program Files\Internet Explorer\Iexplore.Exe"
   $Shortcutfile = "$Env:Userprofile\Desktop\Internet Explorer.lnk"
   $Wscriptshell = New-Object -Comobject Wscript.Shell
   $Shortcut = $Wscriptshell.Createshortcut($Shortcutfile)
   $Shortcut.Targetpath = $Targetfile
   $Shortcut.Save()

   Write-Output "Setting Google Shortcut"
   $Targetfile = "https://google.com"
   $Shortcutfile = "$Env:Userprofile\Desktop\Google.url"
   $Wscriptshell = New-Object -Comobject Wscript.Shell
   $Shortcut = $Wscriptshell.Createshortcut($Shortcutfile)
   $Shortcut.Targetpath = $Targetfile
   $Shortcut.Save()

   Write-Output "Setting MS Excel Link"
   $Targetfile = "C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
   $Shortcutfile = "$Env:Userprofile\Desktop\Excel 2016.lnk"
   $Wscriptshell = New-Object -Comobject Wscript.Shell
   $Shortcut = $Wscriptshell.Createshortcut($Shortcutfile)
   $Shortcut.Targetpath = $Targetfile
   $Shortcut.Save()

   Write-Output "Setting MS Outlook Link"
   $Targetfile = "C:\Program Files (x86)\Microsoft Office\root\Office16\OUTLOOK.EXE"
   $Shortcutfile = "$Env:Userprofile\Desktop\Outlook 2016.lnk"
   $Wscriptshell = New-Object -Comobject Wscript.Shell
   $Shortcut = $Wscriptshell.Createshortcut($Shortcutfile)
   $Shortcut.Targetpath = $Targetfile
   $Shortcut.Save()

   Write-Output "Setting MS Word Link"
   $Targetfile = "C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
   $Shortcutfile = "$Env:Userprofile\Desktop\Word 2016.lnk"
   $Wscriptshell = New-Object -Comobject Wscript.Shell
   $Shortcut = $Wscriptshell.Createshortcut($Shortcutfile)
   $Shortcut.Targetpath = $Targetfile
   $Shortcut.Save()        

   Write-Output "Setting OneNote Link"
   $Targetfile = "C:\Program Files (x86)\Microsoft Office\root\Office16\ONENOTE.EXE"
   $Shortcutfile = "$Env:Userprofile\Desktop\OneNote 2016.lnk"
   $Wscriptshell = New-Object -Comobject Wscript.Shell
   $Shortcut = $Wscriptshell.Createshortcut($Shortcutfile)
   $Shortcut.Targetpath = $Targetfile
   $Shortcut.Save() 


   # Setting shortcut as admin (haven't tested yet)
   Copy-Item $Toolscript 'G:\FileLocation\IT\Tools'
   $ToolShortcut = New-Object -ComObject WScript.Shell
   $Shortcut = $ToolShortcut.CreateShortcut("C:\users\public\Desktop\$Toolscript.lnk")
   $Shortcut.TargetPath = 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
   $Shortcut.Arguments = '-NoProfile -File "G:\FileLocation\IT\Tools\$ToolScript" -Interactive'
   $Shortcut.Save()
   #Manipulation to make it run as admin:
   $bytes = [System.IO.File]::ReadAllBytes("C:\Users\Public\Desktop\Toolbox.lnk")
   $bytes[0x15] = $bytes[0x15] -bor 0x20 # Sets byte 21 (0x15) bit 6 (0x20) to ON
   [System.IO.File]::WriteAllBytes("C:\Users\Public\Desktop\Toolbox.lnk", $bytes)
   ```

