---
title: Force Replication
date: 2019-06-13T23:10:41-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/force-replication
tags:
  - Windows
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

Follow these steps to reset SYSVOL replication between DC's. I noticed this issue when I noticed that some servers were not seeing all the policies in the sysvol share as other servers.

### To Resolve:

1. Logon to your primary DC and stop the DFS Replication service ([Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `Services.msc` => DFS Replication => Stop)

2. Open ADSI Edit (Should be under Admin tools) - ADSI Edit - Connection Settings - Default naming context
   - Navigate to the following
   - `CN=SYSVOL Subscription,CN=Domain System Volume,CN=DFSR-LocalSettings,CN=<the server name to replicate from>,OU=Domain Controllers,DC=<domain>`
     - ADSI Edit - Default Naming Context - Domain Controllers - DC01 - DFSR-LocalSettings - Domain System Volume
   - Change the following attributes to the following values
     - `msDFSR-Enabled=FALSE`
     - `msDFSR-options=1`
     - Note: If you cannot see msDFSR-options, uncheck `Show only attributes that have values`

3. On the ALL other DCs, change the msDFSR-Enabled attribute to `False`
   - ADSI Edit - Default Naming Context - Domain Controllers - DC02 - DFSR-LocalSettings - Domain System Volume - msDFSR-Enabled - False

4. Force Active Directory replication throughout the domain (Run the following on all DC's).
   - `repadmin /syncall primary_dc_name /APed`

5. On the primary DC, start the DFS Replication service ([Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `Services.msc` => DFS Replication => Start)

   - Open up event viewer and navigate to Applications and Services Logs - DFS Replication.  Verify you see Event ID 4114. This may take a few minutes, keep refreshing.

   - Now turn it back to `True`: ADSI Edit - Default Naming Context - Domain Controllers - DC01 - DFSR-LocalSettings - Domain System Volume - Set the value of msDFSR-Enabled to `TRUE`

   - From the Microsoft Article (wasn't needed but putting here just in case) Execute the following via an elevated command prompt: `DFSRDIAG POLLAD`

6. Again, Force Active Directory replication throughout the domain
   - `repadmin /syncall primary_dc_name /APed`

7. Wait a few minutes and you should see Event ID 2002 and 4602 on the PDC.

8. Navigate back to each of your secondary DCs and change the value of msDFSR-Enabled to `TRUE`: ADSI Edit - Default Naming Context - Domain Controllers - DC02 - DFSR-LocalSettings - Domain System Volume - Set the value of msDFSR-Enabled to `TRUE`

9. Verify you see Event ID 2002 and 4602 on each of the secondary DCs.  This took at least 10 minutes in my environment.

10.  At this point, try running a gpupdate on your client.  If all has gone well, each of your shared SYSVOL folders on your DCs should contain the same amount of policies and your client should successfully pull down all policies.


### References:
["SYSVOL and Group Policy out of Sync on Server 2012 R2 DCs using DFSR"](https://jackstromberg.com/2014/07/sysvol-and-group-policy-out-of-sync-on-server-2012-r2-dcs-using-dfsr/)  

["How to force an authoritative and non-authoritative ...."](http://support.microsoft.com/kb/2218556/en-us)   

