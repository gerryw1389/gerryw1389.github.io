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

1. Make sure to leave the default domain policy (just like in AD) as policy number 2 and create your own organizational policy as policy 1.
   - To do this:

   - Identities => Networks => Look under Primary Policy => (Policy Name)

   - Once inside that, just go through the wizard to select your options
   <img class="alignnone size-full wp-image-4518" src="https://automationadmin.com/assets/images/uploads/2017/07/opendns.png" alt="" width="1484" height="518" srcset="https://automationadmin.com/assets/images/uploads/2017/07/opendns.png 1484w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-300x105.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-768x268.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-1024x357.png 1024w" sizes="(max-width: 1484px) 100vw, 1484px" />
   <img class="alignnone size-full wp-image-4519" src="https://automationadmin.com/assets/images/uploads/2017/07/opendns-2.png" alt="" width="1496" height="530" srcset="https://automationadmin.com/assets/images/uploads/2017/07/opendns-2.png 1496w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-2-300x106.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-2-768x272.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-2-1024x363.png 1024w" sizes="(max-width: 1496px) 100vw, 1496px" />

   - You will need to edit the &#8220;Category Setting to enforce&#8221;
   <img class="alignnone size-full wp-image-4520" src="https://automationadmin.com/assets/images/uploads/2017/07/opendns-3.png" alt="" width="1126" height="612" srcset="https://automationadmin.com/assets/images/uploads/2017/07/opendns-3.png 1126w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-3-300x163.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-3-768x417.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-3-1024x557.png 1024w" sizes="(max-width: 1126px) 100vw, 1126px" />

   - You will need to edit the &#8220;Security Setting to enforce&#8221;
   <img class="alignnone size-full wp-image-4521" src="https://automationadmin.com/assets/images/uploads/2017/07/opendns-4.png" alt="" width="1126" height="748" srcset="https://automationadmin.com/assets/images/uploads/2017/07/opendns-4.png 1126w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-4-300x199.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-4-768x510.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-4-1024x680.png 1024w" sizes="(max-width: 1126px) 100vw, 1126px" />

   - Additionally, you may want to add your own sites to the &#8220;Global Block List&#8221;
   <img class="alignnone size-full wp-image-4522" src="https://automationadmin.com/assets/images/uploads/2017/07/opendns-5.png" alt="" width="1124" height="510" srcset="https://automationadmin.com/assets/images/uploads/2017/07/opendns-5.png 1124w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-5-300x136.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-5-768x348.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-5-1024x465.png 1024w" sizes="(max-width: 1124px) 100vw, 1124px" />
   Block Page Settings
   <img class="alignnone size-full wp-image-4523" src="https://automationadmin.com/assets/images/uploads/2017/07/opendns-6.png" alt="" width="1468" height="512" srcset="https://automationadmin.com/assets/images/uploads/2017/07/opendns-6.png 1468w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-6-300x105.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-6-768x268.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-6-1024x357.png 1024w" sizes="(max-width: 1468px) 100vw, 1468px" />
   Details
   <img class="alignnone size-full wp-image-4524" src="https://automationadmin.com/assets/images/uploads/2017/07/opendns-7.png" alt="" width="1472" height="518" srcset="https://automationadmin.com/assets/images/uploads/2017/07/opendns-7.png 1472w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-7-300x106.png 300w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-7-768x270.png 768w, https://automationadmin.com/assets/images/uploads/2017/07/opendns-7-1024x360.png 1024w" sizes="(max-width: 1472px) 100vw, 1472px" />
