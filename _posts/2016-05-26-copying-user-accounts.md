---
title: Copying User Accounts
date: 2016-05-26T04:27:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/copying-user-accounts/
tags:
  - Windows
---
<!--more-->

### Description:

If you want to copy a profile in Windows from one user to another, follow these steps.

### To Resolve:

1. Run => `sysdm.cpl`. Go to the User Profiles tab and select Settings

2. Under Profiles Stored On This Computer, click the user profile you want to copy and then select Copy To.

3. Browse to the location to the new path, which should be under Documents and Settings.

4. To choose a new user, in the Copy To dialog box, click Change. To start your search, in the Select User or Group dialog box, type the complete name of the user, group, or built-in security principle you are looking for, and then click OK.

#### For Windows 7:

1. Run => `compmgmt.msc`. Under Users and Groups, create a new user and profile. You can also do this through User Accounts in the Control Panel.

2. Create an Administrator account if you don't already have one.

3. Sign out of the profile that you are on and sign in to the new profile, not the administrator one.

4. Log off that account once you get to the desktop and login to your administrator account.

5. Once at the desktop, navigate to Users and copy and paste the old profile to the new profile.