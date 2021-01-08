---
title: To Make A Domain Account A Local Admin Account
date: 2016-05-29T03:48:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/to-make-a-domain-account-a-local-admin-account/
categories:
  - Windows
---
<!--more-->

### Description:

Follow these steps to allow domain users to have local access or just to have local admin rights on their workstations.

### To Resolve:

1. Login to an account with &#8220;administrator&#8221; permissions such as the domain admin account or local admin account.

2. Run => `lusrmgr.msc` => Groups => Administrators => Right Click => Properties => Add => Domain account name (user@domain.whatever).

3. Done. Sign out and sign in to your domain account. NOTE: This works even if you have never signed in to your domain account yet.