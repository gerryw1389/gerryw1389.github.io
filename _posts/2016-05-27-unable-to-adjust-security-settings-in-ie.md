---
title: Unable To Adjust Security Settings In IE
date: 2016-05-27T22:16:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/unable-to-adjust-security-settings-in-ie/
tags:
  - Windows
---
<!--more-->

### Description:

Inside of the Internet Properties box, you cannot drag the bar down or change anything. This is because &#8220;IE Enhanced Security&#8221; has been installed. This is only found on Server OS's or computers connected to a domain.

### To Resolve:

1. To uninstall it:

   - For Server 03/ XP: [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `appwiz.cpl` => uncheck it in Add/ Remove Windows Components.
   - For Server 08/ W7: Start => Server Manager => Configure IE ESC- Disable both options.