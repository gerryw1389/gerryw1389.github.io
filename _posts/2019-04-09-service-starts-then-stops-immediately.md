---
title: Service Starts Then Stops Immediately
date: 2019-04-09T20:12:56+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/service-starts-then-stops-immediately/
categories:
  - Windows
---
<!--more-->

### Description:

For Windows Servers, sometimes applications will start and then stop a second later. Event Viewer will not show any helpful messages. Try these steps to troubleshoot.

### To Resolve:

1. Get the service name

2. Go to the directory of the executable by looking at the service path

3. Look for a license file, open up in notepad (.lic)

   - Look at what port the service is set to listen on => sometimes this can be found in the config file in the same directory as the executable.

4. Run &#8220;netstat -ano&#8221; to find the port number and what is listening. Then lookup the PID.

5. Open Task Manager => Processes tab => Add columns => PID and Image Path.

6. Now sort by PID and kill it. If it doesn't work, try through command line: taskkill /pid pid /f

7. Now try to start the service again.