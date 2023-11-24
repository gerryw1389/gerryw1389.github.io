---
title: Admin AD Accounts Best Practice
date: 2018-05-27T03:20:38+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/admin-ad-accounts-best-practice/
tags:
  - SysAdmin
---
<!--more-->

### Description:

Follow these best practices for setting up accounts in your IT department.

### To Resolve:

1. See the following:  

   - Domain Admin => Can only login to DC's  
   - Enterprise Admin => If you have more than one domain, this needs to be separate.  
   - Server Admin => Only servers  
   - Workstation Admin => Only workstations  
   - Normal Account => Day to day

2. (Preference) This is how I name them:  
   - ad.domain.com\d_gerry.williams  
   - ad.domain.com\e_gerry.williams  
   - ad.domain.com\s_gerry.williams  
   - ad.domain.com\w_gerry.williams

3. If you want to ONLY allow a certain group:  
   - `Computer Configuration\`Policies\Security Settings\Local Policies\User Rights Assignment\Allow Log on Locally`  
   - (Add your groups)  

4. If you just want to deny a group (not recommended imo):  
   - `Computer Configuration\Policies\Security Settings\Local Policies\User Rights Assignment\Deny Logon Locally`

5. Some organizations break out the &#8220;Backup Admin&#8221; as well since someone with those rights can extract anything they want from AD, including the Administrator password! Best practice is to have this account as a separate password from any Domain Admin or not even join backup servers to the domain.