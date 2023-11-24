---
title: Installing SEPM
date: 2018-04-07T03:52:03+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/installing-sepm/
tags:
  - LocalSoftware
---
<!--more-->

### Description:

SEPM is the management &#8220;server&#8221; application for SEP (Symantec Endpoint Protection) clients. I did the following steps to install.

### To Resolve:

1. Install Symantec Manager by following the wizard.

2. Import the license

3. Create groups: Office, Servers, Remote

4. Clients => Group you want to set up password protection => Policies tab => Under Location-independent Policies and Settings => Password Settings.

5. From here, it is installed. We have two options => deploy a fresh client or upgrade an existing client.

   - To upgrade: Upgrade clients = Admin => Install Packages => Tasks => Upgrade clients with package
   - To install clients through [remote push](https://support.symantec.com/en_US/article.HOWTO124411.html#v116381837)

### Post install:

1. Check definitions: Home => Endpoint Status => Windows Definitions => compare dates Latest from Manager / Latest From Symantec.

2. Check backup settings: Admin => Servers => Local Site (My Site) => localhost => Tasks => Edit Database Properties => Backup Settings