---
title: Gitignore Issue
date: 2021-09-30T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/09/gitignore-issue
tags:
  - LocalSoftware
tags:
  - VersionControl
---
<!--more-->

### Description

Git Was not ignoring `__pycache__` even though I had it set in `.gitignore`

### To Resolve:

1. Originally read [this](https://github.com/Microsoft/vscode/issues/38270) which didn't seem to help.

2. Then I ran the following per [this article](https://digitizor.com/gitignore-not-ignoring-files-how-to-fix/) and it worked:

   ```shell
   git rm -r --cached .
   git add .
   git commit -m ".gitignore Fixed"
   ```
