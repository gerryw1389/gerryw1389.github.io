---
title: 'Github Actions: Uses For Workflow Dispatch'
date: 2023-05-21T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/05/uses-for-workflow-dispatch
tags:
  - Github
  - Terraform
---
<!--more-->

### Description:

Workflow Dispatch is a [trigger](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow#defining-inputs-for-manually-triggered-workflows) for Github Actions that translates to "manual" in my mind. Here is how it can be used if you prefer to manually run workflows where you present a "form" to developers with radio buttons to control which workflows run:

### To Resolve:

1. First, create 3 files under `./.github/workflows` in your repo. `c.yaml`, `d.yaml`, and `parent.yaml`.

1. Inside `parent.yaml`, copy these contents replacing with your Github username:

   ```yaml
   name: Parent

   on:
   workflow_dispatch:
      inputs:
         one:
            description: 'one'
            required: true
            type: string
         two:
            description: 'two'
            required: true
            type: string
         three:
            description: 'three'
            required: true
            type: boolean
         logLevel:
            description: 'logLevel'
            required: true
            default: 'warning'
            type: choice
            options:
               - info
               - warning
               - debug
   jobs:
   
   call-child-c:
      if: github.event.inputs.one == 'jim' && github.event.inputs.logLevel == 'warning'
      uses: gerryw1389/terraform-examples/.github/workflows/c.yml@main
      with:
         config-path: ${{ inputs.two }}
      secrets:
         token: "blah"
   call-child-d:
      if: github.event.inputs.one != 'jim'
      uses: gerryw1389/terraform-examples/.github/workflows/d.yml@main
      with:
         config-path: ${{ inputs.two }}
      secrets:
         token: "blah"
   ```


1. Inside `c.yaml`, copy these contents:

   ```yaml
   name: c
   on:
   workflow_call:
      inputs:
         config-path:
         required: true
         type: string
      secrets:
         token:
         required: true

   jobs:
   deploy:
      runs-on: ubuntu-latest
      steps:
         - name: Checkout
         uses: actions/checkout@v3

         - name: Display Yaml Name
         run: 
            echo "ran c.yaml"

         # If you ever need to display secret: https://stackoverflow.com/questions/63003669/how-can-i-see-my-git-secrets-unencrypted
         - name: Display Secret
         run: |
            import os
            for q in (os.getenv("SECRET")):
               print(q)
         shell: python 
         env:
            SECRET: ${{ secrets.token }}

         - name: Display Config-Path
         run: 
            echo ${{ inputs.config-path }}
   ```

1. Inside `d.yaml`, copy these contents:

   ```yaml
   name: Reusable deploy workflow
   on:
   workflow_call:
      inputs:
         config-path:
         required: true
         type: string
      secrets:
         token:
         required: true

   jobs:
   deploy:
      runs-on: ubuntu-latest
      steps:
         - name: Checkout
         uses: actions/checkout@v3

         - name: Display Yaml Name
         run: 
            echo "ran d.yaml"

         # If you ever need to display secret: https://stackoverflow.com/questions/63003669/how-can-i-see-my-git-secrets-unencrypted
         - name: Display Secret
         run: |
            import os
            for q in (os.getenv("SECRET")):
               print(q)
         shell: python 
         env:
            SECRET: ${{ secrets.token }}

         - name: Display Config-Path
         run: 
            echo ${{ inputs.config-path }}
   ```

1. Before explaining, make sure [to read official sources](https://docs.github.com/en/actions/using-workflows/reusing-workflows#creating-a-reusable-workflow) on this to follow along. But to explain, in `parent.yaml` you can create as many [inputs](https://github.blog/changelog/2021-11-10-github-actions-input-types-for-manual-workflows/) as you want and then call child workflows based on those inputs.

   - You can see [this is how I used to do it](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-27-terraform-template/yaml/nonprod-build.yaml) in the past. I have since moved to a [git flow model](https://automationadmin.com/2023/04/git-flow-model) that is path based instead of manual input based like this post.

   - But if you wish to do things manually, this is the best way as it presents radio buttons that a user can select to run specific workflows. I don't have many details because I went a different direction when moving for Azure Devops to Github Actions.

1. Another common use for `on: workflow dispatch:` is to stop an automated workflow from running. For example, I may run a `terraform fmt --recursive` in the root of my repo and that would normally trigger multiple terraform runs but I then set the trigger to workflow dispatch so I don't have to worry about anything running before I open my Pull Request to the `develop` branch.