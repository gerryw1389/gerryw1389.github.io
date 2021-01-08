---
title: IDM Reset Universal Password
date: 2019-10-07T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/10/idm-reset-universal-password
categories:
  - LocalSoftware
---
<!--more-->

### Description:

[Netiq Identity Manager](https://www.microfocus.com/en-us/products/netiq-identity-manager/overview)is a LDAP based directory software. In this example, I want to reset a universal password for a user.

### To Resolve:

1. Sign into web GUI of iManager => Objects

2. Go to the search tab => type `name = *AccountNameYouWantToReset` => click Search

3. When the account shows up, choose 'Reset Universal Password' (not 'reset password' as you might think)

4. After some time, all systems downstream should now use the new password.