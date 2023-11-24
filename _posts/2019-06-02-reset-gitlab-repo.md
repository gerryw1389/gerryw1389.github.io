---
title: Reset Gitlab Repo
date: 2019-06-02T01:36:03-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/reset-gitlab-repo/
tags:
  - LocalSoftware
tags:
  - VersionControl
---
<!--more-->

### Description

Follow these steps to keep an existing repo but remove all files and commits to start fresh. This is assuming you only have the branch 'master' with lots of prior commits. For multiple branches you can try the script in one of the answers at [here](https://stackoverflow.com/questions/9683279/make-the-current-commit-the-only-initial-commit-in-a-git-repository)

Script in reference:
   
   ```shell
   for BR in $(git branch); do   
   git checkout $BR
   git checkout --orphan ${BR}_temp
   git commit -m "Initial commit"
   git branch -D $BR
   git branch -m $BR
   done;
   git gc --aggressive --prune=all
   ```

### To resolve:

1. Send your files to zip and copy somewhere else

2. In Gitlab:

   - Unprotect branch 'master' - Go to project: "Settings" - "Repository" - "Expand" on "Protected branches". Remove "Master". We do this to avoid the error "You are not allowed to force push code to a protected branch on this project."

   - Go to "User Settings" - "Access Tokens" - Make sure that you have a "Personal Access Token" copied somewhere. If you have to generate one, make sure it has "api" rights.

3. Open Powershell as admin and:

   ```powershell
   cd C:\scripts\powershell
   cat ./.git/config
   # copy the remote git URI: https://mydomain.com/myuser/powershell.git
   ```

4. Delete all the files in the directory including the .git folder

5. In Windows, open the Credential Manager and clear all instances of git.

   - Now back in the Admin PS prompt: 

   ```powershell
   git init
   new-item -itemtype file -name blah.txt
   git add .
   git commit -m 'reinitialized files'
   git remote add origin https://mydomain.com/myuser/powershell.git
   # if it says one already exists, run 'git remote rm origin' then run it again
   git push --set-upstream origin master
   git push origin --force
   git gc --aggressive --prune=all
   ```

6. If it says:

   ```escape
   HTTP Basic: Access denied and fatal Authentication
   ```

   - Type: `git config --system --unset credential.helper`, then run the command again

7. Assuming you got this far, copy back the files and do another push.

8. Another option, the one I chose, is to use the program 'Github Desktop'. I had issues with credentials so I ended up just using 'GitHub Desktop', but eventually I got a clean git history in the original repo.

9. Another option:

   ```powershell
   git checkout --orphan newBranch
   git add -A  # Add all files and commit them
   git commit
   git branch -D master  # Deletes the master branch
   git branch -m master  # Rename the current branch to master
   git push -f origin master  # Force push master branch to github
   git gc --aggressive --prune=all     # remove the old files
   ```

### References:

["Make the current commit the only (initial) commit in a Git repository?"](https://stackoverflow.com/questions/9683279/make-the-current-commit-the-only-initial-commit-in-a-git-repository)  