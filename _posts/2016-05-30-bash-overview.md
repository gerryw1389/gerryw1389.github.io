---
title: Bash Overview
date: 2016-05-30T05:15:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/bash-overview/
tags:
  - SysAdmin
tags:
  - OneLiners-Bash
  - Scripting-Bash
---
<!--more-->

### Description:

On most Linux systems a program called bash (which stands for Bourne Again SHell, an enhanced version of the original Unix shell program, sh, written by Steve Bourne) acts as the shell program. Besides bash, there are other shell programs that can be installed in a Linux system. These include: ksh, tcsh and zsh.

Bash is an sh-compatible command language interpreter that executes commands read from the standard input or from a file. Bash also incorporates useful features from the Korn and C shells (ksh and csh). Bash is intended to be a conformant implementation of the IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2). A quick reference guide to bash can be found [here](https://community.linuxmint.com/tutorial/view/100).

If the last character of your shell prompt is # rather than $, you are operating as the superuser. This means that you have administrative privileges. This can be potentially dangerous, since you are able to delete or overwrite any file on the system. Unless you absolutely need administrative privileges, do not operate as the superuser.

### Example Commands:

1. Most commands operate like this: `command -options arguments`. Commands can be one of 4 different kinds:

   - An executable program like all those files we saw in /usr/bin. Within this category, programs can be compiled binaries such as programs written in C and C++, or programs written in scripting languages such as the shell, Perl, Python, Ruby, etc.

   - A command built into the shell itself. bash provides a number of commands internally called shell builtins. The cd command, for example, is a shell builtin.

   - A shell function. These are miniature shell scripts incorporated into the environment. We will cover configuring the environment and writing shell functions in later lessons, but for now, just be aware that they exist.

   - An alias. Commands that you can define yourselves, built from other commands. This will be covered in a later lesson.

2. Common commands:

   |Command|What it does|
   |:---|:---|
   |pwd | print working directory|  
   |ls | lists all the files in the directory. Note: you can type &#8220;.&#8221; to refer to the directory you are in or &#8220;..&#8221; for the parent directory. You have to use &#8220;ls -a&#8221; to see files with a period at the beginning of their name. | 
   |less | You use like &#8220;less text_file&#8221;. It is a text viewer. You type &#8220;q&#8221; to exit. You type &#8220;v&#8221; to open it to where you can edit it. | 
   |file | You use like `file name_of_file`. It tells you information about a file, like what type it is.  |
   |cd | Change directory; used to move around the file system.  |
   |cp, mv, rm, mkdir | Copies / moves / deletes / creates directories. You can use wild cards, see below. &#8220;mv&#8221; can also rename files. | 
   |type, which, help, man| Used to learn commands. type will tell you the type, which locates a command, help is local help, and man is the online page. | 
   |echo| prints text arguments of standard outputs. ex: echo * will print current directory. | 
   |chmod, chown, chgrp | modify file access rights / change file ownership / change a file's group ownership = Has to be ran in su.  |
   |su, sudo | temporarily become the superuser. Type &#8220;exit&#8221; to stop commands as super user.  |
   |ps, kill, jobs, bg, fg | list the processes running on the system/ kill (PID from ps)- send a signal to one or more processes (usually to &#8220;kill&#8221; a process)/ an alternate way of listing your own processes/ put a process in the background/ put a process in the forground.|  
   |df -h, du -cksh | Shows disk space / show the size of the current directory. For cksh, just append for another other directory. ex: du -cksh /usr/bin | 
   |uname -a, cat /etc/issue | shows the kernel version installed / shows the OS version you are running. | 
   |cat /etc/resolve.conf | Shows DNS on linux systems. Dig ptr (ipaddress) will return a hostname. Dig a (hostname) returns IP address.|

3. Kill codes: Use these as arguments to the &#8220;kill&#8221; command  
   - SIGHUP = Hang up signal. Programs can listen for this signal and act upon it. This signal is sent to processes running in a terminal when you close the terminal.  
   - SIGINT = Interrupt signal. This signal is given to processes to interrupt them. Programs can process this signal and act upon it. You can also issue this signal directly by typing Ctrl-c in the terminal window where the program is running.  
   - SIGTERM = Termination signal. This signal is given to processes to terminate them. Again, programs can process this signal and act upon it. This is the default signal sent by the kill command if no signal is specified.  
   - SIGKILL = Kill signal. This signal causes the immediate termination of the process by the Linux kernel. Programs cannot listen for this signal.
   - Example: `kill -9 1234` where 1234 is the PID of the process I want to stop.

4. Directories:

   |Path|What it contains|
   |:---|:---|
   | / |  The root directory where the file system begins. In most cases the root directory only contains subdirectories.|   
   | /boot | This is where the Linux kernel and boot loader files are kept. The kernel is a file called vmlinuz. |  
   | /etc |  The /etc directory contains the configuration files for the system. All of the files in /etc should be text files. Points of interest: |  
   | /etc/passwd |  The passwd file contains the essential information for each user. It is here that users are defined.|   
   | /etc/fstab | The fstab file contains a table of devices that get mounted when your system boots. This file defines your disk drives. |  
   | /etc/hosts | This file lists the network host names and IP addresses that are intrinsically known to the system. |  
   | /etc/init.d | This directory contains the scripts that start various system services typically at boot time.  | 
   | /bin, /usr/bin |  These two directories contain most of the programs for the system. The /bin directory has the essential programs that the system requires to operate, while /usr/bin contains applications for the system's users. |  
   | /sbin, /usr/sbin |  The sbin directories contain programs for system administration, mostly for use by the superuser.|   
   | /usr |  The /usr directory contains a variety of things that support user applications. For example, `/usr/share/X11` is support files for the X Window system |  
   | /usr/share/dict | Dictionaries for the spelling checker. Bet you didn't know that Linux had a spelling checker. See look and aspell.|   
   | /usr/share/doc | Various documentation files in a variety of formats. |  
   | /usr/share/man | The man pages are kept here. |  
   | /usr/src | Source code files. If you installed the kernel source code package, you will find the entire Linux kernel source code here.|   
   | /usr/local |  /usr/local and its subdirectories are used for the installation of software and other files for use on the local machine. What this really means is that software that is not part of the official distribution (which usually goes in /usr/bin) goes here. When you find interesting programs to install on your system, they should be installed in one of the /usr/local directories. Most often, the directory of choice is /usr/local/bin.|   
   | /var | The /var directory contains files that change as the system is running. This includes: |  
   | /var/log | Directory that contains log files. These are updated as the system runs. |  
   | /var/spool |  This directory is used to hold files that are queued for some process, such as mail messages and print jobs. When a user's mail first arrives on the local system (assuming you have local mail), the messages are first stored in /var/spool/mail |  
   | /lib |  The shared libraries (similar to DLLs in that other operating system) are kept here. |  
   | /home |  /home is where users keep their personal work. In general, this is the only place users are allowed to write files. This keeps things nice and clean |  
   | /root |  This is the superuser's home directory. |  
   | /tmp |  /tmp is a directory in which programs can write their temporary files.|   
   | /dev |  The /dev directory is a special directory, since it does not really contain files in the usual sense. Rather, it contains devices that are available to the system. In Linux (like Unix), devices are treated like files. You can read and write devices as though they were files. For example /dev/fd0 is the first floppy disk drive, /dev/sda (/dev/hda on older systems) is the first hard drive. All the devices that the kernel understands are represented here.|   
   | /proc |  The /proc directory is also special. This directory does not contain files. In fact, this directory does not really exist at all. It is entirely virtual. The /proc directory contains little peep holes into the kernel itself. There are a group of numbered entries in this directory that correspond to all the processes running on the system. In addition, there are a number of named entries that permit access to the current configuration of the system. Many of these entries can be viewed. Try viewing /proc/cpuinfo. This entry will tell you what the kernel thinks of your CPU. |  
   | /media,/mnt |  Finally, we come to /media, a normal directory which is used in a special way. The /media directory is used for mount points. As we learned in the second lesson, the different physical storage devices (like hard disk drives) are attached to the file system tree in various places. This process of attaching a device to the tree is called mounting. For a device to be available, it must first be mounted. When your system boots, it reads a list of mounting instructions in the file /etc/fstab, which describes which device is mounted at which mount point in the directory tree. This takes care of the hard drives, but you may also have devices that are considered temporary, such as CD-ROMs, thumb drives, and floppy disks. Since these are removable, they do not stay mounted all the time. The /media directory is used by the automatic device mounting mechanisms found in modern desktop oriented Linux distributions. On systems that require manual mounting of removable devices, the /mnt directory provides a convenient place for mounting these temporary devices. You will often see the directories /mnt/floppy and /mnt/cdrom. To see what devices and mount points are used, type mount. |  
   | Multiple Directories and files with a `->` at the end of their filenames are symbolic linked files |  This one file may point to one or more files.| 

5. Wild Cards:

   |Wildcard|Meaning|
   |:---|:---| 
   | * | Matches any characters  | 
   | ? |  Matches any single character |  
   | [characters] |  Matches any character that is a member of the set characters. The set of characters may also be expressed as a POSIX character class such as one of the following: |  
   | (below) |  POSIX Character Classes|   
   | [:alnum:] |  Alphanumeric characters |  
   | [:alpha:] |  Alphabetic characters |  
   | [:digit:] |  Numerals |  
   | [:upper:] |  Uppercase alphabetic characters |  
   | [:lower:] |  Lowercase alphabetic characters  | 
   | [!characters] | Matches any character that is not a member of the set characters| 

   - Examples:

   |Command|Pattern Matches |
   |:---|:---| 
   |*|All filenames|  
   |g*|All filenames that begin with the character &#8220;g&#8221;  |
   |b*.txt|All filenames that begin with the character &#8220;b&#8221; and end with the characters &#8220;.txt&#8221; | 
   |Data???|Any filename that begins with the characters &#8220;Data&#8221; followed by exactly 3 more characters. | 
   |[abc]*|Any filename that begins with &#8220;a&#8221; or &#8220;b&#8221; or &#8220;c&#8221; followed by any other characters.|  
   |[[:upper:]]*|Any filename that begins with an uppercase letter. This is an example of a character class.|  
   |BACKUP.\[[:digit:]\]\[[:digit:\]]|Another example of character classes. This pattern matches any filename that begins with the characters &#8220;BACKUP.&#8221; followed by exactly two numerals. | 
   |*[![:lower:]]|Any filename that does not end with a lowercase letter.|

6. Special Shell Characters:

   |Character|What it does |
   |:---|:---|
   |`'` and `""`| Used for quoting and were described before.|  
   |`<` and `>` | Used for input/output redirection and were described before.|  
   | `|` | Pipes the output of the command to the left of the pipe symbol &#8220;|&#8221; to the input of the command on the right of the pipe symbol. | 
   |`/` | Separate the command words. | 
   |`(` `)` | Enclose command(s) to be launched in a separate shell (subshell). E.g. ( dir ). | 
   |`{` `}` | Enclose a group of commands to be launched by the current shell. E.g. { dir }. It needs the spaces. | 
   |`&` | Causes the preceding command to execute in the background (i.e., asynchronously, as its own separate process) so that the next command does not wait for its completion. When a filename is expected, it matches any filename except those starting with a dot (or any part of a filename, except the initial dot).|  
   |`?` | When a filename is expected, it matches any single character | 
   |`[` `]`| When a filename is expected, it matches any single character enclosed inside the pair of [ ].|  
   |`&&` | Is an &#8220;AND&#8221; connecting two commands. command1 && command2 will execute command2 only if command1 exits with the exit status 0 (no error). For example: cat file1 && cat file2 will display file2 only if displaying file1 succeeded. | 
   | `||` | An &#8220;OR&#8221; connecting two commands. command1 || command2 will execute command2 only if command1 exits with the exit status of non-zero (with an error). For example: cat file1 || cat file2 will display file2 only if displaying file1 didn't succeed. | 
   |`=` | Assigns a value to a variable. Example. The command: &#8220;me=blah&#8221; assigns the value &#8220;blah&#8221; to the variable called &#8220;me&#8221;. I can print the name of the variable using: echo $me|
   |`$` |Precedes the name of a variable to be expanded. The variables are either assigned using &#8220;=&#8221; or are one of the pre-defined variables. | 
   |`$0` | Name of the shell or the shell script being executed.  |
   |`$#` | Number of the positional parameters to the command.|  
   |`$1` | The value of the first positional parameter passed to the command. $2 is the second positional parameter passed to the command. etc. up to $9. | 
   |`$*` | Expands to all positional parameters passed to the command | 
   |`$@` | Expands to all positional parameters passed to the command, but individually quoted when &#8220;$@&#8221; is used.|

7. Operations:

   - `ls > file_list.txt` = Standard output.  
   - `ls >>file_list.txt` = Appends instead of overwrite.  
   - `sort < file\_list.txt` = Standard input. You can do both, ex: sort < file\_list.txt > sorted\_file\_list.txt. This will sort the document and create a text file in the current directory.  
   - `ls -l | less` = Pipelines take the output of one file and use them as input for another.

8.  Filters:

   - One kind of program frequently used in pipelines is called filters. Filters take standard input and perform an operation upon it and send the results to standard output. In this way, they can be combined to process information in powerful ways. Here are some of the common programs that can act as filters:  
   
   |Program|What it does |
   |:---|:---|
   |sort | Sorts standard input then outputs the sorted result on standard output.|  
   |uniq | Given a sorted stream of data from standard input, it removes duplicate lines of data (i.e., it makes sure that every line is unique).|  
   |grep | Examines each line of data it receives from standard input and outputs every line that contains a specified pattern of characters.|  
   |fmt | Reads text from standard input, then outputs formatted text on standard output. | 
   |pr | Takes text input from standard input and splits the data into pages with page breaks, headers and footers in preparation for printing.|  
   |head | Outputs the first few lines of its input. Useful for getting the header of a file.|  
   |tail | Outputs the last few lines of its input. Useful for things like getting the most recent entries from a log file.| 
   |tr | Translates characters. Can be used to perform tasks such as upper/lowercase conversions or changing line termination characters from one type to another (for example, converting DOS text files into |Unix style text files). | 
   |sed | Stream editor. Can perform more sophisticated text translations than tr.|  
   |awk | An entire programming language designed for constructing filters. Extremely powerful.|  
   |lpr | Takes standard input and sends it to the default printer.|

   - Examples:

   - `cat poorly\_formatted\_report.txt | fmt | pr | lpr` In the first example, we use cat to read the file and output it to standard output, which is piped into the standard input of fmt. fmt formats the text into neat paragraphs and outputs it to standard output, which is piped into the standard input of pr. pr splits the text neatly into pages and outputs it to standard output, which is piped into the standard input of lpr. lpr takes its standard input and sends it to the printer.  
   
   - `cat unsorted\_list\_with_dupes.txt | sort | uniq | pr | lpr` The second example starts with an unsorted list of data with duplicate entries. First, cat sends the list into sort which sorts it and feeds it into uniq which removes any duplicates. Next pr and lpr are used to paginate and print the list.  
   
   - `tar tzvf name\_of\_file.tar.gz | less` View the contents of tar files. Tar files are compress folders that were created using gzip. tar = tape archive file. They have &#8220;tar.gz&#8221; or &#8220;.tgz&#8221; extensions.

9. File Permissions:

   `-rwxr-xr-x 1 root root 316848 Feb 27 2000 /bin/bash` = When you see a file like this, the first group of rwx's is permissions. Setup:  
   It is easy to think of the permission settings as a series of bits (which is how the computer thinks about them). Here's how it works:  
   `rwx rwx rwx` = 111 111 111  
   `rw- rw- rw-` = 110 110 110  
   `rwx --- ---` = 111 000 000  
   and so on&#8230;  
   `rwx` = 111 in binary = 7  
   `rw-` = 110 in binary = 6  
   `r-x` = 101 in binary = 5  
   `r--` = 100 in binary = 4

   Now, if you represent each of the three sets of permissions (owner, group, and other) as a single digit, you have a pretty convenient way of expressing the possible permissions settings. For example, if we wanted to set some_file to have read and write permission for the owner, but wanted to keep the file private from others, we would:  
   chmod 600 some_file

   - Examples:

   |Value|Looks Like | Meaning |
   |:---|:---|:---|
   |777 | `rwx-rwx-rwx`| No restrictions on permissions. Anybody may do anything. Generally not a desirable setting.|  
   |755 | `rwx-r-x-r-x`|The file's owner may read, write, and execute the file. All others may read and execute the file. This setting is common for programs that are used by all users.|  
   |700 | `rwx-------`|The file's owner may read, write, and execute the file. Nobody else has any rights. This setting is useful for programs that only the owner may use and must be kept private from others.|
   |666 | `rw-rw-rw-`|All users may read and write the file.|  
   |644 | `rw-r--r--`|The owner may read and write a file, while all others may only read the file. A common setting for data files that everybody may read, but only the owner may change.|  
   |600 | `rw-------`|The owner may read and write a file. All others have no rights. A common setting for data files that the owner wants to keep private.|  
   
   The chmod command can also be used to control the access permissions for directories. Again, we can use the octal notation to set permissions, but the meaning of the r, w, and x attributes is different:  
   r = Allows the contents of the directory to be listed if the x attribute is also set.  
   w = Allows files within the directory to be created, deleted, or renamed if the x attribute is also set.  
   x = Allows a directory to be entered (i.e. cd dir).

### References:

["What is the Shell?"](http://linuxcommand.org/lc3_lts0010.php)