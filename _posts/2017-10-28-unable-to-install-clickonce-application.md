---
title: Unable To Install ClickOnce Application
date: 2017-10-28T05:48:10+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/10/unable-to-install-clickonce-application/
categories:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

The user will be trying to install a ClickOnce Application and will be getting a message like `Your security settings do not allow this application...`  

   <img class="alignnone size-full wp-image-4770" src="https://automationadmin.com/assets/images/uploads/2017/10/unable-to-install-click-once.png" alt="" width="672" height="410" srcset="https://automationadmin.com/assets/images/uploads/2017/10/unable-to-install-click-once.png 672w, https://automationadmin.com/assets/images/uploads/2017/10/unable-to-install-click-once-300x183.png 300w" sizes="(max-width: 672px) 100vw, 672px" /> 

### To Resolve:

1. `Regedit` => `HKLM\SOFTWARE\MICROSOFT\.NETFramework\Security\TrustManager‌​\PromptingLevel\Inte‌​rnet` => Set to `Enabled`

2. This is caused by the [Click Once Trust Prompt Behavior](https://msdn.microsoft.com/en-us/library/ee308453.aspx)
