---
title: 'Linux Live CD's'
date: 2016-05-28T06:27:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/linux-live-cds/
categories:
  - Linux
  - SysAdmin
tags:
  - Pre-Boot
---
<!--more-->

### Description:

Not sure why it took me so long to post this but one of my favorite things to do in the pre-boot environment is to launch linux live CD's.

### To Resolve:

1. First, from within Windows download [Xboot](https://sites.google.com/site/shamurxboot/).

2. Next, download your favorite ISO's to load on there:

   - I recommend [Hirens Boot CD](http://www.hirensbootcd.org/download/) => To reset Windows passwords, boot and nuke, etc.

   - Almost any [Linux distro](https://www.linux.com/learn/five-best-linux-live-cds) you want will have a &#8220;Live CD&#8221; environment where it loads to a desktop where you can browse your Windows disk. This can be the pre-stage for the [Sticky keys trick](https://automationadmin.com/2016/05/reset-windows-password/) or just a way to get data from a Windows drive. I recommend [TailsOS](https://tails.boum.org/) for security.

   - This is also a chance to load your backup software &#8220;boot disk&#8221; that many come with. For example, Paragon has [this](https://www.paragon-software.com/home/rk-free/) one.

3. From here you can create an &#8220;iso image&#8221; that you can then use later or go straight to USB. If you choose the iso for later, you can use tools such as [Rufus](https://rufus.akeo.ie/) or [Yumi](http://www.pendrivelinux.com/yumi-multiboot-usb-creator/) to boot your computer from.

4. In order to boot from a USB, you usually have to press `F12` on boot or whatever &#8220;One time boot menu&#8221; shortcut the hardware vendor implements. It's `F12` for Dell computers.