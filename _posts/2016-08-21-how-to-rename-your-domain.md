---
title: How To Rename Your Domain
date: 2016-08-21T16:55:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/how-to-rename-your-domain/
tags:
  - WindowsServer
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

Say you want to remove the old standard of .local from your domain and rename your domain to the proper ad.company.com. Follow these steps to rename your domain (without building a new one!). Follow the reference link for pictures and the original post. I suggest doing this in a test lab first!

### To Resolve:

1. Setup:

   - Install and promote two domain controllers: DC0 and DC1
   - Install a member server like a file server and a workstation client as well.
   - The key to the procedure is one domain member machine that is not a domain controller to perform almost all steps from. This can be a Windows 7 machine with Remote Server Administration Tool (RSAT) installed, but I prefer to use Windows 2008 R2 server since the rendom utility gets installed automatically as part of &#8220;Active Directory Domain Services&#8221; role. But make sure not to promote the machine to a domain controller as this machine should not be a domain controller.

2. On the domain joined server, (called FILE0 in my case) create a new DNS zone with the new domain. New records will start being created in that zone as soon as we perform the rename.

3. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `rendom /list`. A xml file will be created that lists the current domain that has info such as ForestDNSZones, DomainDNSZones, and Netbios name.

4. Edit this file to replace all mention of the old domain with the new domain name. In this case I've replaced all occurrences of untitled.local with thinkarabia.net and all occurrences UNTITLED with THINKARABIA.

5. Verify by running: `rendom /showforest`

6. Now that we feel more confident, it is time to upload the modified xml to our domain controllers using the command `rendom /upload`.

7. On the DC's, turn off Windows Firewall and open up CMD to type: `rendom /prepare`.

8. Once they say successful, type: `rendom /execute`

9. After execution, all domain controllers will reboot at the same time! After they come back, take your FILE0 and reboot it TWICE to make it aware of the new domain change. On the second time coming up, your server will want to login using the old domain => ignore this and switch user. Login with the new domain name.

10. Group polices still reference the old domain names, and hence we need to fix it. Open up a command prompt and type:

   ```escape
   gpfixup /olddns: untitled.local /newdns:thinkarabia.ent  
   gpfixup /oldnb:UNTITLED /newnb:THINKARABIA
   ```

11. Now we rename the domain controllers themselves. Open up CMD and type:

   ```escape
   netdom computername dc0.untitled.local /add:dc0.thinkarabia.net  
   netdom computername dc0.untitled.local /makeprimary:dc0.thinkarabia.net
   ```

12. Restart both domain controllers. On FILE0, open up CMD and type:

   ```escape
   rendom /clean
   ```

13. At this point, reboot all client machines twice in order for the changes to stick. Done!

### References:

["How to Rename Your Active Directory Domain "](https://www.pluralsight.com/blog/software-development/rename-active-directory-domain)