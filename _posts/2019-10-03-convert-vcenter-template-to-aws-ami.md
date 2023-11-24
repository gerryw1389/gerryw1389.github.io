---
title: Convert Vcenter Template To AWS AMI
date: 2019-10-03T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/10/convert-vcenter-template-to-aws-ami
tags:
  - WebSoftware
---
<!--more-->

### Description:

Follow this guide to take an on-prem vCenter template and allow it to be an AMI (AWS Machine Image) so that you know the default username and password for newly deployed machines (or whatever purpose).


### To Resolve:

1. In vCenter, Create a VM from template. 
   - Then go to Actions - Template - Export as OVF template
   - This worked as expected, but I still wanted a single OVA file. 
   - I  was able to fix this by choosing the option of 'open' in VMWare Workstation locally on my machine from the exported ovf files and then once the VM imported, I exported as a single file OVA. Said another way: I took the exported vCenter files, imported them locally to my VMWare Workstation on my machine, and then exported as a single OVA file.

2. In AWS, Create a bucket
   - Create a user called 'svc_ami' with programatic access and add to group AWS-S3

   - Powershell:

   ```powershell
   Install-Module -Name AWSPowerShell
   Set-AWSCredential -AccessKey seeKeypass -SecretKey seeKeyPass -StoreAs AMI
   $cred = Get-AWSCredential -ProfileName AMI

   New-S3Bucket -BucketName ami-test -Region us-east-1 -Credential $cred
   Write-S3Object -Folder 'c:\scripts\test' -Recurse -BucketName 'ami-test' -Region us-east-1 -KeyPrefix '/vms' -Credential $cred
   ```

   - The end result of this command was I had a bucket named 'ami-test' with folder 'vms' and two files 'win2019.ova' and 'rhel7.ova'

3. At this point, I quit using powershell on Windows and switched over to WSL (because all examples were using awscli) . I then ran:

   ```shell
   # Startup bash
   apt-get update --fix-broken
   apt-get upgrade
   apt install python3-pip
   pip3 install awscli --upgrade --user
   # previous command didn't seem to do anything. So I did:
   apt install awscli
   ```

4. Now that we have awscli installed, we create a series of json files, 

   - In AWS Web UI, create a user called 'svc_api' with programatic access and add to group 'Account-Admin'. You will just need to ensure the user has rights to EC2 and S3 as far as I know.

   - Back in WSL, create 4 json files:
   - `cd /mnt/c/scripts`
   - `vi trust-policy.json`
   - Paste in:

   ```json
   {
   "Version": "2012-10-17",
   "Statement": [{
   "Effect": "Allow",
   "Principal": { "Service": "vmie.amazonaws.com" },
   "Action": "sts:AssumeRole",
   "Condition": {
      "StringEquals":{
         "sts:Externalid": "vmimport"
      }
   }
   }]
   }
   ```

   - `vi role-policy.json`
   - Paste in:

   ```json
   {
   "Version": "2012-10-17",
   "Statement": [{
   "Effect": "Allow",
   "Action": [
   "s3:ListBucket",
   "s3:GetBucketLocation",
   "s3:FullAccess"
   ],
   "Resource": [
   "arn:aws:s3:::ami-test"
   ]},
   {
   "Effect": "Allow",
   "Action": [
      "s3:GetObject"
   ],
   "Resource": [
      "arn:aws:s3:::ami-test/*"
   ]
   },{
   "Effect": "Allow",
   "Action":[
      "ec2:ModifySnapshotAttribute",
      "ec2:CopySnapshot",
      "ec2:RegisterImage",
      "ec2:Describe*",
      "ec2:FullAccess"
   ],
   "Resource": "*"
   }
   ]
   }
   ```

   - `vi cont.json`
   - Paste in:

   ```json
   [
   {
   "Description": "RHEL7",
   "Format": "ova",
   "UserBucket": {
      "S3Bucket": "ami-test",
      "S3Key": "vms/rhel7.ova"
   }
   }]
   ```

   - `vi cont2.json`
   - Paste in:

   ```json
   [
   {
   "Description": "WIN2019",
   "Format": "ova",
   "UserBucket": {
      "S3Bucket": "ami-test",
      "S3Key": "vms/win2019.ova"
   }
   }]
   ```

5. Now we set the credentials and do the actual import

   ```shell
   aws configure
   # enter access key, secret key of 'svc_api' NOT 'svc_ami' as they don't have rights to create new IAM policies
   # enter 'us-east-1' as the region and leave the return statements blank by just pressing 'enter' key
   aws iam create-role --role-name vmimport --assume-role-policy-document file://trust-policy.json
   aws iam put-role-policy --role-name vmimport --policy-name vmimport --policy-document file://role-policy.json
   aws ec2 import-image --description "RHEL7" --license-type BYOL --disk-containers file://cont.json
   aws ec2 import-image --description "WIN2019" --license-type BYOL --disk-containers file://cont2.json
   ```

6. Check the status of the imports

   ```shell
   aws ec2 describe-import-image-tasks --import-task-ids
   # get the id's 
   Now run
   aws ec2 describe-import-image-tasks --import-task-ids import-ami-xxxx
   ```

7. After they import, you can now select them when you go to create an EC2 instance.

