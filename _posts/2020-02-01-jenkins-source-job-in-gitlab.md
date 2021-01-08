---
title: 'Jenkins: Source Job In Gitlab'
date: 2020-02-01T10:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/jenkins-source-job-in-gitlab/
categories:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

So instead of manually typing in a groovy script as a source for a job in Jenkins, I was able to point it to our Gitlab instance. Here are the steps I did to do this:

### To Resolve

1. First, I ssh'd to the Jenkins server and ran:

   ```shell
   sudo su
   cd /root
   mkdir temp
   cd /root/temp/
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   # ssh-add ~/.ssh/id_rsa
   # copy text at ~/.ssh/id_rsa.pub to my gitlab account
   git clone git@gitlab.domain.com:projectTeam/jenkins.git
   # it will then add gitlab to your ~/.ssh/known_hosts
   git ls-remote -h git@gitlab.domain.com:projectTeam/jenkins.git
   # make sure you see a long string and refs/heads/master on the last line
   ```

2. Now, we need to do the same thing as the `jenkins` user:

   ```shell
   runuser jenkins -s /bin/bash -c "ssh-keygen -t rsa -b 4096 -C "my.user@domain.com""
   # this caused it to complain about something, maybe just move on
   runuser jenkins -s /bin/bash -c "ssh-add /var/lib/jenkins/.ssh/id_rsa"
   runuser jenkins -s /bin/bash -c "git ls-remote -h git@gitlab.domain.com:projectTeam/jenkins.git" 
   ```

3. Now in the web UI, I get the following error:

   ```escape
   Failed to connect to repository : Command "git ls-remote -h git@gitlab.domain.com:projectTeam/jenkins.git HEAD" returned status code 128:
   stdout:
   stderr: This $COMPANY information resource, including all related equipment,
   networks and network devices, is provided for authorized use only. All
   unauthorized use of this information resource is prohibited. Misuse is
   subject to criminal prosecution and/or administrative or other
   disciplinary action.

   Usage of this information resource, authorized or unauthorized, may be
   subject to security testing and monitoring. In addition, all information,
   including personal information that is placed on or sent over this
   resource is the properly of the State of Texas and may also be subject
   to security testing and monitoring. Evidence of unauthorized use and/or
   misuse collected during security testing and monitoring is subject to
   criminal prosecution and/or administrative or other disciplinary action.

   Usage of this information resource constitutes consent to all policies
   and procedures set forth by $COMPANY and there is no expectation of
   privacy except as otherwise provided by applicable privacy laws.
   Permission denied, please try again.
   Permission denied, please try again.
   Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password).
   fatal: Could not read from remote repository.

   Please make sure you have the correct access rights
   and the repository exists.

   ```

4. This is actually a good thing since we are getting the banner. What I did next was go back to `/var/lib/jenkins/.ssh/id_rsa.pub` and copied that key to my account in Gitlab as well.

5. I then got the following error:

   ```escape
   error:
   java.lang.IllegalArgumentException: Invalid refspec refs/heads/**
   ```

   - Per [the fix](https://stackoverflow.com/questions/46684972/jenkins-throws-java-lang-illegalargumentexception-invalid-refspec-refs-heads), I just needed to change 'branch specifier' from `**` to `*/*`

6. I now had these settings in the Pipeline section of my job:
   
   - Definition: Pipeline Script from SCM
   - SCM: Git
   - Repository URL: git@gitlab.domain.com:projectTeam/jenkins.git
   - Credentials: None
   - Branch Specifier: `*/*`
   - Script Path = addAzureUser_Jenkinsfile

7. If you have one repo, you can have as many `Jenkinsfile` files as needed that each job points to.

