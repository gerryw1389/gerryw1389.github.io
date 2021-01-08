---
title: Connect To Github Private Repo
date: 2018-02-24T04:44:55+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/02/connect-to-github-private-repo/
categories:
  - LocalSoftware
tags:
  - VersionControl
---
<!--more-->

### Description:

So I've been using Google Drive to store my scripts in a &#8220;public repo&#8221; that I push my sanitized scripts to every so often, but I've always wanted to do it the &#8220;right way&#8221; by using version control (git) and sending to Github. Updated post to include pushing to personal and company repo at same time. Here are the steps I did to do that from my W10 machine:

### To Resolve:

1. First, you have to find out if you want to use HTTPS or SSH for doing 'pushes' to Github/Gitlab/ect. I went with HTTPS for now. I may change it later - see [this](https://stackoverflow.com/questions/18520061/using-https-or-ssh-with-github)

2. Sign in to Github and create a repo, for example https://github.domain.com/gerry/powershell-test. The repo name is `powershell-test` and is initialized with a README.md on Github.
   
   - In the top right, click on Settings => Developer Settings => Personal Access Tokens => Click the 'Generate new token' button => Check 'repo' => Create => Jot this down somewhere, should look something like `1ef09e5aac03f99fc5135a105d104bac70652898`

3. If you haven't already, install [GCM](https://github.com/Microsoft/Git-Credential-Manager-for-Windows). This will allow Windows to store your git credentials securely.

4. Clean up your git repos on your computer. See [my other post](https://automationadmin.com/2019/06/notes-on-git/) on this for more details. But the idea is that you:

   - Clear your credential manager of anything pointing to Github
   - Clear your global git configs and set them back almost empty:

   ```powershell
   Remove-Item ~/.gitconfig

   # Now, set it back to what you want it to be:
   # NOTE: It is important that you run this in powershell on Windows if you have WSL installed. If you do this in bash, vscode will ignore your git config.
   git config --global core.autocrlf true
   git config --global credential.helper manager
   git config --global credential.useHttpPath true
   ```

   - The key for multiple accounts here is the [useHttpPath setting](https://git-scm.com/docs/git-config) and [here](https://dev.to/configcat/lazy-man-s-guide-multiple-github-https-accounts-on-windows-2mad). This will allow you to push to multiple accounts as needed.
   - Now, for each repo you initialize, set it's settings with a `--local` switch so you can push to multiple Github accounts.

   ```powershell
   New-Item -itemtype Directory -Path "c:\scripts\repo\home\powershell-test"
   cd "c:\scripts\repo\home\powershell-test"
   git init .
   git config -l
   # see that my user.name and user.email is not listed. This is because all that is inherited at this time is git Global settings. We will need these set for commits so we add them like:
   git config --local user.name 'Gerry Williams'
   git config --local user.email 'gerry.williams@domain.com'
   git config -l
   # looks good now
   ```

5. Now, to add the Github repo to my computer and authenticate with it, I run the following in vscode:

   ```powershell
   New-Item -ItemType File -Path . -Name "myfile.txt"
   git add --all
   git commit -m 'first'
   git remote add origin https://github.domain.com/gerry/powershell-test
   git pull origin master --allow-unrelated-histories

   # When you do the pull, GCM will pop up over VSCode and ask you to enter credentials into it instead of vscode
   # enter username for github.com and the password as the access token
   git push --set-upstream origin master

   # now anytime you do a `git push`, it will use the credential manager and shouldn't ask for a password
   ```

6. The Git Credential Manager for Windows will often make a mistake saving your credentials, I have found that manually entering them as a 'generic credential' works well:
   - Open Credential Manager ( Run => `rundll32.exe keymgr.dll, KRShowKeyMgr` )
   - Enter `git:https://your-repo.git` as the address
   - Enter `your-github-username` as the user
   - Enter `your-github-personal-access-token` as the password
   - Also, they have been using `main` instead of master lately so the whole thing looks like 

   ```shell
   git config --local user.name 'Gerry Williams'
   git config --local user.email 'me@company.com'
   New-Item -ItemType File -Path . -Name "myfile.txt" | Out-Null
   git add --all
   git commit -m 'first'
   # Don't forget to add the .git on the end or Credential Manager will not tie these together!
   git remote add origin https://github.domain.com/gerry/powershell-test.git
   git branch -M main
   #credential manager
   # git:https://github.domain.com/gerry/powershell-test
   # username: your-github-username
   # password: your-github-Personal-Access-Token
   git pull origin main --allow-unrelated-histories
   git push --set-upstream origin main
   # if you open the repo in vscode, it should work fine now
   ```

7. Using SSH instead would work like (NOTE: I haven't ever tested this since HTTPS seems more common):
   
   - Generate a SSH key pair and copy the public portion to your clipboard
     - `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
     - `ssh-add ~/.ssh/id_rsa`
     - `clip < ~/.ssh/id_rsa.pub`

   - Add the ssh key to your github account.
   - Clone the repo by the following:

   ```powershell
   git config --local user.name 'Gerry Williams'
   git config --local user.email 'gerry.williams@domain.com'
   git clone git@github.domain.com/gerry/powershell-test.git
   ```

8. To reiterate how I separate my work and home credentials, I just run:

   ```powershell
   git config --global credential.useHttpPath true
   git config --global core.autocrlf true
   git config --global credential.helper manager

   git config --global --list
   # verify that is all that is listed

   # now open credential manager and delete all https://github.com saved credentials
   # now each time you try again in vscode, it will ask on a per folder basis
   # enter username for github.com and the password as the access token, GCM will update Credential Manager for you.
   ```

9.  Quicker repo creation after you have a personal access token:

   ```powershell
   # create repo in Github but don't initialize with a readme
   # Create folder in File Explorer
   # Inside folder, open powershell regular (non-elevated)
   git init .
   git config --local user.name 'Gerry Williams'
   git config --local user.email 'gerry.williams@domain.com'
   New-Item -itemtype File -Path . -Name "myfile.txt"
   git add --all
   git commit -m 'first'
   git branch -M master
   git remote add origin https://github.domain.com/gerry/powershell-test
   git pull origin master --allow-unrelated-histories
   # enter github username and personal-access-token in window that pops up.
   # now add folder to vscode workspace and it will auto-detect git and credentials
   git push --set-upstream origin master
   ```

11. Troubleshooting:
   - Run `git status` often and see if it shows any errors. If so, correct them by googling the answers.
   - Run `git config -l` and look for the correct origin. 
   - If it is wrong, type `git remote rm origin` and `git remote add origin https://path/to/repository` then confirm `git remote get-url --all origin`


