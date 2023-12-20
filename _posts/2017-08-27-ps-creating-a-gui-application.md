---
title: 'PS: Creating A GUI Application'
date: 2017-08-27T07:38:59+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/ps-creating-a-gui-application/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

Scripting is something I find myself really enjoying here lately. With sites like poshgui.com it's common to want to create a custom form either for your use or to send to helpdesk users. Here is a post on a template you can use:

This will create a form like the screenshot below that will launch the form and keep it open after you make selections.

<img class="alignnone size-full wp-image-4643" src="https://automationadmin.com/assets/images/uploads/2017/08/gwform.jpg" alt="" width="251" height="407" srcset="https://automationadmin.com/assets/images/uploads/2017/08/gwform.jpg 251w, https://automationadmin.com/assets/images/uploads/2017/08/gwform-185x300.jpg 185w" sizes="(max-width: 251px) 100vw, 251px" /> 

### To Resolve:

1. So just copy and paste this in your PS_ISE and add scriptblocks like in lines 10-29 and then assign them to click events like in lines 56,66,76, ect.

   ```powershell
   Function Invoke-Form
   {
   Function Initialize-Window
   {
      $t = '[DllImport("user32.dll")] public static extern bool ShowWindow(int handle, int state);'
      Add-Type -Name Win -Member $t -Namespace native
      [native.win]::ShowWindow(([System.Diagnostics.Process]::GetCurrentProcess() | Get-Process).MainWindowHandle, 0)
   }
   Initialize-Window

   $StartPowershell = 
   { 
      Powershell.exe Start-Process Powershell -Verb runas 
   }

   $StartPowershellISE = 
   { 
      Powershell.exe Start-Process "Powershell_ise" -Verb runas 
   }

   $RunMyScript = 
   { 
      Start-Process Powershell -Argument "C:\scripts\resources\invokepassword.ps1"
   }

   $EndForm = 
   { 
      Stop-Process -id $pid
   }

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
   }
   }

   Invoke-Form
   ```

2. Source is maintained under [gwApplications](https://github.com/gerryw1389/powershell/blob/main/gwApplications/Public/Invoke-CustomMenuGUI.ps1)