---
title: Credential Manager Access Via PS
date: 2017-08-27T07:53:46+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/credential-manager-access-via-ps/
categories:
  - Security
---
<!--more-->

### Description:

So I have been getting a lot of Outlook credential issues lately so I thought I would post this as a reference for using PS with the Windows Credential Manager.

### To Resolve:

1. To launch from a run command: control /name microsoft.credentialmanager

2. To Clear Completely:

   ```powershell
   cmd /c "cmdkey /list" | ForEach-Object {if ($_ -like "*Target:*")
   {
   cmdkey /del:($_ -replace " ", "" -replace "Target:", "")
   }}
   ```

3. To add via script:

   ```powershell
   #Requires v5

   Install-Module -Name CredentialManager
   #Get-StoredCredential
   #New-StoredCredential
   #Remove-StoredCredential
   #Get-StrongPassword

   $a = get-storedcredential -type generic -ascredentialobject
   Remove-StoredCredential -Type generic -Target LegacyGeneric:target=MicrosoftOffice16_Data:SSPI:example@domain.com
   New-StoredCredential -Type generic -Target MicrosoftOffice16_Data:SSPI:example@domain.com -UserName example@domain.com -Password Pa$$word -Persist Enterprise
   ```

4. You can read up on cmdkey.exe if needed, but I'm trying to move more towards the PS methods. Ex:

   ```powershell
   cmdkey /generic:MS.Outlook:username@domain.com:PUT /user:user /pass:pass
   ```

