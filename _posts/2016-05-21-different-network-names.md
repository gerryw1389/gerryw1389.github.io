---
title: Different Network Names
date: 2016-05-21T22:06:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/different-network-names/
categories:
  - Networking
  - SysAdmin
---
<!--more-->

### Description:

Sometimes you will run into a setup where they have different network names on the same network. It is a common thing for this to happen, especially if they have wired and wireless connections. The name plays no significant role, what you have to find out is:

### To Resolve:

1. Is there any networking issues? Can you map drives to the server? Access the internet? Ping other computers on the same subnet?

2. Are all computers are on the same workgroup/ domain?

3. Is there any special Firewalls or Anti-Virus hardware/ software that could change network names? Note that it could be the sharing configuration settings are off on different computers, see below.

### Windows 7 P2P Networks Have 3 Sharing Configurations:

1. HomeGroup => Works only between Win 7 computers. This type of configuration makes it very easy to Entry Level Users to start Network sharing.

2. Home Network or Work Network => Basically similar(and better) to the previous methods of WorkGroup sharing that let you control what, how, and to whom folders would be shared with.

3. Public Sharing => Public Network (like Internet cafe) to reduce security risks.