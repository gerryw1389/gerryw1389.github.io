---
title: Command Prompt Not Running Commands
date: 2016-05-30T05:48:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/command-prompt-not-running-commands/
tags:
  - Windows
tags:
  - Batch-Commands
---
<!--more-->

### Description:

If you open up the Command Prompt and everything you enter is replying with an error like &#8220;not recognized as a batch file&#8230;&#8221; then try these steps.

### To Resolve:

1. Start menu => type &#8220;cmd&#8221; or find the &#8220;Command Prompt&#8221; icon- right click and &#8220;run as&#8221; administrator.

2. It can also be environmental issues:

   - Open System Properties- Advanced- Environmental Variables
   - Find &#8220;path&#8221; and make sure it has the following: `%SystemRoot%system32;%SystemRoot%;%SystemRoot%System32Wbem;%SYSTEMROOT%System32WindowsPowerShellv1.0` at the very least. Programs register themselves in this path, but the main path for CMD is the system32 folder.
   - Click okay, close, run &#8220;cmd&#8221; and run a command. Should work.