---
title: Network Not Present Error
date: 2016-05-28T06:16:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/network-not-present-error/
categories:
  - Windows
tags:
  - FileSystem
---
<!--more-->

### Description:

You are ever trying to access another computer's shares on the network and you get an error that states &#8220;the network is not present or not started&#8221;.


### To Resolve:

1. Run => `services.msc` => Start the &#8220;Workstation&#8221; service and the &#8220;Server&#8221; service while you are at it. This allows you to view computer's resources that are shared and you have permission to see as well as allows other computer's to see the current computer's shares.