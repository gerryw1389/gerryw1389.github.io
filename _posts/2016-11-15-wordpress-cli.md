---
title: WordPress CLI
date: 2016-11-15T05:13:31+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/wordpress-cli/
tags:
  - LocalSoftware
tags:
  - WebServer
---
<!--more-->

### Description:

As someone who is always messing up my WordPress site, I found a neat tool that can help me get my site back without messing with PHPMyAdmin. It's called wp-cli and many people swear by it.

### To Resolve:

1. First step is to download and install it:

   ```shell
   sudo curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar  
   sudo chmod +x wp-cli.phar  
   sudo mv wp-cli.phar /usr/local/bin/wp  
   # The following gets info on your install and makes sure it is working
   wp info   
   wp cli update
   ```

2. Now for the real power! I can get my site back in a few commands:

   ```shell
   wp search-replace 'example.dev' 'example.com' --skip-columns=guid  
   # or  
   wp option update home http://example.com  
   wp option update siteurl http://example.com  
   # if you want to see your current site URL, type:  
   wp option get siteurl
   ```

