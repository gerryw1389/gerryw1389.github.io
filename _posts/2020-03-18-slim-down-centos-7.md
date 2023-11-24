---
title: Slim Down Centos 7
date: 2020-03-18T07:18:46-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/03/slim-down-centos-7
tags:
  - Linux
tags:
  - Scripting-Bash
---
<!--more-->

### Description:

So my Plex server is already a minimal install, but I was looking for a way to slim it down even more. Here are some things I did:


### To Resolve:

1. Uninstall unneeded packages:
   
   ```shell
   # List packages smallest to largest
   rpm -qa --queryformat '%10{size} - %-25{name} \t %{version}\n' | sort -n
   or
   rpm -qa --queryformat '%10{size} - %-25{name} \t %{version}\n' | sort -nr | head -10

   # Remove orphans
   package-cleanup --quiet --leaves --exclude-bin | xargs yum remove -y
   package-cleanup --problems
   package-cleanup --cleandupes
   ```

2. Find largest files and see if they can be removed: `find / -type f -printf '%s %p\n'| sort -nr | head -10`

3. Will add here when I find more