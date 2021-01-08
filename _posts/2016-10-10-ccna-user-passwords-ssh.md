---
title: 'CCNA: User, Passwords, SSH'
date: 2016-10-10T03:16:31+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/ccna-user-passwords-ssh/
categories:
  - Networking
tags:
  - Router
  - CCNA
---
<!--more-->

### Description:

Banners, passwords, ect

#### To set the banner message (you will see this locally and remotely!)

   ```tcl
   banner motd (banner start identification) banner message (banner end identification)
   Example:
   banner motd $***Unauthorized access to this device is prohibited!***$
   # The above command with set the banner to "Unauthorized access to this device is prohibited"
   ```

#### Device Passwords:

1. To setup an Enable password

   ```tcl
   Router(config)#enable password cisco
   Router(config)#exit
   Router#show run
   # You can see the phrase "enable password cisco" in the output, not good
   ```

2. To setup a enable password with light encryption

   ```tcl
   Router(config)#enable password cisco
   Router(config)#service password-encryption
   Router#show run
   # You can see the phrase "enable password 7 0822455D0A16", better - but still easy to break
   ```

3. To setup a secret password

   ```tcl
   Router(config)#enable secret cisco
   Router(config)#exit
   Router#show run
   # You can see the phrase "enable secret 5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0", best
   ```

#### What if you already set an enable password? How to switch to secret?

   ```tcl
   Router(config)#no enable password
   Router(config)#enable secret cisco

   Router(config)#do show run # you can now see that your secret password is encrypted
   ```

#### To create a key (used by some commands like those in FHRPs):

   ```tcl
   Router(config)#key chain GERRY
   Router(config-keychain)#key 0
   Router(config-keychain-key)#key-string ciscoROCKS!
   Router(config-keychain-key)#accept-lifetime 09:29:00 16 Jan 2017 infinite # this tells it to accept the key starting this day indefinitely. You would ideally set this to the current date.
   # to use, you will just type "key 0" in whatever interface command asks for it.
   ```

---

#### Console/VTY Passwords:

#### To configure passwords for logins:

   ```tcl
   R1(config)#line vty 0 15
   R1(config-line)#password cisco
   R1(config-line)#login # this will require a login password for people telnetting/ssh'ing into the router
   R1(config-line)#exec-timeout 10 # Sets time out period to 10 minutes, example exec-timeout 0 0 is commonly used to disable timouts for console, but 5 min for vty
   ```

#### To configure login names and passwords for logins:

   ```tcl
   R1(config)#line con 0
   R1(config-line)#username paul password cisco
   R1(config-line)#login local #requires a local user account to be used
   ```

#### Using ACLs to Limit remote connections:

   ```tcl
   #The following example defines an ACL permitting Telnet traffic from host 10.10.10.1, which will then be applied inbound to the VTY lines:
   Router(config)#ip access-list extended VTY_ACCESS
   Router(config-ext-nacl)#permit tcp host 10.10.10.1 any eq telnet
   Router(config-ext-nacl)#deny tcp any any
   Router(config-ext-nacl)#exit
   Router(config)#
   Router(config)#line vty 0 15
   Router(config-line)# access-class VTY_ACCESS in
   Router(config-line)#end
   Router#show run | sect line vty
   ```

---

#### Creating Users:

   ```tcl
   username (username) privilege (0-15) password (password)
   username (username) exec level (0-15) command
   Typically, you would do something like:
   Router#config t
   Router(config)#username gerry password cisco
   Router(config)#username billy password cisco
   Router(config)#username jon password cisco
   Router(config)#line vty 0 15 # this will configure all vty lines at once
   router(config-line)#login local
   router(config-line)#exit
   router(config)#exit
   ```

#### Cisco routers have 16 security levels 0-15 where 15 is full access. Example:

   ```tcl
   router#config t
   router(config)#username support privilege 4 password soccer
   router(config)#privilege exec level 4 ping
   router(config)#privilege exec level 4 traceroute
   router(config)#privilege exec level 4 show ip interface brief
   router(config)#line console 0
   router(config-line)#password basketball
   router(config-line)#login local #means password is needed
   ```

---

#### Configuring SSH (and disabling Telnet):

   ```tcl
   Router#show version # make sure it says something about crypto features
   Router#config t
   Router(config)#ip domain-name test.pvt # enter your domain name
   Router(config)#hostname R1 # make sure to set the hostname before generating the private key as it is based on the name of the router.
   Router(config)#ip ssh version 2
   Router(config)#crypto key generate rsa # enter the highest number for the modulus, it has to be above 1024 for ssh version 2. Enter this even if it suggests 512.
   Router(config)#ip ssh time-out 60 # sets the timeout period to 60 seconds
   Router(config)#ip ssh authentication-retries 2 # ssh will reset after 2 failed attempts.
   ```

#### Checking SSH Sessions:

   ```tcl
   Router# Show ssh sessions # get the session ID field number for who you want to disconnect.
   Router# ssh disconnect (session ID)
   ```

#### To apply to VTY Access:

   ```tcl
   R1(config)#line vty 0 15
   R1(config-line)#password cisco
   R1(config-line)#login # this will require a login password for people telnetting/ssh'ing into the router
   R1(config-line)#exec-timeout 10 # Sets time out period to 10 minutes, example exec-timeout 0 0 is commonly used to disable timouts for console, but 5 min for vty
   R1(config-line)#transport input ssh # This is all you need to enable SSH! If you type this, it only enables SSH and disables telnet. If you want both type "transport input ssh telnet" altogether.
   ```

#### A Similar Example:

   ```tcl
   Router#show ip ssh # see if it is possible
   Router#config t
   Router(config)#ip domain-name test.pvt
   Router(config)#hostname R1
   Router(config)#username gerry password cisco
   Router(config)#crypto key generate rsa # enter 2048
   Router(config)#ip ssh version 2
   Router(config)#ip ssh time-out 60 # sets the timeout period to 60 seconds
   Router(config)#ip ssh authentication-retries 2 # ssh will reset after 2 failed attempts.
   Router(config)#line vty 0 15
   Router(config-line)#transport input ssh
   Router(config-line)#login local
   ```

#### To disable SSH:

   ```tcl
   Router(config)#crypto key zeroize rsa
   ```

#### To start a connection to another server:

   ```tcl
   Router#telnet 10.0.0.1
   Router#ssh 10.0.0.1
   ```

#### Show Commands:

   ```tcl
   show crypto key mypubkey rsa # to view your public key
   show ip ssh # to see what version you are running
   show sessions # shows active telnet sessions
   ```

