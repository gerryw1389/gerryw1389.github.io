---
title: Windows Event Viewer Errors To Ignore
date: 2016-05-26T04:09:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/windows-event-viewer-errors-to-ignore/
categories:
  - Windows
tags:
  - Monitoring
---
<!--more-->

### Description:

You shouldn't ever ignore errors, but there are some that will show up a lot that may be false alarms:

### Examples:

1. Errors regarding &#8220;Service Control Manager&#8221; => This means service failed to start. This is common when you were just in Safe Mode. If in regular Windows, check and see what caused the service not to start. Look at dependencies in `services.msc`.

2. Errors regarding &#8220;Time Service&#8221;: Run => cmd w32tm /resync see if that works. These can be signs of networking issues since Windows has to ping the time server to get an updated time every so often.

3. Errors like &#8220;Session Circular Kernel Context Logger&#8221; failed to start with the following error: 0xC0000035&#8243;: This error is safe to ignore, if you really want to get rid of it, try renaming this file: `%windir%panthersetup.etl` to `setup.old` and reboot.