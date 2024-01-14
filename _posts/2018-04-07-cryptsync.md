---
title: CryptSync
date: 2018-04-07T03:08:15+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/cryptsync/
tags:
  - LocalSoftware
tags:
  - PersonalConfig
---
<!--more-->

### Description:

Follow this guide to use a public cloud service (Google Drive in this example) and use [CryptSync](https://tools.stefankueng.com/CryptSync.html) to encrypt the files. If you just want to back your stuff up encrypted and don't care about access on other computers (except one off downloads of encrypted files that you can use 7zip to unzip with your password), skip the article. This is only if you have some &#8220;portable&#8221; stuff and some &#8220;private&#8221; stuff and you want to use more than one computer to access your cloud data.

### To Resolve:

1. Here is my setup at home: I have Google Drive => 1TB per year; 2 TB drives, Z:\ and S:\

2. On Z:\, I have one folder, Google. Subfolders are:

   - Z:\Google\Scripts => Powershell scripts and such  
   - Z:\Google\Data => We'll get to this in a minute  
   - Z:Google\Programs => usually portable programs like WizTree, VSCode, and some others  
   - Z:Google\Docs => work documents that I don't care if Google sees  
   - Z:\Google\&#8230;. => Here you can have as many Google folders and files as you want. They should be treated as &#8220;public&#8221; even if they are not. This is information that you don't mind if Google mines to sell advertisements to you. Should limit to only information that is &#8220;public&#8221;.  
  - Z:\Data => This is the parent folder for 99% of my files that are stored elsewhere, i.e. my &#8220;private&#8221; files. These are family photos, documents, etc. that I **DON'T** want Google to mine.

   - When I add Google Drive to another computer, I sync all directories except Google\Data. This allows me to have a portable Google folder for use in multiple places, but only one place with my important stuff being synced. I can always grab files from my &#8220;private&#8221; stash as explained later.

3. Now we get to CryptSync. What you do is set CryptSync to sync Z:\Data to Z:\google\data and you will get the same folder structure as you normally would (my-docs, my-pics, etc.), but all the files will be automatically encrypted with a password of your choosing. You then just set CryptSync to run on Windows startup and it will always make sure your data is encrypted that you send to Google. Since it uses 7zip, you can always restore by using 7zip to unzip the folder with your password to unencrypt a folder or file.

4. On the S:\, I have one main subfolder: S:\google-backup

5. The last step here is to have a robocopy script that copies:  
   - All of Z:\google except the &#8220;data&#8221; folder because it's encrypted.  
   - All of Z:\data because that is your important files.  
   - My script that does this and grabs folders from various drives and copies to my S drive. From there, I can back it up to an external using FreeFileSync and use Bitlocker for encryption.