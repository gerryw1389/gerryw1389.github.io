---
title: Permissions Errors In A Domain Environment
date: 2016-05-29T03:45:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/permissions-errors-in-a-domain-environment/
tags:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

When computers are on a domain, there may be times when a user gets errors having to do with permissions to various things. The best thing to do is to verify that this user is verified on the domain controller (DC) as an authorized user in the correct group.

### To Resolve:

1. Run the [Netscan](https://www.softperfect.com/products/networkscanner/) utility to identify the server that acts as the DC (Domain Controller) for the network.

   - Verifying that a specific server is a DC: RDP to the server you think is the DC and see if it is listed as a DC under Administrator Tools => Active Directory Users and Computers => Domain Controllers and see if the server is listed. You can also run `lusrmgr.msc` and it will give you an error saying that `You cannot run this on this machine because it is the Domain Controller`

2. RDP to the DC and check to see that the user who is getting the error is one on the domain. Once on the DC, Run => `control admintools` (or navigate to Administrator Tools => Active Directory Users and Computers) => then go to your user => make sure they belong to a group with the proper permissions. This is done through the Member Of tab on the user's properties.

3. Re-add the computer to the domain. Follow the steps in [Workstation Cannot Login To Domain](https://automationadmin.com/2016/05/workstation-cannot-login-to-domain/) if you don't know