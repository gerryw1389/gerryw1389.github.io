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

I recently updated my [About](https://automationadmin.com/about/) page to stress the importance of [automation](https://www.reddit.com/r/sysadmin/comments/cdlar7/psa_still_not_automating_still_at_risk/). Unfortunately, although tools like Power Automate exist where you can use a GUI to manipulate things, you will still need to [learn to code](https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/) on some level in order to automate. If you come from a sysadmin background you thankfully will not need to know how to code entire applications, but instead just scripts instead. I talked about this [a while back](https://automationadmin.com/2016/05/scripting-overview/) and chose my path then. I like to say that scripting/coding is `what separates the boys from the men` in IT because every position I have seen the scripter's excel and move upwards while the ones that stick to GUI usually stagnate (which may be fine with them, I'm not hating. Not everyone wants to win the [rat race](https://en.wikipedia.org/wiki/Rat_race) ) . Here are my reasons for learning scripting:

### To Resolve

1. I'm a fan of levels when it comes to my career. i.e. you start here and work you way up.

   - Devops => [devops.sh](https://roadmap.sh/devops) - I share this reference often and find it a good visual to how to progress in IT if you wish to keep climbing upwards. There is no doubt that Devops/SRE's are the top of talent in IT right now unless you go full stack developer according to [levels.fyi](https://www.levels.fyi/Salaries/Software-Engineer/Site-Reliability/)
   - SysAdmin => [Reddits bootcamp is a good start](https://www.reddit.com/r/sysadmin/wiki/bootcamp/)

1. So why scripting? What does it matter?

   - The common theme is that for Windows or for linux, everytime you do something in the GUI there exists a hidden way you can do it via script.
   - The reason for wanting to do it via script is that you can have a server or some other automation run the task for you when your sleeping, or at certain intervals, or anytime and always get repeatable actions since computer don't make mistakes like humans do.
   - Another reason I like scripting is that once you learn your first language, all the others are similar (assuming you go object oriented language). In other words, every langauge I have learned had variables, loops, conditional logic, ect. and I expect any language I learn in the future will as well. Even languages that arent object oriented like Bash are quick to learn if you start with python or powershell.

1. What you should want to do if you are in a position that doesn't require leveling up is to [ask the community](https://www.reddit.com/r/sysadmin/comments/e0texd/im_feeling_like_a_dinosaur/) ( also [this post](https://www.reddit.com/r/devops/comments/euyzk6/how_to_move_to_using_infrastructure_as_code/) ) of ways to improve if you get stuck. Take their responses and try to implement in your organization or look for a new job if it's not possible.

1. In addition, every six months set a reminder to go browse job listings and look for the position you want and start learning. It's no surprise that many position want similar things for similar titles. For example:

   - Containers: `Docker`, `Podman`
   - Container Management: `Kubernetes`, `Docker Swarm`
   - Infrastructure as Code (IaC): `terraform`, `pulumi`
   - Scripting: `python`, `powershell`, `bash`
   - Config Management: `Ansible`, `Puppet`, `Salt Stack`
   - Continuous Integration/ Continuous Deployment: `Github Actions`, `Azure Devops`, `Gitlab`

1. So again, why scripting? I'm seeing Docker, Kubernetes, Github Actions, ect and none of these use scripting? Well the answer is that these tools are built on top of scripting. For example, `terraform` is compiled from `golang`, CI/CD pipelines usually run scripts that call executables in a specific order, and Kubernetes and Docker are automated deployment of applications that started back in the day with powershell/bash scripts locally on servers.

   - Since markets tend to centralize (cloud) and decentralize (on-prem) in cycles, there is a high chance that eventually automation will move back on-prem again in the coming years. Usually companies like AWS and Azure will have good pricing to get companies in their environment and then rise the prices once they have them captured. Many enterprises will take years to move back on-prem once locked in and they know this.
   - Nonetheless, there will most likely be a time that we go back on-prem.
   - Well, instead of going back to Vcenter with Virtual machines running all your services, you can instead have [Azure Stack Hub](https://azure.microsoft.com/en-us/products/azure-stack/hub/#overview) with all the cloud services running on-prem and you can still use Terraform/CICD/powershell/python/ect tools as well so the idea is that scripting will always be useful.
   - Worst case scenario, you can always build "script servers" that use Powershell/Python/Golang ect to run automation on a schedule using crontab/Scheduled Task or self host Gitlab and a Jenkins servers to deploy automation on-premise with every commit to a repo so your options are never limited. :)