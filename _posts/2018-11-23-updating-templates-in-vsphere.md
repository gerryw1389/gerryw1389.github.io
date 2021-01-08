---
title: Updating Templates In vSphere
date: 2018-11-23T16:29:06+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/11/updating-templates-in-vsphere/
categories:
  - LocalSoftware
tags:
  - VirtualizationSoftware
---
<!--more-->

### Description:

Follow these steps to update a template in vSphere.

### To Resolve:

1. In vSphere, right click the template to &#8220;Convert to Virtual Machine&#8221;

2. Do changes => Install updates, push over new scripts, whatever changes you need done to the template.

3. When done, just right click &#8220;Convert to Template&#8221;.It's really is that easy.

4. But lets say you have a Server 2016 / SQL 2014 template and you want to make a Server 2016 / SQL 2016. You would follow similar steps:

   - Clone the Server16SQl14 template to a new template and give the clone an name like Server16SQL16.
   - Convert the new Server16SQL16 template into a temporary test VM.
   - Setup SQL Server install files or whatever changes you need from SQL 14 to SQl 16.
   - Convert back to a template.