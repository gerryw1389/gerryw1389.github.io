---
title: Domain Replication Issues
date: 2016-05-29T03:36:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/domain-replication-issues/
categories:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

Use the following troubleshooting steps when running into Domain Replication issues. These will sometimes happen when replacing DC's without going through the proper replacement steps which should be the following:

1. Add the new DC's => Promote them.

2. Integrate them => Configure roles and services.

3. Take the originals offline => Keep them running side by side at least for 24 hours if possible.

NOTE: DHCP/DNS issues can usually be resolved by adding the IP as a secondary on the new servers NIC once you power the old server off.
{: .notice--success}

### To Resolve:

1. On the domain controller, Run => `eventvwr.msc` => Check the logs regarding Active Directory. If there are errors or warnings, try the following:

2. Type each of the commands and study their output:

   ```escape
   repadmin /showrepl * /errorsonly >log.txt # see [this](https://technet.microsoft.com/en-us/library/cc770963.aspx)  
   repadmin /replsummary  
   repadmin /syncall

   dcdiag /c /e /v /q /f:results.txt # see [this](https://technet.microsoft.com/en-us/library/cc731968.aspx)

   netdiag /q /v /dcAccountEnum /l >>log.txt# see [this](https://technet.microsoft.com/en-us/library/cc731434.aspx)
   ```