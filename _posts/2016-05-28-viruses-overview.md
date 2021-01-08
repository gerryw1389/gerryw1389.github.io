---
title: Best Practice For Viruses
date: 2016-05-28T06:59:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/viruses-overview/
categories:
  - SysAdmin
tags:
  - Viruses
---
<!--more-->

### Description:

Viruses get on PC's in a number of ways but the most common is through pop up ads on the internet or email attachments. I tell customers all the time that the people who write viruses nowadays don't require you to be on the internet to get a virus, you computer just has to have CONNECTION to the internet to get infected. Remember to tell them that there is no absolute way not to get a virus on a computer unless you unplug the ethernet cable and never install anything on it.

Recommended virus removal steps can be found at: [Best Virus Removal Link](https://www.reddit.com/r/techsupport/comments/33evdi/suggested_reading_official_malware_removal_guide/)

### Common Signs of An Infection:

Computer is real slow -If you can try and open Task Manager and look at the Performance tab, or just Run => resmon.

Annoying Pop Up Windows => Customer will have pop ups about a program &#8220;scanning&#8221; their computer for a virus when it is itself a virus.

Anything that Blocks you from desktop when you login. These are common like the FBI and CryptoViruses. They belong to a class called ransomware.

**First Things to Check:**

Memory Usage  
Processes  
Run => %temp% (Windows 7)

### List of Best Practices:

1. Don't let users run arbitrary code. Set [SRP on Windows](https://technet.microsoft.com/en-us/library/Hh831534.aspx?f=255&MSPPError=-2147217396) and whitelist only trusted directories and executable hashes.

2. Make sure users can't write on trusted directories.

3. Make sure users don't have admin privileges at all.

4. Use an updated Antivirus.

5. Block any executable code (and zipped executables) on mail servers.

6. Install Chrome+uBlock/AdBlock to filter out adware. Ads are a big source of malware.

7. Add L-7/IPS/IDS filtering on your corporate firewall.

8. Use OpenDNS or another DNS filtering to stop malware requests.

9. Enable File System Resource Manager (FSRM) to detect early infection on Shared Folders. You can have a rule for strange behaviour (warn) and another for 100% sure infection (block user or disable the whole sharing service).

10. Keep Windows Updated.

11. Limit network privileges to users. They should only write on folders they need, the same for read access.

12. Ensure you have Shadow Copies both on users' computers and file servers.

13. Make backup of files and servers.

14. Ditch Flash and Java on web browsers.

15. Make your own Cryptowall Filters/Detectors. You can't trust commercial ones because these are the first that malware creator will test.