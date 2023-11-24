---
title: 'Terraform: Deploy VM'
date: 2021-10-06T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/10/terra-deploy-vm
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description

After following ["Create Terraform Service Principle"](https://automationadmin.com/2021/10/create-terra-az-ad-app), I did the following to deploy a VM following the official guide [here](https://docs.microsoft.com/en-us/azure/developer/terraform/create-linux-virtual-machine-with-infrastructure).

### To Resolve:

1. Since cloudshell already has Terraform cli installed, I just did the following in cloudshell Bash:

   ```shell
   # first, make sure environmental vars are populated from previous steps (see reference to previous post)
   printenv | grep ^TF_VAR*

   cd clouddrive
   mkdir terra
   cd terra
   ```

2. Upload [main.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2021-10-06-terra-deploy-vm/main.tf) using the upload tool.

3. Now we just run a series of commands using terraform cli:

   ```shell
   # Init and install modules
   terraform init

   # Create a plan => Tells you what actions it will do like create resources but doesn't do it
   terraform plan -out main.tfplan

   # Apply the plan => Creates resources
   terraform apply main.tfplan
   ```

4. SSH into the VM

   ```shell
   terraform output -raw tls_private_key
   # Copy/paste to c:\scripts\key.txt

   # now open powershell and type:
   wsl
   cp /mnt/c/scripts/key.txt /home/gerry/key.txt

   mv /home/gerry/key.txt /home/gerry/mykey
   chmod 400 mykey
   # replace the IP on next step with public IP of your Ubuntu VM
   ssh -i ./mykey azureuser@13.90.207.214

   # notice I can ssh in with key and also have root access, 'sudo su' for example
   ```

5. Now that we have deployed an environment, let's tear it down to not incur any costs:

   ```shell
   terraform plan -destroy
   terraform apply -destroy
   ```

