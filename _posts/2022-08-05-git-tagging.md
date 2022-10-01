---
title: Git Tagging
date: 2022-08-05T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/08/git-tagging
categories:
  - LocalSoftware
tags:
  - VersionControl
---
<!--more-->

### Description

I touched on this previously in [another post](https://automationadmin.com/2022/08/calling-remote-modules), but I wanted to follow up with [git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) and how they are a core concept in designing Terraform [modules](https://www.terraform.io/language/modules/syntax).

### To Resolve

1. To create a tag for Github, you must run `git tag <tag details>` followed by `git push origin tag_name`. By default, when you push to Github it [does not include tags](https://stackoverflow.com/questions/5195859/how-do-you-push-a-tag-to-a-remote-repository-using-git) so you have to include that information when you push.

1. The reason this is its own post is because I wanted to share using tagging with the trunk based development (see below) model. What I have found is that if you are working on a branch and then you tag a commit, when you merge that branch back into main/master/trunk and delete the remote branch, the tag will still persist even if that original branch has been deleted. This works with ["merge no fast forward"](https://devblogs.microsoft.com/devops/pull-requests-with-rebase/) from my experience so far.

1. So with "trunk based development", my current workflow is:

   ```shell
   cd to /dir/repo/myrepo

   # pull latest info
   git pull origin main/master

   # See different branches
   git branch -va

   # Delete local branches
   git branch -D my_local

   # create a new local branch
   git checkout -b my_fix

   ```

   - So I will commit on branch `my_fix` over and over until I'm ready to send a pull request back into main/master. From there I choose the default option above which will delete my branch `my_fix` when the pull request is approved. What I'm saying about tags is that if I tag a commit on my branch `my_fix`, say `v1.0.2`, that tag will still exist after I merge the branch and delete it.

1. So now we have created a tag and pushed it to to Github, what's the big deal? Well now I can navigate to Github in the Web UI and target a specific point in time that the repo existed. For example [see v1.0.0 of my Resource Group module](https://github.com/gerryw1389/terraform-modules/tree/v1.0.0). What's cool about this is:

   - The [variables.tf](https://github.com/gerryw1389/terraform-modules/blob/v1.0.0/resource-group/variables.tf) that is required when I call the module will never change (unless someone deletes the tag and recreates it with the same name on a different commit).

   - The code I'm using will never change as long as the tag never changes commits. This ensures that if I have 100+ repos calling my code targeting a tag it will always work because the code will never change.

1. So let's say I want to make `tags` optional in that [variables.tf](https://github.com/gerryw1389/terraform-modules/blob/v1.0.0/resource-group/variables.tf) file, all I would have to do is:

   - cd to the directory
   - create a branch and make my change. 
   - Push it and merge it back with main/master
   - create a new tag like `v1.0.1`. See [here](https://github.com/gerryw1389/terraform-modules/blob/v1.0.1/resource-group/variables.tf) where I did this (ignore line 19, I copied/pasted and wasn't paying attention. I don't think a var can reference another var in a `default` block like that but you get the idea).
 
   - Then in my 100+ repos I can modify my code that called the module from:

   ```terraform
   module "azure_learning_rg" {
   source              = "git::https://github.com/gerryw1389/terraform-modules.git//resource-group?ref=v1.0.0"
   resource_group_name = "aa-${var.env_stage_abbr}-${var.region_abbr}-test-remote"
   location            = var.region
   tags                = local.sbx_tags
   }
   ```

   - to 

   ```terraform
   module "azure_learning_rg" {
   source              = "git::https://github.com/gerryw1389/terraform-modules.git//resource-group?ref=v1.0.1"
   resource_group_name = "aa-${var.env_stage_abbr}-${var.region_abbr}-test-remote"
   location            = var.region
   }
   ```

   - See how the `ref=` went up a version and now with the new version of the module the `tags` attribute is no longer required? That is how this works.
   - So in my 100+ repos I can point to my modules repo pinning to a tag version that will/will not make tags optional. This is a basic example that shows the concept.

1. So using this technique, you can have different versions of your modules being called scattered all through the enterprise. I haven't tested moving a tag like `latest` but I would imagine that any breaking changes like `v2.0.1` to `3.1` would cause everything to break so I don't think that would be a good idea. Not sure, will check back in a couple years but for now I will keep pinning module calls to tags to keep things simple and then set a scheduled task to go and update my module calls every now and then to the latest version by testing the new variables/ect.