---
title: 'Logoff Workaround: Add User To Group'
date: 2018-04-07T03:27:23+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/logoff-workaround-add-user-to-group/
categories:
  - Windows
---
<!--more-->

### Description:

When you access resources on Windows, Kerberos is used for authentication (with NTLM as a fallback). The user's initial Kerberos ticket (TGT) is retrieved at logon which contains the user's group memberships at the moment of logon which will be copied into the service tickets (TGS) that are fetched when accessing resources. This is why group membership changes made in AD do not immediately permit/deny access.  

1. If you force the use of NTLM, group membership changes are reflected immediately due to the way NTLM authentication works. Kerberos only works with DNS names so by accessing a resource via IP address Windows will be forced to use NTLM authentication.  

2. If you purge the user's Kerberos tickets, a new TGT will be automatically fetched which will contain current group memberships. You can do this with the `klist purge`  command. Consequently, the command klist lists the user's current Kerberos tickets.

### To Resolve:

1. People have issues with multiple sessions so I have this snippet. You can populate $AccountName with system too to avoid reboots when adding computers to groups.

   ```powershell
   $AccountName = 'user'
   $loggedOn = Get-CimInstance Win32_LoggedOnUser | where {$_.Antecedent.Name -like $accountName}
   foreach ($sess in $loggedOn)
   {
   C:\Windows\System32\klist.exe purge -li ("0x{0:X}" -f [int]$sess.Dependent.LogonId)
   }
   ```

### References:

["Workaround for having to log off/on to apply Windows folder permissions?"](https://www.reddit.com/r/sysadmin/comments/6vzwzb/workaround_for_having_to_log_offon_to_apply)  
