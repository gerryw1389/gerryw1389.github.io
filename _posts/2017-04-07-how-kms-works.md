---
title: How KMS Works
date: 2017-04-07T16:52:16+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/04/how-kms-works/
tags:
  - WindowsServer
tags:
  - WindowsServer-Roles
---
<!--more-->

### Description:

This post is a quick introduction on how KMS works: KMS is a role you can install on a server that manages activations for computers in the environment. In general, you'll get a KMS key that is saved on the hosts. They check in with the KMS server to activate the product, and tracks compliance.

### To Resolve:

1. You need to get a 2016 KMS OS key, a CSVLK, not a GVLK, and install it on your KMS Server.

2. After that, you should verify your Win10 Machines have GVLK's on them, then point them at your KMS Server (I'd suggest DNS entries).

   - In a nutshell, there are 2 types of KMS Keys, a GVLK (Generic) that you install on almost everything, and a CSVLK (Not Generic) that you install only on your KMS HOST. Then you point your OS's at the Host, and the GVLK talks to the host and gets approved, assuming you have a valid CSVLK on the host for the OS.

   - You need a different OS CSVLK (and office) for each version that host is supporting.

   - I suggest you download VAMT from Microsoft to help you manage this.

3. Troubleshooting KMS:

   - When comes to troubleshooting KMS, the only commands I usually use are `cscript c:\windows\system32\slmgr.vbs` and its options.
   - For example: Re-register with KMS is `cscript c:\windows\system32\slmgr.vbs -dlv`
   - To uninstall and reinstall the product key:

   ```powershell
   cscript c:\windows\system32\slmgr.vbs -upk
   cscript c:\windows\system32\slmgr.vbs -ipk XXXXX-XXXXX-XXXXX-XXXXX-XXXXX  
   # from [docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)  
   # for Server 2019 Datacenter
   cscript c:\windows\system32\slmgr.vbs -ipk 6NMRW-2C8FM-D24W7-TQWMY-CWH2D
   ```

