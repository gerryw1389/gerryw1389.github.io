---
title: Windows Time Issues
date: 2016-05-28T06:18:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/windows-time-issues/
tags:
  - Windows
---
<!--more-->

### Description:

Sometimes, to resolve networking issues, you will notice that Windows Time can play a significant role and is usually overlooked. Follow these steps to get a computer to get back on the correct time.

### To Resolve:

1. Run => `timedate.cpl` => Find the name of the time server in the Internet Time => Change Settings tab.

2. Try to ping the name of the time server.

3. If it doesn't work, [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) 

   ```escape 
   net stop w32time
   w32tm /unregister
   w32tm /register
   net start w32time
   ```

4. If you get &#8220;Access Denied&#8221; messages anywhere in there, just try going back to `timedate.cpl` and changing the servers to one of these:

   ```escape
   ts1.aco.net  
   nist1-la.WiTime.net  
   ntp.alaska.edu  
   utcnist2.colorado.edu  
   tick.ucla.edu  
   tick.usno.navy.mil
   ```

5. For me, the issue was resolved on the last step. After changing the time server, it worked right away!

6. Update 2018-02: The PDC should configure time like:

   ```escape
   w32tm /config /manualpeerlist:'0.pool.ntp.org, 1.pool.ntp.org, 2.pool.ntp.org' /syncfromflags:manual /reliable:yes /update  
   net stop w32time && net start w32time  
   w32tm /resync /rediscover  
   w32tm /query /status
   ```

   - All other domain computers should be:

   ```escape
   w32tm /config /syncfromflags:domhier /update  
   w32tm /resync /rediscover  
   net stop w32time && net start w32time
   ```

7. But I wanted to include a little more info here.

   - First, make sure port 123 UDP is open for the server.

   - Second, if you run `w32tm /monitor` it should say `NTP -0` in a domain environment.