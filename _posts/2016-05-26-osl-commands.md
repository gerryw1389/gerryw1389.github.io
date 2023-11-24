---
title: OSL Commands
date: 2016-05-26T04:00:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/osl-commands/
tags:
  - Linux
  - SysAdmin
tags:
  - LinuxClient
  - OneLiners-Bash
---
<!--more-->

### Description:

Upon installing OpenSuse (OSL => Open Suse Linux) and reading the beginners guide at [opensuse-guide](http://opensuse-guide.org/), I found a list of new zypper commands:

### To Resolve:

   ```shell
   # Lists currently installed packages (without version)
   rpmqpack

   # Lists currently installed packages (with full version and architecture)
   rpm -qa –qf '%{name}-%{version}-%{release}.%{arch}n'

   # Gives you an OBS URL to the exact sources for the package PACKAGE. You can, for instance, check them out with osc co DISTURL
   rpm -q –qf "%{DISTURL}n" PACKAGE

   # List all packages explicitly installed
   awk -F| '$6 && $2 == "install" {print $3}' /var/log/zypp/history

   # Runs zypper shell, no need to type zypper for each command
   zypper sh

   # Simulate (Dry run) an upgrade on all active repositories
   zypper -v dup -D 

   # Makes debian users feel at home
   zypper moo 

   # Journald is replacing the old logging technologies in openSUSE (at least for most common cases). The two most important commands you need to know:
   # The old "cat /var/log/messages"
   journalctl 

   # The old "tail -f /var/log/messages"
   journalctl -f
   ```

