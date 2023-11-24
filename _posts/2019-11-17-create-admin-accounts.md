---
title: Create Admin Accounts
date: 2019-11-17T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/11/create-admin-accounts/
tags:
  - WindowsServer
tags:
  - Scripting-Powershell
  - ActiveDirectory
---
<!--more-->

### Description:

I took the following steps to bulk create admin accounts for my organization.

### To Resolve:

1. Create the users:

   ```powershell
   $users = @(
      'billy',
      'jimmy',
      'gerry'
   )
   Import-Module ActiveDirectory
   Foreach ($user In $users)
   {
      Try
      {
         $u = Get-ADUser -Identity $user -ErrorAction Stop
      }
      Catch
      {
         Write-output "Unable to find user: $user"
      }

      If ( $u.Name.Length -gt 0 )
      {
         $first = $($u.Givenname)
         $last = $($u.Surname)
         $upn = ( $($u.name) + '-a@domain.com')
         $display = $upn.replace("@domain.com", "")
         $ou = "OU=Admins,DC=Company,DC=com"
         $Pass = ConvertTo-SecureString -string 'seeKeypass' -AsPlainText -force
         $Params = @{
               'Name'                  = $display
               'Accountpassword'       = $Pass
               'Changepasswordatlogon' = $False
               'Givenname'             = $first
               'Surname'               = ($Last + '-Admin')
               'Displayname'           = $display
               'Emailaddress'          = $upn
               'Enabled'               = $True
               'Userprincipalname'     = $Upn
               'Path'                  = $Ou
         }
         New-Aduser @Params
         Write-Output "New user created: $display"

      }
      Clear-Variable u
   }
   ```

2. Create Groups

   ```powershell
   $groups = @(
      'Admins-IT',
      'Admins-Security',
      'Admins-Support')

   foreach ($group in $groups)
   {
      New-ADGroup -Name $group -Path "OU=Admins,DC=Company,DC=com"
   }

   # Manually add users to each group since this is a one time task:
   Add-ADGroupMember -Identity "Admins-IT" -Members "gerry"
   Add-ADGroupMember -Identity "Admins-Support" -Members "jimmy"
   ```

3. Lastly, added the new group to a list of server administration groups that already exists:

   ```powershell
   $groups = Get-ADGroup -Filter * -SearchBase "OU=Servers,DC=Domain,DC=com"
   foreach ($group in $groups)
   {
      Add-ADGroupMember -Identity $($group.name) -Members "Admins-IT"
      Write-Output "Adding server admins to: $($group.name)"
   }
   ```

