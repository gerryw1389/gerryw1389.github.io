---
title: DFS Best Practices
date: 2018-05-27T03:34:31+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/dfs-best-practices/
categories:
  - WindowsServer
tags:
  - WindowsServer-Roles
---
<!--more-->

### Description:

Some advice I've read from an admin that does this for a living about setting up DFS. He mentions &#8220;Keep it simple (KISS Principle), &#8220;A good filesystem is like a good joke, if you have to explain it to people then it's a bad file system&#8221;.

### To Resolve:

1. In general:  
   - Run a MAX of 5 network shares total.  
   - A single DFS namespace.  
   - Drive letters are consistent across the entire company, so the Staff drive "S" is the exact same drive for every single employee.  
   - Consistency is key for ease of troubleshooting and finding data.  
   - DO NOT create new network drives and shares, stick with the bare minimum and create new subfolders instead.

2. Drive examples:  
   - S drive => Staff => Every department has a subfolder. If you aren't in a particular department then you don't have access to that folder. This way if someone in say accounting needs to see inventory in the maintenance folder, you just give them permissions to the folder. This way accounting and maintenance see the same things in the same place and you don't have to add misc drive letters to individual peoples login scripts.

   - U Drive => Users => Every user has a dedicated user folder that only they can access. This is commonly called home folders. I hate using "H" for this because USB drives etc tend to use those letters. Collaboration happens in the "S" drive, the U drive is for You and only You.

   - P drive => Public => visible to the entire company, used for Forms, HR information, benefits, Policies, safety committee, pictures, logos the hockey pool etc. Some employees (front line staff for instance) don't get access to any department drives so it's handy to have a dedicated drive for public stuff  

   - Profile$ => hidden share for Terminal Services Roaming profiles (if required)

   - T => Application => A drive for running applications off the network. Certain applications require a centralized network share in order to operate.  

   - These drives can be hosted on different servers if required, but all exist within the same DFS namespace. Use GPOs to deploy the drives to computers. Login scripts are a pain in the ass to manage, don't use them.

3. Permissions  
   - File permissions are assigned from top to bottom, least restricted to most restrictive. The further down you drill into a file system the more secure it should be.  
   - Folder structure should not be deeper than 3-4 levels if possible  
   - If you have a subfolder that needs to be accessed by different departments (for instance \server\accounting\budgets) move the folder up to the root level to avoid inheritance issues (\server\budgets)

4. Enable Access Based enumeration to hide folders that people don't have permissions too in order to cut down on clutter.

   - To do this: Open an admin PS window on a server that has the Distributed File System role service or Distributed File System Tools feature installed.

   ```powershell
   Set-DfsnRoot -Path "\\Contoso\AccountingResources" -EnableRootScalability -EnableAccessBasedEnumeration
   ```

