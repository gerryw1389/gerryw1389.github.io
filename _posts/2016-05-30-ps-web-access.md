---
title: 'PS: Web Access'
date: 2016-05-30T04:44:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ps-web-access/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - WebServer
---
<!--more-->

### Description:

Windows PowerShell Web Access acts as a Windows PowerShell gateway, providing a web-based Windows PowerShell console that is targeted at a remote computer. It enables IT Pros to run Windows PowerShell commands and scripts from a Windows PowerShell console in a web browser, with no Windows PowerShell, remote management software, or browser plug-in installation necessary on the client device. All that is required to run the web-based Windows PowerShell console is a properly-configured Windows PowerShell Web Access gateway, and a client device browser that supports JavaScript and accepts cookies.

### To Resolve:

1. First run:

   ```powershell
   Install-WindowsFeature WindowsPowershellWebAccess
   ```

   - This installs IIS, .NET v4.5, and a new PS Module

2. Next you run:

   ```powershell
   Install-PSWAWebApplication -UseTestCertificate
   ```

   - This installs creates a 90 day test cert, you are highly advised to point to your own signed cert instead.

3. Next you run:

   ```powershell
   Add-PSWAAuthorizationRule -Computername Computername -Username Domainuser
   ```

   - This allows a user to control a remote computer.

4. Next you run:

   ```powershell
   Add-PSWAAuthorizationRule * * *
   ```

   - This allows you to have full control. Typically not what you want, but it's just for testing.

5. You should now be able to open up a browser and use it to run powershell on any machine in your network you have access to.

6. I just scratched the surface of this, but will continue to look into how it works.

### References:

["Install and Use Windows PowerShell Web Access"](https://technet.microsoft.com/en-us/library/Hh831611.aspx)