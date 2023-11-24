---
title: Barracuda High Alert Message
date: 2016-05-21T05:05:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/barracuda-high-alert-message/
tags:
  - Hardware
---
<!--more-->

### Description:

You will get an email saying Barracuda has a &#8220;HighAlertInQueue&#8221;. This means someone sent a mass email or something got bogged down.

### To Resolve:

1. Login to Barracuda and on the main status page towards the top right, there will be a label called &#8220;In/Out Queue Size&#8221; with a number (ex: 0/17). This should be red which generates the alert. Just monitor it for a minute and see if the number is going down.

2. If the number still does not go down, reboot the Barracuda device. Go to Basic => Administration => Restart (at the bottom)

3. If it is STILL slow, login to &#8220;YourMailServer&#8221; and restart the services associated with your email server application. Reboot the mail server if you still have issues.