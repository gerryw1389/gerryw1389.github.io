---
title: Bash Pipeline Tasks
date: 2022-04-03T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/04/bash-pipeline-tasks
tags:
  - Azure
  - AzureDevops
tags:
  - Bash
---
<!--more-->

### Description:

So this post will be a basic primer on different tasks you can do using just bash scripts during image builds. Mostly just different ways to use the [Bash@3](https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/bash?view=azure-devops) task of Azure Devops.

So let's say you want to create a company Ubuntu image and upload it to an image gallery for your users to pull and use, here are the steps you can go through to do this.

### To Resolve:

1. In general, these are the steps to build a generalized VM from an image and upload to the gallery:

   - Start with [az login](https://docs.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-login) using service principle and passing secrets from Keyvault using the Libraries feature in Azure Devops.
   - Do an [az vm create](https://docs.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-create)
   - Pass a series of `az vm run-command invoke --name "$(vmName)" --resoure-group $(resource_group) --command-id RunShellScript --scripts @./scripts/myscript.sh` type commands
   - Next, run an [az vm deallocate](https://docs.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-deallocate)
   - Then [az vm generalize](https://docs.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-generalize)
   - Then [az image create](https://docs.microsoft.com/en-us/cli/azure/image?view=azure-cli-latest#az-image-create), see example `az image create -g MyResourceGroup -n image1 --source MyVm1`
   - Now delete all the resources:
      - [az vm delete](https://docs.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-delete)
      - [az disk delete](https://docs.microsoft.com/en-us/cli/azure/disk?view=azure-cli-latest#az-disk-delete)
      - [az network nic delete](https://docs.microsoft.com/en-us/cli/azure/network/nic?view=azure-cli-latest#az-network-nic-delete)
      - And if you create a NSG at the NIC level, [az network nsg delete](https://docs.microsoft.com/en-us/cli/azure/network/nsg?view=azure-cli-latest#az-network-nsg-delete)

1. Inside the `myscript.sh` file, you can use bash to setup your VM to your hearts desire:

   ```shell

   # Set file contents
   cat > /home/gerry/txt.txt << 'endmsg'
   something
   something else
   endmsg

   # Set file contents a different way; These are called here-docs, see https://stackoverflow.com/questions/2953081/how-can-i-write-a-heredoc-to-a-file-in-bash-script
   cat << EOF < /somefile
   blah
   blah2
   EOF

   # Search for package and install if not present
   if [ `rpm -qa | grep -i myPackage | wc -l` == 0 ]; then wget "b" -o some/file; chmod 700 somefile; ./somefile; fi

   # Enable a service
   systemctl enable myservice || true

   # check number of files in dir
   filecount = (ls -1 /somepath | wc -l)

   # reboot in one minute
   atd
   echo "init 6" | at now +1 minute

   # clear a file
   cat /dev/null > /root/.bash_history

   # Overwrite one line
   sed -i 's/^#X11 use localhost.*/X11 use localhost yes/' /some/file

   # Setup python3 as default python
   yum install python3
   python3 -m pip install --upgrade pip
   python3 -V; alternatives --set python /usr/bin/python3; python -V

   ```

1. You can then add sleep steps and can test your VM while it is being built by passing in a public key during image build. Here is a limited example:

   ```yaml
   name: ubuntu-image-builder-$(Date:yyyy-MM-dd-HH-mm-ss)
   trigger: none # `main` for ci

   jobs:
      - job: build-image
      continueonerror: false
      pool:
         - name: 'default'
         - demands: agent.os -equals linux
      steps:
         - task: Bash@3
         displayname: BuildVM
         inputs:
            targetType: 'filePath'
            filePath: './scripts/build.sh'  
         - task: Bash@3
         displayname: sleep
         inputs:
            targetType: 'inline'
            script: 'echo "sleeping for 5 seconds..."; sleep 5'        
         - task: Bash@3
         displayname: Configure Settings
         inputs:
            targetType: 'inline'
            script: az vm run-command invoke --name "$(vmName)" --resoure-group $(resource_group) --command-id RunShellScript --scripts @./scripts/mysettings.sh    
   ```

1. Lastly, to update a variable while running scripts, read [the docs](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/set-variables-scripts?view=azure-devops&tabs=bash) but essentially in your script create a line like `echo "##vso[task.setvariable variable=vmName]$vmName"` for example to update a VM Name before it moves to another task. This is useful as you may have initial variables configured at the top of the pipeline that you then want passed down to each task and updated along the way.

1. After creating a build pipleline that creates an image, you should then create a release pipeline that pulls the image down, builds a VM, runs some tests to ensure it has the latest copies of things, and then deletes the VM. You could also include these steps in your build pipeline as a way of unit testing.