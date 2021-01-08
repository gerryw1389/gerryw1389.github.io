---
title: 'Veeam: Domain Controller DR'
date: 2016-05-24T12:32:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/veeam-domain-controller-dr/
categories:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

So our domain controller was running on a physical host that got stuck in a Windows Update boot loop, so we had to recover it before the next business day. Thankfully, we use a software called Veeam Backup and Recovery in which we have certain production server VM's that are being replicated in real time to another physical host in the event of a crash. This is what we did when our FSMO AD DC crashed:

### To Resolve:

1. Make sure the old server is powered off and not on the network.

2. Start up the replication server VM instance.

3. Once in the OS, make sure the NIC is enabled. What I found is that the server restored with the proper settings but there was a &#8220;Network cable unplugged&#8221; in the VM. In the host, I went to Hyper-V settings and assigned the LAN access to the VM.

4. We then monitored the event viewer logs for issues with domain replication. The VM instantly created a new GUID and started the replication.

5. After a couple hours, we opened up the DHCP application and chose the option to &#8220;unauthorize&#8221; and &#8220;authorize&#8221;. This allowed the server to start handing out DHCP addresses once again.

  <img class="alignnone size-full wp-image-646" src="https://automationadmin.com/assets/images/uploads/2016/09/domain-controller-dr.png" alt="domain-controller-dr" width="340" height="139" srcset="https://automationadmin.com/assets/images/uploads/2016/09/domain-controller-dr.png 340w, https://automationadmin.com/assets/images/uploads/2016/09/domain-controller-dr-300x123.png 300w" sizes="(max-width: 340px) 100vw, 340px" />

6. For DNS, we just verified that the DNS service was running in `services.msc`. You can also open the applet and choose the option to restart all services.

7. Monitored the server the next day for any new errors. Everything seemed to have worked as planned.