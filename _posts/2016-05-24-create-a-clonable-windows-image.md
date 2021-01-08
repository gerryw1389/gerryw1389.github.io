---
title: Create A Clonable Windows Image
date: 2016-05-24T13:50:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/create-a-clonable-windows-image/
categories:
  - LocalSoftware
tags:
  - VirtualizationSoftware
---
<!--more-->

### Description:

While creating VMs in Virtual Box is an easy task, Windows will want their money for each install you do. Follow these steps to bypass activation for VMs NOT TO BE USED IN PRODUCTION.

Disclaimer: I will use the same one in the article&#8230; Please do not use this for your production environment, separate windows licenses must be purchased on production usage. This is only for the local test environment and temporary usage.

### To Resolve:

1. Create a new VirtualBox VM for Windows 2008 R2 or Windows 7

2. Before installing the Windows 2008 R2 or Windows 7 OS from ISO image, open the newly created *.vbox file with any text editor. Look for the machine UUID and copy the value without brackets.

3. Go to any [online UUID generation](https://www.guidgenerator.com/) website and create a new UUID.

4. Run the following command, where first UUID is the machine UUID, the second UUID is the one generated from one of the above website:

&#8220;C:Program FilesOracleVirtualBoxvboxmanage&#8221; modifyvm 69310832-0890-4f83-9e9f-72f978818f6c =>hardwareuuid b93ff710-28ee-11e1-bfc2-0800200c9a66

5. The *.vbox file should have the newly added hardware UUID.

6. Now, start to install the Windows 2008 R2 or Windows 7 on the new VM. After installation complete, activate the windows. When clone based on the activated Windows VM, there is no need to reactivate again, because the same hardware UUID will be cloned into new Windows VM which the activation depend on.

### References:

["Practical Programming and Architecture "](http://luchen1021.blogspot.com/2011/12/create-cloneable-virtualbox-vm-without.html)