---
title: 'Best Practice: DNS Settings On Domain Controllers'
date: 2018-04-01T06:38:20+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/best-practice-dns-settings-on-domain-controllers/
tags:
  - Networking
  - SysAdmin
  - WindowsServer
---
<!--more-->

### Description:

Quick post on the current best practice for Domain Controllers.  


### To Resolve:

1. First, never ever just have one DC. If you have to, install a second one on a workstation => no reason to ever have only one.

2. Example setup with 3 Domain Controllers (example: DC1 holds all FSMO roles):

   - DC1 Settings:
     - Primary DNS => DC2  
     - Secondary DNS => DC3  
     - Tertiary DNS => 127.0.0.1

   - DC2 Settings: 
     - Primary DNS => DC1  
     - Secondary DNS => DC3  
     - Tertiary DNS => 127.0.0.1

   - DC3 Settings:
     - Primary DNS => DC1  
     - Secondary DNS => DC2  
     - Tertiary DNS => 127.0.0.1