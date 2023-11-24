---
title: Linux Overview
date: 2016-05-24T14:08:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/linux-overview/
tags:
  - Linux
  - SysAdmin
---
<!--more-->

### Description:

Linus Torvalds created Linux between 1991-1994. Although it is commonly compare with Unix, it is NOT part of Unix. The Linux kernel itself is open source and distributed freely. What we see nowadays is different &#8220;distributions&#8221; of Linux. Here are some common ones:

1. Trustix- Thought to be the most secure.  
2. Ubuntu- Primarily used for office tasks and browsing.  
3. Red Hat- Very popular in businesses, it offers enterprise support.  
4. SUSE (&#8220;Software und System-Entwicklung&#8221; meaning &#8220;Software and systems development&#8221; translated from German)- Very popular in businesses, it offers enterprise support.  
5. DSL- Damn small Linux => Small distro, said to be around 53MB.  
6. &#8230; many more. See http://en.wikipedia.org/wiki/List\_of\_Linux_distributions for example..

There is usually two versions of each &#8220;distro&#8221;: Desktop and Server. Server versions usually have a stripped down version and expect the end user to know a good deal about Linux before downloading it. It's highly advised to start out with a &#8220;desktop&#8221; distro if you are new to Linux. But before getting into Linux, you must understand what it really means to be open source. Open source, although usually means free, you have to be aware of the different ways they make money with Open Source software as well. The most common are:

1. The developers give away software free to use, BUT you must pay for help when you need it.

2. Free for &#8220;personal and non-commercial use only&#8221;. You MUST pay to use in a business environment or you will pay a hefty fine.

3. You buy the software outright, but you can see the source code telling you how software works. Note that you usually are not allowed to modify the code in any way either.

4. The software is free to download, but you have to pay to &#8220;use&#8221; the software on a re-occurring basis. This is common with Enterprise distributions.

After you pick a distro and install it, it is best to visit the support website for the distribution for any new questions you may have. The main thing to get used to in Linux is the concept of &#8220;root&#8221;. Root is the highest level of anything in Linux (similar to the &#8220;administrator&#8221; account in Windows). The second thing worth mentioning is that Linux is case sensitive unlike Windows, you can see more in the sections below.

NOTE: The following sections are copied from the &#8220;openSUSE&#8221; distro of Linux and therefore may not apply to all distro's of Linux. See http://opensuse-guide.org/.

### Main System Components:

Any modern computer operating system is a very large and complicated contraption => and GNU/Linux distributions are no exception. The Linux kernel is just one of many components. The figure below shows the core components and what their respective roles are.

  <img class="alignnone size-medium wp-image-672" src="https://automationadmin.com/assets/images/uploads/2016/09/linux-11-268x300.png" alt="linux-11" width="268" height="300" srcset="https://automationadmin.com/assets/images/uploads/2016/09/linux-11-268x300.png 268w, https://automationadmin.com/assets/images/uploads/2016/09/linux-11.png 628w" sizes="(max-width: 268px) 100vw, 268px" />

File Tree:

Most users will hardly ever need to work outside their home folder, but nevertheless it's probably a good idea to have a basic idea about the how the file hierarchy works.

On GNU/Linux you only have one file tree, unlike Windows which has a different file tree for each file system/partition. On GNU/Linux separate file systems/partitions are mounted in folders within a single file tree. The root folder for the file tree is &#8220;/&#8221; and paths are written using forward slashes.

So a path might look like this in GNU/Linux:  
/home/username/Desktop/

In MS Windows a comparable path might look like this:  
C:Documents and SettingsusernameDesktop

In GNU/Linux filenames and folders are case sensitive.

  <img class="alignnone size-medium wp-image-674" src="https://automationadmin.com/assets/images/uploads/2016/09/linux-2-300x259.png" alt="linux-2" width="300" height="259" srcset="https://automationadmin.com/assets/images/uploads/2016/09/linux-2-300x259.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/linux-2.png 545w" sizes="(max-width: 300px) 100vw, 300px" />


### Hidden Files:

Files and folders starting with &#8220;.&#8221; (dot) are hidden. You can make them visible in Dolphin file manager via the keyboard shortcut Alt+. or View => Show Hidden Files in the menubar.

Applications store the user settings and data in hidden folders in the users home folder, e.g. /home/username/.mozilla/, /home/username/.config/vlc/,/home/username/.kde4/share/config/ etc. If you uninstall an application the settings and data will remain in the home folder. To &#8220;reset&#8221; an application, you just rename or (re)move the settings and/or data hidden in your home folder.

Important Config Files:

In GNU/Linux configurations and settings are usually stored in human-readable plain text files. Almost any configuration can be done graphically via YaST or various other GUI applications, but nevertheless it can be useful to know the location of some key config files.

System wide configurations are mainly stored in /etc/, user settings are stored in hidden files in the home folder for the individual user.

  <img class="alignnone size-medium wp-image-675" src="https://automationadmin.com/assets/images/uploads/2016/09/linux-3-300x110.png" alt="linux-3" width="300" height="110" srcset="https://automationadmin.com/assets/images/uploads/2016/09/linux-3-300x110.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/linux-3.png 677w" sizes="(max-width: 300px) 100vw, 300px" />


### General Troubleshooting:

Here are some basic troubleshooting tips for GNU/Linux in case an application crashes or won't start at all.

1. If an application fails, try running it from a terminal to get more/better output.

2. Try removing/renaming the hidden folder(s) for the application in the users home folder.

3. Try creating a new user and see if the problem persists. If the problem does not persist for a new user, the cause can probably be found in the settings/data in the home folder of the user with the problem.

4. Check out relevant log files