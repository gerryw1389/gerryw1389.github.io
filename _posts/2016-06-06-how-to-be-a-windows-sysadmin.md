---
title: How To Be A Windows SysAdmin
date: 2016-06-06T15:53:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/how-to-be-a-windows-sysadmin/
categories:
  - SysAdmin
---
<!--more-->

### Description:

This is not a definitive guide but if you can get through this list, you could be considered half way &#8220;competent&#8221; by your peers. It is important early in your career that you learn as much as possible. My [links](https://automationadmin.com/2016/02/bookmarks/) page is a great resource along with keeping a tab of [whatis](http://whatis.techtarget.com/) open to learn on the IT acronyms and what they mean.

### To Resolve:

1. Windows 101 => need to learn the OS at the high level of what it does. How does Windows boot? What services start up during the boot process? What happens when a user logs in, what user context is loaded? Where do apps store user data and system data? How do you properly create a package to deploy with the MS stack (like a MSI for example). How do you configure and setup all basic things like but not limited to: Firewall, disk encryption, network settings, user settings, system settings, etc. You need to know where everything is at a high level and how it works. Probably should know about the system registry as well.

2. Server 101 => what roles does Windows Server offer? Sure you have your DNS, DHCP, AD, IIS, and the like, so you should know what each of these is and have a decent foundation of them. You need to understand how the server OS works and how to health check it. You obviously cannot have a single server run every service in an enterprise so knowing when you need to split services to dedicated boxes isn't an exact science. It is based of data and experience. So learn how to get metrics on your servers (covered later) but able to collect those metrics you must first understand at a system level what they mean.

3. Virtualizaton => it is huge and standard every where, you need to learn this at some level

4. Basic Networking knowledge => if you are going into NetOps you need to be an expert on the TCP/IP stack and every service or platform the network offers. If you aren't going into NetOps you need to have a decent foundation of knowledge, so when you work with NetOps you can actually hold a good conversation with them. DNS, DHCP, Firewalls, Load balancers, WAFs, proxies, so on and so forth.

5. Client to Server relationships => you need to understand how clients communicate to servers and what services control that. For example AD is pretty big in this space. How do you deploy software and settings from a centralized server to a bunch of clients? GPO, WSUS, MDT, PowerShell, third party tools, etc. A computer joined to an AD domain will have a lot of options for IT to deploy settings and use LDAP as a central form of authentication not only into the local computer but into other servers, which brings up the next subject.

6. Server to Server relationships => how do you get servers to talk and work with other servers? AD joined computers is a pretty common method in the MS stack, but there are of course other ways. SSO, tokens, security, services, etc. You need to learn how this works.

7. PowerShell => learn to code in PowerShell, also I highly recommend Python. Automation with code is such a huge thing

8. The rest of the MS ecosystem => SCCM, WSUS, MDT, PowerShell, AD, Exchange, InTune, O365, Sharepoint, IIS, DSC, MS SQL, .NET and every other product MS offers. At the very least know what it is and the basics, if the job requires you need to know more expand the knowledge into that specific thing as it comes up.

9. Now after you get to a point where you are semi competent in the MS stack start to Learn Linux and repeat this until you can integrate Linux with Windows systems. We really live in an and world and no longer in an or world. Meaning we live in a Microsoft and Linux and Mac world, so expanding your knowledge into these realms is great. You may not need to be an expert outside of Microsoft, but having a base knowledge helps you work with the teams that manage other platforms.

10. Cloud Offerings => basically anything as a service you may not ever go full cloud but there will be times when certain things make more sense to put in the cloud versus on-prem and vice versa. Knowing how it works can only help you if you ever have to work in a hybrid model of infrastructure

11. Metrics => you need to learn how to gain intelligence on your infrastrcture, track events, trends, data, resource management and the like. Put this into a metrics system and gain intelligence on how your infrastructure works. Remember if you are employed by an Org you are the resident expert. You will know best, and with out data you are flying blind. Collect as much relevant data as you can about your infrastructure and overtime trend these into metrics so you can understand how to scale and support your Orgs needs. Check out my posts [Network Documentation](https://automationadmin.com/2016/11/network-documentation/), [IT Policies](https://automationadmin.com/2016/05/it-policies-overview/), and [Reporting](https://automationadmin.com/2017/01/documentation-for-reporting/).

12. Start with a [Windows SysAdmin Checklist](https://automationadmin.com/2016/10/windows-sysadmin-checklist/) challenge and move on into Powershell challenges.

### References:

[Learning Path](https://www.reddit.com/r/sysadmin/comments/4mr954/learning_path)