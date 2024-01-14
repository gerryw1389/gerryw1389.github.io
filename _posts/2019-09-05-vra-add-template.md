---
title: VRA Add Template
date: 2019-09-05T09:00:44-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/09/vra-add-template/
tags:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:
VRA or Vrealize Automation is a designer software where you build a form that is called a Blueprint that users will go to and fill out. This form, once completed allows your infrastructure to deploy VM's at the push of a button. It does this by using Vrealize Orchestrator in the background to run workflows which then tie into multiple systems like Vcenter, SQL servers, IPAM, etc. If your company has a huge VMWare presence, it is fully worth investing your time into learning how this works because it can not only provision a server, but it can decom a server, rename a server, etc. This software can also connect your organization to AWS/Google Cloud/Azure so that your users can have a single form that provisions where ever you want.

Follow this post to add a new Vcenter Template as one you can deploy with VRA:

### To Resolve:

1. Create a new template in vSphere

2. In VRA, update collections:
   - Infrastructure – Infrastructure – Compute Resources – Data Collection on $yourVcenter
   - Now go to Administration, Property Dictionary – Component Profiles
   - Image – Edit – Go to Value Sets – Add
   - Copy the customization specs to your clipboard

3. Create a new one by giving it:
   - A name
   - Change Action to 'Clone'
   - Change Provisioning workflow to 'CloneWorkflow'
   - Change clone from to your template
   - Note: If the template hasn't shown up here, try updating the collections again. Sometimes if you just converted a VM to a template, this will take a few runs before it works again.
	- Change customization spec to the Windows one if a Windows VM and Linux one if a linux VM.

4. Now go to Design – Select your blueprint – Edit – Profiles – Check the box – Then add them as a selection in your dropdown in your custom form.

5. Now click 'Edit Form' and select 'What is the OS?' (for example) – Enter the value as: `(name | display)`. See [VRA Forms](https://automationadmin.com/2019/09/vra-forms/) if this part is confusing.

