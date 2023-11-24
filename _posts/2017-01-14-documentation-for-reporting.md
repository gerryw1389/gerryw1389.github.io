---
title: Documentation For Reporting
date: 2017-01-14T08:36:56+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/01/documentation-for-reporting/
tags:
  - SysAdmin
---
<!--more-->

### Description:

A big part of systems administration is producing reports for your management team to let them know what it is you do. This is especially true if you have a solid grasp on your network as users will think since they don't see you, you are not doing anything.

### To Resolve:

1. For starters, learn to use Powershell to [send you reports](https://automationadmin.com/2016/05/basic-powershell-to-html/) to your mailbox at regular intervals.

2. Think of ways to collect Windows logs, networking bandwidth statistics, uptime charts, etc. from your monitoring solution. The goals is to get it to spit out a series of reports that you can then find ways to present to management.

3. Examples:

   - Error logs for Windows Events = Types, aggregate total, what you did (hopefully created tickets that proactively treated an issue before it arose)
   - Network Bandwidth logs over time
   - Computer patch status
   - Closed support tickets and their categories
   - Vendor support tickets

4. Get a list of your current assets and find a way to make metrics from them:

   - How many sysadmins do we have?  
   - How many users do we provide service to?  
   - How many machines do we manage?  
   - How much total disk space? RAM? CPU cores?  
   - How many open tickets are in our ticket system right now?  
   - How many new tickets were created since last month?  
   - Who (or what department) opened the most tickets this month?  
   - What was the tickets per sysadmin average last month?  
   - Pick 4-5 important SLAs and record how close you were to meeting them.  
   - How much Internet bandwidth was consumed last month?

5. Example Report:

   - Subject: Weekly IT Action Items
   - Support Tickets: This week there were 103 trouble tickets. 80% were resolved within 15 minutes. 30 of the tickets were confusion about the new version of X software so I've made a quick guide available on the Intranet for easy reference. 15 tickets were hardware problems with our old scanner that may need to be replaced.
   - Software Updates: This week there were 14 Windows updates released. After testing, I logged into the network at 2:00AM Wednesday to install them without causing any network downtime for any employees.
   - Hardware Upgrades: The computers in accounting were taking too long to run their excel reports so I've upgraded them and reduced the time wasted waiting for them to run by 25%.
   - Planned Items: The email system is still on track to be upgraded over the weekend of Oct 17th. I'm researching the most cost efficient solution to upgrade our scanner.


6. Get in a habit of talking to management like:

   - Right now it takes the PC 6 minute to start up, 3 minutes to open Outlook, and 2 minutes to open a web browser. Thats 11 minutes of a user sitting there waiting, just in the morning.
   - Then it takes 3 minutes for it to unlock each time they come back from lunch, and an hour when they reboot for updates.
   - At $20/hr that employee wastes $$ just waiting for a slow PC.
   - Buying a new PC with an SSD for $800 would be payed back in 237 days just in employee time equals dollars saved.
   - Thats how you have to calculate and present it. &#8220;Because its slow&#8221; sounds like a complaint &#8220;because spending $800 will save you money six months from now&#8221; sounds like a great thing.

### References:

["3. Does the team record monthly metrics?"](http://www.opsreportcard.com/section/3)