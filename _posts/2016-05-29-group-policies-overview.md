---
title: Group Policies Overview
date: 2016-05-29T04:13:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/group-policies-overview/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

GPO's or Group Policy Objects are rules that are passed from a domain controller to all computers that are attached to that domain. Administrators use these often and for various reasons, the most common is to protect users from themselves or viruses while working on their computers. Workstation's can see what policies are currently applied to them by running `rsop.msc` (newer version is `gpresult /h c:\scripts\result.html`) and get new policies automatically or by running `gpudate /force`.

### To Resolve:

1. Check out [this MS article](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects) for more information.