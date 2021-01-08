---
title: VRA Create Test Blueprint
date: 2019-09-05T10:00:44-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/09/vra-create-test-blueprint/
categories:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:
VRA or Vrealize Automation is a designer software where you build a form that is called a Blueprint that users will go to and fill out. This form, once completed allows your infrastructure to deploy VM's at the push of a button. It does this by using Vrealize Orchestrator in the background to run workflows which then tie into multiple systems like Vcenter, SQL servers, IPAM, ect. If your company has a huge VMWare presence, it is fully worth investing your time into learning how this works because it can not only provision a server, but it can decom a server, rename a server, ect. This software can also connect your organization to AWS/Google Cloud/Azure so that your users can have a single form that provisions where ever you want.

This post will go over how to create a test blueprint aside from your production one that you can use to test changes without affecting production blueprints.

### To Resolve:

1. Go to Design – Select the blueprint – Select Copy – Then give it a unique name

2. On the original blueprint, go to Custom Form – Edit – Click Actions at the top and Export as YML

3. Edit your new form for your new blueprint and you will see it is blank.

4. Drag and drop one of the unique properties like `Company.Servername` and take note of the `field ID`

5. Take your YML file and do a find and replace so that it matches the new form as opposed to the original form.
   - So it may have been `CompanyTest.ServerName` and now it will be `CompanyTest2.ServerName`.

6. Import the YML file by going to the form and choosing Actions – Import YML.

7. Activate the form by selecting the radio button on the top right.

8. Make the blueprint viewable in the catalog.

9. Go to edit – Select the blueprint – Select publish.

10. Go to Administration – Catalog Maangement – Catalog Items – Select your item – Activate – and then choose Service – IaaS.