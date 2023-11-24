---
title: 'PS: Template Script'
date: 2016-11-27T07:20:14+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/ps-template-script/
tags:
  - Windows
tags:
  - Scripting-Powershell
  - Powershell-Designing
---
<!--more-->

### Description:

When writing PS Scripts, I find it helpful to come up with a template type system. Here is mine, feel free to modify for yourself.

### To Resolve:

1. These have been moved to my [Github](https://github.com/gerryw1389/powershell/tree/main/Other/templates)

2. [My current script](https://github.com/gerryw1389/powershell/blob/main/Other/templates/_current-template-w-logging.ps1) will create a folder in the script's running directory called `PSLogs` and will have a `2019-01-01-function-name.log` file associated with it. The good thing about this setup is that since it uses `Start-Transcript`, it will record any errors that would normally show on the console. This has been my template for the last two years!
 
3. Older scripts like the one that writes to the Event Viewer may be more practical for you, what they do is:
   - It creates a file at `c:\scripts\scriptname` automatically for each script.
   - It writes to the `Application` log in the Windows Event Viewer so it is easy to query. This is great as you will always be able to tell: if your script ran, if it completed, if it had errors, and it can output variables which change each time the script runs. You can easily integrate this in a log aggregation system.
   - It logs statements like comments.

4. Before using this template, please make sure to go over [Begin, Process, and End](https://automationadmin.com/2016/06/ps-software-commands/) in Powershell scripts. For details on how you can use this template to create scripts that run against multiple machines, check out my post on [Running Scripts Against Multiple Computers](https://automationadmin.com/2017/09/running-ps-scripts-against-multiple-computers/)