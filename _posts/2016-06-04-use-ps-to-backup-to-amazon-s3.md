---
title: 'PS: Backup To Amazon S3'
date: 2016-06-04T06:04:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/use-ps-to-backup-to-amazon-s3/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - Cloud
  - FileSystem
---
<!--more-->

### Description:

So here is the situation: Our AS400 sends backups to our FTP daily. We needed a way to zip the files and upload them to Amazon S3. I found a way to do this PS, hopefully it will help someone out. To backup to Amazon S3 in Powershell, try the following:

NOTE: These steps require you download and install [PSCX](https://pscx.codeplex.com/) and [AWS PS Tools](https://aws.amazon.com/powershell/)

### To Resolve:

1. In the SFTP VM: Copy and paste this into Powershell ISE (or Notepad and save as .ps1). Save to &#8220;C:\Scripts&#8221; (substitute your information below):

   ```powershell
   # Step 1: Import Modules
   Import-Module pscx
   Import-Module "C:\Program Files (x86)\AWS Tools\PowerShell\AWSPowerShell\AWSPowerShell.psd1"

   # Step 2: Setup Amazon Environment
   $AKey= "accessKeyhere"
   $SKey= "secretKeyhere"
   Set-AWSCredentials -AccessKey $AKey -SecretKey $SKey

   # Step 3: Compress the most recent backups to a zip file
   $source = "F:\Backups"
   $item = Get-Childitem $source | Where-Object { $_.PSIsContainer } | Sort-Object CreationTime -Desc | Select-Object -First 1
   $iname = $item.name
   $destination = "F:\Backups\$iname.zip"
   Set-Location $source
   Write-Zip -LiteralPath $item -OutputPath $destination -Level 9

   # Step 4: Write to bucket then delete the original file
   # NOTE: Another script will delete all the zip files every weekend
   Write-S3Object -BucketName backups -File $destination
   Remove-Item $item -Force
   ```

2. Next step is to find a way to upload these to the Amazon Cloud Storage. First we download PSCX and Amazon PS Tools and install them to SFTP.

3. Go to [IAM](https://console.aws.amazon.com/iam/). From there go to Groups => Name: Administrators => Policies: Administrator Access => Finish.

4. Now go to Users => name: (AdminAccountName) => Download credentials. Make sure to add that user to the Administrators group and assign the admin password via &#8220;Manage Password&#8221;.

5. Now that the account is setup, we can run the script in step 1.

   - You can load into your profile by running:  
   - `echo $profile` #take note of the directory  
   - `notepad $profile` #this opens it. If it doesn't exists it creates it. Paste in:  
   - `Import-Module "C:\Program Files (x86)\AWS Tools\PowerShell\AWSPowerShell\AWSPowerShell.psd1"`  
   - Save the notepad document in the location from step A. If the directory doesn't exist, create it exactly named as so.

6. Source is maintained under [gwFileSystem](https://github.com/gerryw1389/powershell/blob/master/gwFilesystem/Public/Backup-ToAmazon.ps1)