---
title: Use Powershell To Get Weather Using Wttr.in
date: 2017-12-24T05:29:19+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/use-powershell-to-get-weather-using-wttr-in/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

Wttr.in has a neat API for the site that generates cmdline views of weather for your city. I especially like the moon phases as well.

Note: This doesn't always play well with the ISE, it's best to just put it in a ps1 function and call it that way.

<img class="alignnone size-full wp-image-4916" src="https://automationadmin.com/assets/images/uploads/2017/12/get-weather-1.jpg" alt="" width="1255" height="858" srcset="https://automationadmin.com/assets/images/uploads/2017/12/get-weather-1.jpg 1255w, https://automationadmin.com/assets/images/uploads/2017/12/get-weather-1-300x205.jpg 300w, https://automationadmin.com/assets/images/uploads/2017/12/get-weather-1-768x525.jpg 768w, https://automationadmin.com/assets/images/uploads/2017/12/get-weather-1-1024x700.jpg 1024w" sizes="(max-width: 1255px) 100vw, 1255px" /> 

<img class="alignnone size-full wp-image-4915" src="https://automationadmin.com/assets/images/uploads/2017/12/get-weather-2.jpg" alt="" width="1220" height="602" srcset="https://automationadmin.com/assets/images/uploads/2017/12/get-weather-2.jpg 1220w, https://automationadmin.com/assets/images/uploads/2017/12/get-weather-2-300x148.jpg 300w, https://automationadmin.com/assets/images/uploads/2017/12/get-weather-2-768x379.jpg 768w, https://automationadmin.com/assets/images/uploads/2017/12/get-weather-2-1024x505.jpg 1024w" sizes="(max-width: 1220px) 100vw, 1220px" /> 

### To Resolve:

1. Function - [Get-Weather](https://github.com/gerryw1389/powershell/blob/main/gwMisc/Public/Get-Weather.ps1)