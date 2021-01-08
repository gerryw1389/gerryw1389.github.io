---
title: SMB SysAdmin Advice
date: 2016-08-21T17:04:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/smb-sysadmin-advice/
categories:
  - SysAdmin
---
<!--more-->

### Description:

This is advice I have read for SMB setups. The list is not exhaustive, but does point out good points for smaller networks.

### To Resolve:

1. Structured cabling => run all cabling into a single room or closet vs hoping office to office with small switches causing network issues, slow uplinks, etc.

2. Have two ISPs, even if the second one is only a 20/5 connection so you can at least get access to emails.

3. At least two physical servers to host VMs => the second server hosts replicas of services from the first like AD, SQL, etc.

4. Office365 for email, lync (skype), sharepoint, office documents, etc.

5. To standardize printers, computers, networking, and server equipment. Don't buy 1 HP workstation, 1 Dell workstation, 1 IBM laptop, etc. It makes it easier to manage drivers if you use services like WDS.

6. Get open licensing from Microsoft with software assurance if you have at least 25 client PCs. I don't think open licensing is worth managing for anything less.

7. Use VLANs for servers, printers, and client pcs.

8. Have a backup on site. Use cloud services to backup off site or take a hard disk home every day of your data.

9. For storage, don't buy consumer hard drives. At the very least buy WD RE drives that are designed to run 24/7.

10. I don't think small companies need a SAN. A simple file server or Synology with a solid backup is more cost effective and can be expanded until they outgrow it.

11. Documentation. Document everything.

12. Password management => get a password management tool like LastPass or 1Password. Don't store your passwords in a word document or sticky note.

13. Help Desk software => zendesk, Jira, etc.. it's great to keep track of tickets to reference later if needed. You can also use it for projects by creating a ticket for it until you can afford an actual PM software tool.

14. AD permissions => Start using roles/user groups now. Create them for Finance, HR, Safety, etc. and apply permissions to the group, not individual users. This will save tons of time, even in a small company environment.

15. Hire help => Even if you're small design like you're big. Don't be afraid to have specialists help you. They are not going to steal your job and they don't want it either.v