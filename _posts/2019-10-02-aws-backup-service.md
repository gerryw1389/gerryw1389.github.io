---
title: AWS Backup Service
date: 2019-10-02T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/10/aws-backup-service
categories:
  - WebSoftware
tags:
  - Cloud
---
<!--more-->

### Description:

Follow this guide to auto backup certain instances in AWS.

### To Resolve:

1. Go to instance and get the EBS Volume, I copied them to a notepad++ document

2. Type in 'Backup' and create a backup plan

   - Create backup plan = 'Default-Backup'
   - Backup Rule = Template - Daily 35 day rotation (why not? Choose whatever template you want)
   - Resource Assignments = Make up a name, I choose 'domain-controllers' and choose the option for AWS to assign an IAM role, I called it 'Default'
   - Now, under resources, hit the dropdown and choose 'Resource ID' in the first column, 'EBS' in the second column, and copy/paste the Volume ID for the third - column from step 1. 
   - Do this repeatedly for all volumes.
