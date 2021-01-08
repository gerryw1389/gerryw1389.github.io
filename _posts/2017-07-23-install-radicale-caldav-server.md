---
title: Install Radicale CalDAV Server
date: 2017-07-23T06:45:49+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/install-radicale-caldav-server/
categories:
  - LocalSoftware
  - Linux
tags:
  - Setup
---
<!--more-->

### Description:

So like many of my peers, I'm trying to move to [self-hosting](https://github.com/Kickball/awesome-selfhosted) as much as possible. This post will outline how I went from Google Calendar to CentOS Radicale Server with Thunderbird client as the replacement.

### To Resolve:

1. If you haven't already, create a CentOS 7 VM that you use as a &#8220;base&#8221; image that you can clone. I have one with MATE installed that I spin up every now and then to run updates. We will start by making a clone and logging in.

2. The first thing we need to do is setup a python environment, I used [this](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7) guide:

   - Type:

   ```shell
   sudo yum -y update
   sudo yum -y install yum-utils
   sudo yum -y groupinstall development
   sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
   sudo yum -y install python36u

   # Check
   python3.6 -V
   sudo yum -y install python36u-pip

   # To install a package: sudo pip3.6 install package_name
   sudo yum -y install python36u-devel

   # Setting up environment
   mkdir environments
   cd environments
   python3.6 -m venv my_env
   # To use, we have to activate: source my_env/bin/activate
   # NOTE: Within the virtual environment, you can use the command python instead of python3.6, and pip instead of pip3.6 if you would prefer. If you use Python 3 on your machine outside of an environment, you will need to use the python3.6 and pip3.6 commands exclusively.
   ```

3. To install Radicale, we issue two commands:

   ```shell
   sudo python3.6 -m pip install --upgrade radicale
   sudo python3.6 -m radicale --config "" --storage-filesystem-folder=~/.var/lib/radicale/collections
   # Open http://localhost:5232/ in your browser and create a calendar. I called it home.
   ```

4. We could just be done here, but the problem is that anyone can get to your server without a password (any password works!). So the next step is to increase security by using bcrypt.

   - Type:

   ```shell
   sudo yum install httpd-tools
   sudo htpasswd -B -c /home/gerry/apps/users gerry

   # This does two things, it creates a file called "users" and sets an encrypted password
   sudo python3.6 -m pip install --upgrade passlib bcrypt
   sudo mkdir /home/gerry/.config/radicale
   cd /home/gerry/.config/radicale
   sudo touch config
   sudo vi config

   # Paste the following:
   [auth]
   type = htpasswd
   htpasswd_filename = /home/gerry/apps/users
   # Encryption method used in the htpasswd file
   htpasswd_encryption = bcrypt
   [server]
   hosts = 0.0.0.0:5232, 192.168.0.15:5232
   [server]
   max_connections = 20
   # 1 Megabyte
   max_content_length = 10000000
   # 10 seconds
   timeout = 10
   [auth]
   # Average delay after failed login attempts in seconds
   delay = 1000
   [storage]
   filesystem_folder = /home/gerry/.var/lib/radicale/collections
   # Save and exit - Now Radicale requires a password!
   ```

5. Now you can run Radicale by just typing &#8220;radicale&#8221;. The website has a way to set it up as a service using systemd, but I couldn't get it to work because I'm a newb with linux. Instead, I just set it as a startup application using MATE's Startup Applications as &#8220;/usr/bin/radicale&#8221;. Only downside is I will have to login after each reboot. I'm sure I will create a cron for this later o_O

6. Next step is to import your google calendar. Download it via the web and then edit it with Notepad++. We need to remove the UID's that Google uses or Radicale won't import properly. This is the error you will get: `Muliple VEVENT components with different UIDs in object: "p64bb8045e8sdfskv90ean9gesi6vggoogle.com", "o1vl26smvm4vdfs7oed9h155kb598google.com"` or something to that effect.

   - Do a find and replace in Regular Expression mode and set it like:

   ```escape
   find = UID:.*
   replace = UID:whateveryouwant
   # save the file and exit.
   ```

7. Now we just import it to your radicale profile:

   - Copy your .ics to file to /home/gerry/.var/lib/radicale/collections/calendar.ics => it will start to create multiple events => that's okay.

8. Now would be the time to open port on router and forward to your new CalDAV server if you want to access it out of your home. Make sure to create a firewall rule to allow port 5232 open on your CentOS vm.

9. Once you have your login info, login and copy the URL to your server, it should end in a random GUID.

10. Install Thunderbird and set it to that path using Lightning. It should prompt for a username/password.

11. Profit! As a benefit, you can always go back to any other application that imports .ics files by logging into Radicale via your web GUI and just downloading the calendar.