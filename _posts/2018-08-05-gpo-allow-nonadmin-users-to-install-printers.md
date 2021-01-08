---
title: 'GPO: Allow NonAdmin Users To Install Printers'
date: 2018-08-05T07:32:28+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/08/gpo-allow-nonadmin-users-to-install-printers/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

Follow these steps to allow non-admins to install print drivers.

### To Resolve:

1. Create a GPO at: `Computer Configuration\Policies\Administrative Templates\System\Driver Installation`

   - Allow non-administrators to install drivers for these devices setup classes = Enabled  
   - Device class GUID of printers: {4d36e979-e325-11ce-bfc1-08002be10318}
   - Computer Configuration/Policies/Administrative Templates/Printers  
   - Point and Print Restrictions = Enabled
   - Security Prompts: When Installing Drivers for a new connection = Do not show warning or elevation prompt
   - Edit: You may need to include PNPPrinters as well => {4658ee7e-f050-11d1-b6bd-00c04fa372a7}

2. If you have issues with GPO, check the reg keys at:  
   - [https://getadmx.com/?Category=Windows\_10\_2016&Policy=Microsoft.Policies.DeviceInstallation::DriverInstall\_Classes\_AllowUser](https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.DeviceInstallation::DriverInstall_Classes_AllowUser)  
   - [https://getadmx.com/?Category=Windows\_10\_2016&Policy=Microsoft.Policies.Printing::PointAndPrint\_Restrictions\_Win7](https://getadmx.com/?Category=Windows_10_2016&Policy=Microsoft.Policies.Printing::PointAndPrint_Restrictions_Win7)