---
title: 'AZDO: Manual Validation Task'
date: 2023-01-17T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/azdo-manual-validation
categories:
  - WedSoftware
tags:
  - CICD
---
<!--more-->

### Description:

Follow these steps to add a manual validation between terraform `plan` and `apply` in your pipeline:

### To Resolve:

1. Not show below is a job above called `terraform_build`. In that job, you just run a `terraform plan` as usual. Then you add this job below it:

   ```yaml
   - job: manual_validation
      dependsOn: terraform_build
      displayName: 'Get Validation Approval'
      continueOnError: true
      pool: server
      steps:
         - task: ManualValidation@0
         displayName: 'Validate execution plan'
         timeoutInMinutes: 120
         inputs:
            notifyUsers: my-dl@domain.com
            instructions: Please validate the execution plan and resume
            onTimeout: reject

   - job: terraform_apply
      dependsOn: 
      - terraform_build
      - manual_validation
      condition: and(eq(dependencies.terraform_build.result, 'Succeeded'), in(dependencies.manual_validation.result, 'Succeeded', 'Skipped'))
      displayName: 'NonProd_Apply'
      workspace:
         clean: all 
      timeoutInMinutes: 0
      cancelTimeoutInMinutes: 0
      pool:
         name: 'my-buildagent'
      variables:
         - group: My Secrets
      steps:
         - checkout: self
   ```

1. So the way it works is the [ManualValidation@0](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/manual-validation-v0?view=azure-pipelines) will pause the pipeline until a member from the `my-dl@domain.com` Distribution List comes in to the repo and clicks on `Resume` or `Reject`.

   - Take note that the `pool` is set to `server` instead of your private build agent.
   - Take note the `dependsOn` property is set to the `displayName` of your `terraform plan` job.
   - Take note of the `dependsOn` and `condition` of the subsequent `terraform apply` job that says that both the plan and validation should be successful before continuing.

1. You can see this repeated in all my `release` pipelines if you search [in the template](https://github.com/gerryw1389/terraform-examples/tree/main/2023-02-27-terraform-template/yaml/spoke/release). Search in those for more specific examples.