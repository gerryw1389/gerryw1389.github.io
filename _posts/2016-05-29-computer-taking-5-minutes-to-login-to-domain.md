---
title: Computer Taking 5 Minutes To Login To Domain
date: 2016-05-29T03:34:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/computer-taking-5-minutes-to-login-to-domain/
categories:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

If you go to sign in on a computer on a domain and it is taking longer than usual or anything more than a minute, try these steps.

### To Resolve:

1. You want to look for network slowness first, many times this is a failing switch or break in communication between the workstation and the Domain Controller.

2. Go ahead and login. Once in, Run => `regedit`.

3. Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`

4. Create a DWORD and name it `verbosestatus` with a Data Value = `1`

5. Exit `regedit` and logoff the account. Now sign back in, I have seen this work multiple times.
