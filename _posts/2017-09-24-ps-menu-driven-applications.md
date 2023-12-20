---
title: 'PS: Menu Driven Applications'
date: 2017-09-24T07:10:47+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/09/ps-menu-driven-applications/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

So at some point or another you will be tasked to come up with a menu application either for yourself to launch your custom scripts or for helpdesk staff. Personally, this is one of my favorite things about my job is diving into Powershell and finding ways to implement it. That being said, this post will be script heavy, so I will place them in the bottom and talk about them towards the top.

Essentially, the three types of applications I have made with Powershell are either text driven menus, application menus, or just simple forms. I will go over each 3 here. Keep in mind you can go all out like [this guy](https://gallery.technet.microsoft.com/LazyWinAdmin-04-9da94d7f) and really dig in!

### To Resolve:

1. The main thing you want to do is get a template like mine below and then add functions that will be called when the user makes a selection.

2. For example, to add an action to the GUI application you would write a function like I did on lines 47-50. Then just call the function with the click event on line 297.

3. For menu application I did the same thing on lines 605-608 and then called on line 628. I like this script a little more because it auto expands and has sub menu's. Invoke-GWCustomMenuGUI:

   ```powershell
   Add-Type -AssemblyName System.Windows.Forms
   $Form = New-Object system.Windows.Forms.Form 
   $Form.Text = "GerrysScripts"
   $Form.TopMost = $true
   $Form.BackColor = "#0b0b0b"
   $Form.Width = 256
   $Form.Height = 410

   $label = New-Object system.windows.Forms.Label 
   $label.Text = "Select A Task `r`nTo Run:"
   $label.AutoSize = $true
   $label.ForeColor = "#0CF110"
   $label.Width = 217
   $label.Height = 10
   $label.location = new-object system.drawing.point(5, 19)
   $label.Font = "Verdana,12"
   $Form.controls.Add($label) 

   $button = New-Object system.windows.Forms.Button 
   $button.Text = "StartPS"
   $button.ForeColor = "#0CF110"
   $button.Width = 159
   $button.Height = 23
   $button.location = new-object system.drawing.point(4, 70)
   $button.Font = "Verdana,10"
   $button.Add_Click($StartPowershell)
   $Form.controls.Add($button)

   $button2 = New-Object system.windows.Forms.Button 
   $button2.Text = "StartISE"
   $button2.ForeColor = "#0CF110"
   $button2.Width = 159
   $button2.Height = 23
   $button2.location = new-object system.drawing.point(4, 100)
   $button2.Font = "Verdana,10"
   $button2.Add_Click($StartPowershellISE)
   $Form.controls.Add($button2)

   $button3 = New-Object system.windows.Forms.Button 
   $button3.Text = "button"
   $button3.ForeColor = "#0CF110"
   $button3.Width = 159
   $button3.Height = 23
   $button3.location = new-object system.drawing.point(4, 130)
   $button3.Font = "Verdana,10"
   $button3.Add_Click($RunMyScript)
   $Form.controls.Add($button3) 

   $button4 = New-Object system.windows.Forms.Button 
   $button4.Text = "button"
   $button4.ForeColor = "#0CF110"
   $button4.Width = 159
   $button4.Height = 23
   $button4.location = new-object system.drawing.point(4, 160)
   $button4.Font = "Verdana,10"
   $button4.Add_Click($StartPowershellISE)
   $Form.controls.Add($button4)

   $button5 = New-Object system.windows.Forms.Button 
   $button5.Text = "button"
   $button5.ForeColor = "#0CF110"
   $button5.Width = 159
   $button5.Height = 23
   $button5.location = new-object system.drawing.point(4, 190)
   $button5.Font = "Verdana,10"
   $button5.Add_Click($StartPowershellISE)
   $Form.controls.Add($button5) 

   $button6 = New-Object system.windows.Forms.Button 
   $button6.Text = "button"
   $button6.ForeColor = "#0CF110"
   $button6.Width = 159
   $button6.Height = 23
   $button6.location = new-object system.drawing.point(4, 220)
   $button6.Font = "Verdana,10"
   $button6.Add_Click($StartPowershellISE)
   $Form.controls.Add($button6) 

   $button7 = New-Object system.windows.Forms.Button 
   $button7.Text = "button"
   $button7.ForeColor = "#0CF110"
   $button7.Width = 159
   $button7.Height = 23
   $button7.location = new-object system.drawing.point(4, 250)
   $button7.Font = "Verdana,10"
   $button7.Add_Click($StartPowershellISE)
   $Form.controls.Add($button7) 

   $button8 = New-Object system.windows.Forms.Button 
   $button8.Text = "button"
   $button8.ForeColor = "#0CF110"
   $button8.Width = 159
   $button8.Height = 23
   $button8.location = new-object system.drawing.point(4, 280)
   $button8.Font = "Verdana,10"
   $button8.Add_Click($StartPowershellISE)
   $Form.controls.Add($button8)

   $button9 = New-Object system.windows.Forms.Button 
   $button9.Text = "button"
   $button9.ForeColor = "#0CF110"
   $button9.Width = 159
   $button9.Height = 23
   $button9.location = new-object system.drawing.point(4, 310)
   $button9.Font = "Verdana,10"
   $button9.Add_Click($StartPowershellISE)
   $Form.controls.Add($button9)

   $button10 = New-Object system.windows.Forms.Button 
   $button10.Text = "Close Form"
   $button10.ForeColor = "#0CF110"
   $button10.Width = 159
   $button10.Height = 23
   $button10.location = new-object system.drawing.point(4, 340)
   $button10.Font = "Verdana,10"
   $button10.Add_Click($EndForm)
   $Form.controls.Add($button10)     

   $Form.ShowDialog() | out-null
   ```

4. If you prefer a menu driven application, try the following:

   ```powershell
   Begin
   {
   Function Write-Color
   {
   <#
   .SYNOPSIS
      Enables support to write multiple color text on a single line
   .DESCRIPTION
      Users color codes to enable support to write multiple color text on a single line
      ################################################
      # Write-Color Color Codes
      ################################################
      # ^cn = Normal Output Color
      # ^ck = Black
      # ^cb = Blue
      # ^cc = Cyan
      # ^ce = Gray
      # ^cg = Green
      # ^cm = Magenta
      # ^cr = Red
      # ^cw = White
      # ^cy = Yellow
      # ^cB = DarkBlue
      # ^cC = DarkCyan
      # ^cE = DarkGray
      # ^cG = DarkGreen
      # ^cM = DarkMagenta
      # ^cR = DarkRed
      # ^cY = DarkYellow
      ################################################
   .PARAMETER text
      Mandatory. Line of text to write
   .INPUTS
      [string]$text
   .OUTPUTS
      None
   .NOTES
      Version:        1.0
      Author:         Brian Clark
      Creation Date:  01/21/2017
      Purpose/Change: Initial function development
      Version:        1.1
      Author:         Brian Clark
      Creation Date:  01/23/2017
      Purpose/Change: Fix Gray / Code Format Fixes
   .EXAMPLE
      Write-Color "Hey look ^crThis is red ^cgAnd this is green!"
   #>

   [CmdletBinding()]
   Param (
   [Parameter(Mandatory = $true)][string]$text
   )

   ### If $text contains no color codes just write-host as normal
   if (-not $text.Contains("^c"))
   {
   Write-Host "$($text)"
   return
   }


   ### Set to true if the beginning of $text is a color code. The reason for this is that
   ### the generated array will have an empty/null value for the first element in the array
   ### if this is the case.
   ### Since we also assume that the first character of a split string is a color code we
   ### also need to know if it is, in fact, a color code or if it is a legitimate character.
   $blnStartsWithColor = $false
   if ($text.StartsWith("^c"))
   {
   $blnStartsWithColor = $true
   }

   ### Split the array based on our color code delimeter
   $strArray = $text -split "\^c"
   ### Loop Counter so we can generate a new empty line on the last element of the loop
   $count = 1

   ### Loop through the array
   $strArray | % {
   if ($count -eq 1 -and $blnStartsWithColor -eq $false)
   {
      Write-Host $_ -NoNewline
      $count++
   }
   elseif ($_.Length -eq 0)
   {
      $count++
   }
   else
   {

      $char = $_.Substring(0, 1)
      $color = ""
      switch -CaseSensitive ($char)
      {
         "b"
         {
            $color = "Blue" 
         }
         "B"
         {
            $color = "DarkBlue" 
         }
         "c"
         {
            $color = "Cyan" 
         }
         "C"
         {
            $color = "DarkCyan" 
         }
         "e"
         {
            $color = "Gray" 
         }
         "E"
         {
            $color = "DarkGray" 
         }
         "g"
         {
            $color = "Green" 
         }
         "G"
         {
            $color = "DarkGreen" 
         }
         "k"
         {
            $color = "Black" 
         }
         "m"
         {
            $color = "Magenta" 
         }
         "M"
         {
            $color = "DarkMagenta" 
         }
         "r"
         {
            $color = "Red" 
         }
         "R"
         {
            $color = "DarkRed" 
         }
         "w"
         {
            $color = "White" 
         }
         "y"
         {
            $color = "Yellow" 
         }
         "Y"
         {
            $color = "DarkYellow" 
         }
      }

      ### If $color is empty write a Normal line without ForgroundColor Option
      ### else write our colored line without a new line.
      if ($color -eq "")
      {
         Write-Host $_.Substring(1) -NoNewline
      }
      else
      {
         Write-Host $_.Substring(1) -NoNewline -ForegroundColor $color
      }
      ### Last element in the array writes a blank line.
      if ($count -eq $strArray.Count)
      {
         Write-Host ""
      }
      $count++
   }
   }
   }

   Function New-MenuItem
   {
   <#
   .SYNOPSIS
      Creates a Menu Item used with New-Menu
   .DESCRIPTION
      Use this in conjunction with New-Menu and Show-Menu
      to generate a menu system for your scripts
   .PARAMETER Name
      Mandatory. Text that shows up in the menu for this menu item.
   .PARAMETER Command
      Mandatory. Command the menu item executes when selected
      Important Note: Define your command in single quotes '' and not double quotes ""
   .INPUTS
      [string]$Name
      [string]$Command
   .OUTPUTS
      [PSObject] Name, Command
   .NOTES
      Version:        1.0
      Author:         Brian Clark
      Creation Date:  03/23/2017
      Purpose/Change: Initial function development
   .EXAMPLE
      $item = New-MenuItem -Name "List All Services" -Command 'Get-Service'
      $item_end = New-MenuItem -Name "Exit Menu" -Command 'End-Menu'
      $item_switch_menu = New-MenuItem -Name "View Menu 2" -Command 'Show-Menu $menu2'
   #>
   [CmdletBinding()]
   Param ([Parameter(Mandatory = $true)][string]$Name,
   [Parameter(Mandatory = $true)]$Command)

   ### The first whole word should be the cmdlet.
   $cmd_array = $Command.Split(" ")
   $cmd = $cmd_array[0]

   ### Ensure cmdlet/function is defined if so create and return the menu item
   if ($cmd -eq "End-Menu" -or (Get-Command $cmd -ErrorAction SilentlyContinue))
   {
   $menu_item = New-Object -TypeName PSObject | Select Name, Command
   $menu_item.Name = $Name
   $menu_item.Command = $Command
   return $menu_item
   }
   else
   {
   Write-Error -Message "The command $($Command) does not exist!" -Category ObjectNotFound
   return $null
   }
   }

   Function New-Menu
   {
   <#
   .SYNOPSIS
      Creates a looping menu system
   .DESCRIPTION
      Use this in conjunction with New-MenuItem and Show-Menu
      to generate a menu system for your scripts
   .PARAMETER Name
      Mandatory. Text that shows up as the menu title in the menu screen
   .PARAMETER MenuItems[]
      Mandatory. Array of Menu Items created via the New-MenuItem cmdlet
   .INPUTS
      [string]$Name
      [PSObject]$MenuItems[]
   .OUTPUTS
      [PSObject] Name, MenuItems[]
   .NOTES
      Version:        1.0
      Author:         Brian Clark
      Creation Date:  03/23/2017
      Purpose/Change: Initial function development
   .EXAMPLE
      $main_menu = New-Menu -Name 'Main Menu' -MenuItems @(
         (New-MenuItem -Name 'Get Services' -Command 'Get-Service'),
         (New-MenuItem -Name 'Get ChildItems' -Command 'Get-ChildItem'),
         (New-MenuItem -Name 'GoTo Sub Menu' -Command 'Show-Menu -Menu $sub_menu'),
         (New-MenuItem -Name 'Exit' -Command "End-Menu")
      )
   #>
   [CmdletBinding()]
   Param ([Parameter(Mandatory = $true)][string]$Name,
   [Parameter(Mandatory = $true)][PSObject[]]$MenuItems)

   ### Create Menu PSObject
   $menu = New-Object -TypeName PSObject | Select Name, MenuItems
   $menu.Name = $Name
   $menu.MenuItems = @()

   ### Loop through each MenuItem and verify they have the correct Properties
   ### and verify that there is a way to exit the menu or open a different menu
   $blnFoundMenuExit = $false
   $blnMenuExitsToMenu = $false
   for ($i = 0; $i -lt $MenuItems.Length; $i++)
   {
   if ((-not $MenuItems[$i].PSObject.Properties['Name']) -or 
      (-not $MenuItems[$i].PSObject.Properties['Command']))
   {
      Write-Error "One or more passed Menu Items were not created with New-MenuItem!" -Category InvalidType
      return
   }
   if ($MenuItems[$i].Command -eq "End-Menu")
   {
      $blnFoundMenuExit = $true 
   }
   if ($MenuItems[$i].Command.Contains("Show-Menu"))
   {
      $blnMenuExitsToMenu = $true 
   }
   $menu_item = New-Object -TypeName PSObject | Select Number, Name, Command
   $menu_item.Number = $i
   $menu_item.Name = $MenuItems[$i].Name
   $menu_item.Command = $MenuItems[$i].Command
   $menu.MenuItems += @($menu_item)
   }
   if ($blnFoundMenuExit -eq $false -and $blnMenuExitsToMenu -eq $false)
   {
   Write-Error "This menu does not contain an End-Menu or Show-Menu MenuItem and would loop forever!" -Category SyntaxError
   return
   }
   return $menu

   }

   Function Show-Menu
   {
   <#
   .SYNOPSIS
      Starts the menu display/selection loop for a menu created with New-Menu
   .DESCRIPTION
      Use this in conjunction with New-Menu and New-MenuItem
      to generate a menu system for your scripts
   .PARAMETER Menu
      Mandatory. A menu created with the New-Menu cmdlet
   .INPUTS
      [PSObject]$Menu
   .OUTPUTS
      Starts the Menu Display Loop
      This function returns nothing
   .NOTES
      Version:        1.0
      Author:         Brian Clark
      Creation Date:  03/23/2017
      Purpose/Change: Initial function development
   .EXAMPLE
      Show-Menu $MyMenu
   #>
   [CmdletBinding()]
   Param ([Parameter(Mandatory = $true)][PSObject]$Menu)

   ### Verify $Menu has the right properties
   if ((-not $Menu.PSObject.Properties['Name']) -or 
   (-not $Menu.PSObject.Properties['MenuItems']))
   {
   Write-Error -Message "The passed object is not a Menu created with New-Menu!" -Category InvalidType
   return
   }

   ### Display the Menu via a Do Loop
   $blnMenuExit = $false
   $choice = -1
   Do
   {
   Write-Host "`r`n===================================================================================================="
   Write-Host "$($Menu.Name)" -ForegroundColor DarkYellow
   Write-Host "----------------------------------------------------------------------------------------------------"
   for ($i = 0; $i -lt $Menu.MenuItems.Length; $i++)
   {
      Write-Color " ^cg$($i)^cn) ^cy$($Menu.MenuItems[$i].Name)^cn"
   }
   Write-Host "`r`n====================================================================================================`r`n"
   Write-Host "Please select an item (0-$($Menu.MenuItems.Length-1)) : " -ForegroundColor DarkYellow -NoNewline
   $choice = Read-Host
   $choice = ($choice -as [int])
   if ($choice.GetType() -ne [int])
   {
      Write-Host "`r`nError - Invalid choice!`r`n" -ForegroundColor Red
   }
   elseif ($choice -lt 0 -or $choice -ge $Menu.MenuItems.Length)
   {
      Write-Host "`r`nError - choice must be between 0 and $($Menu.MenuItems.Length-1)!`r`n" -ForegroundColor Red
   }
   else
   {
      if ($Menu.MenuItems[$choice].Command -eq "End-Menu" -or 
         $Menu.MenuItems[$choice].Command.Contains("Show-Menu"))
      {
         $blnMenuExit = $true
      }
      else
      {
         Invoke-Expression -Command $Menu.MenuItems[$choice].Command
      }
   }
   } Until ($blnMenuExit -eq $true)

   if ($Menu.MenuItems[$choice].Command.Contains("Show-Menu"))
   {
   Invoke-Expression -Command $Menu.MenuItems[$choice].Command
   }
   }
   }
   Process
   {   


   # MENU SAMPLE

   Function Start-PowershellISE 
   { 
   Powershell.exe Start-Process "Powershell_ise" -Verb runas 
   }

   ### Setup Window for best fit of menu
   $Host.UI.RawUI.BackgroundColor = "Black"
   $HOST.UI.RawUI.ForegroundColor = "White"
   $Host.UI.RawUI.WindowTitle = "Scripts"
   $pshost = Get-Host
   $pswindow = $pshost.ui.rawui
   $newsize = $pswindow.buffersize
   $newsize.height = 3000
   $newsize.width = 100
   $pswindow.buffersize = $newsize
   $newsize = $pswindow.windowsize
   $newsize.height = 50
   $newsize.width = 100
   $pswindow.windowsize = $newsize
   [System.Console]::Clear();

   $main_menu = New-Menu -Name 'Main Menu' -MenuItems @(
   (New-MenuItem -Name 'LaunchPS' -Command 'Invoke-Item "c:\scripts\ps.bat"'),
   (New-MenuItem -Name 'LaunchPSISE' -Command 'Start-PowershellISE'),
   (New-MenuItem -Name 'GoTo Sub Menu' -Command 'Show-Menu -Menu $sub_menu'),
   (New-MenuItem -Name 'Exit' -Command "End-Menu")
   )
   $sub_menu = New-Menu -Name 'Sub Menu' -MenuItems @(
   (New-MenuItem -Name 'Directory' -Command 'Dir'),
   (New-MenuItem -Name 'Hostname' -Command 'Hostname'),
   (New-MenuItem -Name 'GoTo Main Menu' -Command 'Show-Menu -Menu $main_menu'),
   (New-MenuItem -Name 'Exit' -Command "End-Menu")
   )

   Show-Menu -Menu $main_menu	

   }
   ```

5. Source is maintained under [gwApplications](https://github.com/gerryw1389/powershell/blob/main/gwApplications/Public/Invoke-CustomMenu.ps1)