---
title: Cisco Routers
date: 2016-05-21T05:09:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/cisco-routers/
tags:
  - Hardware
---
<!--more-->

### Description:

It will be a difficult task to imagine networks without Cisco routers and switches, they are just everywhere. That being said, here is a general overview on Cisco routers:

### To Resolve:

Cisco routers have different modes and certain commands that you have to run for each mode. Here they are:

1. User mode => First mode you enter when the router boots. It's the basic low priv mode. Output should say `Router>` or something like that.

2. Privileged Mode => Typing `enable` at the user mode prompt takes you to this mode after you enter the enable password. You type `disable` to return to user mode and `logout` or `exit` to leave altogether. Prompt may look like `Router#` at this mode.

3. Global Configuration Mode => You type `configure terminal` or config t for short at the privileged mode prompt. It should look like `Router(config)#` at this prompt.

4. Interface Configuration Mode => This mode allows you to enter commands for specific router interfaces. It is entered by typing `interface (interface name)`. The prompt will look like `Router(config-if)#`

5. Line Configuration Mode => This mode is used to make changes to the console, Telnet, or aux ports. You can control who can access the router via these ports as well as put passwords or a security feature called `access control lists` on them. Ex command `line console 0` will enter this mode. Ouput will look like `Router(config-line)#`

6. Router Configuration Mode => This mode is used to configure protocols. Ex: `router rip` changes the prompt to `Router (config-router)#`

7. VLAN Configuration Mode => This mode is only on switches, but it's worth mentioning here. You would type `config t` and then `vlan 10` for instance to access features of a VLAN. Routers equipped with Ethernet switch cards will use VLAN Database Configuration Mode which is similar to the switches VLAN Config Mode. You would run `vlan database` and then `vlan 10` to add vlan 10 to the list.

8. Configuring a router: At the most basic, type a `?` to get a list of commands for each mode. You tap the spacebar to see `more` and you type `q` or Ctrl+Z to get back to the command prompt. The prompt enables tab completion and wildcard completion as well.

10. If you want to configure an interface, you can type `interface ?` after the enable and config t prompts. Most people only use FastEthernet, Serial, and Loopback so don't be discouraged by the long list.