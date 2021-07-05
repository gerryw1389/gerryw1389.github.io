---
title: Windows Network Security
date: 2017-05-24T15:15:28+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/05/windows-network-security/
categories:
  - Security
  - SysAdmin
  - Windows
---
<!--more-->

### Description:

One of the main goals in Systems Administration is for you to lock down your network. Security is an important aspect that most administrators take seriously. The principle of least privilege is used in most places as it is considered best practice. Here is a list of security measures you can use to help lock down your network.

### To Resolve:

1. Set domain admin accounts to only be able to login to domain controllers (from console only, not remotely). Any member of Domain Admins is prohibited (by group policy) from logging into any workstation, laptop, PC, or member server. Domain Admin accounts are only used specifically for making changes to the domain.

2. Resetting passwords for end users (but not other secure operator accounts) is delegated to lower level administrator accounts that cannot log into a domain controller (must use RSAT from a jumpbox).

3. Use separate server admin accounts that are used to administer member servers and applications. These accounts can't log into DCs, laptops, or PCs. Only member servers.

4. Use separate workstation admin accounts that are used to administer User PCs. This is in addition to the local admin account which is administered via LAPS. NOBODY in your organization should be able to log into their PC with administrative privileges, not even IT. These workstation admin accounts can only log into PCs, not servers or DCs.

5. None of these privileged accounts have access to email or the internet.

6. Each member of IT should have a separate privileged access workstations, completely separate from their regular user PC. These allow connection to various secured jump boxes inside the datacenter to administer servers through RSAT and other infrastructure via SSH.

7. PAWs are on a different network segment than user PCs.

8. All service accounts are individual to the specific service, managed, and don't have domain admin privileges. If vendor states that their software requires domain admin we look for a new vendor.

9. Servers should not have access to the internet except for only the ports they need exposed. All other ports should be blocked by default (this should be done at the firewall level). Updates should be pushed via WSUS from a computer on the LAN. Antivirus software should block all request originating from the internet except for the port being used for a service (i.e. port 80 for HTTP traffic and 443 for HTTPS).

10. Utilize port security on switches. A user should not be able to plug a device into a port and get an IP addressed. Setting up 802.1x authentication would be useful as well.

11. Setup Software Restriction Policies through GPO's. Applocker for Enterprise. File Systems Resource Manager is another route many admins take.

   - For many of the ransomware viruses going around, administrators may place hidden folders on their shares and set up FSRM to email when one is modified. For example, create a hidden folder named `_HONEYPOT` and `ZZZ_Honeypot` on each share so they appear first and last when sorted alphabetically. Set it so that each one contains 2 files => `_do_not_modify_or_delete.txt` and `Stop.png`. The text file explains the purpose of the file in case anyone has hidden files visible and starts poking around, and the PNG file is the image of a stop sign => this way it serves dual purposes. Setup FSRM to complete certain actions if these files are modified/deleted.

12. The list of GPO's that can be used to increase security is almost endless, but essentially you need: Block macro's in Office documents, software restriction policies, restricted accounts, etc.

13. Last but not least, you need to follow the 3-2-1 backup rule: 3 copies of your data on 2 different devices locally and at least one copy offsite. For example, at home I backup my data to two external drives at a time and backup to a third drive which I take over to  my parents house as an offsite backup. All encrypted using Veracrypt. Cloud service isn't mandatory, but will provide more up-to-date information if you lose your data. On the other hand, restoring from online providers will usually take a day or more depending on the size of your data set.
