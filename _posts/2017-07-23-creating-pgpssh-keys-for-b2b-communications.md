---
title: Creating PGP/SSH Keys For B2B Communications
date: 2017-07-23T04:05:37+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/creating-pgpssh-keys-for-b2b-communications/
categories:
  - Security
---
<!--more-->

### Description:

Example: Every two to five years, the keys will expire for communications from Company A to B. The SSH key validates Company A client when it connects to Company B server. The PGP Key is to encrypt the payload when sending over information. Before you begin, make sure to install the GPG4Win Suite of software.

### To Resolve:

1. Create new folders to store these keys. Example dir:

   - 2017Keys
     - PGP
       - =>PGPPublic
       - =>PGPPrivate
     - SSH
       - =>SSHPublic
       - =>SSHPrivate

   NOTE: It shouldn't have to be written but if you are using NTFS, make sure to place VERY STRICT restrictions on who can access these paths. They will need to be somewhere that people can get to them for the following steps.
   {: .notice--success}

2. Create the PGP keys using Kleopatra.

   - Install the software
   - Generate your keypair so you can encrypt/decrypt messages. Go to File => New Certificate… => Create a personal OpenPGP key pair.
   - Make sure it is 2048 bit RSA. Expires in two years. Make note of the passphrase.
   - Right click on your key, then click `Export Certificates…` This is your public key. Save the key to the folders in step 1.
   - Right click on your key, then click `Export Secret Keys…` This is your private key. Save the key to the folders in step 1.

3. Create the SSH Keys using PuttyGen.

   - Create a key using SSH-2 RSA. Set bits to 2048. Create a complex passphrase.
   - Save the keys to the folders in step 1.

4. Now for the renewal process => Create two files using Notepad++:

   - companya.transportin.dat = SSH Key => Copy and paste your SSH public key in here.
   - companya.payloadin.dat = PGP Key => Copy and paste your PGP public key in here.

5. Send the two dat files over via WinSCP to CompanyB. Wait for them to confirm they got them. Once the company confirms they got the keys, you will use WinSCP to transfer files to them on the day they specify they will cut over keys on their servers.

6. Configuring WinSCP to import the SSH Key:

   - Launch WinSCP and Create a new site:
   - Protocol: `SFTP`
   - Hostname: `companybservername.domain.com`
   - PortNumber: `22`
   - Username: `companya_username` #provided by company B
   - Password: `your_password` #provided by company B, should be setup already if you are renewing
   - Edit => `Advanced`
   - Directories:
   - Remote = `/path/on/companyBserver/for/transportkeys`
   - Local = `\path\users\use\to\transfer\files\to\companyB`
   - Authentication:
   - Authentication Parameters: Private key file = `Path\to\PrivateSSHKey`
   - Now connect by entering your passphrase for the SSH key.

7. Configure WinSCP to use PGP Key for payload encryption and file signing: No path setup, you have to import the private key into each server that connects to Company B.

   - Open up the GPA program.
   - Click `Import` in the top menu bar.
   - Navigate to the location of the private key: `Path\to\PrivatePGPKey`
   - Import the key.

8. Log the expiration dates in your documentation software.