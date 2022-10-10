---
title: Internet Running Slow
date: 2016-05-22T07:32:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/internet-running-slow/
categories:
  - Networking
---
<!--more-->

### Description:

Browsing to websites takes a long time. Browser is &#8220;stuck with the spinning circle&#8221;. If all computers experience this the first step is to find out if it's the modem or your local router causing the issue. ISP's will always have you do their test first which is to plug a single computer to the modem and run a speedtest, if it's fine, they tell you the issue is on your end and it's not their problem.

Their test:

1. Take a laptop or a computer that can reach the modem and place it on DHCP (Run => `ncpa.cpl` => Local Area Connection => Right Click => Properties => Internet Protocol Version 4 Properties => Properties => Automatically Obtain... for both IP and DNS).

2. Take the cable going from the modem's Ethernet port to the router's WAN port and unplug it from the router and plug it in to the computer.

3. On the computer, [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `ipconfig`. It should have a different IP address assuming the modem's DHCP server is enabled properly. For me, I go from a 192.168.x.x to a 172.158.x.x.

4. Now ping google.com, if it is normal replies in normal times- that means the problem is internal (past the router), if it still takes a while => call the ISP. You should also go to Speedtest.net and run that. If it's local to one computer, check: Actual networking (cable/switch/setup), browsers, firewalls, antivirus, network card, and finally a virus scan.

### To Resolve:

1. Find out if networking is slow or their browser. Always start with a

   - [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `ping 8.8.8.8 -t`

   - Analyze the packets, are they less than 100ms? Chances are it's a browser issue if you see no drops and a decent connection. Confirm by going to speedtest.net or any speedtest website.

2. If it is the connection, start testing the possibilities: faulty cable, faulty switch port, or (rarely) faulty NIC on the workstation.

3. Most of the time it's a browser issue. Reset IE if they are using it: [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `inetcpl.cpl` => Advanced Tab => Reset => Make sure to leave the Delete Personal Settings unchecked. This should be one of the first steps for most IE issues. Firefox and Chrome have similar functions.

4. See if it's a network setup issue:

   - If the computer is on a domain, set the primary DNS to the DC's IP address and leave the secondary DNS blank.

   - If the computer is on a workgroup, set the primary DNS to the default gateway and the secondary to a public DNS server, I always use 8.8.8.8.

5. See if it's a cable/NIC issue: Use the keyboard shorcut `CTRL+SHIFT+ESC` to bring up the Task Manager (you can also Run => taskmgr). Navigate to the Networking Tab and check the link speed. Does it match those on the rest of the network? Remember a network typically matches it's slowest Link Speed.

   - [Run =>](https://automationadmin.com/2016/05/command-prompt-overview/) `devmgmt.msc` => find the Network Adapters => Right click on yours and check it's settings. Set everything to Automatic/ Negotiable.

6. If the computer has any kind of cloud backup, it can cause internet slowness. I can ping &#8220;google.com&#8221; with nothing running and get replies in the 20 to 70 ms response time, but if I have MediaFire or GoogleDrive running, my replies go up to about 700ms. The simple test is to pause your online sync and run a long ping to google.com, if it speeds up in around 5 minutes or so, you have your answer.

7. Check antivirus. Try disabling for a minute to see if connection improves.

8. If it is still running slow, check for a possible virus infection.