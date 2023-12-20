---
title: New To Powershell?
date: 2018-02-23T16:35:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/02/new-to-powershell/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

A lot of times someone will say, "Hey Gerry I'm just now learning Powershell but I don't know what I can test it on?". I know for me, I first got hooked with powershell once I realized that you can run a single script and it could [set hundreds or thousands of settings to configure your Windows install](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-Template.ps1) and [part 2](https://github.com/gerryw1389/powershell/blob/main/gwConfiguration/Public/Set-HomePC.ps1). It just blew my mind that I could take a fresh Windows install and set all the things I used to do manually in the GUI (slow/error prone). It was that moment that I realized I would probably never want to use the GUI again if I had a choice! Anyhow, here is my common response:

### To Resolve:

1. Main Response:
   - Read [reddit.com/r/powershell](https://reddit.com/r/powershell) but please, please, please search your question before asking! 
   - Specifically, follow [this thread](https://www.reddit.com/r/PowerShell/comments/9c5vib/what_have_you_done_with_powershell_this_month/) for examples

2. Second response: Read 'Powershell in a month of lunches'

3. Third, I've heard of using modules like [PSKoans](https://github.com/vexx32/PSKoans), but I prefer you start with tackling stuff in your environment. Do each of these and if you don't know how, just google `powershell $example` where example is the task you want to accomplish:  

   - Write a script that will pull event logs from all the systems that you manage and report on the 10 most common errors. Then for each of those, write a script for each that will detect\identify the root cause. Then write a script that will correct the root cause. Then repeat. Not only does that give an endless supply of tasks, you gain a very intimate understanding of your environments issues.
   - Create a template like system where you pass in just what you need and it expands out the full commands.  
   - Display some static text  
   - Display the current date/time  
   - Display some information about the local system  
   - Print the first input parameter  
   - Display every 5th number between two given numbers  
   - Check if a file exists  
   - Check if that file contains a line with specific text  
   - Add a new line to the text file  
   - Output the above items in JSON format  
   - Query all servers to get the version of AntiVirus and the last time it was updated.  
   - Logon script that adds, removes, and sets default printers based on AD Groups.  
   - Reset AD Password to random generated password and emails it to the user.  
   - Automatically disable any AD account that has not been used in 90 days.  
   - Query all servers for any services or application pools running under a domain admin account.  
   - Check all services on servers with a startup type of Automatic and start any that have stopped.  
   - Delete any snapshots on AWS that are over 14 days old.  
   - Optimize a Virtual Desktop gold image in a single command.  
   - Dynamically create and update a HTML page for an employee directory complete with picture, name, extension, and email.  
   - password expiry notifications for users and create reporting for you or anyone dealing with AD in any way  
   - user and group membership,  
   - mailbox statistics with ActiveSync devices usage,  
   - audit of file shares,  
   - service accounts),  
   - cleanup jobs (unused computer accounts, DNS records, ActiveSync devices)  
   - resetting permissions on userhome folders.  
   - fixing corrupted permissions on several other folders.  
   - What if your company acquires a another company and you need to mass import users?  
   - Mass importing/exporting contacts to/from Exchange.  
   - Emergency push of an update to multiple computers.  
   - Audit folder and file permissions etc.  
   - We had to migrate a few thousand users from physical PCs to a VDI environment. I wrote a PowerShell script to:  
   - Backup the users' PC  
   - Reimage the users' PC as a pseudo thin client & move to new OU  
   - Move the users' personal drive to a new server  
   - Tidy up the users' folder structure  
   - Move the users' account to a new OU  
   - Set a bunch of user settings - 
   - Unlock accounts  
   - Get mailbox status reports by user  
   - Find and fix users who don't have quotas set or override default quota  
   - Find out which users are not syncing mobile email on their phone that are required to.  
   - Report on and fix accounts with things like password never expires.  
   - Verify, add, or uninstall specific hotfixes against servers.  
   - Expired password and/or locked password account reports.  
   - Generate reports of servers/workstations which are low on disk space.  
   - Find and remove old user profiles regularly from workstations and servers.  
   - Scan and force workstations reboots if they haven't rebooted in a week.  
   - Report on AD group membership changes for key groups.  
   - Find accounts which haven't logged on in X days and remove/disable/expire them (usually vendors or contractors)  
   - Report on changes to AD OU objects.  
   - Run cleanup scripts against remote workstations to make sure no users (or only allowed users) in local admin or power user groups. Report any anomalies.  
   - email users to tell them they have to change their passwords. The script also sends me a report so if I know if somebody is going to get locked out, I can stop it before it happens.  
   - upload old files to aws and send me a report.  
   - delete old files.  
   - run and distribute an excel report to the sales team.  
   - Set expiry for user accounts, with PS you can set it to the minute instead of just the end of the day.  
   - Check for and remove email forwarding rules when staff leave  
   - NTFS permissions reports ( they get gussied up in excel)  
   - Setting exchange mailbox permissions  
   - Checking for locked users, unlocking them  
   - Reporting on user mailbox sizes  
   - Reporting the devices users have connected with through activesync  
   - Anything you do in ADUC, do it in powershell instead. Start with a basic command, then build on it. If your scripts are always using hard coded variables, change them to take arguments. Then work on error - handling and throw in some output logging. The http://powershellcookbook.com is a pretty good investment.  
   - This is what I did. It was the easiest way for me to learn. I use Get-ADUser, Add-ADGroupMember, and Get-ADPrincipalGroupMembership all the time.  
   - It's also a great tool to use if you need to remove X security group from Y number of users or any other kind of batch operation.  
   - A script that automates the process of setting up a loaner laptop (clears profiles, runs some updates, etc).  
   - A script that runs a network speed test on a machine using iPerf and outputs results + other network information to a Cisco Webex Teams chat channel for viewing, mainly used to verify network connectivity on new - computer setups.  
   - A script that filters an Excel spreadsheet containing print job history to see what printers are being used most often as well as what users are printing to them.  
   - A script to re-create the assigned ports for printers on our old print server that were set up to use WSD ports => it assigns a TCP/IP port using the IP address gathered from the WSD port configuration.  
   - Various other small one-off scripts to automate manual data evaluation that would otherwise take a significant amount of time.  
   - A suite of installation scripts for my PowerShell profile/dev environment.  
   - Resetting AD passwords and sending temporary password and instructions  
   - AD user account creation and provisioning based on data from our HR system's API  
   - Terminations => disabling AD User, converting mailbox to shared in O365 and recovering license, setting autoresponse on their email  
   - Non-domain-joined computer setup (we inherit PCs often)  
   - Migrating mailboxes to Office 365  
   - Reporting Hyper-V Replication status  
   - Auditing inconsistencies, such as comparing our HR data to AD attributes  
   - A script that automates the process of setting up a loaner laptop (clears profiles, runs some updates, etc).  
   - A script that runs a network speed test on a machine using iPerf and outputs results + other network information to a Cisco Webex Teams chat channel for viewing, mainly used to verify network connectivity on new computer setups.  
   - A script that filters an Excel spreadsheet containing print job history to see what printers are being used most often as well as what users are printing to them.  
   - A script to re-create the assigned ports for printers on our old print server that were set up to use WSD ports => it assigns a TCP/IP port using the IP address gathered from the WSD port configuration.  
   - Various other small one-off scripts to automate manual data evaluation that would otherwise take a significant amount of time.
   - **The list is virtually unlimited.. Powershell can have a Windows system do just about anything. Be sure to check out my [Github](https://github.com/gerryw1389) for any scripts that may be useful in your environment!**

4. As a shameless self promotion, [this site](https://automationadmin.com/tags/#powershell) is great for powershell examples as well!