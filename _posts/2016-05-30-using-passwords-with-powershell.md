---
title: 'PS: Using Passwords In Your Scripts'
date: 2016-05-30T06:02:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/using-passwords-with-powershell/
categories:
  - Windows
  - Security
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Sometime when using PS, you will have a set of credentials that you want to store for future use (like automation). There are multiple ways to doing this, some are more secure than others.

### To Resolve:

1. First, the version that encrypts using your User Account:
   - First we need to get our password and pump it to a file:

   ```powershell
   Read-Host -Assecurestring | Convertfrom-Securestring | Out-File C:\Scripts\Cred.Txt
   
   # Then, draw it back into our scripts:
   $Password = Get-Content C:\Scripts\Cred.Txt | Convertto-Securestring
   
   #Finally, we create a credential object which we pump into other cmdlets:
   $Creds = New-Object -Typename System.Management.Automation.Pscredential -Argumentlist Yourusername, $Password
   ```

   - You could store your password in your profile dirctory (usually `C:\Users\userName\Documents\WindowsPowerShell`) and then place it in your profile script in order to always have it.

   - A variation of the same thing:   

   ```powershell
   # Encryption
   $credpath = "c:\scripts\MyCredential.xml"
   New-Object System.Management.Automation.PSCredential("mycomputer\gerry", (ConvertTo-SecureString -AsPlainText -Force "Pa$$word")) | Export-CliXml $credpath

   # Decryption, placed in scripts on that machine
   $cred = Import-Clixml -Path $credpath
   ```

   - This way seems to be common, but only works if you run as the same user on the same computer. Most of my scripts will touch multiple servers so this does not work.

2. A less secure way that relies on NTFS permissions that uses a portable keyfile:

   - What you can do, is to create a random 32-bit key (the maximum supported by AES) and store it to a file:

   ```powershell
   $KeyFile = "C:\Scripts\AES.key"
   $Key = New-Object Byte[] 32
   [Security.Cryptography.RNGCryptoServiceProvider]::Create().GetBytes($Key)
   $Key | out-file $KeyFile
   
   # Then, invoking the stored key, create the encrypted password:
   $PasswordFile = "C:\Scripts\AESpassword.txt"
   $Key = Get-Content "C:\Scripts\AES.key"
   $Password = "password" | ConvertTo-SecureString -AsPlainText -Force
   $Password | ConvertFrom-SecureString -key $Key | Out-File $PasswordFile
   ```

   - Then, in your script call the password and key:
   
   ```powershell
   $User = "domain\administrator"
   $PasswordFile = "C:\Scripts\AESpassword.txt"
   $Key = Get-Content "C\:Scripts\AES.key"
   $Creds = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, (Get-Content $PasswordFile | ConvertTo-SecureString -Key $Key)
   ```

   - As you can imagine, this makes scripts portable as you can place the key and password file on a fileserver and share it out.
   - The main thing there is to just set the correct NTFS permissions. Your password is essentially wide open if an attacker were to get the key.

   - A variation of the same concept, but stores the key directly in the file:

   ```powershell
   # Encryption
   $Key = (3,4,2,3,56,34,254,222,1,1,2,23,42,54,33,233,1,34,2,7,6,5,35,43)
   Read-Host -Assecurestring | Convertfrom-Securestring -Key $Key | Out-File 'C:\Scripts\Encrypted_Pw.xml'

   # Decryption
   $Key = (3,4,2,3,56,34,254,222,1,1,2,23,42,54,33,233,1,34,2,7,6,5,35,43)
   $Password = Get-Content 'C:\Scripts\Encrypted_Pw.xml' | Convertto-Securestring -Key $Key
   $Username = "gerry"
   $Cred = New-Object -Typename System.Management.Automation.Pscredential -Argumentlist $Username, $Password
   ```

   - Lastly, if you ever want to just encrypt a string instead of credentials, you just pass a blank user name:

   ```powershell
   $Key = (3,4,2,3,56,34,254,222,1,1,2,23,42,54,33,233,1,34,2,7,6,5,35,43)
   $Password = Get-Content 'C:\Scripts\Encrypted_Pw.xml' | Convertto-Securestring -Key $Key
   $Username = "blank"
   $Cred = New-Object -Typename System.Management.Automation.Pscredential -Argumentlist $Username, $Password
   $string = $cred.GetNetworkCredential().Password
   Write-Output "text is $string"
   # Alternatively, just call [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($Password))
   ```

### References:

["Powershell Tip – Storing and Using Password Credentials"](https://blogs.technet.microsoft.com/robcost/2008/05/01/powershell-tip-storing-and-using-password-credentials/)  

["Encrypt Passwords"](http://www.virtualtothecore.com/en/encrypt-passwords-in-powershell-scripts/)