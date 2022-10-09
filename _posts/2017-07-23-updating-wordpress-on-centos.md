---
title: Updating WordPress On CentOS
date: 2017-07-23T04:22:45+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/updating-wordpress-on-centos/
categories:
  - Linux
tags:
  - WebServer
---
<!--more-->

### Description:

Updating WordPress is a manual process for me since I host it locally. Here are the commands I run:

### To Resolve:

1. Get the latest WordPress zip (or tar.gz) file: Download to my `~/Downloads` via Firefox. Sure I could curl/wget, but meh.

2. Unpack the zip file that you downloaded.

3. Deactivate plugins.

4. First, we want to remove what we need full replacements for (I use a `~/trash` folder instead of rm -rf) :

```shell
sudo systemctl stop httpd
cd /var/www/html
sudo mv wp-includes ~/trash
sudo mv wp-admin ~/trash
```

5. Now copy files from Downloads to site:

```shell
cd ~/Downloads
sudo tar -xzf wordpress(whatever... tab complete)
cd wordpress
sudo cp -R wp-includes /var/www/html/wp-includes
sudo cp -R wp-admin /var/www/html/wp-admin
#sudo cp -R wp-content /var/www/html/wp-content/wp-content
rsync -a -v --ignore-existing ~/Downloads/wordpress/wp-content /var/www/html/wp-content
sudo cp *.* /var/www/html/*.*

cd ..
sudo mv wordpress ~/trash
```

6. Lastly, we just set permissions to the site:

```shell
sudo chown apache:apache /var/www/html -R
sudo chown root:root /var/www/html/wp-config.php

cd /var/www/html
sudo find . -type f -exec chmod 644 {} +
sudo find . -type d -exec chmod 755 {} +
sudo chmod 644 wp-config.php

sudo systemctl start httpd
```