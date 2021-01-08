---
title: Breaking Into SA Jobs
date: 2016-05-29T05:03:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/breaking-into-sa-jobs/
categories:
  - SysAdmin
---
<!--more-->

### Description:

As a Systems Administrator, I get asked a lot about how to become one or what paths to take. The typical paths I have seen are:

Tech support => Tech Support Lvl 2/3 => Onsite Tech (you could start here and gain experience/responsibility too) => Jr. Sys Admin => Sys Admin => Senior Sys Admin => It Manager => VP of IT => CIO (or top level &#8220;Information&#8221; executive title)

or something to that effect. Another thing to consider, which is actually [standard nowadays](http://thedailywtf.com/articles/Up-or-Out-Solving-the-IT-Turnover-Crisis), is to always switch jobs when you feel you are not being challenged enough.

### For Certifications:

1. Certifications are mostly important in the beginning part of your career and later depending on the company. Standard practice is to have a Net+, Sec+, A+ for entry level positions (Tech Support/ Onsite Tech) and CCNA, MCSA, etc. later on (post Jr. Admin). These tend to depend on the company as many companies will not even look at you without X cert and others will overlook them completely for official education/ experience.

### For Official Education:

1. To break into the field IT is recommended to at least have an Associates Degree (Tech Support+). Anything past Jr. Admin will most likely require a Bachelors. Anything beyond that will help break into management and out of &#8220;strictly IT&#8221; (IT Manager+).

### For Tech Skills:

1. Official work experience is **ALWAYS PLACED FIRST** at every job I have ever had. Certifications/ education are good to breaking into the field but experience will get you anywhere you need to go past that. The hard part is finding a place that keeps you challenged. Try to learn new things every day and always ask &#8220;what is something new I can add to my resume?&#8221;. It is common practice these days to stay at a company long enough to learn new skills and then move on, usually the biggest complaint I always hear is &#8220;how am I supposed to get experience when nobody will hire me to start with?&#8221;. To start:

   - Create a website using Github Pages with Jekyll (here). Other options include Google Sites, WordPress, Jumla, or Drupal.

   - Although many certs are not indicative of skills because people can cram, I have found the [TestOut Network Pro](https://www.testout.com/courses/network-pro) exam to be a good starter cert for Systems Administration.

   - If you went to a decent college recently, you most likely have a Microsoft DreamSpark subscription that you could be using to download and install FULL VERSION MS PRODUCTS in a home lab. I use just one computer to run 10+ different VM's and networks (not all at once obviously), here's how:

   - Install Oracle Virtual Box, Vmware Workstation (not free) or MS Hyper V role (Win8+) and create virtual machines running any and all Linux OS's you feel like downloading. If you have the DreamSpark subscription, install as many Server OS's as you can as well as a couple client OS's. In addition, you can install specialized OS's such as Pfsense and FreeNAS as virtual machines.

   - Install GNS3 (application/ not a VM) to run virtual networking appliances. You can refer to my GNS3 sections for more info but just download the BIN files for these appliances and run them like VM's.

   - Using these virtual networks/ OS's you can do just about anything you can in a production environment except for using high priced proprietary software. Just for example you could:

     - Setup a domain. Have at least two domain controllers and take one down. See about transfering roles.  
     - Practice all the server roles at one point or another. I am currently working on WDS with MDT, but you can start with a WSUS Server, Print Server, etc.  
     - Practice Powershell against a list of virtual servers (ps remoting). Eventually look into something like DSC.  
     - Use VeeamZIP to backup your VM's.  
     - Create a high availabilty cluster using FreeNAS and two Server VM's (I have a section on this).  
     - Install a PFsense VM (firewall OS) and test it out.  
     - Setup virtual networks in GNS3 (still looking into this myself)  
     - Install a self-hosted (usually cheaper or free) monitoring software like Spiceworks or PRTG Monitor and get it to send alerts. Correct errors and learn about WMI/ SNMP.  
   
   - These are some things I have done in the last year and I have only been in IT for 3 years. I would imagine this list could get quite long if one puts their time into it. A list of my currently installed VM's (9-13-15):

   <img class="alignnone wp-image-637 size-full" src="https://automationadmin.com/assets/images/uploads/2016/09/breaking-into-sa-jobs.png" alt="breaking-into-sa-jobs" width="338" height="503" srcset="https://automationadmin.com/assets/images/uploads/2016/09/breaking-into-sa-jobs.png 338w, https://automationadmin.com/assets/images/uploads/2016/09/breaking-into-sa-jobs-202x300.png 202w" sizes="(max-width: 338px) 100vw, 338px" />

2. Another option I didn't do personally but would definitely show that you are trying is volunteering. Churches and non-profits are usually seeking assistance. This would actually count as &#8220;official experience&#8221; though.

3. Documentation. I personally use [VScode with Markdown](https://automationadmin.com/2019/06/vscode-config) for documentation, but the idea is to always be looking a new things to try out and learn. Follow tech news sites, forums, and blogs if you unsure where to start (or try my links). Document everything you learn and then expand on things you know little about. It's absolutely overwhelming at first, but just tackle one task at a time on your free time and you will be &#8220;a somewhat competent admin&#8221; in most peoples eyes.

4. Lastly, and this may be me, but always put your home lab experience as an &#8220;Unofficial Experience&#8221; section on your resume. It shows employers that you are interested in learning new technologies and go out of your way to prove it. Use a public facing website, blog, or some kind of documentation to show that not only do you try new things, but you document them as well.

### For People Skills:

1. See [People Skills](https://automationadmin.com/2016/05/people-skills/) notes.