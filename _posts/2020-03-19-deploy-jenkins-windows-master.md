---
title: Deploy Jenkins Windows Master
date: 2020-03-19T07:18:46-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/03/deploy-jenkins-windows-master
tags:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

So I have deployed Jenkins [on-prem](https://automationadmin.com/2019/12/rhel7-deploy-jenkins/) as a RHEL box, now I want to deploy one as a Windows box. [Why Jenkins?](https://adamtheautomator.com/jenkins-powershell-git/) Well because I want to have my organization start using Github more and centralize our scheduled tasks. In the next few posts, I will create a 3 part series that will deploy jenkins master node, then two nodes in a cluster-like setup, and then connect each of them to our company Github so that you only configure the jobs in Jenkins once and then to maintain the code, you will simply update your repo in Github and won't have to login to Jenkins web UI every time you want to make a change!

This is part of a 3 part series:

   - 1 - Deploy Jenkins Master
   - [2 - Deploy Jenkins Nodes](https://automationadmin.com/2020/03/deploy-jenkins-windows-node)
   - [3 - Connect To Github](https://automationadmin.com/2020/04/connect-windows-to-github)


### To Resolve:

1. Go to Azure Marketplace and choose [Jenkins + WS2019](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/cloud-infrastructure-services.jenkins-windows-2019?tab=Overview). Optionally, deploy a WS2019 instance and install Jenkins, it's really the same thing.

   - Named it: `schedtasks-win2019.domain.com`

2. Update the Network security group in Azure to allow traffic to the new VM on port 443/tcp.

3. Do the initial setup where you copy the key from `C:\Program Files (x86)\Jenkins` and create a local admin user.

4. Now, setup HTTPS:

   ```escape
   cd 'C:\Program Files (x86)\Jenkins\jre\bin'
   ./keytool -genkey -keyalg RSA -keystore Jenkins.jks -alias schedtasks-win2019.domain.com -keysize 2048
   Pa$$word
   first/lastname: schedtasks-win2019.domain.com
   organizational unit? Info from CA
   organization? Info from CA
   City? Info from CA
   State? Info from CA
   Country? Info from CA
   Is $stuffFromBefore correct? y

   ./keytool -certreq -Keystore jenkins.jks -alias schedtasks-win2019.domain.com -file jenkins.csr -keysize 2048

   # Send Jenkins.csr to your cert provider and request a PKCS#7 cert which has a .p7b (not the PEM encoded one)
   # copy to `C:\Program Files (x86)\Jenkins\cert\schedtasks-win2019_domain_com.p7b`

   ./keytool -import -trustcacerts -file 'C:\Program Files (x86)\Jenkins\cert\schedtasks-win2019_domain_com.p7b' -keystore jenkins.jks -alias schedtasks-win2019.domain.com
   Pa$$word

   # now edit
   %PROGRAMFILES{x86)%/Jenkins/jenkins.xml

   # find this 
   <arguments>-Xrs -Xmx256m -Dhudson.lifecycle=hudson.lifecycle.WindowsServiceLifecycle -jar "%BASE%\jenkins.war" --httpPort=8080 --webroot="%BASE%\war"</arguments>

   # replace with this
   <arguments>-Xrs -Xmx256m -Dhudson.lifecycle=hudson.lifecycle.WindowsServiceLifecycle -jar "%BASE%\jenkins.war" --httpPort=-1 --httpsPort=443 --httpsKeyStore="C:\Program Files (x86)\Jenkins\jre\bin\Jenkins.jks" --httpsKeyStorePassword="Pa$$word" --webroot="%BASE%\war"</arguments>

   Restart-Service jenkins
   ```

5. From here, I did [step 3](https://automationadmin.com/2019/12/rhel7-deploy-jenkins/) in my previous post to configure security so that only certain users in AD can manage Jenkins. Next we will add nodes and configure Github - see links above in the description.
