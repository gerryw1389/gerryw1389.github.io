---
title: Changing The Domain Admin Password
date: 2016-05-29T04:53:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/changing-the-admin-password/
tags:
  - WindowsServer
  - SysAdmin
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

It's good practice to change the admin password on your servers (local/domain) periodically. Use this as a checklist of things to consider.

### To Resolve:

1. First, let everyone know in advance. Then reset the admin password on the primary domain controller (the PDC).

2. Check scheduled tasks. Open up every active task and paste the new password in and hit OK. Ideally, you would run tasks as the lowest user possible, but that doesn't always happen in smaller environments.

3. If you are using a Network Monitoring Solution, make sure WMI has the new credentials. Again, it's best practice to have a specific user with WMI rights but some places just use the domain admin credentials.

4. Let everyone know that if anything breaks in the next couple weeks, it may be due to the admin password change. This is a good way to weed out hard coded passwords in scripts or anything that relies on the current admin password.