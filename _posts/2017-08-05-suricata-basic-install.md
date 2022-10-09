---
title: Suricata Basic Install
date: 2017-08-05T05:32:03+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/suricata-basic-install/
categories:
  - Linux
---
<!--more-->

### Description:

I call this one a basic install because that's all it really is. I haven't configured anything as of yet => an IDS comes with lots of learning!

### To Resolve:

1. Clone my base CentOS image, give it a static IP, and set its hostname (sudo hostnamectl set-hostname ids)

2. Type:

   ```shell
   su

   yum install epel-release

   yum -y install gcc libpcap-devel pcre-devel libyaml-devel file-devel \

   zlib-devel jansson-devel nss-devel libcap-ng-devel libnet-devel tar make \

   libnetfilter_queue-devel lua-devel

   wget http://www.openinfosecfoundation.org/download/suricata-3.1.tar.gz

   tar -xvzf suricata-3.1.tar.gz

   cd suricata-3.1

   ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --enable-nfqueue --enable-lua

   make

   make install

   ldconfig # not sure if needed

   make install-full
   ```

3. Now set it up:

   ```shell
   vi /etc/suricata/suricata.yaml

   # set home network ip, save and exit.
   ```

4. Test it by running it on your NIC:

   ```shell
   sudo suricata -c /etc/suricata/suricata.yaml -i enp0s3 --init-errors-fatal
   ```

5. To see if it is working:

   ```shell
   cd /var/log/suricata

   tail -f http.log

   tail -fn 50 stats.log
   ```

6. Mine had some errors about &#8220;tls-events.rules&#8221; so I went back to the /etc/suricata/suricata.yaml and found that line and commented it out. Started seeing logs. That's about as far as I got for now&#8230;

7. Next task: Find a GUI front end as this is the server piece. Also need to tweak for my network.