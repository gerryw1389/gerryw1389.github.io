---
title: Role Based Access Control
date: 2017-04-23T16:53:59+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/04/role-based-access-control/
tags:
  - WindowsServer
---
<!--more-->

### Description:

Not many of us get the opportunity to create AD from scratch or change the way the company assigns permissions in the environment, but if you do, please see following response from SpiceWorks that is cited often:

### To Resolve:

1. From: [New AD Setup](https://community.spiceworks.com/topic/1996452-new-ad-setup and [NTFS Permissions Issue](https://community.spiceworks.com/topic/1225228-ntfs-permissions-issue)

I'm going to put a different spin on this. My post will not answer your question directly, but may give you a better understanding of RBAC, and how you should go about permissions with folders, naming conventions, etc. What you are asking, I see you solved this with a deny permission => these are DANGEROUS => they can have ill-effects later on as Deny always wins over allow.

Anyways, here is my spiel.

&#8220;Change the way you think => Change your life.&#8221; Watch this video, and change the way you look at security. This video will give you a RBAC foundation to build your security permissions on.

From the small 1 person company to the large Fortune 500 companies => this solution just plain works. You will create a whole lot of groups, for nesting, but the other side is that with the scripts that he provides (Attached for ease => are the scripts that he references in the video), you just need to run his script and you can see who has what access to what folders, and what type of access they have. (Eg. who has access to this folder? what does this user have access to? Run the script, it will tell you.)

It will change the way you assign permissions to everything => and it will make your life easy. It will take a bit of grunt work to switch over to RBAC but if you do it right, it's a 1 time change. On each file share's NTFS Permissions tab, you will only have 1 security group with Read, 1 with modify, 1 with list folder contents, and 1 with Full and 1 `SYSTEM`. Nothing else. Share permissions will ALWAYS be Everyone > Full Control (unless there is a specific need that the share must stay read only). Grant access based on groups, not individuals, and not groups that individuals are a part of (eg Sales Department). Create a nested group Access Control List (ACL) Structure. This way, you can find out EVERYTHING by using included scripts.

If you wanted to take it a step further for having a File Admins group (not just Domain Admins), set up a &#8220;File Admins&#8221; group, use it instead of Domain Admins on all root folder NTFS Permissions for where the rest of your files are located (eg. D:\CompanyFiles). Set it up as a member of every ACL that has Full Control. Don't make Domain Admins a member of that group, but control the individuals as members of that File Admins group. Then you can give Domain Admin to any other Admin user (if needed), and then they will not have access to the files and folders of your company's files. Of course they can take ownership of the folder structure as they are a Local Administrator of the file server (by rights of Domain Admin), but that will irradiate all security on the object and they will be caught in the act.

I also recommend that you couple RBAC with Access Based Enumeration (ABE). This way users can only see files and folders that they have access to. If they don't have access, they can't see it. It makes it much more secure, and an easier experience for the user.

On top of everything, make your life easier by enabling Distributed File System (DFS) with replication (DFSR) if you have multiple servers for files. Using DFS(R) coupled with RBAC, you have a secure, easy to manage, least privilege, best practice file system in effect at your company. The beauty of DFS is that if you change servers in the future (buy a new server, etc) or you need some extra space that is not utilized on a different server, you can adjust DFS to suit your needs, or introduce DFSR and sync across the data automatically, keeping High Availability (HA) and/or faster access at multiple locations, or even replication of data to replacement server. Don't forget, DFS(R) is a service and needs to be duplicated for HA, just like Domain Controllers (DCs), which is why I suggest using the DCs as your DFS Namespace Servers as they usually are already distributed properly for HA (separate hardware, separate UPSs, etc) and AD already uses DFSR (Server 2012) to replicate SysVol and other AD folders.

The best advice is to do it step by step.

Start by mapping out your entire folder structure's permissions set using AccessEnum

http://live.sysinternals.com/AccessEnum.exe

This will not only give you a backup of the security settings, but also a map as to how to create your security groups.

Start with your job titles => create groups for them. Add the appropriate people into the job titles as members.

Then go to the other end of the scale => file structure => create your groups with regards to your department security

EG: Sales will need 4 groups minimum.

ACL\_Sales\_Read

ACL\_Sales\_Modify

ACL\_Sales\_ListFolderContents (in advanced permissions, set this for &#8220;This folder only&#8221;)

ACL\_Sales\_Full

Add the sales oriented job title groups you just created as &#8220;member of&#8221; the ACL\_Sales\_Modify group. Add all ACL\_Sales\_* groups to the Sales folder.

LEAVE IT FOR A FEW DAYS. => you haven't taken away anyone's access, you've only added groups, and you need to make sure that all users have at least logged in 1 time again so that the TGT from Kerberos has been updated to include the group memberships you added them to. After a few days (a week is good => it gives those who are remote users who don't connect to the network often enough time to get the updates. If all are internal, next day is fine) remove direct members permissions on the Sales folder.

After this, create another set of groups for the next and next folders inside

ACL\_Sales.2015 Sales Folder\_Modify => make this group a MEMBER OF ACL\_Sales\_ListFolderContents, and add the members ROLES to this group. Add the group to the folder security. Wait a week, and then remove the direct memberships. At this point you can remove or include inheritance from the folder structure above depending on the nature of the folder.

You then finish this for all file shares. Then move on to printers. ACL\_Printer1\_Print, ACL\_Printer1\_Manage, ACL\_Printer1\_Full, etc.

You may have some roles that contain multiple ACL groups that replicate across roles => eg, if you have a committee like Health & Safety. Then create a new role for that, add all the ACL memberships in the member of tab, and for the members, add the individual users as you're creating a new role. Wait for the TGT to be recreated at next login for each user (wait a few days) and then remove the direct ACL groups from their employee role. Now the user Sally has a role of Sales Representative, and also Health & Safety Committee Representative.