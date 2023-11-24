---
title: 'Plex: Automount With VirtualBox'
date: 2018-03-31T23:27:36+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/plex-automount-with-virtualbox/
tags:
  - Linux
tags:
  - Scripting-Bash
  - MediaEditing
---
<!--more-->

### Description:

So, the last time I moved some folders around between my drives I setup a new Plex directory for movies and such and now it won't auto mount like it used to. I used to fstab entries and it worked fine. I was tinkering around and I found a method, but I can't seem to get it to work. Will update this post when it is complete, but right now what I do is:  

- Reboot the VM  
- Login and run a bash file that automounts the drives  
- Not sure why crontab isn't working

### To Resolve:

1. First, I setup the shared folders in Virtualbox and then expose them to the CentOS vm as read only and auto mount.

2. I then set cron to start automatically before login:

   ```powershell
   sudo systemctl enable crond
   ```

3. Here is a bash script that will get called

   ```powershell
   #!/bin/sh
   mount -t vboxsf google /mnt/google/
   mount -t vboxsf vids /mnt/vids/
   ```

4. Here is the crontab entry

   ```powershell
   sudo crontab -e

   @reboot sleep 15; /home/user/myscript.sh
   ```

5. Reboot to test, didn't work. Had to do steps in description&#8230;

### UPDATE: 2018-04-01 - This was fixed by doing the following:

1. Remove the auto mount drives for VirtualBox completely.

2. In my Windows Host, I just created a new user &#8220;smb&#8221;.

3. I took my two folders that Plex needs to access and gave the security permissions for &#8220;smb&#8221; to read only.

4. In my CentOS VM, I tested:

   ```powershell
   smbclient -m SMB3 -U smb //192.168.0.20
   (enter password)
   # Prompt changes to: smb:
   exit
   ```

5. So I know that it works interactively. Next I just made sure to enable &#8220;samba&#8221; and &#8220;samba-client&#8221; in the firewall.

6. Now just need to update my /etc/fstab so it will automount:

   ```powershell
   //192.168.0.20/google-backup /mnt/google cifs vers=3.0,username=smb,password=Pa$$word,rw,uid=1000,gid=976 0 0
   //192.168.0.20/vids /mnt/vids cifs vers=3.0,username=smb,password=Pa$$word,rw,uid=1000,gid=976 0 0
   ```

7. It would be better to create a credentials file and put that in your home directory and access it that way:

   - From [https://wiki.ubuntu.com/MountWindowsSharesPermanently](https://wiki.ubuntu.com/MountWindowsSharesPermanently)

   ```escape
   The quickest way to auto-mounting a password-protected share is to edit /etc/fstab (with root privileges), to add this line:

   //servername/sharename /media/windowsshare cifs username=msusername,password=mspassword,iocharset=utf8,sec=ntlm 0 0  
   This is not a good idea however: /etc/fstab is readable by everyone and so is your Windows password in it. The way around this is to use a credentials file. This is a file that contains just the username and password.

   Using a text editor, create a file for your remote servers logon credential:

   gedit ~/.smbcredentials  
   Enter your Windows username and password in the file:

   username=msusername  
   password=mspassword  
   Save the file, exit the editor.

   Change the permissions of the file to prevent unwanted access to your credentials:

   chmod 600 ~/.smbcredentials  
   Then edit your /etc/fstab file (with root privileges) to add this line (replacing the insecure line in the example above, if you added it):

   //servername/sharename /media/windowsshare cifs credentials=/home/ubuntuusername/.smbcredentials,iocharset=utf8,sec=ntlm 0 0  
   Save the file, exit the editor.

   Finally, test the fstab entry by issuing:

   sudo mount -a  
   If there are no errors, you should test how it works after a reboot. Your remote share should mount automatically.
   ```
