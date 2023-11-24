---
title: Office 365 Duplicate Email Issue
date: 2016-05-24T12:23:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/office-365-duplicate-email-issue/
tags:
  - LocalSoftware
tags:
  - MSOffice
---
<!--more-->

### Description:

Users who have Office 365 will have duplicate emails if they use a POP account.

### To Resolve:

1. First, disable Office updates. Inside Outlook, go to File => Office Account => Update Options (dropdown) => Disable Updates.

2. Close out of all Office applications that are open.

3. Now open an elevated command prompt (Search => cmd => CTRL+SHIFT+Enter) and run the following:

   ```powershell
   C:\Program Files\Common Files\microsoft shared\ClickToRun\OfficeC2RClient.exe /update user updatetoversion=16.0.6366.2068
   ```

   - This reverts you to the February build, you will need to re-enable updates in the future once MS comes up with a fix for this.

### References:

["Outlook 2016: POP3 duplicates after installing the February 16 Update"](https://www.howto-outlook.com/news/outlook-2016-pop3-duplicates-february-2016.htm)