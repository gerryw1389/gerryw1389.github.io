---
title: 'MS Outlook: Adding Account Issue'
date: 2016-05-23T19:01:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ms-outlook-adding-account-issue/
categories:
  - LocalSoftware
tags:
  - MSOffice
  - Regedit
---
<!--more-->

### Description:

I once had an issue with a client where every time they launched Outlook 2016, it would error out on the part where you &#8220;log on to the mail server and send a test email&#8221; saying something about connectivity to the server. This is after signing in on the pop up that verifies your server and everything.

  <img class="alignnone size-full wp-image-685" src="https://automationadmin.com/assets/images/uploads/2016/09/outlook-2016-add-account-issue.png" alt="outlook-2016-add-account-issue" width="464" height="111" srcset="https://automationadmin.com/assets/images/uploads/2016/09/outlook-2016-add-account-issue.png 464w, https://automationadmin.com/assets/images/uploads/2016/09/outlook-2016-add-account-issue-300x72.png 300w" sizes="(max-width: 464px) 100vw, 464px" />

   - We knew the account wasn't the issue because we could add it on one of our lab machines.  
   - We knew it wasn't a DNS issue because we could ping autdiscover.ourdomainname.com.  
   - We knew it wasn't account credentials because we could sign into Outlook online (OWA).

### To Resolve:

1. Run => regedit. Navigate to: HKEY_CURRENT_USER\Software\Microsoft\Office\x.0\Outlook\AutoDiscover (create if not there)

   - `x.0` in the above registry path corresponds to the Outlook version (16.0 = Outlook 2016, 15.0 = Outlook 2013, 14.0 = Outlook 2010, 12.0 = Outlook 2007

2. Add the following keys:

   ```escape
   Type=DWORD32, Name=ExcludeHttpsRootDomain, Value=1
   Type=DWORD32, Name=ExcludeScpLookup, Value=1
   ```

3. Either close out of all windows or reboot. NOTE: I had originally done this on a test user account and had to re-create the keys on the problem user account. Pay attention to which hive you are in (obvious HKLM wouldn't have this problem).

4. Try again, should work this time.

### References:

["Exchange Account Set-up Missing in Outlook 2016"](http://www.slipstick.com/outlook/exchange-account-set-up-missing-in-outlook-2016)