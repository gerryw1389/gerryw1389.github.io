---
title: DHCP Server Migration
date: 2016-05-29T04:07:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/dhcp-server-migration/
tags:
  - WindowsServer
tags:
  - Migration
---
<!--more-->

### Description:

We once had to migrate the DHCP role from a WS2008 DC to a WS2012 DC. These are the steps to follow:

### To Resolve:

1. On the old computer, open up DHCP and right click on the server name => Backup. Point to a path you can get to on the new server

2. Backup the DHCP service and stop the services.

3. On the new DHCP server, make sure the services are not running.

4. Restore the file to the new DHCP server and start the services.

5. After it has been restored, make sure you right click on DHCP in the DHCP Management snap in and select "Manage Authorized Servers" and select that one.
