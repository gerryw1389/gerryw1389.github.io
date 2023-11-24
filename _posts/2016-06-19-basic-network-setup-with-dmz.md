---
title: Basic Network Setup With DMZ
date: 2016-06-19T07:44:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/basic-network-setup-with-dmz/
tags:
  - Networking
tags:
  - Router
  - Setup
---
<!--more-->

### Description:

When configuring a network from the ground up, it is common practice to follow these steps:

### To Resolve:

1. You need to configure 4 parts of your network:

WAN => The Internet.

The DMZ => This is where all packets from the internet go.

The Protected DMZ => This is a layer of the network where only protected traffic orginating from a DMZ address can enter through on specific ports

LAN => Internal network

<img class="aligncenter wp-image-645 size-full" src="https://automationadmin.com/assets/images/uploads/2016/09/dmz.png" alt="dmz" width="569" height="427" srcset="https://automationadmin.com/assets/images/uploads/2016/09/dmz.png 569w, https://automationadmin.com/assets/images/uploads/2016/09/dmz-300x225.png 300w" sizes="(max-width: 569px) 100vw, 569px" /> 

2. As a systems administrator you will often be asked to place servers on the internet for clients to be able to access. The first thing you need to do is determine if a VPN would be better instead since very few applications need direct access for ANYONE to use. Assuming you have already tried this, move to the next step.

3. All you would need to do is configure access rules in your firewall:

*If the source is from the internet, make sure only specific ports are open and disable domain logins (local accounts only)

*If the source is from the DMZ, open the required ports for the application to access the Protected DMZ nodes.