---
title: Not Able To Remote In
date: 2016-05-22T07:34:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/not-able-to-remote-in/
tags:
  - Networking
---
<!--more-->

### Description:

Sometimes you will try remoting in to a workstation through RAS (Remote Access Software) and the computer will not let you in. This is usually do a browser redirect malware or browser settings and security.

### To Resolve:

1. Verify that the internet is working. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `ping google.com` or `ping 8.8.8.8`

2. If successful, [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `inetcpl.cpl` => Advanced Tab => &#8220;Reset&#8221; => Make sure to leave the &#8220;Delete Personal Settings&#8221; unchecked. This should be one of the first steps for most IE issues. Firefox and Chrome have similar functions.

3. If it still doesn't work, look at the time on the computer and make sure it matches others on the network. Time is a commonly overlooked setting in network authentication.

4. If it still doesn't work then look at the link speed on the workstation. Task Manager => Networking => Link Speed. Does it match others in the office? If not, you may have a bad ethernet cable.

5. Start looking at a possible virus infection. See [Jumping To A Computer Through the Internal Network](https://automationadmin.com/2016/05/jumping-to-a-computer-through-the-network/) to get in.