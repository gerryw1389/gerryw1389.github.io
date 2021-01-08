---
title: 'Bash: Hardware Commands'
date: 2016-05-30T05:44:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/bash-basic-commands/
categories:
  - SysAdmin
tags:
  - Scripting-Bash
  - OneLiners-Bash
---
<!--more-->

### Description:

Bash hardware commands that have to do with the file system and accessing files.

### Navigating the file system, basic commands:

#### To move directories

   ```shell
   cd /path/to/go/to

   # Navigates to a user's "home". For root = /root/home or a user "gerry" is /home/gerry
   cd ~

   # Navigates to root of filesystem
   cd /
   ```

#### To view a directories contents (hidden and in list form):

   ```shell
   ls -al
   ```

#### To create a file

   ```shell
   touch filename
   touch mytext.txt
   ```

#### To copy a file (can use &#8220;.&#8221; as current path)

   ```shell
   cp soure/path destination/path

   # Copy file.txt from current directory to user's home directory
   cp ./file.txt /home/user/
   ```

#### To delete a file

   ```shell
   rm file.txt

   # Force remove a directory recursively. Be careful with this one!! 
   rm -rf 

   # Also run an echo first to make sure, example:
   echo rm -rf /home/user/docs

   #check output - looks safe; let's do it for real...
   rm -rf /home/user/docs
   ```

#### To move files

   ```shell
   mv /source /dest
   mv mytext.txt /home/user/documents/
   ```

#### To create a shortcut

   ```shell
   ln source destination
   ln mytext.txt /home/user/documents/
   ```

#### To create a folder

   ```shell
   mkdir foldername
   mkdir my-docs
   ```

#### To delete a folder (only if empty)

   ```shell
   rmdir my-docs
   ```

#### To mount drives in Linux

   ```shell
   mount (device name) /destination
   ```

#### To unmount drives

   ```shell
   umount /currentMountPoint

   # Unmount all drives
   umount /a
   ```

#### To Search for files # there are 3 ways to find files in Linux, &#8220;find&#8221; is the most aggresive

1. locate => to use this, you need to run &#8220;updatedb &&#8221; first (use & to background it). This &#8220;db&#8221; is a built-in index of your file system. ex: locate mytext.txt  

2. which => which is used to figure out a programs dir. Ex: which nc.exe # should return `/usr/share/windows-binaries/nc.exe` or wherever you have `nc.exe` installed  

3. [find](http://www.tecmint.com/35-practical-examples-of-linux-find-command/) => This is the most common. Tons of switches. Ex: find / -name mytext.txt

### Archiving & Compression

Tar => The basic &#8220;zip&#8221; file for Linux systems. Commonly used with Gzip (see below).

#### To compress a directory to a tar.gz

   ```shell
   tar -czvf name-of-archive.tar.gz /path/to/directory-or-file
   ```

#### To extract a tar to the current dir

   ```shell
   tar -xzvf archive.tar.gz
   ```

#### To extract a tarball into location where you want

   ```shell
   tar -xzvf backup.tar -C /location
   ```

   - NOTE: Only use `z` with gzip 
   - Gzip => This program compresses the contents of files using complex mathematical algorithms. Files compressed in this way are given the extension .gz and need to be uncompressed before they can be used. To compress several files or even entire directories, use the tar command. The archive files created by tar end with .tar. If the tar archive was also compressed using gzip, the ending is .tgz or .tar.gz. If it was compressed using bzip2, the ending is .tar.bz2.

### Viewing files:

#### To see a file's information

   ```shell
   file filename
   file mytext.txt
   ```

#### To view a file in terminal

   ```shell
   cat filename

   # Use path to file
   cat ./mytext.txt
   ```

   - View a file half a page at a time:

   ```shell
   less filename
   less mytext.txt
   ```

#### To search within a file for a particular string

   ```shell
   # Searches files for your search string
   grep (search string)

   # Used often with pipelined input
   cat mytext.txt | grep info
   ```

#### To compare files

   ```shell
   diff file1 file2
   ```

### File System Information:

#### To lists the disks

   ```shell
   fdisk -l
   ```

#### To see how much free disk space you have

   ```shell
   df -h

   # Human readable
   df -aT
   ```

#### To see how much used space you have (in current dir)

   ```shell
   du -h
   ```

#### To see how much free memory you have

   ```shell
   # Output in MB
   free -m
   ```

#### To see currently running programs memory usage

   ```shell
   # Press H for customization
   #### Top
   ```

#### To see a processes usage

   ```shell
   ps
   aux
   ```

#### To stop a process

   ```shell
   # You have to use -9 to force kill. This command requires that you know the process id first
   kill (process-id)

   # Allows you to specify name instead of PID
   killall (processname)
   ```

### System Details

#### To Show system date

   ```shell
   date
   ```

#### To display PCI devices

   ```shell
   lspci
   ```

#### To see architecture of machine

   ```shell
   # To see lots of info
   uname -a

   # To see architechture
   arch
   uname -m

   # To display operating system
   uname -o

   #### To see the hardware platform
   uname -i

   # Network node hostname
   uname -n
   hostname

   # Show kernel version
   uname -r

   # for specific distro info:
   cat /etc/SuSE-release
   cat /etc/redhat-release
   ```

#### To see kernel messages

   ```shell
   dmesg | less
   dmesg | grep -i # (usb, memory, and many other options)
   ```

#### To see hardware info for attached devices:

   ```shell
   # CPU information
   cat /proc/cpuinfo

   # Show memory use
   cat /proc/meminfo

   # Show file swap
   cat /proc/swaps

   # Show version of the kernel
   cat /proc/version

   # Show mounted file systems
   cat /proc/mounts
   ```