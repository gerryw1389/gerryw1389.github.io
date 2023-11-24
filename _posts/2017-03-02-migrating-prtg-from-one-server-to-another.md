---
title: Migrating PRTG From One Server To Another
date: 2017-03-02T05:04:07+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/03/migrating-prtg-from-one-server-to-another/
tags:
  - LocalSoftware
tags:
  - Monitoring
  - Setup
---
<!--more-->

### Description:

So we wanted to move PRTG from one server to another. Seems simple enough, let's do this! I skipped licensing because we use the free version.

### To Resolve:

1. Install PRTG on destination server.

2. Stop the Core and Probe services on original and target systems. I think that can be done through the admin tool, but I just used `services.msc`.

3. On the source computer, copy and paste the following into a folder, zip it, and transfer to the destination server:

   - Find the main files by launching PRTG Admin Tool => Core Server tab => Local Storage of Data files.. for me this was `C:\Program Data\PRTG` or something
   - [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `regedit` => Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Paessler\PRTG Network Monitor` => export this to the folder you will zip/transfer.

4. On the original computer, disable the services we stopped, on the destination server, start them.

5. Poke around the PRTG Admin Tool and correct where appropriate. Then launch the web GUI and do the same there. Most of my stuff just imported just fine. We don't have remote probes setup so please follow the guide if you do, I recommend following it anyways as my environment is real simple and this is just basic notes.

6. After making sure everything is correct, I then had to go to my switches and redirect their [SNMP traffic](https://automationadmin.com/2017/02/configuring-snmp/) to the new destination server.

### References:

["How can I move (migrate) my PRTG installation to another computer?"](https://kb.paessler.com/en/topic/413-how-can-i-move-migrate-my-prtg-installation-to-another-computer)