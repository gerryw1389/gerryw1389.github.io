---
title: RunDLL Windows Mail Error
date: 2016-11-15T02:56:44+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/rundll-windows-mail-error/
categories:
  - Windows
---
<!--more-->

### Description:

Inside the Control Panel, you launch the &#8220;Mail&#8221; app to configure an account and as soon as it launches => it throws a &#8220;RunDDL&#8221; error and crashes.

### To Resolve:

1. Open MS Word. Go to File => Options => Advanced. Scroll down to &#8220;display&#8221; section. Check the box that says &#8220;Disable Hardware Graphics Acceleration&#8221;

2. Try adding the account again, should work.

NOTE: The post I read said something about this being an issue with Office trying to use a dedicated graphics card and this forces it to use the motherboard integrated one, but I've seen this on many types of PC's so I'm not so sure about this explanation.