---
title: 'PS: Lock Computer And Turn Off Monitors'
date: 2018-03-31T23:55:20+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/ps-lock-computer-and-turn-off-monitors/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

There is a pretty known way to lock your computer using the user32.dll, but what isn't as easy to find is a way to turn off your monitors as well. Sometimes, like when I'm done for the day on my home computer, I want to lock it AND turn off my screens.

### To Resolve:

1. There are two main options, one is a Powershell Script and the other is using NirCmd.exe. Both are free and pretty easy to configure. The Powershell script:

   ```powershell
   Add-Type -TypeDefinition '
   using System;
   using System.Runtime.InteropServices;
   
   namespace Utilities {
      public static class Display
      {
         [DllImport("user32.dll", CharSet = CharSet.Auto)]
         private static extern IntPtr SendMessage(
            IntPtr hWnd,
            UInt32 Msg,
            IntPtr wParam,
            IntPtr lParam
         );
   
         public static void PowerOff ()
         {
            SendMessage(
               (IntPtr)0xffff, // HWND_BROADCAST
               0x0112,         // WM_SYSCOMMAND
               (IntPtr)0xf170, // SC_MONITORPOWER
               (IntPtr)0x0002  // POWER_OFF
            );
         }
      }
   }
   '
   "%windir%\system32\rundll32.exe user32.dll,LockWorkStation"
   [Utilities.Display]::PowerOff()
   ```

2. The nircmd.exe way: Create shortcut, edit target:

   ```escape
   # Wait two seconds and turn off the computer monitor.
   "C:\path\to\nircmd.exe" cmdwait 2000 monitor off
   # Optional: Assign hotkey, change icon to lock, place in taskbar
   ```