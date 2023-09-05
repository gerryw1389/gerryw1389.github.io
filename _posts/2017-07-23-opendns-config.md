---
title: OpenDNS Config
date: 2017-07-23T04:58:52+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/opendns-config/
categories:
  - Networking
tags:
  - Cloud
---
<!--more-->

### Description:

This is just a post with screenshots to complement my [first](https://automationadmin.com/2016/05/opendns/) OpenDNS post.

### To Resolve:

1. Make sure to leave the default domain policy (just like in AD) as policy number 2 and create your own organizational policy as policy 1. To do this:

   - Identities => Networks => Look under Primary Policy => (Policy Name)

   - Once inside that, just go through the wizard to select your options
   
   - ![opendns](https://automationadmin.com/assets/images/uploads/2017/07/opendns.png){:class="img-responsive"}

   - ![opendns-2](https://automationadmin.com/assets/images/uploads/2017/07/opendns-2.png){:class="img-responsive"}

1. You will need to edit the &#8220;Category Setting to enforce&#8221;

   - ![opendns-3](https://automationadmin.com/assets/images/uploads/2017/07/opendns-3.png){:class="img-responsive"}

1. You will need to edit the &#8220;Security Setting to enforce&#8221;

   - ![opendns-4](https://automationadmin.com/assets/images/uploads/2017/07/opendns-4.png){:class="img-responsive"}

1. Additionally, you may want to add your own sites to the &#8220;Global Block List&#8221;

   - ![opendns-5](https://automationadmin.com/assets/images/uploads/2017/07/opendns-5.png){:class="img-responsive"}

1. Block Page Settings

   - ![opendns-6](https://automationadmin.com/assets/images/uploads/2017/07/opendns-6.png){:class="img-responsive"}

1. Details
   - ![opendns-7](https://automationadmin.com/assets/images/uploads/2017/07/opendns-7.png){:class="img-responsive"}
