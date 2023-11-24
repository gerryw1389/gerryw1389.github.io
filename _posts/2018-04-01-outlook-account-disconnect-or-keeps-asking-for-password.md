---
title: 'Outlook: Account Disconnected Or Keeps Asking For Password'
date: 2018-04-01T06:48:57+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/outlook-account-disconnect-or-keeps-asking-for-password/
tags:
  - LocalSoftware
tags:
  - MSOffice
---
<!--more-->

### Description:

Follow this post if you have Outlook constantly asking for a password, even if you enter it and hit save. Also, if you have an account that says &#8220;disconnected&#8221;.

### To Resolve:

1. This almost always has to do with the credential manager getting tripped up.

   - Close Outlook.
   - Open a Run command (keyboard shortcut Windows+R) and type: `outlook /safe`

2. This brings Outlook up in safe mode, here it should ask for that account's password. Enter it. If the windows never comes up, edit the following key and set value to 1 and try again: `HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Identity -Name "DisableADALatopWAMOverride" Value "1"`

   - I've seen a lot of cases where Outlook will say &#8220;connecting to email1@domain.com&#8221; and will already pre-fill one of the choices as email2@domain.com. If it does this, choose &#8220;More Options&#8221; and manually type in &#8220;email1@domain.com&#8221; and its password.

   - The key is to match whatever account is at the top next to &#8220;connecting to&#8221; that you cannot edit. Make sure you entered them once, just press the &#8220;X&#8221; in the top right corner. It doesn't matter if it acts like they are correct or not, the main thing is that we just enter them fresh and check the box to remember the passwords.

3. Close Outlook and re-enter back in Outlook normal mode by just selecting the Outlook icon as usual. Verify the status bar now says &#8220;Connected To: Microsoft Exchange&#8221; in the bottom right corner.

4. If it still doesn't work, Open your Credential Manager search &#8220;cred&#8221; to find it, and delete all entries with email1@domain.com in them. For a quicker list, run:

   ```powershell
   rundll32.exe keymgr.dll, KRShowKeyMgr
   ```

5. Repeat step 2. Now open Outlook. Select one folder for each of your email accounts and verify that in the bottom right it says &#8220;Connected To: Microsoft Exchange&#8221;.