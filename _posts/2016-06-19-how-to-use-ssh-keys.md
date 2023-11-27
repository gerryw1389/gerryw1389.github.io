---
title: How To Use SSH Keys
date: 2016-06-19T07:30:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/how-to-use-ssh-keys/
tags:
  - Linux
  - Security
  - PKI
---
<!--more-->

### Description:

SSH is an encrypted protocol that is often used for remote management in Linux and networking devices. Windows will probably implement SSH natively in the next few years as well.

### To Resolve:

1. Generate a keypair on Box1.

   ```shell
   ssh-keygen -t dsa
   ```

2. Now, you can put the public half of the key pair into the &#8220;authorized_keys&#8221; file in your account on another box, and after you do so, you'll use the key to log in, not your password.

   - Your key:

   ```shell
   cat ~/.ssh/id_dsa.pub
   ```

   - That's your public key.

   - You can copy it to Box2:

   ```shell
   cat ~/.ssh/id_dsa.pub | ssh you@box2 'cat >> ~/.ssh/authorized_keys'
   ```

   - You can just copy and paste it from the shell into a text editor like nano.

   ```escape
   ssh Box2  
   password:  
   vi ~/.ssh/authorized_keys
   # Paste in your copied password and save it, then exit the session.
   ```

   - The next time you ssh into Box2, it won't ask you for a password at all because it's using your ssh key pair for authentication:  

   ```escape
   ssh Box2  
   you@Box2:~$
   ```


3. You can use the same key you generated on Box1 to get you into Box3, as well => even if your user account on box3 is under an entirely different name:

   ```shell
   you@box1:~$ cat ~/.ssh/id_dsa.pub | ssh me@box3 'cat >> ~/.ssh/authorized_keys
   me@box3's password:
   you@box1:~$ ssh me@box3
   me@box3:~$
   ```

4. Add the following to your .ssh/config:

   ```shell
   Host *+*
   ProxyCommand ssh $(echo %h | sed 's/+[^+]*$//;s/([^+%%]*)%%([^+]*)$/2 -l 1/;s/:/ -p /') nc -q0 $(echo %h | sed 's/^.*+//;/:/!s/$/ %p/;s/:/ /')

   # It lets you ssh directly along a chain of hosts, for example:
   ssh jumphost1+jumphost2+destination
   ```