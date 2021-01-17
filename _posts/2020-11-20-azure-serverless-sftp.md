---
title: Azure Serverless SFTP
date: 2020-11-20T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/11/azure-serverless-sftp
categories:
  - Azure
tags:
  - Azure-StorageAccounts
  - Azure-ContainerInstances
---
<!--more-->

### Description:

Following [this template](https://github.com/Azure/azure-quickstart-templates/tree/main/201-aci-sftp-files-existing-storage) I was able to create a powershell script that when ran in the portal would deploy new instances of SFTP by connecting to our storage account and creating one share per user. This works great as a one off solution to have user's send you files and each user is to have their own chroot. Source is  maintained at Github [here](https://github.com/gerryw1389/powershell/tree/main/azure/serverless-sftp).

The way to use is:

- Download from my Github
- Replace `p.json` with your info. Replace `run.ps1` with your info. Look over `t.json` but I'm sure you don't have to change anything in there.
- Upload to your Azure Cloud Storage by going to portal.azure.com => Click on powershell icon => Once you sign in => `cd ./clouddrive/yourname` and then upload all three files into a folder
- Then run `./run.ps1` and it will deploy the containers
- Go to Azure Container Instances to see the result!

### To Resolve:

1. First, create `run.ps1` in cloud shell and paste in [this](https://github.com/gerryw1389/powershell/blob/main/azure/serverless-sftp/run.ps1)

2. Create the template file `t.json` and paste in [this](https://github.com/gerryw1389/powershell/blob/main/azure/serverless-sftp/t.json)

3. Create the parameters file `p.json` and paste in [this](https://github.com/gerryw1389/powershell/blob/main/azure/serverless-sftp/p.json)

4. What I do is keep these three files in a folder, and when needed copy the folder, rename it, tweak parameters, and deploy again for each department in my org that needs a SFTP folder to upload to.
