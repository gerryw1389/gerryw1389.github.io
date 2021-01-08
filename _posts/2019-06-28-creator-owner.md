---
title: Set Creator Owner To Full Control
date: 2019-08-10T23:03:25-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/creator-owner/
categories:
  - Windows
---
<!--more-->

### Description:

So the other day I was working on something where, in AD, we had to set the `creator owner` permissions to full control. Here are the steps I did to complete this:

### To Resolve:

1. Disable inheritence

2. Remove all inherited permissions

   ![creator-owner-1](https://automationadmin.com/assets/images/uploads/2019/06/creator-owner-1.png){:class="img-responsive"}

3. Reset to default

4. Set 'Self' to full control

5. Exit out completely

6. Go back and set Creator Owner to full control - it will clear in the GUI

7. Go to advanced settings and it shows full control

   ![creator-owner-2](https://automationadmin.com/assets/images/uploads/2019/06/creator-owner-2.png){:class="img-responsive"}
