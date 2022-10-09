---
title: Network Documentation
date: 2016-11-15T03:03:30+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/network-documentation/
categories:
  - SysAdmin
---
<!--more-->

### Description:

Documentation is one of the main things you will have to do as a systems administrator. The good thing is, many people don't make it far in IT unless they are the organized type, so for most of us, it just comes naturally. This post is about the different things you should document in your environment.

### To Resolve:

1. Security Audit:

   ```escape
   How often does your software get patched? OS?  
   Is your AV valid & functional?  
   What does your firewall look like?  
   What do your 3rd party connections look like?  
   Physical security review. Locks on server/network rooms?  
   What services are running on what ports? Start with your servers  
   Do users have admin access on their workstations?  
   .. this list can go on forever as there is always ways to make things more secure.
   ```

2. Network Audit:

   ```escape
   IP subnet review. Is there any conflicts?  
   Routing protocol reviews. Is there any AS/Area number conflicts with EIGRP/OSPF?  
   Is your network edge security in proper order? What is allowed in/out?  
   VLANs? If not implemented, why not?  
   802.1x authentication?  
   Bandwidth capacity planning  
   How is it billed?  
   Domain registration/ DNS hosting / Certificate renewals?  
   Third party service like OpenDNS?  
   What ports are public facing? Are they DMZ'd off?
   ```

4. Hardware Audit:

   ```escape
   Life Cycle Planning Review  
   Maintenance Contract Review  
   Is anything near-death?  
   Are serial numbers tracked?  
   Do you have UPS units? Generator? Double check RPO/RTO documentation and see if you can make it better.  
   Cable management? Can they be organized?
   ```

5. Software Audit:

   ```escape
   Is your software tracked? Can you provide a license for each instance of installed software? Use [MS MAP](https://technet.microsoft.com/en-us/library/dd627342.aspx)  
   Is the cost perpetual, monthly, or paid for?  
   Is there anything hosted in the cloud?  
   If more than 5 computers, are you on a domain?  
   Do you manually image each machine?  
   Email => On premise? How many accounts? What are common SOP's regarding your mail server?  
   Email => Hosted? What are common SOP's from managing in the web GUI?
   ```

6. Monitoring System Audit:

   ```escape
   Is everything being monitored? What sensors?  
   Is there auditing? Do you have something in place for event logs / netflow / syslog ?
   ```

7. Documentation Audit:

   ```escape
   Here is some examples I have seen over the years:

   Password Sheet => Passwords for admin portals, client phone numbers, ect.  
   Server sheet => Documentation on each physical server, their Windows key, OS version, VM's hosted, disk space, ect. Much of this can be pulled from your monitoring system.  
   Domain Info => Public IP's, what's being hosted on what, ports opened  
   Employee List => Sheet of office employees (not needed in bigger companies)  
   Video Conferencing Rooms => A sheet that list rooms for users.  
   Task List => Tasks lists for your department  
   Change Control => A list of any change you make to any server/network device  
   Software Renewals => A list of what software needs to be renewed when. You should document every service your company uses here.  
   Network Overview => A list of all your LAN IP's and what is connected to what. Or just the main devices  
   IT Policies => See [my post](https://automationadmin.com/2016/11/it-policy-documentation/) on this

   Most of this can be pulled directly from your monitoring system, but some of it may be in spreadsheets or Word documents throughout your organization. One of the main tasks of administrators is to get this information together, centralize it, and place it somewhere secure on the network and back it up. Remember the principle of least privileges and know that in any down time, you can ALWAYS DOCUMENT MORE!
   ```

### Security Baseline

1. Networking/Ports  

   - Scan router for any ports that open WAN => LAN and close any not being used. If RDP is open, replace with a VPN solution => never have 3389 open!!  
   - Set antivirus on all computers to block all ports not needed => This is a huge one that will take lots of time. Mainly just look for things to improve like SFTP instead of FTP for example.  
   - Install/configure an IDS if possible

1. Limit Power => This is to restrict the amount of power users have on the network  
   - Remove Corp users from local admin rights => Doing this will stop most viruses right away  
   - Implement LAPS local admin account is reset at normal intervals and values stored in AD  
   - Enable UAC => UAC can notify users of apps that are changing permissions.

1. Restrict Access => Need to restrict access to the least amount of privilege  
   - Setup IT to have separate admin accounts Setup admin accounts for server access: a\_username and one for domain admin access d\_username  
   - Remove service accounts => Need to set up GMSA => https://blogs.technet.microsoft.com/askpfeplat////windows-server=>group-managed-service-accounts/  
   - Disable the built in Admin account  
   - Setup Unique Passwords For All Devices Switches, WAP, ect will need to have a unique password for each user  
   - Set certain machines to block internet access

1. Encryption  
   - Enterprise CA => Setup a Cert server => see https://www.starwindsoftware.com/blog/using-the-microsoft-certificate-authority-to-get-rid-of-those-self-signed-certs#more-7694  
   - Best practice is to have a 100% airgapped root CA issue a PUBLIC key certificate to an online enterprise issuing CA, turn it off, store in a safe with chain of custody procedures. You will need to use the root CA to generate a new CRL around 2-3 times per year.  
   - Bitlocker => Encrypt data at rest NTserver, Fileserver, backups  
   - Encrypt LAN traffic Enable SSL over AD => https://www.google.com/search?q=encrypt+ldap+traffic&ie=utf-&oe=utf-#q=ldap+over+ssl+server+&*

1. Patching  
   - Setup a WSUS Server Enables automatic updates for all computers => Completed  
   - Find a way to update servers not on domain DMZ servers cannot point to WSUS via GPO, may need to create a RODC

1. Tasks  
   - Finish documentation  
   - Setup yearly reviews/updates of IT security documentation/policies  
   - Setup yearly pentest/vulnerability assesment  
   - set up yearly training for Corp users to review security awareness, best practices, and current polices.

1. Backups  
   - Send to a second location Following the 3-2-1 rule, we will send backups to a second location: 3 copies of data, 2 different devices, 1 offsite  
   - Encrypt Backups

1. Start Logging  
   - Setup a Greylog server and forward Windows events to it via Nxlog.  
   - Start logging processes accepted by user https://eventlogxp.com/blog/process-tracking-with-event-log-explorer/. Can track who started what, maybe feed to Greylog  
   - Setup PS Script to email when domain admin logs in => Track who did what at what time.

1. Security GPOs  
   - Setup File Extension behaviror => Change .hta to open in notepad for instance  
   - Domain Admins only have access to DC's Domain admins should only access DC's via console only. Server Admins for all other servers.  
   - Setup Software Restriction Policies => Stops certain file extensions from running in %appdata%  
   - Setup automatic lock screen => Stops people from leaving computers unlocked  
   - Setup FSRM Set alerts when certain files are modified and actions against them


### UPDATE: Found this post (see references) about starting a new job

1. Audit/check/Inventory/review:

   ```escape
   General documentation: do not improve until you understand the environment (do backup before change)  
   Crucial services inventory: Identify mission critical services and where they are hosted; identify who is responsible for them if its not you  
   Disaster Recovery Plan: Backups are running properly? Backup rotation? Last DR test? Automated? In case of my absence?  
   Business Continuity Plan  
   Business Impact Analysis  
   Network topology: configuration (backup?), passwords, routers, gateways, subnets, vlans, static addresses, dhcp, labeled cables  
   Power supply/UPS  
   ISP: contact, agreements, SLA, contracts  
   Support for environment's components: contact, agreements, consultants, SLA, contracts; renew/remedy any issues regarding lack of support, get replacement parts in a timely fashion, maintenance contract situation  
   VPN / Remote Access  
   Firewall policies: understand what's being permitted/blocked  
   AV: existing on systems (servers, desktops, mobiles), activated, updated, custom exclusions  
   Password repository: existing? Up to date?  
   Admin accounts: running services  
   Encryption certificates expiration date  
   Windows Updates: policies, working?  
   Applications updates: policies? automated?  
   Software Inventory: licenses (with charges), warranty, legal  
   Hardware Inventory: warranty, replacements parts, end of life cycle situation  
   Scheduler jobs on servers  
   GPOs review  
   Scripts review  
   Observe network/systems: to know what is normal behavior; known problems; check logs  
   Study last audits reports.  
   Process reviews for incidents, problems management, service requests, escalation [ITIL]  
   [Optional]: Phone systems => VOIP;Skype for Business;other communication solutions/channels  
   ```

2. Prepare/make

   ```escape
   Meetings: with heads of departmentswhat their team does, what they use, what their major issues are  
   Make a "Small wins" list that you can fix that will give you a bit of face to work with => this will contribute to people trusting that you're a professional there to provide a service.

   *Double check:  
   Remote workers  
   Telephone systems, including company cellphones  
   HR procedures for working with IT  
   Legal Compliance issues
   ```

3. Change

   ```escape
   Budget: now and in the future; limit extra useless PCs/laptops  
   Categorize tickets: for future analyzing  
   Monitoring software: Icinga (or other software); iLo/iDrac sending mails; enable smart monitoring on disks, UPSes  
   Clean up lazy permissions  
   IDS/IPS (Intrusion Detection System/Intrusion Prevention System) if no existed
   ```

### References:

[https://www.reddit.com/r/sysadmin/comments/5aj9jo/my\_boss\_informed\_me\_that\_they\_acquired_another/](https://www.reddit.com/r/sysadmin/comments/5aj9jo/my_boss_informed_me_that_they_acquired_another/)

[https://www.reddit.com/r/sysadmin/comments/1gouum/checklistuseful\_info\_on\_new\_job/](https://www.reddit.com/r/sysadmin/comments/1gouum/checklistuseful_info_on_new_job/)