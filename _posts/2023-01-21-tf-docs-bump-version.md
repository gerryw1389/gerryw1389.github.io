---
title: 'TF Docs and Bump Version Pipeline'
date: 2023-01-21T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/tf-docs-bump-version
tags:
  - WebSoftware
tags:
  - CICD
---
<!--more-->

### Description:

So one pipeline I add to all module repos is to "bump version" and "update tf docs". This is a single pipeline that developers run when they want to increment a [git tag](https://automationadmin.com/2022/08/git-tagging) like mentioned in my [changelog post](https://automationadmin.com/2023/01/update-changelog). This pipeline solves 3 main things:

   - First, using `semver`, it will increment the module's git tag to the next version.
   - Second, using plain bash it will update the changelog with the latest notes.
   - Last, it will use [terraform-docs](https://terraform-docs.io/) to update the README in the repo according to a config file.

See below for more details.

### To Resolve:

1. Below is an example pipeline:

   ```yaml

   parameters:
      - name: increment
      displayName: Bump version
      type: string
      default: patch
      values:
         - major
         - minor
         - patch

   resources:
      repositories:
      - repository: module.example
         type: git
         name: my project/module.example
         ref: main

   trigger:
      - none

   stages:
   - stage: Bump_Version
      jobs:
      - job: bump_version
      displayName: 'Bump module version'
      condition: ne(variables['Build.Reason'], 'PullRequest')
      continueOnError: false
      pool:
         name: 'my-buildagent'
      steps:
         
         - checkout: self
            persistCredentials: true

         - checkout: module.example

         # Download terrform-docs and run it using config file under ./yaml/
         - task: Bash@3
            inputs:
            targetType: 'inline'
            script: |
               mkdir src
               cd src
               curl -SL https://github.com/terraform-docs/terraform-docs/releases/download/v0.16.0/terraform-docs-v0.16.0-$(uname)-amd64.tar.gz --output terraform-docs.tar.gz
               tar -xzf ./terraform-docs.tar.gz
               chmod +x ./terraform-docs
            displayName: 'Install Terraform-docs'

         - script: |
            git config --global user.email '$(Build.RequestedForEmail)'
            git config --global user.name '$(Build.RequestedFor)'
            displayName: 'Enable scripts to run git commands'
            failOnStderr: true

         # TF Docs custom config path => https://terraform-docs.io/user-guide/configuration/
         - task: Bash@3
            inputs:
            targetType: 'inline'
            failOnStderr: true
            script: |
               ./src/terraform-docs -c $(Build.SourcesDirectory)/my-repo/yaml/tf-docs-config.yml $(Build.SourcesDirectory)/my-repo
            displayName: 'Generate documentation from Terraform modules'

         - task: Bash@3
            inputs:
            targetType: 'inline'
            workingDirectory: $(Build.SourcesDirectory)/my-repo
            failOnStderr: true
            script: |
               git add -A && (git diff-index --quiet HEAD || git commit -am '[skip ci] generate docs')
            displayName: 'Commit changes'
         
         Step 2: Download semver and increment the input param by one
         - task: Bash@3
            inputs:
            targetType: 'inline'
            workingDirectory: $(Build.SourcesDirectory)
            script: |
               mkdir src
               cd src
               curl -SL https://raw.githubusercontent.com/fsaintjacques/semver-tool/master/src/semver --output semver
               chmod +x ./semver
               ./semver --version
            displayName: 'Download semver tool'

         # Git tag cmd ref => https://gist.github.com/loisaidasam/b1e6879f3deb495c22cc
         - task: Bash@3
            inputs:
            targetType: 'inline'
            workingDirectory: $(Build.SourcesDirectory)/my-repo
            failOnStderr: true
            script: |
               old_version="$(git tag | tr - \~ | sort -V | tr \~ -| tail -1)"
               echo "vso[task.setvariable variable=Version.Old;isreadonly=true]$old_version"

               new_version="$(../src/semver bump ${/{ parameters.increment }} $old_version)"
               full_new_version=v$new_version
               echo "vso[task.setvariable variable=Version.New;isreadonly=true]$full_new_version"

               echo "vso[build.updatebuildnumber]$full_new_version"
            displayName: 'Bump version'

         - task: Bash@3
            inputs:
            targetType: 'inline'
            failOnStderr: true
            workingDirectory: $(Build.SourcesDirectory)/my-repo
            script: |
               unreleased_query="baseVersion=GBmain\&targetVersion=GT$(Version.New)\&_a=commits"
               unreleased_url="$(Build.Repository.Uri)/branchCompare?${unreleased_query}"
               unreleased_header=" [Unreleased]($unreleased_url)"

               released_query="baseVersion=GT$(Version.New)\&targetVersion=GT$(Version.Old)\&_a=commits"
               released_url="$(Build.Repository.Uri)/branchCompare?${released_query}"
               date="$(date '+%Y-%m-%d')"
               released_header=" [$(Version.New)]($released_url) - $date"

               sed -e "s|^ \[Unreleased\].*|$unreleased_header\n\n$released_header|" --follow-symlinks -i docs/changelog.md
            displayName: 'Update changelog'

         - task: Bash@3
            inputs:
            targetType: 'inline'
            failOnStderr: true
            workingDirectory: $(Build.SourcesDirectory)/my-repo
            script: |
               git config --global user.name "$(Build.RequestedFor)"
               git config --global user.email $(Build.RequestedForEmail)

               git commit -a -m "Bump version to $(Version.New)" -m '[skip ci]' --allow-empty
               git tag -a -m 'Release $(Version.New)' $(Version.New)
            displayName: 'Create release tag'

         Step 3: Push these changes to the repo
         - task: Bash@3
            inputs:
            targetType: 'inline'
            failOnStderr: true
            workingDirectory: $(Build.SourcesDirectory)/my-repo
            script: |
               git push --follow-tags --porcelain origin 'HEAD:$(Build.SourceBranchName)'
            displayName: 'Push release tag'

   ```

   - Couple things happening here... first, we download the contents of an other repo because the checkout stage will name the folders correctly [only if you checkout another repo](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/multi-repo-checkout?view=azure-devops#specify-multiple-repositories) (see the text *"Each designated repository is checked out to a folder named after the repository, unless a different path is specified in the checkout step. To check out self as one of the repositories, use checkout: self as one of the checkout steps."*)

   - Next, we set trigger to `none` because we don't want this running unless we run it manually.

   - Next, we download the tf-docs executable from Github and then run it against `$(Build.SourcesDirectory)/my-repo` using its config file at `$(Build.SourcesDirectory)/my-repo/yaml/tf-docs-config.yml`

   - Next, we download the `semver` tool and run it against the output from a generic bash script that gets the latest tag in the repo. This gives us a new incremented version that we will do 2 things with:

      - First, we will use it to update our changelog.
      - Next, we will use it to create a new tag for the repo and push it.
   
   - The last few steps do just that, update the changelog using some `sed` commands and then push the latest tag to the repo.


1. As discussed, the `./yaml` directory has this file called `./yaml/tf-docs-config.yaml`

   ```yaml
   formatter: markdown document

   version: ">= 0.14.0, < 1.0.0"

   sections:
   show:
      - inputs
      - outputs

   output:
   file: README.md
   mode: inject

   sort:
   enabled: false

   settings:
   html: false
   indent: 3
   ```

1. Finally, you just create a pipeline in Azure Devops pointing to this file for your module and you can run it on demand.

1. [Here is an example](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-27-terraform-template/yaml/bump_module_steps.yaml) that doesn't use `semver` or `tf-docs` and only increments using bash.