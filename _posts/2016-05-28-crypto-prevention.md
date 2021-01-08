---
title: Crypto Prevention
date: 2016-05-28T07:01:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/crypto-prevention/
categories:
  - WindowsServer
tags:
  - WindowsServer-Roles
  - Viruses
---
<!--more-->

### Description:

In light of all the crypto viruses going around, I found this great guide on Reddit for crypto prevention techniques:

### To Resolve:

1. 2019-06-13 Updated notes

   ```escape
   Offline backups. 3-2-1 Backup Rule. Test it.

   Enable AppLocker. Allow signed execution only. Disallow %Temp% or %AppData% entirely.

   Require local administrators enter credentials for UAC (and minimize the number of local admins).

   Network segregation: Workstations should not be able to SMB to one another cross-departmentally, or cross-floors/cross-rooms/whatever segregation/etc. This can isolate an infection to a single department/floor/room/space only. And should use centralized servers for inter-file transfers (or email/OneDrive/chat services). Local Admins should not have access to C$ on the servers.

   Don't allow email to contain: Executables, password protected zip files, or Office macros.

   Another one i'd like to add: Use LAPS to randomize your local admin passwords! most of these cryplockers are not that smart and use stuff like psexec to spread itself and if you have the same local admin password on all your machines you are pretty much frakked.

   Also, get something that monitors your network and file servers for suspicious activity like mass encryption of files. And/or get a virus scanner that doesnt just look at files but also behaviour like for example CB defense.

   Also remove the ability to execute js, vbs, wse, vbe, jse, vbe and ps1, also tonnes of group policy templates online to block if applocker not available and you fallback to SRP.

   ```

   - [Source](https://www.reddit.com/r/sysadmin/comments/c9r8g7/crypto_virus_ilove911dotcom_currently_attacking/)


1. Install File Server Resource Manager

   - 2008(R2): Server Manager => Roles => Add Roles => Add Roles Wizard => Server Roles - File Services => Role Services => File Server Resource Manager

   - 2012(R2): Server Manager => Manage => Add Roles and Features => Add Roles and Features Wizard => Server Roles - File and Storage Services => File and iSCSI Services => File Server Resource Manager

2. Server-side protection from further encryption

   - Open File Server Resource Manager (Start => Run => `fsrm.msc`)

   - File Screening Management => File Groups => Create File Group => File group name: 1-PreventCrypto

   ```escape
   Files to include:
   *.aaa  
   \*.cryptotorlocker\*  
   *.ecc  
   *.encrypted  
   *.exx  
   *.ezz  
   *.frtrss  
   *.vault  
   *.vvv  
   \*restore_fi\*.*  
   \*want your files back.\*  
   confirmation.key  
   cryptolocker.*  
   decrypt_instruct\*.\*  
   enc_files.txt  
   help_decrypt\*.\*  
   help_restore\*.\*  
   help\_your\_file\*.\*  
   how to decrypt\*.\*  
   how_recover\*.\*  
   how\_to\_decrypt\*.\*  
   how\_to\_recover\*.\*  
   howtodecrypt\*.\*  
   install_tor\*.\*  
   last_chance.txt  
   message.txt  
   readme\_for\_decrypt\*.\*  
   recovery_file.txt  
   recovery_key.txt  
   vault.hta  
   vault.key  
   vault.txt  
   your_files.url  
   \*gmail\*.crypt  
   howto\_restore\_file\*.\*  
   *.crjoker
   ```

   - After creating the file group per above, update the entire list easily by running `C:\Windows\1-PreventCrypto-FileGroupUpdate.bat`. You must edit this .bat to include the name of your file group

   -Batch file source:  

   ```console
   @ECHO OFF  
   REM This file was last updated 01/13/2016

   REM Edit to match your filegroup below  
   filescrn.exe filegroup modify /filegroup:"1-PreventCrypto" /members:"\*.aaa|\*.cryptotorlocker\*|\*.ecc|\*.encrypted|\*.exx|\*.ezz|\*.frtrss|\*.vault|\*.vvv|\*restore\_fi\*.\*|\*want your files back.\*|confirmation.key|cryptolocker.\*|decrypt\_instruct\*.\*|enc\_files.txt|help\_decrypt\*.\*|help\_restore\*.\*|help\_your\_file\*.\*|how to decrypt\*.\*|how\_recover\*.\*|how\_to\_decrypt\*.\*|how\_to\_recover\*.\*|howtodecrypt\*.\*|install\_tor\*.\*|last\_chance.txt|message.txt|readme\_for\_decrypt\*.\*|recovery\_file.txt|recovery\_key.txt|vault.hta|vault.key|vault.txt|your\_files.url|\*gmail\*.crypt|howto\_restore_file\*.\*|*.crjoker"  
   ECHO.

   PAUSE  
   EXIT
   REM More info at [Filescrn filegroup modify](https://technet.microsoft.com/en-us/library/cc788114(v=ws.10).aspx)

   ```

   - File Screening Management => File Screen Templates => Create File Screen Template

   ```escape
   - Settings tab  
   Template name: 1-PreventCrypto  
   Screening type: Passive screening  
   File groups: Check "1-PreventCrypto"

   -E-mail Message tab  
   Subject: Unauthorized file from the [Violated File Group] file group detected  
   Body:  
   User [Source Io Owner]  
   Saved [Source File Path] to [File Screen Path]  
   On server: [Server]  
   This file is in the [Violated File Group] file group in FSRM, which generated this alert.  
   A batch was run to remove all server shares until corrective action is taken.

   -Event Log tab  
   Check "Send warning to event log"

   -Command tab  
   Check "Run this command or script"  
   Browse C:\Windows\1-PreventCrypto.bat  
   NOTE: you must edit this .bat to include the names of all your shares  
   Select radio button: "Local System"
   ```

   - File Screening Management => File Screens => Create File Screen  

   ```escape
   -File screen path: C: (or just the drive/folder containing shares)  
   Select radio button: "Derive properties from this file screen template (recommended)"  
   Select from dropdown: "1-PreventCrypto"
   ```

   - File Server Resource Manager (Local) => right-click: Configure options&#8230;

   ```escape
   -Email Notifications tab  
   Set SMTP server name (use SMTP relay if you don't have a mail server on-site)  
   Set Default administrator (see how to)

   -Notification Limits tab  
   Set all to 2 minutes
   ```

3. Other protections worth doing

   - Ensure Internet filter is updating to block known badware domains (suggestion: DNS Redirector)
   - Ensure Internet filter is blocking ccTLDs and IDNs that are not relevant to your business (suggestion: DNS Redirector, see how to)
   - Ensure Firewall is blocking any URLs with an IP address (only the bad guys do this)  
   - Bad: http://93.184.216.34 | Good: http://example.com | see how to
   - Ensure Firewall is blocking DNS outbound from everything except your internal/AD DNS server IP(s)
   - Ensure Firewall is allowing only good/necessary ports outbound (NOT any/any)  
   - Suggestion for DCs: 53,80,123,443,3544 | Suggestion for End-Users: 80,443,1935,3544
   - Run CryptoPrevent by Foolish IT on every end-user workstation, apply at least the standard rules, restart
   - Consider implementing Software Restriction Policies (SRP) via Group Policy (or AppLocker, or application whitelist)
   - Use an anti-virus product and/or Malwarebytes on end-user workstations, ensure it is updating

4. Cleanup procedure
   - Either you received an email from FSRM with the details, or you suddenly realized all server shares are missing&#8230;
   - On the server which detected the bad files go to Event Viewer > Windows Logs > Application  
   - Look for a Warning entry from SRMSVC as the source, the General box contains the details of the username and filename which triggered the shares to be removed
   - Unplug the offending user's machine from the network
   - Cleanup user's temp folders and startup items (suggestion: CCleaner)
   - Ensure user's machine is malware/toolbar/nonsense free (suggestion: Malwarebytes)
   - Run CryptoPrevent by Foolish IT apply at least the standard rules, restart
   - Format and reload the OS on this user's machine if you prefer
   - Restore any files that did get encrypted from your backups. NOTE: Many variants of this badware do NOT change the file modified time/date stamp to when encryption occurred
   - Add all the shares back to the server (see created file: C:\Windows1-PreventCrypto-PreviousShares.txt)
   - Re-enable the Windows firewall rules for File and Printer Sharing


### References:

["Cryptolocker/Cryptowall prevention file screening..."](https://www.reddit.com/r/sysadmin/comments/3gm9ji/cryptolockercryptowall_prevention_file_screening/)  
["Stop CryptoLocker (and copy-cat variants of this badware) before it ruins your day"](http://jpelectron.com/sample/Info%20and%20Documents/Stop%20crypto%20badware%20before%20it%20ruins%20your%20day/1-PreventCrypto-Readme.htm)  