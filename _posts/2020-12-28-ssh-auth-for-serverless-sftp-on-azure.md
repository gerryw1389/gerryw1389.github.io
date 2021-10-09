---
title: SSH Key Auth For Serverless SFTP On Azure Containers
date: 2020-12-28T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/ssh-auth-for-serverless-sftp-on-azure
categories:
  - Azure
  - Linux
tags:
  - Cloud
  - Azure-ContainerInstances
---
<!--more-->

### Description:

This post is a variation of my [previous post](https://automationadmin.com/2020/11/azure-serverless-sftp) about serverless SFTP on Azure. What this does is allow you to run Container Instances that mount two file shares - one for actual storage and another that mounts ssh keys per [this issue](https://github.com/Azure-Samples/sftp-creation-template/issues/2). Source is maintained at Github [here](https://github.com/gerryw1389/terraform-examples/tree/main/container-groups/serverless-sftp-ssh-auth).

The way to use is:

- Download from my Github
- Replace `p.json` with your info. Replace `run.ps1` with your info. Look over `t.json` but I'm sure you don't have to change anything in there.
- Upload to your Azure Cloud Storage by going to portal.azure.com => Click on powershell icon => Once you sign in => `cd ./clouddrive/yourname` and then upload all three files into a folder
- Then run `./run.ps1` and it will deploy the containers
- Go to Azure Container Instances to see the result!

### To Resolve:

1. So before offering this service to users in my company, I tested on my machine first. On my Windows computer, I ran the following to create a key pair: `ssh-keygen -t rsa -b 4096 -f ssh_host_rsa_key | Out-Null`

2. Upload public key to file storage. You can use the [Storage Explorer](https://azure.microsoft.com/en-us/features/storage-explorer/) app or go to portal.azure.com => Type storage accounts => Your storage account => File Shares => Upload the key file there.

3. Test:

   - First I used WinSCP GUI and filled in hostname, username, then clicked Advanced => Key Auth => Point to private key => It then tells you it will convert it to Putty format `.ppk` => Select 'yes' and okay.

   - That worked perfectly! Next, I used command line:

   ```shell
   [C:\scripts]
   > sftp -i "C:\path\to\private\key\ssh_host_rsa_key" user@dnslabel.southcentralus.azurecontainer.io
   connected to user@dnslabel.southcentralus.azurecontainer.io.
   sftp> exit
   [C:\scripts]
   >   
   ```

   - Worked again!

4. So now I had someone try and do it from an older RHEL 6 box:

   - First, upload their public key to the correct SSH Keys container and restarted the container group

   - Then they ran:

   ```shell
   sudo serviceAccount
   sftp -F ~/.ssh/config.sftp user@dnslabel.southcentralus.azurecontainer.io
   connected to user@dnslabel.southcentralus.azurecontainer.io.
   sftp> exit
   ```

   - Where the file `.ssh/config.sftp` looked like:

   ```shell
   Host dnslabel.southcentralus.azurecontainer.io
   User user
   IdentityFile /home/serviceAccount/.ssh/id_rsa
   ```

   - Identity file should be the private key

   - Also, the biggest drawback of containers is that their host key changes every time they reboot, so on each client device I usually set:

   ```shell
   Host dnslabel.southcentralus.azurecontainer.io
      StrictHostKeyChecking no
      UserKnownHostsFile=/dev/null
   ```

   - For all users in `/etc/ssh/ssh_config` or just the current user in `~/.ssh/config`

   - Not sure if needed, but from command line try something like:

   ```shell
   # SSH
   ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no  user@dnslabel.southcentralus.azurecontainer.io
   # SCP
   scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no somefile.txt user@dnslabel.southcentralus.azurecontainer.io:/var/tmp/
   ```
