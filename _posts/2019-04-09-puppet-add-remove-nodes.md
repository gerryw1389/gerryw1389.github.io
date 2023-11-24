---
title: 'Puppet: Add/Remove Nodes'
date: 2019-04-09T16:38:23+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/puppet-add-remove-nodes/
tags:
  - LocalSoftware
tags:
  - ConfigManagement
---
<!--more-->

### Description:

Follow this to install/uninstall Puppet on a client

### To Resolve:

1. To Install:

   - For Linux:

   ```powershell
   sudo su
   curl -k https://puppetserver.yourdomain.com:8140/packages/current/install.bash | bash
   ```

   - For Windows: We have this as part of the imaging process, but there is a similar PS script you can run from your puppet server.

2. To remove a node:

   - For Linux:

   ```powershell
   # on puppet master
   ssh root@yourpuppet.domain.com
   puppet node purge $hostnameWithoutFQDN
   scp /opt/puppetlabs/bin/puppet-enterprise-uninstaller root@yourclient.domain.com:/root/

   # On node:
   rm -rf /etc/puppetlabs/puppet/ssl
   rm -rf /etc/puppetlabs/mcollective/ssl/clients
   /root/puppet-enterprise-uninstaller
   ```

   - For Windows: Do the server part except transferring the uninstaller then on the node just use add/remove programs to uninstall.