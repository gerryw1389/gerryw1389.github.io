---
title: Temporary Local Admin
date: 2019-06-15T00:16:11-05:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/06/temporary-local-admin
tags:
  - Windows
---
<!--more-->

### Description

So apparently you still have to have admin rights to change your cursor theme. If you right click and `install` and then enter admin credentials, the scheme never shows up. For this you need 'temporary local admin'. This walkthrough assumes you use a regular domain account that is not local admin and have access to an account that does have local admin. Follow these steps to resolve:

### To Resolve

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `lusrmgr.msc` this will open the GUI for you to add your user to local admins.

2. Do this and use your regular domain credentials when it prompts for it. 

3. Now right click on any cursor theme you want and choose `install` it will bring up a credential box. Type in your **regular** credentials.

   - This will allow you to keep your cursor scheme permanently.

4. Now repeat the steps again to remove your domain user from local admins.