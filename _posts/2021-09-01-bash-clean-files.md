---
title: Bash Clean Files
date: 2021-09-01T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/09/bash-clean-files
categories:
  - LocalSoftware
tags:
  - Scripting-Bash
---
<!--more-->

### Description

So a team member came with the following problem:

A server was executing the following bash commands to clean files in a directory:
`cd /mnt/c/scripts/backups/; ls -l; find . -name \*.dat* -mtime +31 -exec ls -l {} \;; find . -name \*.dat* -mtime +31 -exec rm {} \;`

The issue was that for some scripts worked but for others, bash was dropping into a directory it wasn't supposed to and deleting files there.

### To Resolve:

1. Proposed solution:

   ```shell
   dir="/mnt/c/scripts/backups"; if [ -d "$dir" -a ! -h "$dir" ]; then ls -l; find . -name \*.dat* -mtime +31 -exec ls -l {} \;; find . -name \*.dat* -mtime +31 -exec rm {} \; else :; fi
   ```

2. I first tried various things like:

   ```shell
   #!/bin/bash

   cd /mnt/c/scripts2
   RESULT=$?
   if [ $RESULT -eq 0 ]; then
   echo "success"
   else
   echo "failed"
   fi
   ```

   ```shell
   dir="/mnt/c/scripts2"
   if [ -d "$dir" -a ! -h "$dir" ]
   then
      echo "$dir found"
      cd /mnt/c/scripts
   else
      :
   fi
   ```

   - This worked as expected. I would get `success` for valid directories and `failed` for non-valid. But I wanted it to "do nothing", so I used `:` instead.

   - And then tried to make them one liners:

   ```shell
   dir="/mnt/c/scripts2"; if [ -d "$dir" -a ! -h "$dir" ]; then echo "$dir found"; cd /mnt/c/scripts; else :; fi
   # blank as expected
   dir="/mnt/c/scripts"; if [ -d "$dir" -a ! -h "$dir" ]; then echo "$dir found"; cd /mnt/c/scripts; else :; fi
   # echo line "/mnt/c/scripts found"
   ```
