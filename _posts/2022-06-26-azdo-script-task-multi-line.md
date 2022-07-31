---
title: 'AZDO: Script Task Multiline'
date: 2022-06-26T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/06/azdo-script-task-multi-line
categories:
  - WebSoftware
tags:
  - CICD
---
<!--more-->

### Description:

Follow these steps to set your scripts to be multiline if you use a Windows build agent or a linux build agent. More info can be found [here](https://docs.microsoft.com/en-us/azure/devops/pipelines/scripts/cross-platform-scripting?view=azure-devops&tabs=yaml). Post was inspired by [this](https://stackoverflow.com/questions/59198459/how-to-break-a-single-command-inside-a-script-step-on-multiple-lines) and tested to confirm.

### To Resolve:

1. As mentioned in the article in the description, the easiest fix is to just target the `bash` task regardless of what your agent is. Then it will work on Windows or linux. 

   ```yaml
   - task: Bash@3
      displayName: "terraform init"
      inputs:
         targetType: inline
         failOnStderr: true
         script: |
            terraform init -backend-config="access_key=$(my-key)"
   - task: Bash@3
      displayName: "terraform validate"
      inputs:
         targetType: inline
         failOnStderr: true
         script: |
            terraform validate
   - task: Bash@3
      displayName: "terraform plan"
      inputs:
         targetType: inline
         failOnStderr: true
         script: |
            set TF_LOG=ERROR
            set TF_LOG_PATH=$(Build.ArtifactStagingDirectory)\crash.log
            set
            terraform plan \
               -var="subscription_id=$(myvar1_value)" \
               -var="tenant_id=$(myvar2_value)" \
               -var="client_id=$(myvar3_value)" \
               -var="client_secret=$(myvar4_value)" \
               -var="region=westus" \
               -out "tf.plan"
   ```

1. For Windows build agents specifically, use the `^` character which is line continuation for batch scripts:

   ```yaml
   - script: |
         terraform plan ^
         -var="subscription_id=$(myvar1_value)" ^
         -var="tenant_id=$(myvar2_value)" ^
         -var="client_id=$(myvar3_value)" ^
         -var="client_secret=$(myvar4_value)" ^
         -var="region=westus" ^
         -out "tf.plan"
      displayName: 'terraform plan'
   ```

1. For linux build agents specifically, use the `\` character which is line continuation for bash scripts:

   ```yaml
   - script: |
      set TF_LOG=ERROR
      set TF_LOG_PATH=$(Build.ArtifactStagingDirectory)\crash.log
      set
      terraform plan \
         -var="subscription_id=$(myvar1_value)" \
         -var="tenant_id=$(myvar2_value)" \
         -var="client_id=$(myvar3_value)" \
         -var="client_secret=$(myvar4_value)" \
         -var="region=westus" \
         -out "tf.plan"
     displayName: 'terraform plan'
   ```