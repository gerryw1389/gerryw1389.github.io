---
title: How To Restart In Safe Mode From Command Line
date: 2016-05-30T05:51:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/how-to-restart-in-safe-mode-from-command-line/
categories:
  - Windows
tags:
  - Scripting-CMD
---
<!--more-->

### Description:

If you ever want to reboot a computer in safe mode from within Windows follow these steps.

### To Resolve:

1. Run => `Msconfig` => Boot tab => Check the Safe-Boot checkbox and select minimal radio button for regular safe mode, choose network for safe mode with networking. Then reboot the machine.

2. Alternatively, follow the steps below to go the `BCDedit` route. Make sure to keep a backup of your `Bcdedit` settings before continuing.

   - Open either an elevated command prompt or a command prompt at boot. Run the following: `bcdedit` and take note of your {current} settings. NOTE: Under the Windows Boot Loader sections, make note of the identifier value (ex: {current}) for the OS description (ex: Windows 7) that you want to use in steps c, d, or e below.

3. Do either step below for what you would like to do.

   - To Start in Safe Mode: In the command prompt, type the command below and press enter. Substitute identifier in the command below with the actual value or long GUID number to the right of identifer in the command used from step a:

   ```powershell
   bcdedit /set {identifier} safeboot minimal
   :: For example: If I wanted to have Windows 7 boot into Safe Mode using the values in the screenshot under step 2, I would type this command below and press Enter:
   bcdedit /set {current} safeboot minimal
   ```

   - Then reboot the machine.

   - To Start in Safe Mode with Networking: In the command prompt, type the command below and press enter. Substitute identifier in the command below with the actual value or long GUID number to the right of identifer in the command used from step 2.

   ```powershell
   bcdedit /set {identifier} safeboot network
   :: For example: If I wanted to have Windows 7 boot into Safe Mode with networking using the values in the screenshot under step 2, I would type this command below and press Enter:
   bcdedit /set {current} safeboot network
   ```

   - Then reboot the machine.

   - To Start Windows 7 back in Normal Mode: From step 2, look for the identifier (ex: {current}) for the OS description (ex: Windows 7) under a Windows Boot Loader section that has the safeboot value in it. In the command prompt, type the command below and press enter: (Substitute identifier in the command below with the actual value or long GUID number to the right of identifer in the command used from step 2):

   ```powershell
   bcdedit /deletevalue {identifier} safeboot
   ```

   - Then reboot the machine.
