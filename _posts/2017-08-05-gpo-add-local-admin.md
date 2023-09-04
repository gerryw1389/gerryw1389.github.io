---
title: 'GPO: Add Local Admin'
date: 2017-08-05T05:44:18+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/gpo-add-local-admin/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

This GPO will add a domain account as a local admin on all workstations.

### To Resolve:

1. First you need to create a security group called Local Admin: Log onto a Domain Controller, open Active Directory Users and Computers (`dsa.msc`) Create a security Group name it Local Admin. From Menu Select Action => New => Group => Name the group as Local Admin. Add the members to Local Admin group. I will add two users say Tom and Bob.

2. Next you need to create a group policy called "Local Admin GPO":  Open Group Policy Management Console (`gpmc.msc`) Right click on Group Policy Objects => select New => Type the name of the policy &#8220;Local Admin GPO&#8221;

3. Configure the policy to add the "Local Admin" group as Administrators: Here you will add the Local Admin group to the Local Admin GPO policy and put them in the groups you wish them to use. Right click "Local Admin GPO" Policy then select Edit.  
   - Expand `Computer configuration\Policies\Windows Settings\Security Settings\Restricted Groups` In the Left pane on Restricted Groups, Right Click and select "Add Group"  
   - In the Add Group dialog box, select browse and type Local Admin and then click "Check Names"  
   - Click OK twice to close the dialog box.  
   - Click Add under "This group is a member of:" Add the "Administrators" Group. Add "Remote Desktop Users" Click OK twice.
   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2017/08/gpo-local-admin.png){:class="img-responsive"} 

   - NOTE: It is important to NOT touch the `Members of this group` field as that will allow ONLY those you select and remove anything else. We are adding to, not taking away!
   {: .notice--danger}

4. Linking GPO In Group policy management console: Right click on the domain or the OU and select Link an Existing GPO => Select the Local Admin GPO

5. Testing GPOs: Log on to a PC which is join to the domain and then run `gpupdate /force` and check the local administrators group. You should see Local Admin in that group now. Make sure all PCs you want to access should be move to an OU and properly link above GPO. Tom and Bob domain users can now access all PCs remotely as a local administrator.

### References:

["How to Make a Domain User the Local Administrator for all PCs"](https://social.technet.microsoft.com/wiki/contents/articles/7833.how-to-make-a-domain-user-the-local-administrator-for-all-pcs.aspx)  
