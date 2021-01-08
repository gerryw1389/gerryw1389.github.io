---
title: Adding More Than 10 Exchange Accounts
date: 2017-01-14T06:50:06+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/01/adding-more-than-10-exchange-accounts/
categories:
  - LocalSoftware
tags:
  - MSOffice
---
<!--more-->

### Description:

So I ran into an issue during a conversion process moving some clients to Exchange where it would throw an error saying &#8220;too many Exchange accounts already exist; Please add the account as POP/IMAP&#8221;. Upon looking it up, I found that it is supposed to do this after 10, but it was doing this sometimes while adding the second account!

### To Resolve:

1. Run => regedit

2. Navigate to: `HKEY_CURRENT_USER\Software\Microsoft\Exchange`

3. Create a new entry called:

   ```escape
   DWORD: MaxNumExchange
   Outlook 2010 values: a number between 1 and 15
   Outlook 2013 values: a number between 1 and 9999
   Outlook 2016 values: a number between 1 and 9999 # I usually just set this to 20.
   ```

4. Try adding the account again.


### References:

["Multiple Exchange accounts limit"](https://www.msoutlook.info/question/490)

