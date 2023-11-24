---
title: 'PS: Find If User/Computer Exists Without AD Module'
date: 2019-04-09T16:25:22+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/ps-find-if-user-computer-exists-without-ad-module/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Sometimes you may want to run a powershell script that checks against AD without actually importing the AD module to a server. For example, on a file server you may want to check certain directories that are mapped to usernames in AD in order to clean up old accounts.

### To Resolve:

1. Use this in your PS Script to check if a user or computer exists in AD:

   ```powershell
   #user properties
   $san = 'myuser'
   $getad = (([adsisearcher]"(&(objectCategory=User)(samaccountname=$san))").findall()).properties
   #$getad
   If ($getad.count -gt 0)
   {
   write-output "account exists: $getad"
   }
   Else
   {
   write-output "account DOESNT exists: $getad"
   }

   #Computer properties
   $pc = 'computername'
   $getad = (([adsisearcher]"(&(objectCategory=Computer)(name=$pc))").findall()).properties
   $getad
   ```

2. Another option is `implicit remoting` which I haven't tested but seems to be the more supported way:

   ```powershell
   function Get-ActiveDirectorySession 
   {
      param
      (
      [string]$Server = 'server.mydomain.com'
      )
      $session = New-PSSession -ComputerName $Server
      Invoke-Command -Session $session -ScriptBlock {Import-Module ActiveDirectory}
      return $session
   }

   #Then at the beginning of your script you can do something like this:

   if (Get-Module -ListAvailable ActiveDirectory)
   {
   Import-Module ActiveDirectory
   }
   else {
   Import-PSSession -Session (Get-ActiveDirectorySession) -Module ActiveDirectory | Out-Null
   }
   ```

