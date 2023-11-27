---
title: Create RepoBot For TF Module Private Repos
date: 2023-07-02T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/07/create-repo-bot-for-tf-modules
tags:
  - Github
  - Terraform
---
<!--more-->

### Description:

In Gihub Actions, you have two main ways you can call multiple Terraform Module private repos at run time, I have only documented and tested two ways:

   - Using Deploy Keys as documented [here](https://automationadmin.com/2023/10/using-deploy-keys-for-multiple-tf-module-repos)
   - Using a Github App (this post)

Here I will show you how I used a Github App as it was much easier than people make it out to be.

### To Resolve:

1. First, you need to be an "Organizational Admin" to install Apps but you can be assigned an organizational ['App Manager'](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#github-app-managers) role that allows you to create applications, but not **install** them.

1. Next, I created an app called `repo-bot` and only gave these permissions only at the "Repository" level:
   - Actions: Read and Write
   - Admin: Read-only
   - Contents: Read-only
   - Deployments: Read-only
   - Metadata: Read-only
   - Pull Requests: Read-only
   - Secrets: Read-only
   - Workflows: Read and Write

1. I then generated a SSH Key Pair for the Github App and downloaded the private key portion PEM file to my machine.

1. Next, in repo [`sic.mgmt`](https://github.com/AutomationAdmin-Com/sic.mgmt), I uploaded the private key to the Actions Secret ["REPO_BOT_PEM"](https://github.com/AutomationAdmin-Com/sic.mgmt/blob/facf9eeb7dc99966174b83cc230868eaf1c86b0b/.github/workflows/init.yml#L96C32-L96C48) and then created a workflow that will use it.

1. The workflow uses a few actions that is an exact copy of this [user's comment](https://github.com/hashicorp/setup-terraform/issues/33#issuecomment-1299919416) I had saved when trying to set this up using SSH keys.

   - Note: Since our organization does not allow you to use third party actions, what you have to do is go a tag for an action, download it, and upload it into your own repo ( only AFTER reading the code and understanding it of course!) so that is what I did for [`getsentry/action-github-app-token`](https://github.com/getsentry/action-github-app-token/tree/v2.0.0).

   - NOTE: The App Id is **NOT** the client id, it is the literal `App ID` in Github Apps.

1. I ran the workflow and got an error about `Cannot read properties of undefined (reading 'id')` . Thankfully there was a [Github Issue](https://github.com/getsentry/action-github-app-token/issues/69) for this action that told me exactly what I needed to do => Install the Github App to the repo. Thankfully, in Github organizations, you can [install to specific repos](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app#installing-your-own-github-app) instead of installing across all repos in the organization, so I was able to install just my Terraform module repos.

1. NOTE: When using this method, all module calls look like `"git@github.com:AutomationAdmin-Com/module.rg.git?ref=v0.0.2"` , you don't have to replace anything with special host names like [with deploy keys](https://automationadmin.com/2023/10/using-deploy-keys-for-multiple-tf-module-repos).

1. Next, I re-ran the same exact workflow and it worked perfectly!