---
title: Add A VPN User To Cisco Router
date: 2016-05-22T06:37:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/add-a-vpn-user-to-cisco-router/
tags:
  - Hardware
  - Networking
tags:
  - Router
---
<!--more-->

### Description:

Follow these steps to add a user to the list of VPN users in a Cisco router.

### To Resolve:

1. Open Putty and remote into the router: 10.10.10.254 / Port 22

   ```tcl
   username: test
   password: # Enter password
   cisco>enable
   cisco> # Enter password
   cisco# config t
   cisco(config)#group-policy remote attributes
   cisco(config)#username gerry password Pa$$word
   # If you want the user to have privileges, you enter "privilege 15" for root access after the password. 
   # So setup is username/password/privilege in one line.
   # Example:
   # cisco(config)#username gerry password Pa$$word 15

   cisco(config)# write mem
   ```

8. At this point, the user can VPN in. To see your current VPN users, type:

   ```tcl
   show config
   ```

   - Tap the space bar to go to the very bottom and then manually scroll up to see if the user is there.

9. If you ever need to delete a user enter the following:

   ```tcl
   username: test
   password: # Enter password
   cisco>enable
   cisco> # Enter password
   cisco# config t
   cisco(config)# group-policy remote attributes
   cisco(config)# no username gerry
   cisco(config)# write mem
   cisco(config)# exit
   ```

