---
title: 'GPO: Home Folders'
date: 2018-04-01T00:04:34+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/gpo-home-folders/
tags:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

I'm thinking of rolling this out in my environment instead of the current robocopy script we are running (which is essentially the same thing). A &#8220;home folder&#8221; is a drive that end users see connected automatically when the login that they can store their files in.

### To Resolve:

1. On your fileserver's data drive, create a folder on the server => name it Home (or whatever).

   - Share the folder with Advanced Sharing full control to everyone.
   - Go to Security and convert existing NTFS permisions to Explicit permissions by disabling inheritence. Then back out completely and go back in. 

2. Open Active Directory Users and Computers and select the users that need to have a home directory => View the properties of the users => Select the Profile tab => Select the radio button near connect => Select a drive letter for the home directories. (When the user logins in, this is the drive letter that will 'point' to his/her home folder. You should choose a letter that you know won't be used by the user's local machine – the N drive is becoming a popular choice.)

3. Type the UNC path to the home folder in the &#8220;to&#8221; text box area `\\ServerComputerName\sharename\%username%`  
   - For example, if my server name is Server2008 and my share name is home, then I'd type `\\Server2008\home\%username%`  
   - If your share name includes spaces, enclose the path in quotes. 

4. Select "OK" to exit the user's properties. Check the contents of the shared folder; a folder that matches the user's name should exist in this folder. If an error occurs when you OK out of this screen, chances are the directory didn't get created. Check the shared folder to see if the folder was created and check your UNC path and make sure you've entered it correctly.