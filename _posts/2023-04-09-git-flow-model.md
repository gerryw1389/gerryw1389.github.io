---
title: Git Flow Model
date: 2023-04-09T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/04/git-flow-model
tags:
  - Azure
  - Github
  - VersionControl
---
<!--more-->

### Description:

I have come to a standard for setting up Github Repos following a [git flow](https://learn.microsoft.com/en-us/azure/devops/repos/git/gitworkflow?view=azure-devops) model which is an [industry supported model](https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops#review-and-merge-code-with-pull-requests) as seen with [Githubs Official Starter Workflow For Terraform](https://github.com/actions/starter-workflows/blob/main/deployments/terraform.yml). I will be going over Github Actions in a series of posts but this one will focus on the overall "Pull Request Model" that some people call it.

### To Resolve:

1. Basically, the way it works is you have three main branches: `feature`, `develop`, and `main`. 

1. In the feature branch, you make your changes to terraform code and push to that branch one, two, or twenty commits. Then, when you are ready to run a `terraform plan`, you simply trigger a Pull Request to the `develop` branch.

1. Once the Pull Request has been reviewed by looking at the Github Action's output for Terraform plan, the approver will click `Approve` and this will trigger a `terraform apply`. 

1. After the merge, you then repeat by merging `develop` to `main` where no Actions run except a [`check_branch`](https://automationadmin.com/2023/04/default-branch-protection-rules) script that we cover in a different post. Main is just a stable working copy of your terraform code.

1. That's it! Some orgs set it up to where a merge to main will trigger pipelines or some variation of that, but the idea is still the same in most places - you do a PR to a branch which triggers `terraform plan` and then the acceptance triggers a `terraform apply`. Here is a visual of how it works:

   - ![workflow](https://automationadmin.com/assets/images/uploads/2023/11/workflow.png){:class="img-responsive"}

1. Here's the main section of the workflow that controls this:

   ```yaml
   on:
   #workflow_dispatch:
   push:
      branches:
         - "develop"
   pull_request:
      types: [opened, edited, synchronize]
      branches:
         - "develop"
   ```

   - See that we trigger 2 times => One for any "push to develop" which is the same as a merged Pull Request. Next is during an initial Pull Request to develop ("opened" event) or any pushes to the feature branch while the Pull Request is open ("edited/synchronize" events) .

   - If you don't want your `terraform plan` to keep triggering, you need to **close** your Pull Request and make all your changes, and then you can open another one once you are ready.

1. Note that I always leave `workflow_dispatch:` as an option because sometimes I need to turn off continuous integration to test some things and then turn it back off by commenting it out. You can read more about how I use workflow dispatch in [this post](https://automationadmin.com/2023/05/uses-for-workflow-dispatch).
