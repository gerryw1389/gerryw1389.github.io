---
title: 'MS Outlook: Enter Network Password Message'
date: 2016-05-23T18:18:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ms-outlook-enter-network-password-message/
categories:
  - LocalSoftware
tags:
  - MSOffice
  - Regedit
---
<!--more-->

### Description:

Each time you use Microsoft Office Outlook 2007 to connect to your POP3 e-mail account, you might be prompted for a password even if you specified that your password should be saved in your password list. The two main causes for this is your password is incorrect/ changed or you saved your password but the registry contains incorrect information for the Protected Storage System Provider subkey for the user account.

### To Resolve:

1. Update your password by entering the password in the field listed.

2. Run => regedit => HKEY_CURRENT_USER\Software\Microsoft\Protected Storage System Provider. Export and save as .reg. Then delete all sub keys under here. DO NOT delete the main &#8220;Protected Storage System Provider&#8221; key.