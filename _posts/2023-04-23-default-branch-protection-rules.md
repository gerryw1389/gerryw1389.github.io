---
title: My Github Default Branch Protection Rules
date: 2023-04-23T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/04/default-branch-protection-rules
tags:
  - Github
  - Terraform
---
<!--more-->

### Description

I have been using this standard for creating Branch Protection rules in every Github Repo I create following my [git flow model](https://automationadmin.com/2023/04/git-flow-model).

### To Resolve:

1. First, let's assume you have an empty repo except for a README.md on main. The first thing I do is create a `feature` branch off of main.

1. Next, on your `feature` branch, create a file called `./.github/workflows/main_protector.yaml` and fill it in like so:

   ```yaml
   # https://stackoverflow.com/questions/71120146/allowing-only-certain-branches-to-pr-merge-to-mainmaster-branch

   name: 'protect_main_branch'

   on:
   pull_request:
      branches:
         - "main"

   jobs:
   check_branch:
      runs-on: ubuntu-latest
      steps:
         - name: Check branch
         if: github.base_ref == 'main' && github.head_ref != 'develop'
         run: |
            echo "ERROR: You can only merge to main from develop branch."
            exit 1

   ```

   - This ensures that the only way our `main` branch will accept pushes is through an approved Pull Request from the `develop` branch.
   
   - [Here](https://docs.github.com/en/actions/learn-github-actions/contexts) you can search the docs for `head_ref` versus `base_ref` but base is the branch you are merging in TO and head ref is the branch you are doing the request FROM.

1. Next, create a branch called `develop` based of `main`. It's important that you base it off main and not the feature branch we just created because we need it to be different so that when we pull request in to it, it won't say "no changes detected".

1. Next, create a Pull Request from `feature` to `develop` and accept it to merge. Then merge from `develop` to `main`. Finally merge back from `main` back to your `feature` branch. This allows Github to know about your `main_protector.yaml` file we created because it will be on the main branch.

   - If you are unfamiliar with the reason for all these pull requests, please refer to my [git flow post](https://automationadmin.com/2023/04/git-flow-model).

1. Next, click on the repo and go to Settings => Branches => Add Rule.
   - Branch name pattern: `main`
   - In section "Protect matching branches" Check `Require a pull request before merging` only and uncheck `Require approvals`
   - Check the main section `Require status checks to pass before merging` and start searching for `check_branch` in the matching workflows. Then check the box for `Require branches to be up to date before merging`
   - Further down, check the box `Do not allow bypassing the above settings`
   - Finally, click Save Changes

1. Now create a rule for 'develop':
   - Branch name pattern: `develop`
   - In section "Protect matching branches" Check `Require a pull request before merging` only and uncheck `Require approvals`
   - That's it, Save Changes
