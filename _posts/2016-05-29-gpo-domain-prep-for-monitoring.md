---
title: 'GPO: Domain Prep For Monitoring'
date: 2016-05-29T04:17:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gpo-domain-prep-for-monitoring/
categories:
  - WindowsServer
tags:
  - Monitoring
  - GroupPolicy
---
<!--more-->

### Description:

This GPO is used to when you want to setup a monitoring application like PRTG Network Monitor, Spiceworks, or Zabbix. It essentially opens the ports for domain joined computers to where you can query them remotely.

### To Resolve:

1. Remote into the Domain Controller and open up Group Policy Managment.

2. Navigate to Forest:ForestName => Domains => (YourDomainName). Right click on your domain name and choose the options to &#8220;Create a GPO and link it here&#8221;. Call it &#8220;WMIPermissions&#8221;.

3. Right Click WMIPermissions in the list and choose &#8220;edit&#8221;.

4. Navigate to: `Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options`

5. On the right, click on &#8220;DCOM: Machine Access Restrictions in Security Descriptor&#8230;&#8221; and open it up. Check the box for &#8220;Define this setting&#8221; and click on the &#8220;edit security&#8221; button.

6. Click &#8220;Add&#8221; and add the domain admin credentials. OK. In the &#8220;group or user names&#8221; select the domain admin. In the permissions for Administrators field, ensure there is a checkmark in Allow for &#8220;remote access&#8221;. OK. OK.

7. On the right, click on &#8220;DCOM: Machine Launch Restrictions in Security Descriptor&#8230;&#8221; and open it up. Check the box for &#8220;Define this setting&#8221; and click on the &#8220;edit security&#8221; button.

8. Click &#8220;Add&#8221; and add the domain admin credentials. OK. In the &#8220;group or user names&#8221; select the domain admin. In the permissions for Administrators field, ensure there is a checkmark in Allow for &#8220;remote launch&#8221; and &#8220;remote activation&#8221;. OK. OK.

9. This may not be necessary, but I also go to: `Computer Config\Policies\Windows Settings\Security Settings\Windows Firewall with Advanced Security\Windows Firewall with Advanced Security\Inbound Rules node`

10. Right click on the right UI => New Rule => Predefined Option => WMI => Check all => Allow the connection.

11. Now navigate to: `Computer Configuration\Administrative Templates\Network\Network Connections\Windows Firewall\Domain Profile`. Enable:

   - Windows Firewall: Enable remote administration
   - Windows Firewall: All ICMP exceptions => check all the options.

12. Close out of everything and wait for the domain policy to replicate (usually about 15 minutes). You can run `gpupdate /force` and then `gpresult /scope computer /h c:\scripts\gpresult.html` on the clients to make sure the settings applied.

### References:

["Is there a way to set access to WMI using GroupPolicy?"](http://serverfault.com/questions/262590/is-there-a-way-to-set-access-to-wmi-using-grouppolicy)  
["How to: Group Policy to Allow WMI Access to Remote Machine"](https://community.spiceworks.com/how_to/17452-group-policy-to-allow-wmi-access-to-remote-machine)  