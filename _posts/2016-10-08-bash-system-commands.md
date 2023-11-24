---
title: 'Bash: System Commands'
date: 2016-10-08T21:25:36+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/bash-system-commands/
tags:
  - SysAdmin
tags:
  - OneLiners-Bash
  - Scripting-Bash
---
<!--more-->

### Description:

These commands have to do with system resources, user accounts, permissions, ect.

### User commands

#### To change owners for files

   ```shell
   # -R in this case is recursive
   chown -R apache:apache /var/www/html/*
   ```

#### To add a group:

   ```shell
   groupadd newGroup
   ```

#### To change group membership for files

   ```shell
   chgrp (groupname) files

   # Change the owning group of /office/files, and all subdirectories, to the group staff.
   chgrp -hR staff /office/files
   ```

#### To change access permissions  
   - chmod (mode) files # see [here](http://www.computerhope.com/unix/uchmod.htm) for more examples

   ```shell
   chmod -R 777 root /var/www/html

   # Commonly used to run scripts you create
   chmod +x /path/to/your/filename.extension

   # Commonly used to secure a file or directory
   chmod 644
   ```

#### To see your user id

   ```shell
   # id (username) - view uid, guid, and groups
   id gerry
   ```

#### To add a new user:

   ```shell
   useradd newUser
   ```

#### To delete a user:

   ```shell
   # Remove root privileges if needed.
   userdel newUsersudo visudo
   ```

#### To add your user to a group:

   ```shell
   usermod -a -G (groupname) username
   ```

   - [other options](http://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/)

#### To see permissions for a file

   ```shell
   getfacl
   ```

#### To list all groups

   ```shell
   lid -g (groupname)
   ```

#### To list all users

   ```shell
   cut -d: -f1 /etc/passwd
   awk -F'[/:]' '{if ($3 >= 1000 && $3 != 65534) print $1}' /etc/passwd
   ```

   - Or [this](http://www.cyberciti.biz/faq/linux-list-users-command/) link

#### To list actively logged on users

   ```shell
   w
   ```

#### To Add user to sudo:

   ```shell
   # If the user doesn't have rights you either need to add to /etc/sudoers file 
   # Or add to wheel group: 
   adduser testUser
   usermod -aG wheel testUser
   usermod -aG sudo testUser
   ```

### System commands (to be ran as root)

#### To run a command as root

   ```shell
   # Most common command you will probably use
   sudo (command)

   # Just type this command by itself to run all other command past it as root. 
   # Then type "exit" to get back to your user prompt.
   su
   ```

#### To install an application (depending on the package manager and distro):

   ```shell
   # Installs a Linux application, in this case – xchat or IRC.
   sudo apt-get install xchat

   # For CentOS
   sudo yum install xchat

   # For Fedora
   sudo dnf install xchat
   ```

#### To Add A New Path To Path Variable:

   - This order from all users to most specific  
   - `/etc/profile`
   - `~/.bash_profile`  
   - `~/.bash_login`  
   - `~/.profile`

   ```shell
   PATH="$PATH:/opt/puppetlabs/bin";export PATH
   ```

  - New way (preferred)

   ```shell
   echo 'pathmunge /opt/puppetlabs/puppet/bin' > /etc/profile.d/puppet.sh
   chmod +x /etc/profile.d/puppet.sh
   . /etc/profile
   ```

#### To set the time zone:

   ```shell
   # set time zone to correct zone
   mv /etc/localtime /etc/localtime.bak
   ln -s /usr/share/zoneinfo/America/Chicago /etc/localtime
   ```


#### To remove software:

   ```shell
   sudo yum remove (packageName)

   # Removes a couple programs at once
   sudo yum remove orca gedit evince empathy 

   # Remove all packages that don't have dependencies:
   # Shows them
   sudo package-cleanup --leaves 
   # Removes them
   sudo yum remove `package-cleanup --leaves`
   ```

#### To change a password for a user

   ```shell
   # If left blank, changes current users password
   passwd (username)
   passwd root
   ```

#### To change the date

   ```shell
   date (options)

   # Change the year but keep the same time
   date -s "2014-12-25 $(date +%H:%M:%S)"
   ```

#### To Check Top Processes

   ```shell
   # like task manager on Windows
   top
   
   # quick
   ps aux k-pcpu | head -6
   ps -eo pcpu,pid,user,args --no-headers| sort -t. -nk1,2 -k4,4 -r |head -n 5
   ```


#### To Shutdown

   ```shell
   shutdown -h now

   # Shuts down at 12:30
   shutdown -h 12:30
   ```

#### To logout

   ```shell
   logout
   ```

#### To Reboot

   ```shell
   reboot
   shutdown -r
   ```

   - [Interesting article](http://www.binarytides.com/linux-command-shutdown-reboot-restart-system/) between shutdown, halt, and poweroff

#### To start a service

   ```shell
   sudo systemctl start httpd
   ```

#### To see a service status

   ```shell
   sudo systemctl status httpd
   ```

#### To set a service to run on startup

   ```shell
   sudo systemctl enable httpd

   # This enables the ssh service to start on runtime
   update-rc.d ssh enable
   ```

#### To restart a service

   ```shell
   sudo systemctl restart httpd
   ```

#### To have a GUI for services:

   ```shell
   # Use spacebar to enable whichever you want. You can also run "sysv-rc-conf". These are called TGUI programs.

   # For Debian based: 
   sudo rcconf

   # For SysV Services (RPM based): 
   sudo ntsysv

   # For SystemD Services (default): 
   systemctl list-unit-files | less | grep enabled

   # For almost any Linux distro: 
   chkconfig --list
   ```

#### To open a port on your firewall

   ```shell
   # Check which zones are active
   firewall-cmd –get-active-zones

   # Add the port
   firewall-cmd –permanent –zone=public –add-port=3389/tcp

   # Reload the firewall
   firewall-cmd –reload
   ```

#### To close a port on your firewall

   ```shell
   # Check which zones are active
   firewall-cmd –get-active-zones

   # Remove the port
   firewall-cmd –permanent –zone=public –remove-port=3389/tcp

   # Reload the firewall
   firewall-cmd –reload
   ```

#### To View Credentials to Shares/ Passwords if you are using Nautilus.

   ```shell
   seahorse
   ```

### Misc

#### To see a history of your commands

   ```shell
   history
   ```

#### To clear the screen

   ```shell
   clear
   ```

#### To see a calendar of a previous year

   ```shell
   cal 2010
   ```

