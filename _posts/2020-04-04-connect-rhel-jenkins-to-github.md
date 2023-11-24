---
title: Connect RHEL Jenkins To Github
date: 2020-04-04T07:18:46-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/04/connect-rhel-jenkins-to-github
tags:
  - WebSoftware
tags:
  - VersionControl
---
<!--more-->

### Description:

This is the steps I completed in order to move a RHEL 7 server hosting Jenkins from using Gitlab to instead use Github.

### To Resolve:

1. First, ensure repos in both Gitlab and Github mirror each other (part of migration prior to this post)

2. Login as root and `su` to the jenkins user: `su -s /bin/bash jenkins`

3. Create ssh key pair:

   ```shell
   ssh-keygen -t rsa -b 4096 -C "svc_windowsJenkins@domain.com"
   /var/lib/jenkins/.ssh/id_rsa_github
   cat /var/lib/jenkins/.ssh/id_rsa_github.pub
   ```

4. Copy this to Github under the service account 'SSH Keys'. Should be like `ssh-rsa AAAAB3N...50SQ== svc_windowsJenkins@domain.com`. Like before, make sure to authorize it for SSO.

5. Do a test clone and ensure that Github is stored in `known_hosts`:

   ```shell
   eval "$(ssh-agent -s)"
   ssh-add /var/lib/jenkins/.ssh/id_rsa_github
   cd /var/lib/jenkins
   mkdir test
   cd test
   git init .
   git config --local user.name 'Service Windows Jenkins'
   git config --local user.email 'svc_windowsJenkins@domain.com'
   git clone git@github.com:company/jenkinsRepo.git
   ```

6. Then in each job, I went to Credentials and Added SSH username `svc_windowsJenkins@domain.com` and password: `pasted contents of /var/lib/jenkins/.ssh/id_rsa_github`
