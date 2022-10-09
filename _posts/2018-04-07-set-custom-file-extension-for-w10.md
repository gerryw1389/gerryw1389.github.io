---
title: Set Custom File Extension For W10
date: 2018-04-07T03:22:30+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/set-custom-file-extension-for-w10/
categories:
  - Windows
tags:
  - GroupPolicy
---
<!--more-->

### Description:

I haven't done this yet, but I wanted to take notes for when I do this. Follow this guide to set custom file extensions in Windows 10.

### To Resolve:

1. Setup computer the way you want

2. Run:

   ```powershell
   dism /online /export-defaultappassociations:"C:\Temp\IE-DefaultBrowser.xml"
   ```

   - NOTE: DO NOT delete lines from this.

   - This didn't work, what DID work was:

   ```powershell
   Dism /Online /get-DefaultAppAssociations >C:\TEMP\DefaultApps.txt
   ```

   - Then just rename to XML.

3. On new computer:

   ```powershell
   Dism.exe /online /import-defaultappassociations:c:\temp\CustomFileAssoc.xml
   ```

   - Your file will be copied in `C:\Windows\System32` with the following name `OEMDefaultAssociations.xml`

4. Or through GPO:

   - Configure the following policy `Set a default associations configuration file` located in `Computer\Policies\Administrative Templates\Windows Components\File Explorer`

   - If this group policy is enabled and the client machine is domain-joined, the file will be processed, and default associations will be applied at logon time.

   - To control only some extensions, see the reference.

### References:

["Windows 10 – How to configure file associations for IT Pros?"](https://blogs.technet.microsoft.com/windowsinternals/2017/10/25/windows-10-how-to-configure-file-associations-for-it-pros/)  

