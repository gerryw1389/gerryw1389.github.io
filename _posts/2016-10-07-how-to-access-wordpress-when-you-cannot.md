---
title: How To Access WordPress When You Cannot
date: 2016-10-07T04:14:33+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/how-to-access-wordpress-when-you-cannot/
categories:
  - LocalSoftware
tags:
  - WebServer
---
<!--more-->

### Description:

I know the title is confusing on this one, but essentially here is the issue: You are in WordPress under General and you change the Site Home or Site URL and now you can't access the site.

### To Resolve:

1. Install PHPMyAdmin:  

```shell
sudo yum install phpmyadmin  

#restart apache  
sudo service httpd restart
```

2. Go to the web gui `http://127.0.0.1/phpmyadmin`

3. Go to your wordpress database name on the left column => Then click on the wp_options table => Click on edit next to site url and site home => Edit them and then click `go` for them to run. Problem solved!