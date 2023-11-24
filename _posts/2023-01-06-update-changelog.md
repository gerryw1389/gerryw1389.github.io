---
title: 'AZDO: Update Changelog'
date: 2023-01-06T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/update-changelog
tags:
  - LocalSoftware
tags:
  - VersionControl
---
<!--more-->

### Description:

So a [Changelog](https://keepachangelog.com/en/1.0.0/) is a common software practice where developers will note any changes between [git tags](https://automationadmin.com/2022/08/git-tagging) in a repo. Here is how I'm implementing changelogs for my module repos:

### To Resolve:

1. So first, just create a `./docs/changelog.md` in your repo and follow a pattern like this:

   - Note: In this example, I will add some notes between version `v0.0.2` and `v0.0.3` 

   - So as of `v0.0.2`, it looks like this:

   ```markdown

   # Changelog

   All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

   ## [Unreleased](https://my-org@dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GBmain&targetVersion=GTv0.0.2&_a=commits)

   ## [v0.0.2](https://my-org@dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GTv0.0.2&targetVersion=GTv0.0.1&_a=commits) - 2023-01-11

   ### Added
   - Updated terragrunt

   ### Changed

   ### Removed

   ### Fixed

   ## [v0.0.1](https://dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GBmain&targetVersion=GTv0.0.1&_a=commits)

   ### Added

   - Initialized repo

   ### Changed

   ### Removed

   ### Fixed

   ```

   - So reading this, we can see the initial version `v0.0.1` initialized the repo and `v0.0.2` updated terragrunt. Not very descriptive, but a basic example.

   - So now lets add some notes before bumping our repo to `v0.0.3`:

   - First, add a line break before the `## [v0.0.2]` line but after the `## [Unreleased]` line

   - Then copy/paste these 4 blocks

   ```markdown
   ### Added

   ### Changed

   ### Removed

   ### Fixed

   ```

   - Now, add whatever comments by typing `- comment` replacing `comment with human readable updates between your last git tag and the one you are about to bump to.

   - Here I will add `- Test comment` so it now looks like this:

   ```markdown

   # Changelog

   All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

   ## [Unreleased](https://my-org@dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GBmain&targetVersion=GTv0.0.2&_a=commits)

   ### Added

   ### Changed
   - Test comment

   ### Removed

   ### Fixed

   ## [v0.0.2](https://my-org@dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GTv0.0.2&targetVersion=GTv0.0.1&_a=commits) - 2023-01-11

   ### Added
   - Updated terragrunt

   ### Changed

   ### Removed

   ### Fixed

   ## [v0.0.1](https://dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GBmain&targetVersion=GTv0.0.1&_a=commits)

   ### Added

   - Initialized repo

   ### Changed

   ### Removed

   ### Fixed


   ```

1. Now commit your changes and run your [`bump version` pipeline](https://automationadmin.com/2023/01/tf-docs-bump-version)

1. Lastly, do a pull in your repo since the bump version pipeline pushes. It should now look like this

   ```markdown

   # Changelog

   All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

   ## [Unreleased](https://my-org@dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GBmain&targetVersion=GTv0.0.3&_a=commits)

   ## [v0.0.3](https://my-org@dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GTv0.0.3&targetVersion=GTv0.0.2&_a=commits) - 2023-01-11

   ### Added

   ### Changed
   - Test comment

   ### Removed

   ### Fixed

   ## [v0.0.2](https://my-org@dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GTv0.0.2&targetVersion=GTv0.0.1&_a=commits) - 2023-01-11

   ### Added
   - Updated terragrunt

   ### Changed

   ### Removed

   ### Fixed

   ## [v0.0.1](https://dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GBmain&targetVersion=GTv0.0.1&_a=commits)

   ### Added

   - Initialized repo

   ### Changed

   ### Removed

   ### Fixed


   ```

   - See how it added the line for you? `## [v0.0.3](https://my-org@dev.azure.com/my-project/_git/my-repo/branchCompare?baseVersion=GTv0.0.3&targetVersion=GTv0.0.2&_a=commits) - 2023-01-11` ?

   - That's it!