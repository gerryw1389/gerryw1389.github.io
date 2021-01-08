---
title: 'GPO: Deny Logon Local'
date: 2017-06-23T17:10:46+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/06/gpo-deny-logon-local/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

Follow these steps to modify which users/computers can access a computer.  
  
</br>

### To Resolve:

1. Navigate to: `Computer Configuration\Policies\Security Settings\Local Policies\User Rights Assignment`

   - &#8220;Allow log on locally&#8221; => Any accounts that will have access
   - &#8220;Deny access to this computer from the network&#8221; => Add: `Local accounts and Guests`