---
title: 'Veeam: Encrypting Backup Jobs'
date: 2017-08-26T05:22:16+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/veeam-encrypting-backup-jobs/
tags:
  - LocalSoftware
tags:
  - Backup
---
<!--more-->

### Description:

Encrypting backup jobs with Veeam is pretty straightforward. You create a passphrase on the Veeam Server and it uses its technology to encrypt your backups for you.

### To Resolve:

1. Enable configuration backup encryption: Main Menu => Config Backup => Encrypt => Enter your password.

2. Go into jobs and right click properties => Storage => Advanced => Storage => Check the box to use encryption.

3. That's literally all you have to do!

4. More info: The backup job processing with encryption enabled includes the following steps:

   - You enable encryption for a backup job and specify a password.  
   - Veeam Backup & Replication generates the necessary keys to protect backup data.  
   - Veeam Backup & Replication encrypts data blocks on the backup proxy, either the dedicated or default one, and transfers them to the backup repository already encrypted.  
   - On the backup repository, encrypted data blocks are stored to a resulting backup file.

5. Restore of an encrypted backup file includes the following steps:

   - You import a backup file and define a password to decrypt the backup file. If the password has changed once or several times, you need to specify the password in the following manner:  
   - If you import an incremental backup file, you need to specify the latest password that was used to encrypt files in the backup chain.  
   - If you import a full backup file, you need to specify the whole set of passwords that were used to encrypt files in the backup chain.  
   - Veeam Backup & Replication uses the provided password(s) to generate user key(s) and unlock the subsequent keys for backup file decryption.  
   - Veeam Backup & Replication retrieves data blocks from the backup file, sends them to the source side and decrypts them on the backup proxy, either the dedicated or default one.

### References:

[https://helpcenter.veeam.com/docs/backup/hyperv/config\_backup\_encrypted.html?ver=95](https://helpcenter.veeam.com/docs/backup/hyperv/config_backup_encrypted.html?ver=95)

[https://helpcenter.veeam.com/docs/backup/hyperv/encryption\_backup\_copy_job.html?ver=95](https://helpcenter.veeam.com/docs/backup/hyperv/encryption_backup_copy_job.html?ver=95)

A full walk through scenario: [https://helpcenter.veeam.com/evaluation/backup/hyperv/en/em\_restore\_no_password.html](https://helpcenter.veeam.com/evaluation/backup/hyperv/en/em_restore_no_password.html)