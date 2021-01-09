---
title: 'Resetting A Domain Users Password'
date: 2016-05-29T04:06:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/resetting-a-domain-users-password/
categories:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

A user will need their password reset for whatever reason.

### To Resolve:

1. On the DC, open up ADUC (Active Directory Users and Computers), locate the user in the their OU, right click &#8220;reset password&#8221;.

2. Note you go to the same place if the user's account is locked. You just right click on their name => Properties => Uncheck the &#8220;Account is Locked&#8221; checkbox.