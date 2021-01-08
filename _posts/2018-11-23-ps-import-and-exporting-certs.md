---
title: 'PS: Import and Exporting Certs'
date: 2018-11-23T16:14:47+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/11/ps-import-and-exporting-certs/
categories:
  - Windows
  - Security
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

So as part of the provisioning process, many companies will have their servers import and export certs. It shouldn't matter if you use a third party CA or an Enterprise CA, these scripts simply create a CSR "Request-NewCert" and import the .cer file "Import-Cert".

### To Resolve:

1. Go to my [gwSecurity](https://github.com/gerryw1389/powershell/tree/master/gwSecurity/Public) section on Github and run the scripts for importing and exporting certificates.

   - The `Request-NewCert` will create a CSR that you can run through a third party CA and get the .cer file to import.

   - Then you can run `Import-Cert` to import it to the Cert:\LocalMachine\My\ location.

   - If you want, you can also run the `Show-ComputerCerts` scripts to open an MMC file directly to your local machine certificates.

1. After importing, make sure that you see the lock icon next to the certs name. This verifies you have both the public and private key for the cert.

   - I have seen cases where certs didn't import correctly. If that happens, just run:
   - Get the `SerialNumber` from viewing the cert properties; make sure to remove any special characters or spaces
   - Open an admin CMD prompt and type: `certutil –repairstore my 010101010100101` replacing with 01 sequence with your serialnumber.
   - Example:
   
   ```powershell
   certutil –repairstore my 43e5e29096b64fd91a03b44eb040283f
   ```

