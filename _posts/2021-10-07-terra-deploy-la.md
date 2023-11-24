---
title: 'Terraform: Deploy Logic App'
date: 2021-10-07T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/10/terra-deploy-la
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description

After following ["Terraform: Deploy VM"](https://automationadmin.com/2021/10/terra-deploy-vm), I then wanted to see how to deploy a Logic App since I have plenty of these I have worked on in the past. Here is what I did (credits to April since I mostly followed [this post](https://azapril.dev/2021/04/12/deploying-a-logicapp-with-terraform/)):


### To Resolve:

1. Save an example exported Logic App template as `email_filter.json` [source](https://github.com/gerryw1389/terraform-examples/blob/main/2021-10-07-terra-deploy-la/email-filter-1/email_filter.json)

2. Created [main.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2021-10-07-terra-deploy-la/email-filter-1/main.tf)

3. Using cloud shell bash, ran a Terraform deployment:

   ```shell
   # first, make sure environmental vars are populated from previous steps (see reference to previous post)
   printenv | grep ^TF_VAR*

   cd clouddrive
   mkdir terra2
   cd terra2
   ```

   - Upload `email_filter.json` and `main.tf` using the upload tool.
   
   ```shell
   mv email_filter.json main.tf ./clouddrive/terra2/

   # Init and install modules
   terraform init

   # Creat a plan
   terraform plan -out main.tfplan

   # apply the plan
   terraform apply main.tfplan
   ```

4. This created a resource group called `email-filter-la` with a Logic App called `email-filter`. 

   - If you go to Deployments blade on the Resource Group, you can see the deployment `la_deployment_2021-10-06-20-01-18`

5. What I will work on next is how to modify an existing Logic App and deploy once again.

   - Add an Action to the Logic App `email-filter`. Let's do `Initialize Variable` with variable called `strName` and a value of `gerry`.
   - Let's also clone the Logic App to a new one called `blah`. This is because we want to ensure that a new deployment doesn't wipe any other Logic Apps in the same RG. To do this, just go to Overview blade and then "clone".
   - Now go to Export Template and save the export at `c:\scripts\email_filter.json` [source](https://github.com/gerryw1389/terraform-examples/blob/main/2021-10-07-terra-deploy-la/email-filter-2/email_filter.json)
   - IMPORTANT! In order to test that incremental overwrites, we need to REVERT the Logic App. This is simple:
     - On the Logic App blade, select Versions and `Promote` the original version of the Logic App.
   - Create a new [main.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2021-10-07-terra-deploy-la/email-filter-2/main.tf) with `Incremental` instead of `Complete` and then create a new directory to upload the two new files:

   ```shell
   cd clouddrive
   mkdir terra3
   cd terra3
   ```

   - Upload `email_filter.json` and `main.tf` using the upload tool.
   
   ```shell
   mv email_filter.json main.tf ./clouddrive/terra3/

   # Init and install modules
   terraform init

   # Creat a plan
   terraform plan -out main.tfplan
   # Take note of Plan: 1 to add, 0 to change, 0 to destroy.
   # This means that it does not know it is updating an existing resource. This will be explained below.

   # apply the plan
   terraform apply main.tfplan
   ```

6. Notice this time the resource group was left alone and two changes were made:

   - If you go to Deployments blade on the Resource Group, you can see the deployment `la_deployment_2021-10-06-20-05-29`
   - The Logic App should now have the `strName` variable initialized thus overwriting the previously "promoted" version.
   - If you go to the Activity tab blade, you will see 'Event Initiated by' is equal to `az-terraform-sp` [as expected](https://automationadmin.com/2021/10/create-terra-az-ad-app).
   - ![tf-apply](https://automationadmin.com/assets/images/uploads/2021/10/tf-apply.jpg){:class="img-responsive"}

7. So what's the problem? The Logic App deployed! Well the problem seems to be that Terraform treats ARM deployments different from the resources they deploy so when you do an update to an existing Logic App, they get out of whack in many scenarios. Here is one [issue](https://github.com/hashicorp/terraform-provider-azurerm/issues/6045) but I had found others. I will need to look into this more.

