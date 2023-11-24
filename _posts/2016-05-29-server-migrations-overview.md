---
title: Server Migrations Overview
date: 2016-05-29T05:16:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/server-migrations-overview/
tags:
  - SysAdmin
tags:
  - Migration
---
<!--more-->

### Description:

A common task for a Systems Administrator is to migrate an older server to a newer server. I will list a few that I have done, but essentially all migrations follow these steps:

1. Spin up a new VM. Call it the same name as the old VM but append a &#8220;2&#8221; on the end of it.

2. Copy the data or program to the new VM and ensure it works correctly.

3. Rename the new original VM after you verified it's safe to remove. Remove any DNS records or DHCP reservations going to the old VM. Also ensure that all the data off the old VM is safe to be gone e.g. Scheduled Tasks, Data, Local Users, ect.

4. Rename the new VM to the old VM's hostname if necessary. 
   
   NOTE: DO NOT DO THIS FOR DOMAIN CONTROLLERS (DC's)!
   {: .notice--danger}