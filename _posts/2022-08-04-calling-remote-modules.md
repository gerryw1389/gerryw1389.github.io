---
title: 'Terraform: Calling Remote Modules'
date: 2022-08-04T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/08/calling-remote-modules
tags:
  - Azure
  - AzureDevops
  - Terraform
tags:
  - VersionControl
---
<!--more-->

### Description

One of the first things you will want to do once you start learning terraform is to break out code into chunks called [modules](https://www.terraform.io/language/modules/syntax). Using this in combination with a remote repo will allow you pin certain terraform configurations to [git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging). 

So strategically speaking, what you want to do is create two different types of repos for your Terraform code: One for applications and one for modules. The applications will then call the modules in chunks. Anyone familiar with a scripting language will be familiar with these terms:

   - Controller script that calls functions
   - [Stacks](https://en.wikipedia.org/wiki/Call_stack) that call sub routines.

Well Terraform calls Stacks or Controller scripts ["module compositions"](https://www.terraform.io/language/modules/develop/composition) and the functions or small repeatable 'do-one-thing-and-one-thing-only' type code modules. The following is how you would go about doing this with Azure Devops Pipelines. 


Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-examples/tree/main/2022-08-04-calling-remote-modules).
{: .notice--success}

### To Resolve

1. So in your `main.tf` (or whatever file) for your application deployment, you will just make various calls to your remote modules like on [line 49 here](https://github.com/gerryw1389/terraform-examples/blob/main/2022-08-04-calling-remote-modules/main.tf).

   - Note the remote calls using the `source` argument. Also note that these should always point to a specific tag. The tag can be generated through a release which I cover in [another post](https://automationadmin.com/2022/08/git-tagging).
   {: .notice--success}
   
   - Also note the passing of data between the module calls like in `module.learning-vnet.name` which works just like the [data](https://automationadmin.com/2022/07/tf-reference-current) block or any other Terraform block. See [line 57](https://github.com/gerryw1389/terraform-examples/blob/main/2022-08-04-calling-remote-modules/main.tf).
   {: .notice--success}

2. The next thing to be aware of when you call another module is your Azure Devops Pipeline. I'm not an expert on Azure Devops permissions so please bear with me if I'm wrong, but this is what I have done to get one repo in our Devops Organization to call a remote repo in our Devops Organization. See [here](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/multi-repo-checkout?view=azure-devops) for the docs. In the `build.yaml` add this to the top:

   ```yaml
   resources:
      repositories:
      - repository: MyRepo-subnet
         type: git
         name: MyProject/MyRepo-subnet
         ref: main
   ```

   - And then under steps:

   ```yaml
   steps:
      - checkout: self        
      - checkout: MyRepo-subnet
      - task: PowerShell@2
         displayName: Tokenize TF-Module Sources
         env:
            SYSTEM_ACCESSTOKEN: $(System.AccessToken)
         inputs:
            targetType: 'inline'
            script: |
            git config --global http.extraHeader 'Authorization: Bearer $(System.AccessToken)'
   ```

   - Doing these steps should allow one repo to pull the contents of another repo based on a git tagged version which will never change (a point in time) unless the called repo deletes the git tag and pins that same tag name to another commit which is bad practice if following [semantic versioning](https://semver.org/). I cover this more in [my other post](https://automationadmin.com/2022/08/git-tagging).

