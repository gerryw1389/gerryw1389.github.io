---
title: LastPass to Keepass Conversion
date: 2017-08-26T05:50:20+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/lastpass-to-keepass-conversion/
categories:
  - LocalSoftware
tags:
  - Tweaks
---
<!--more-->

### Description:

So in order to move everything towards self-hosting, I recently migrated LastPass to KeePass. So far so good, just more of a hassle entering my password to unlock every so often.  
Overall view: I went from a third party cloud based company that conveniently stored all my passwords to a self hosted password manager with a HTTP extension that allows filling sign in's automatically. The main downside to my current setup is that KeePass has to be running in the system tray at all times so you have to make sure to auto-lock at certain time intervals. This of course makes it brutal as almost every time I need a password, I have to unlock my database first and that password is long! I guess, as with anything with security you are trying to balance convenience with security.

### To Resolve:

1. Programs: Keepass itself, KeePass Helper (Google Extension), and KeePass Google Sync (KeePass Extension)  

   - Install KeePass with KeePass Helper (Google Extension)
   - Download/Install KeePassHttp by dropping `KeePassHttp.plgx` into the KeePass Program Files directory
   - Log into KeePass
   - Verify KeePassHttp has been installed correctly by checking Tools > Plugins
   - Navigate to any page containing a password
   - Click the toolbar button
   - Switch to the KeePass window and enter a descriptive name into the dialog that popped up and click save.
   - Your passwords are now securely retrieved from KeePass and automatically entered into password forms and fields when needed.

2. This worked great until I got home and started having renames on my Google Drive due to it being open in both places. So then I download/installed KeePass Google Drive Extension:

   - Go to [Google API Console](https://console.developers.google.com/apis)
   - Create a new project => call it Keepass Google Sync
   - Enable Drive API on Library Screen
   - Go to credentials => Oauth Consent Screen => fill in your email and ProductName = Keepass Google Sync => Save.
   - Go to credentials => Create Credentials => Oauth 2.0 => Other => Copy client ID and password.
   - Now copy the plug in to your plugins and open up Keepass.
   - Make an entry with your Google credentials using [Google accounts](https://accounts.google.com/) in the URL. On that entry, go to Properties tab and copy the UUID at the bottom of the box.
   - Enter them in Tools => Google Sync => Configuration
   - Sign in to Google => then do an initial sync.
   - From now on, just sync with google!