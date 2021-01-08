---
title: NTFS Permissions
date: 2017-08-26T05:10:58+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/ntfs-permissions/
categories:
  - Windows
  - SysAdmin
---
<!--more-->

### Description:

Reference posts because many SysAdmin's get requests to setup directories with certain permissions. It's best to design your network with Group permissions so that individual users can just be added/removed from groups in AD to access certain folders => usually done by department.

### To Resolve:

1. First is the most common request: I need my team to be the ONLY ONES who can see/access this share:

   - Create the folder in the share

   - Right click => Properties => Security => Advanced => Change Permissions => Uncheck "Include inheritable..." => Add. This will make them explicit permissions. Click ok all the way back to the Explorer window.

   - Now go to Properties => Security and remove all entries. Then add only the people you want to have access.

   - Example: Add `domain.com\enterprise admins` full control and `ITStaff` with everything but full control (add full control then uncheck just the full control box => this will enable modify, read, write, ect but remove special permissions).

2. To allow everyone to view/open files but not be able to delete or add (read only):

   - Follow steps in step 1.

   - Add `authenticated users`

   - Set permissions to allow only on read/execute, list folder contents, and read. Do not deny anything or add anything else.


3. To have the subfolders match permissions of a parent folder:

   - Example: We once had an issue where the root folder was setup right, but all subfolders had stricter permissions.
   - To fix you just go to the root folder and go to Security => Advanced => Change Permissions => Check the box that says &#8220;replace all child permissions&#8230;&#8221;. This will set all files/folders under the parent folder to have the exact same rights.

4. If you see a red &#8220;x&#8221; next to a user in folder permissions:
   - It is most likely because you have a local account on that server with the same account name as a domain account and that local account is disabled. See [here](https://serverfault.com/questions/459174/folder-permissions-red-x-on-user-object) and [here](https://community.spiceworks.com/topic/446687-folder-permissions).