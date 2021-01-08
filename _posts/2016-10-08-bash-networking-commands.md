---
title: 'Bash: Networking Commands'
date: 2016-10-08T21:26:04+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/bash-networking-commands/
categories:
  - SysAdmin
tags:
  - OneLiners-Bash
  - Scripting-Bash
---
<!--more-->

### Description:

These commands have to do with networking in Linux distros.

### Networking Commands

#### To check your IP address

   ```shell
   ifconfig -a
   ```

#### To test connections to another network node

   ```shell
   ping (ip)
   ping google.com
   ```

#### To see a path a packet takes to its destination

   ```shell
   traceroute google.com
   ```

#### To query a DNS server

   ```shell
   dig -a google.com
   host google.com
   ```

#### To connect to a SSH server

   ```shell
   ssh (username@hostname) [command]
   ```

#### To download from any site

   ```shell
   wget www.example.com/example.tar.gz
   ```

#### To check open ports on a remote server without telnet (Used often!):

   ```shell
   # this will check if port 22 is open on 10.10.80.1
   curl -v telnet://10.10.80.1:22
   ```

#### To transfer files between linux boxes or Windows running WSL and a linux box (Used often!):

   ```shell
   # transfer foo.txt from current directory to remote /root/ location
   scp foo.txt  root@remotehost:/root/

   # transfer foo.txt from Windows c:\scripts to remote /root/ location
   scp /mnt/c/scripts/foo.txt  root@remotehost:/root/foo.txt

   # this also works in reverse! Transfer files from remote location locally
   scp root@remotehost:/root/foo.txt /mnt/c/scripts
   ```

#### To view a list of ports that are listening

   ```shell
   netstat -a

   netstat --all --listening --numeric --tcp
   netstat -natl

   # Checks to see if ssh is running
   netstat -antp | grep sshd
   ```

#### To use DNS Enumeration

   ```shell
   #!/bin/bash
   for url in $(cat cisco.txt) ;do
   host $url | grep "has address" | cut -d" " -f4
   done
   ```

#### To use Ping sweeper

   ```shell
   #!/bin/bash
   for ip in $(seq 200 210) ; do
   echo 192.168.31.$ip |grep "bytes from" | cut -d":" -f1 & #adding the ampersand allows the pings to run in parrallel. Much faster response time
   done
   ```

#### To use Forward zone lookup

   ```shell
   #!/bin/bash
   for name in $(cat list.txt) ;do
   host $name.megacorpone.com|grep "has address" | cut -d" " -f1,4
   done
   ```

   ```escape
   list.txt:  
   www  
   ftp  
   mail  
   owa  
   proxy  
   router  
   admin  
   www2  
   firewall  
   mx  
   pop3
   ```

#### To use Reverse zone lookup

   ```shell
   #!/bin/bash
   for ip in $(seq 72 91) ;do
   host 38.100.193.$ip |grep "megacorp" | cut -d" " -f1,5
   done
   ```

#### To use Zone transfer script

   ```shell
   #You run by ./zonetransfer.sh megacorpone.com or any other domain name.

   #!/bin/bash

   if [ -z "$1" ]; then
   echo "[*] Simple Zone Transfer Script"
   echo "[*] Usage : $0 "
   exit 0
   fi

   for server in $(host -t ns $1 |cut -d" " -f4) ;do
   host -l $1 $server |grep "has address"
   done
   ```

#### To verify email addresses against a SMTP server using Bash

   ```shell
   #!/bin/bash
   for user in $(cat list.txt) ;do
   echo VRFY $user | nc -nv -w 192.168.15.215 25 2>/dev/null | grep ^"250";
   ```

   ```escape
   list.txt: Usually from theharvester or info gathering stage.  
   root  
   backup  
   bob  
   dick  
   david  
   harry  
   apache  
   igor  
   ron  
   mike  
   joseph
   ```