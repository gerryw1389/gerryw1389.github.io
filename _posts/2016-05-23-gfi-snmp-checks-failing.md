---
title: 'GFI: SNMP Checks Failing'
date: 2016-05-23T12:45:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gfi-snmp-checks-failing/
tags:
  - Hardware
tags:
  - Monitoring
---
<!--more-->

### Description:

SNMP check will fail on the GFI Agent dashboard. This means there is a Hardware component that failed or you need to update the driver or firmware for a component.

### To Resolve:

1. If all six checks are failing, you may need to look at services. The SNMP Service may have stopped or you may need to restart the &#8220;DSM Data Manager&#8221; service (If it's a Dell Server). To do this: Select the client in the Dashboard => remote background => find the &#8220;DSM Data Manager&#8221; service => if disabled, enable and start.

   - Open up Dell Open Manage or HP Insight and see what's generating the error.

2. Download the newest driver or firmware related to it. For Perc Adapters, download the newest driver under the &#8220;SAS-Raid&#8221; section. For a &#8220;Storport out of date&#8221; error, go to (link dead, search yourself) and install that. The Dell site doesn't have it.

3. For &#8220;Processor Temperature Fail&#8221;, check to see if it's an older server. If it is, bump the check up to &#8220;400&#8221; instead of &#8220;350&#8221; through the check's settings in the agent. If it fails again, you will need to have the customer open up the server and blast it with air duster.

4. For &#8220;RAID => Storage&#8221; failures, it's most likely going to be a &#8220;Predicted Failure&#8221; of a drive in OpenManage, or a &#8220;RAID Degraded&#8221; for a failed drive. Find if the drive is a SAS drive or a SATA, SAS drives have 3 year warranties and SATAs only have 1. Warranty or have them purchase a replacement drive and then follow the steps in &#8220;Changing Drives On A Server&#8221;. Another possibility is that the server has rebooted, and the perc battery needs to charge back up. Note that if this is the case, this check will fail for up to 8 hours and then pass again.

5. For &#8220;Dell => Voltage Status&#8221; you most likely need to update the Idrac. Follow the steps in &#8220;System Board PS1 PG Fail In Dell OM&#8221;. Download and install the newest Lifecycle Controller, RAID, BIOS, and Idrac.

6. For &#8220;Dell => Fans&#8221; you most likely just need to call Dell to get them replaced. This check rarely fails.