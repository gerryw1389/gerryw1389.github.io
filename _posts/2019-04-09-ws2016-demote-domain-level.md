---
title: 'WS2016: Demote Domain Level'
date: 2019-04-09T15:57:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/ws2016-demote-domain-level/
categories:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

Follow these steps to demote a WS2016 DC to a 2012r2 domain so 2012r2 DC's can join the domain.

### To Resolve:

1. Open Admin PS on the domain controller and type:

   ```powershell
   (Get-ADForest).ForestMode	
   Set-ADForestMode -ForestMode Windows2012r2Forest
   (Get-ADForest).ForestMode	
   (Get-ADDomain).DomainMode
   Set-ADDomainMode -DomainMode Windows2012r2Domain
   (Get-ADDomain).DomainMode
   ```

2. You really only need the two Set- commands, I just put the others to see the before and after => look at the properties before and after you change them!