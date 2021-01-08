---
title: Setting Up An External Fileshare
date: 2016-05-22T08:16:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/setting-up-an-external-fileshare/
categories:
  - WindowsServer
tags:
  - WebServer
  - Setup
---
<!--more-->

### Description:

You may need to be able to share files with clients outside of your internal network. I ran into a situation like this some time ago at my last job. Since we are already hosting a website, we just added a new site to our web server for users to download files from there.

NOTE: For files that are sensitive by nature, it is absolutely essential not to follow this guide => this is for files you don't care who gets. I recommends a SFTP server for secure file transfers.

### To Resolve:

1. Log in to your DNS provider (ours is WorldWideDNS) and find an external IP to use.

2. Make a new entry for subdomain.domain.com. We used &#8220;stor.example.com&#8221;.

3. On the internal network, log in to the machine that is public facing => ours is a web server we use to host our website.

4. Open IIS if that's what you use and &#8220;Create a new site&#8221;. We did this and called it &#8220;stor&#8221;:

  <img class="alignnone size-full wp-image-699" src="https://automationadmin.com/assets/images/uploads/2016/09/setting-up-an-external-fileshare.png" alt="setting-up-an-external-fileshare" width="395" height="224" srcset="https://automationadmin.com/assets/images/uploads/2016/09/setting-up-an-external-fileshare.png 395w, https://automationadmin.com/assets/images/uploads/2016/09/setting-up-an-external-fileshare-300x170.png 300w" sizes="(max-width: 395px) 100vw, 395px" />

5. Login to the domain controller. Go to DNS (A or AAAA)= stor on x.x.x.x where x = IP address of your web server

6. Go to https://www.guidgenerator.com/ and copy a random GUID.

7. Now go back to the web server and create a folder with the name of the random GUID under the new directory &#8220;stor&#8221; and place whatever files in it.

   - It is not necessary to create a random GUID folder when sharing files publicly. We did this because we don't want average internet browsers to access these files on our site. The information is not sensitive and if someone wanted the files they could get them => it's just a precautionary measure.

8. Now it's time to test. Access it from web browser on internal network. http://webserverhostname/stor/random-guid/filename. Do you get a download prompt?

9. Wait 10 minutes for DNS to propagate and try to access from computers outside the network. If so, send the link to whomever needs access to your files.