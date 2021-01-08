---
title: To Move Home To Another Drive
date: 2016-10-07T03:27:43+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/10/to-move-home-to-another-drive/
categories:
  - Linux
---
<!--more-->

### Description:

Follow these steps to move your /home directory to another drive.

### To Resolve:

1. Open terminal => type:

```shell
# Change to root
su

# Change ownership of second drive to your user. If you don't know the path to the second drive type "blkid" to find your drive.
chown gerry -R /dev/sdb1

# Give yourself permissions to that drive
chmod 666 -Rv /dev/sdb1

# Create a temp mount point
mkdir /mnt/tmp

# Mount your drive to that mount point
mount /dev/sdb1 /mnt/tmp

# Copy your current /home dir to that point
rsync -avx /home/ /mnt/tmp

# Unmount the drive
umount /mnt/tmp

# Rename the old home
mv /home /home.old

# Copy your drive UUID to a text editor like Pluma
blkid

#Open the auto mount file. Feel free to use vim or whatever.
vi /etc/fstab

#Paste in:
UUID=bdab1550-7619-495c-abf3-19ea3f95af60    /home    ext4    defaults   0  2

# Save and exit the file, then reboot
reboot
```

2. Your drive should be auto mounted!