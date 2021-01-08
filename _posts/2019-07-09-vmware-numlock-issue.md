---
title: VMWareWS Numlock Issue
date: 2019-07-09T00:03:43-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/07/vmware-numlock-issue/
categories:
  - LocalSoftware
---
<!--more-->

### Description

If I move the cursor into the VMWare window a message comes on say "NUM LOCK: OFF" when I move it out of the VMWare window I see message "NUM LOCK: ON".  

### To Resolve:

1. Ensure VM is powered off. Go to top menu: VM - Power - Power on to Firmware. In the BIOS go to Keyboard Settings - Auto (I first tried to 'ON' and this didn't work)

2. Inside the guest, run the following Powershell lines as admin:

   ```powershell
   Set-ItemProperty -Path 'Registry::HKU\.DEFAULT\Control Panel\Keyboard' -Name "InitialKeyboardIndicators" -Value "2"
   Set-ItemProperty -Path 'Registry::HKCU\Control Panel\Keyboard' -Name "InitialKeyboardIndicators" -Value "2"
   ```

