---
title: 'PS: Code Signing'
date: 2016-11-27T07:51:02+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/ps-code-signing/
tags:
  - Windows
  - Security
tags:
  - Powershell
---
<!--more-->

### Description:

When creating scripts in Powershell, it's a good idea to setup a code signing cert and add it to your cert store. Here are the steps I use(d).

### To Resolve:

1. First, I know MS has the New-SelfSignedCertificate natively now, but I still downloaded the one [here](https://gallery.technet.microsoft.com/scriptcenter/Self-signed-certificate-5920a7c6#content).

2. Then, in Powershell ISE, just run:

```powershell
New-SelfsignedCertificateEx -Subject "CN=Test Code Signing" -EKU "Code Signing" -KeySpec "Signature" `
-KeyUsage "DigitalSignature" -FriendlyName "Test code signing" -NotAfter $([datetime]::now.AddYears(5))
```

3. Then, to sign a script, just type:

```powershell
$MyCert =(dir Cert:\CurrentUser\My -CodeSigningCert)[0]
# Example Set-AuthenticodeSignature .\test.ps1 -Certificate $MyCert
```

4. You could place the $MyCert variable in your profile on the machine you ran this on and then just have that sign all the scripts you produce.