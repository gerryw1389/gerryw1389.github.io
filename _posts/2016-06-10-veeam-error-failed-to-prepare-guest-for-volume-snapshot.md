---
title: 'Veeam Error: Failed To Prepare Guest For Volume Snapshot'
date: 2016-06-10T13:28:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/veeam-error-failed-to-prepare-guest-for-volume-snapshot/
categories:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

So we use Veeam for backups and replications and I ran into an issue the other day. It is common practice to have all SQL and Domain Controller VM's to have &#8220;Application Awareness&#8221; turned on in the backup settings. The problem is, when I enable them I get errors. If I turn them off, they backup fine. This didn't make sense to me because Application Awareness was turned on for the same VMs that failed on our replications. WTF? Anyways, I put in a ticket with Veeam and this is what fixed it:

Just to preface, you will have errors such as:

   ```escape
   # SQL VM: 
   - Unable to subscribe to guest processing components: VSSControl: HvIsSnapshotInProgress failed. Transaction logs will not be truncated.. Error: Error code: 0x80070005 Failed to invoke func [HvIsSnapshotInProgress]: Access is denied.. Failed to check whether guest Hyper-V snapshot is in progress. RPC function call failed. Function name: [HvIsSnapshotInProgress]. Target machine: [<ip address>]. RPC error:Access is denied. Code: 5 Error code: 0x80070005 Failed to invoke func [HvIsSnapshotInProgress]: Acc  
   - Failed to create snapshot (Microsoft Software Shadow Copy provider 1.0) (mode: Veeam application-aware processing) Details: Failed to prepare guests for volume snapshot.  
   - Error: Failed to prepare guests for volume snapshot.
   - Guest processing skipped (check guest OS VSS state and hypervisor integration components version)  
   - Failed to create snapshot (Microsoft Software Shadow Copy provider 1.0) (mode: Crash consistent) Details: Failed to prepare guests for volume snapshot.  
   - Failed to create snapshot (Microsoft Software Shadow Copy provider 1.0) (mode: Veeam application-aware processing) Details: Failed to prepare guests for volume snapshot.  

   # Domain Controller VM:  
   - Failed to create snapshot (Microsoft Software Shadow Copy provider 1.0) (mode: Veeam application-aware processing) Details: Failed to prepare guests for volume snapshot. 
   - Error: Failed to prepare guests for volume snapshot.
   ```

I could access the share `\\ServerComputerName\admin$` via Windows Explorer (CIFS/SMB) and ping these machines just fine so I was sure it wasn't networking/firewall related...

### To Resolve:

1. Go into the backup job settings for whichever VMs are failing and go to the &#8220;Guest Processing&#8221; section.

2. Under &#8220;Guest OS Credentials&#8221; make sure you have the credentials for the host server in there. Then click the Credentials button to the right of it. This only becomes available after you check the &#8220;Enable application-aware processing&#8221; checkbox.

3. Now add the credentials to the VMs using the `Domain\User.Name` standard instead of `user@domain` standard. That's all it was!

### References:

["RPC function call failed. RPC error:Acces is denied"](https://forums.veeam.com/vmware-vsphere-f24/rpc-function-call-failed-rpc-error-acces-is-denied-t24111.html)