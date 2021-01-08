---
title: 'PS: GUI Commands'
date: 2016-12-03T02:25:40+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/ps-gui-commands/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

Here is a list of random commands I use in Powershell that will probably end up being moved around later.


### To Resolve:

#### To send key presses:

   ```powershell
   $wshell = new-object -com wscript.shell
   $wshell.SendKeys("{CAPSLOCK}")
   ```

#### To create an input box:

   ```powershell
   [void] [System.Reflection.Assembly]::LoadWithPartialName("'Microsoft.VisualBasic")
   $data = [Microsoft.VisualBasic.Interaction]::InputBox('hi user give me your data', 'inputboxtitle')
   ```

#### To create a pop up box:

   ```powershell
   [void] [System.Reflection.Assembly]::LoadWithPartialName("'Microsoft.VisualBasic")
   [Microsoft.VisualBasic.Interaction]::MsgBox("tada","OKOnly,SystemModal,Information","msgboxtitle")
   ```

#### To create a GUI for Powershell scripts:

   - Use [PoshGUI](https://poshgui.com/)

   - Use [XAML](https://blogs.technet.microsoft.com/platformspfe/2014/01/20/integrating-xaml-into-powershell/)

   - Example:

   ```powershell
   [void][System.Reflection.Assembly]::LoadWithPartialName('presentationframework')
   [xml]$XAML = @'
   <Window xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
         xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
         Title="MainWindow" Height="350" Width="300" MinHeight="350" MinWidth="300" ResizeMode="CanResizeWithGrip">
      <Grid>
         <TextBox Name="textBox" Height="25" Margin="10,10,125,0" TextWrapping="Wrap" Text="TextBox" VerticalAlignment="Top"/>
         <Button Name="button" Content="Button" Height="25" Margin="0,10,10,0" VerticalAlignment="Top" HorizontalAlignment="Right" Width="110"/>
         <DataGrid Name="dataGrid" Margin="10,40,10,10"/>
      </Grid>
   </Window>
   '@

   $reader=(New-Object System.Xml.XmlNodeReader $xaml) 
   try{$Form=[Windows.Markup.XamlReader]::Load( $reader )}
   catch{Write-Host "Unable to load Windows.Markup.XamlReader."; break}
   $xaml.SelectNodes("//*[@Name]") | %{Set-Variable -Name ($_.Name) -Value $Form.FindName($_.Name)}

   $button.Add_Click({
      $textBox.Text = "OK!"
   })

   $Form.ShowDialog() | Out-Null
   ```

#### To Pause A Script:

   ```powershell
   Function Pause-Script
   {
   Write-Output -InputObject "Press any key to continue…"
   [void]$host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
   }
   ```

#### To Prompt For A Choice:

   ```powershell
   $Title = "Continue"
   $Info = "Would you like to continue?"
   $Options = [System.Management.Automation.Host.ChoiceDescription[]] @("&Yes", "&No")
   [int]$DefaultChoice = 0
   $Opt = $host.UI.PromptForChoice($Title , $Info, $Options, $DefaultChoice)
   switch ($Opt)
   {
   0
   {
   Write-Verbose -Message "Yes"
   }
   1
   {
   Write-Verbose -Message "No"
   }
   }
   ```

#### To Hide A Window (For Form Launching Scripts):

   ```powershell
   Function Initialize-Window
   {
   $t = '[DllImport("user32.dll")] public static extern bool ShowWindow(int handle, int state);'
   Add-Type -Name Win -Member $t -Namespace native
   [native.win]::ShowWindow(([System.Diagnostics.Process]::GetCurrentProcess() | Get-Process).MainWindowHandle, 0)
   }
   Initialize-Window
   ```

#### To Lock The Computer Screen:

   ```powershell
   cmd /c "%windir%\system32\rundll32.exe user32.dll,LockWorkStation"
   ```

#### To Turn Off Monitors:

   ```powershell
   powershell (Add-Type '[DllImport(\"user32.dll\")]^public static extern int SendMessage(int hWnd, int hMsg, int wParam, int lParam);' -Name a -Pas)::SendMessage(-1,0×0112,0xF170,2)
   ```

#### To Create FullScreen PopUps Transparent and Not:

   ```powershell
   Function Show-MessageFullScreenTransparent ( $message )
   {
   Add-Type -AssemblyName System.Windows.Forms
   $Screens = [system.windows.forms.screen]::AllScreens
   $i = 0;
   foreach ($Screen in $Screens)
   {
   $i++;
   if ( $Screen.Primary )
   {
   $w = $Screen.Bounds.Width #$Screen.WorkingArea.Width
   $h = $Screen.Bounds.Height #$Screen.WorkingArea.Width
   }
   }
   $objForm = New-Object System.Windows.Forms.Form
   $objForm.StartPosition = "CenterScreen"
   $objForm.Size = New-Object System.Drawing.Size($w, $h)
   $font = New-Object System.Drawing.Font("arial", 22, [System.Drawing.Fontstyle]::Regular)
   $objForm.Font = $font
   $text = New-Object System.Windows.Forms.Label
   $text.Text = "$message"
   $text.Size = New-Object System.Drawing.Size($w, $h)
   $text.TextAlign = "MiddleCenter"
   $objForm.Controls.Add($text)
   $objForm.Autosize = $true
   $objForm.MinimizeBox = $false
   $objForm.MaximizeBox = $false
   $objForm.ShowIcon = $false
   $objForm.TransparencyKey = "#000000"
   $objForm.BackColor = "#000000"
   $objForm.ForeColor = "#00FF00"
   $objForm.SizeGripStyle = "Hide"
   $objForm.FormBorderStyle = "None"
   $objForm.Show()
   Start-Sleep -Seconds 1
   $text = New-Object System.Windows.Forms.Label
   $text.Text = "please"
   $text.Size = New-Object System.Drawing.Size($w, $h)
   $text.TextAlign = "MiddleCenter"
   $objForm.Controls.Add($text)
   $objForm.Close()
   }
   Function Show-MessageFullScreenWithBackground ( $message )
   {
   Add-Type -AssemblyName System.Windows.Forms
   $Screens = [system.windows.forms.screen]::AllScreens
   $i = 0;
   foreach ($Screen in $Screens)
   {
   $i++;
   if ( $Screen.Primary )
   {
   $w = $Screen.Bounds.Width #$Screen.WorkingArea.Width if you don't want to go full fullscreen
   $h = $Screen.Bounds.Height #$Screen.WorkingArea.Height if you don't want to go full fullscreen
   }
   }
   $objForm = New-Object System.Windows.Forms.Form
   $objForm.StartPosition = "CenterScreen"
   $objForm.Size = New-Object System.Drawing.Size($w, $h)
   $font = New-Object System.Drawing.Font("arial", 22, [System.Drawing.Fontstyle]::Regular)
   $objForm.Font = $font
   $text = New-Object System.Windows.Forms.Label
   $text.Text = "$message"
   $text.Size = New-Object System.Drawing.Size($w, $h)
   $text.TextAlign = "MiddleCenter"
   $objForm.Controls.Add($text)
   $objForm.Autosize = $true
   $objForm.MinimizeBox = $false
   $objForm.MaximizeBox = $false
   $objForm.ShowIcon = $false
   $objForm.BackColor = "#000000"
   $objForm.ForeColor = "#00FF00"
   $objForm.SizeGripStyle = "Hide"
   $objForm.FormBorderStyle = "None"
   $objForm.Show()
   Start-Sleep -Seconds 1
   $text = New-Object System.Windows.Forms.Label
   $text.Text = "please"
   $text.Size = New-Object System.Drawing.Size($w, $h)
   $text.TextAlign = "MiddleCenter"
   $objForm.Controls.Add($text)
   $objForm.Close()
   }
   Show-MessageFullScreenTransparent -Message "Stop"
   Show-MessageFullScreenWithBackground "No really, stop!!!!"
   Show-MessageFullScreenTransparent -Message "Let's Get Started"
   ```

#### To Display A Picture:

   ```powershell
   $Picture = 'C:\temp\pic.jpg'
   [void][reflection.assembly]::LoadWithPartialName("System.Windows.Forms")
   $file = (get-item $Picture)
   $img = [System.Drawing.Image]::Fromfile($file);
   [System.Windows.Forms.Application]::EnableVisualStyles();
   $form = new-object Windows.Forms.Form
   $form.Text = "Image Viewer"
   $form.Width = $img.Size.Width;
   $form.Height =  $img.Size.Height;
   $pictureBox = new-object Windows.Forms.PictureBox
   $pictureBox.Width =  $img.Size.Width;
   $pictureBox.Height =  $img.Size.Height;
   $pictureBox.Image = $img;
   $form.controls.add($pictureBox)
   $form.Add_Shown( { $form.Activate() } )
   $form.ShowDialog()
   ```

#### To Encode / Decode The Picture In a Script:

   ```powershell
   $Picture = 'C:\temp\pic.jpg'

   # Convert-FileToBase64
   $EncodedFile = [convert]::ToBase64String( (get-content -Path $Picture -Encoding Byte) )
   $EncodedFile = $EncodedFile -replace '.{64}', "$&`r`n"

   # Embed the script in the file
   $Base64 = @'
   Super long String from above....
   '@
   $Content = [System.Convert]::FromBase64String($Base64)
   Set-Content -Path $env:temp\file.jpg -Value $Content -Encoding Byte

   # Delete the temp file
   Remove-Item $env:temp\file.jpg
   ```

#### To Use Jobs To Show Progress Bars:

   ```powershell
   # Start with a collection of items to show progress on while we loop through
   $Nums = 1..10

   # Start a job that is NOT set to OK until someone clicks 'OK'
   $Null = Start-Job -Name 'Test' -Scriptblock {
      Add-Type -Assemblyname System.Windows.Forms
      [System.Windows.Forms.Messagebox]::Show('Cancel?', 'Write-Progress Test', 0)
   }

   # Initialize counter outside of the loop
   $Index = 0

   # Go Through Each Item in Items
   Foreach ($Num In $Nums)
   {
      # Increment counters until we run out of items
      $Index++
      # Just a display to show the progress
      Write-Progress -Activity 'Test' -Percentcomplete ($Index / $Nums.Count * 100)
      # Referencing the above job... Only if the user presses 'OK', break out of the script
      If ((Receive-Job -Name 'Test').Value -Eq 'Ok')
      {
         Break
      }
      # Otherwise, sleep for one second and go to the next item until all items are processed.
      Start-Sleep 1
   }
   # End the script since all the items were processed and the user never hit 'OK'
   Remove-Job -Name 'Test'
   # Optional - Show what number they stopped at if they hit it early on or just waited until the end. 
   Write-Output "You Stopped At $Num"
   ```

