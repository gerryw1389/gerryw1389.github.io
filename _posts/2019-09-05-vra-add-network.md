---
title: VRA Add Network
date: 2019-09-05T08:00:44-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/09/vra-add-network/
tags:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:
VRA or Vrealize Automation is a designer software where you build a form that is called a Blueprint that users will go to and fill out. This form, once completed allows your infrastructure to deploy VM's at the push of a button. It does this by using Vrealize Orchestrator in the background to run workflows which then tie into multiple systems like Vcenter, SQL servers, IPAM, ect. If your company has a huge VMWare presence, it is fully worth investing your time into learning how this works because it can not only provision a server, but it can decom a server, rename a server, ect. This software can also connect your organization to AWS/Google Cloud/Azure so that your users can have a single form that provisions where ever you want.

Follow this post in order to add a network from your vCenter to VRA.

### To Resolve:

1. First, make sure that VRA can select it from Vcenter:
   - Sign into VRA and go to: Infrastructure – Infrastructure – Network Profiles
   - Create one
   - Right click – Choose New - External
   - Infrastructure – Infrastructure – Reservations – Networks – check the box and assign the profile

2. Now make sure that your Property Definitions are up-to-date with this new network
   - Go to Administration – Administration – Property Definitions – Virtual.Network.Name and add it to the list

3. Lastly, add the network to your form. For example, you may have a question for your user like 'Which Network does this VM need to reside on?'
   - Go to Design – Blueprint – Custom Form/Edit – Find the dropdown for that question and enter the value as: (network name | display). See [VRA Forms](https://automationadmin.com/2019/09/vra-forms/) if this part is confusing.
