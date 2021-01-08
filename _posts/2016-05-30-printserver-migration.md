---
title: PrintServer Migration
date: 2016-05-30T05:04:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/printserver-migration/
categories:
  - WindowsServer
tags:
  - Migration
---
<!--more-->

### Description:

We needed to migrate the Print Server to Server 2012.

### To Resolve:

1. Follow the steps on [Create A New VM](https://automationadmin.com/2016/05/hyper-v-to-create-a-new-vm/).

2. On the old print server, get a list of all the printers and their model numbers, names, and IP's if you can. I then went to their manufacturer websites and downloaded the newest versions of their drivers for Server2012 64b.

3. Copy those over to the new server and install them one by one. I'm sure there is a faster way, but coming from Server 200 to Server 2012 was a mission of itself.

4. Once the printers are installed on the new server, you simply share them out giving `administrator` full control and `everyone` print only permissions.

5. I then installed the Print Server role under Server Manager.

6. Lastly, if you Run => `control printers` => Under each printers properties and the General tab in the Location text box, I put in the IP address of the printer just for documentation sake.