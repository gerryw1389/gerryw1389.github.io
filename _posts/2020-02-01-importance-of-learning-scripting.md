---
title: 'Importance Of Learning Scripting'
date: 2020-02-01T08:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/importance-of-learning-scripting/
categories:
  - SysAdmin
---
<!--more-->

### Description:

I recently updated my [About](https://automationadmin.com/about/) page to stress the importance of [automation](https://www.reddit.com/r/sysadmin/comments/cdlar7/psa_still_not_automating_still_at_risk/). Unfortunately, although tools like Power Automate exist where you can use a GUI to manipulate things, you will still need to [learn to code](https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/) on some level in order to automate.

### To Resolve

1. Similar to the responses [here](https://www.reddit.com/r/sysadmin/comments/e0texd/im_feeling_like_a_dinosaur/), you work your way up like so:

   - For Windows, learn to write advanced functions with Powershell
   - For Linux, learn to write python scripts and bash scripts (shell scripts)
  
2. For the config management tool (or IaC - Infrastructure as code), choose:

   - Ansible
   - Chef
   - Puppet (if needed, many have moved to more advanced products - check the dates on the forge to see what I mean)
   - Salt Stack
   - Terraform

3. Finally, learn a CI/CD tool like:

   - vRealize Orchestrator - not really a [good tool for this category](https://www.reddit.com/r/devops/comments/bwik7p/vmware_vrealize_automationorchestrator_as_a/) but sometimes you gotta play the cards you are dealt
   - Jenkins
   - Vagrant
   - Docker

4. If you are still having questions, give [this](https://www.reddit.com/r/devops/comments/euyzk6/how_to_move_to_using_infrastructure_as_code/) a read, and then browse that sub - you will get a clear picture.

