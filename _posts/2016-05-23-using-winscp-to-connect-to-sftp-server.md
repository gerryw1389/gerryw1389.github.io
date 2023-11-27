---
title: Using WinSCP To Connect To SFTP Server
date: 2016-05-23T12:33:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/using-winscp-to-connect-to-sftp-server/
tags:
  - LocalSoftware
  - SysAdmin
  - PKI
---
<!--more-->

### Description:

In every SSH/SFTP connection there are 2 key-pairs involved:

User private key- Usually a .ppk generated from PuttyGen. It is protected by a passphrase that should be long (that why it is not called a password).

User public key- Safely revealed to anyone.

Host private key- stored on the server, not revealed => client doesn't care about it

Host public key- given to anyone, the client is asked if they want to connect to it.

### To Resolve:

1. Generate a key pair using Putty/ Pageant:

   - Tools => PUttyGen => Generate A Key. This generates a private and public key for the client. Save the keys to path you will remember.

   - Tools => Pageant => Load the key pair.

2. Login to your SSH Server on the other end through some other means besides PKI.

3. Once logged in to your SSH/SFTP server, configure it to accept your public key that was generated in the previous step.

   - If you are using OpenSSH: 
     - Navigate into a .ssh subdirectory of your account home directory. You may need to enable showing hidden files to see the directory. If the directory does not exists, you need to create it first.  
     - Once there, open a file authorized_keys for editing. Again you may have to create this file, if this is your first key.  
     - Switch to the PuTTYgen window, select all of the text in the Public key for pasting into authorized_keys file box, and copy it to the clipboard (Ctrl+C). Then, switch back to the editor and insert the data into the open file, making sure it ends up all on one line.
     - Save the file.  
     - Ensure that your account home directory, your .ssh directory and file authorized\_keys are not group-writable or world-writable. 
     - Recommended permissions for .ssh directory are 700. 
     - Recommended permissions forauthorized\_keys files are 600. Read more about changing permissions.

   - If you are using SSH.COM:
     - Save a public key file from PuTTYgen, and copy that into the .ssh2 subdirectory of your account home directory.  
     - In the same subdirectory, edit (or create) a file called authorization. 
     - In this file you should put a line like Key mykey.pub, with mykey.pub replaced by the name of your key file.

   - For other SSH server software, you should refer to the manual for that server.

4. Next, configure your session: When configuring session, specify path to your private key on SSH > Authentication page of Advanced Site Settings dialog. Alternatively, load the private key into Pageant.

### References:

["Understanding SSH Key Pairs"](https://winscp.net/eng/docs/ssh_keys)  
["Set up SSH public key authentication"](https://winscp.net/eng/docs/guide_public_key)