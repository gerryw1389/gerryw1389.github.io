---
title: 'GPO: Enable-PSRemoting'
date: 2016-05-29T04:21:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gpo-enable-psremoting/
tags:
  - WindowsServer
tags:
  - GroupPolicy
  - Powershell
---
<!--more-->

### Description:

Follow these steps to enable PowerShell remoting via GPO.

### To Resolve:

1. On the DC, create a new domain policy.

2. Edit the newly created GPO.

3. Navigate to: `Computer Configuration\Policies\Administrative Templates\Windows Components\Windows Remote Management WinRM Service`

4. Open the "All remote server management.." policy and change it to `enabled` and set the filters for IPv4/6 to `*`
   - NOTE: After you ensure this works, go back and change this to your appropriate subnet instead - see [here]() for more info.

   <img class="alignnone size-full wp-image-661" src="https://automationadmin.com/assets/images/uploads/2016/09/gpo-enable-psremoting-1.png" alt="gpo-enable-psremoting-1" width="956" height="752" srcset="https://automationadmin.com/assets/images/uploads/2016/09/gpo-enable-psremoting-1.png 956w, https://automationadmin.com/assets/images/uploads/2016/09/gpo-enable-psremoting-1-300x236.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/gpo-enable-psremoting-1-768x604.png 768w" sizes="(max-width: 956px) 100vw, 956px" />

5. Now we need to configure the firewall. Navigate to: `Computer Configuration\Policies\Windows Settings\Security Settings\ Windows Firewall\Inbound Rules`

6. Right click => Create A New Rule => Predefined: Windows Remote Management => Keep defaults for next screens and finish.

   <img class="alignnone size-full wp-image-662" src="https://automationadmin.com/assets/images/uploads/2016/09/gpo-enable-psremoting-2.png" alt="gpo-enable-psremoting-2" width="728" height="505" srcset="https://automationadmin.com/assets/images/uploads/2016/09/gpo-enable-psremoting-2.png 728w, https://automationadmin.com/assets/images/uploads/2016/09/gpo-enable-psremoting-2-300x208.png 300w" sizes="(max-width: 728px) 100vw, 728px" />

7. Now, in the same tree that you are in, navigate up to "System Services" => Select "Windows Remote Management" Service => check "define this setting" and set it to `automatic`.

8. Navigate back up to: `Computer Configuration\Preferences\Control Panel Settings\Services`.

9.  Right click - New - Service => General Tab: Startup= No Change, ServiceName= WinRM, ServiceAction (optional)= Start Service => Recovery tab => set all 3 dropdowns to "restart the service"

10. Done. Run gpupdate on the domain controller and wait for it to be pushed to the clients.



### References:

["PS Remoting Considerations"](https://blogs.technet.microsoft.com/poshchap/2014/07/03/ps-remoting-considerations/)    
["Enable Powershell Remoting via Group Policy "](https://www.briantist.com/how-to/powershell-remoting-group-policy/)  