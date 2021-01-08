---
title: Realm AD Group Sudo Access
date: 2019-04-09T21:17:53+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/realm-ad-group-sudo-access/
categories:
  - Linux
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

So with [SSSD on RHEL boxes](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/windows_integration_guide/index), one thing we want to do is use Active Directory groups on linux machines. This is how you can do this:

NOTE: For this to work, users in AD must have a "uidNumber" and a "gidNumber" assigned. These can be viewed on "Attributes" tab in the AD User object and the AD Group Object which only has a gidNumber.

### To Resolve:

1. Create AD Group

2. Assign gidnumber to the group

   ```powershell
   $group = mygroup
   # Set a new GID value 
   
   $properties = @{ 
      'LDAPFilter' = "(&(objectCategory=group)(gidNumber=*))" 
      'SearchBase' = 'OU=blah,DC=domain,DC=com' 
      'Properties' = 'gidNumber' 
   } 
   $groups = Get-ADObject @Properties| Select-Object @{Name = "DN"; Expression = {$_.DistinguishedName}}, @{Name = "gid"; Expression = {$_.gidNumber}} 
   $lastgid = ($groups | Sort-Object -Property gid | select -Last 1).gid 
   $newVal = $lastgid + 1 
   
   If ($newVal.tostring().length -eq 10) 
   {  
      Write-Output "New gid Number: $newval" 
   } 
   Else  
   { 
      "unable to find a value for new gid" 
   } 
   Get-ADGroup $group | Set-ADGroup -Add @{ gidNumber = $newval }
   ```

3. Edit /etc/sudoers to allow them under wheel

   ```escape
   # Uncommment to allow people in group wheel to run all commands  
   # %wheel ALL=(ALL) ALL  
   %test-group ALL=(ALL) ALL
   ```

4. Add user to that group in AD

5. Upon removing user from group, they will not have sudo access.

6. Any time you make a change to group membership in AD for linux servers, you must run `sss_cache -E; service sssd stop ; rm -rf /var/lib/sss/db/* ; service sssd start` on the servers you want the users to access for it to take effect.
