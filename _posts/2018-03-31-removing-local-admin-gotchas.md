---
title: Remove Local Admin Gotchas
date: 2018-03-31T23:43:09+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/removing-local-admin-gotchas/
tags:
  - SysAdmin
---
<!--more-->

### Description:

Removing local admin is a good way to stop chances of user's getting viruses at a real high percentage, but unfortantely many organizations require that users run as local admin. I'm dealing with this at my org and have started removing it and tweaking issues as they come along. I found a post the other day and wanted to write down some steps that might be helpful to others in this situation.

### To Resolve:

1. Users can't write to program files

   ```powershell
   ICACLS "C:\Program Files (x86)\Your\Program" /grant Users:(OI)(CI)M
   ```

2. AppCompatFlags  
   - Some Applications can be flagged in the registry to run in compatibility mode. You can use AppCompat Flags to specify an application to run in XP mode, and require admin access. Just because an application prompts for admin, doesnt mean it Requires it.
   - `HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers`
   - Simply deleting the key can cause the application to work. I have also seen this key below used, though much less commonly.
   - `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers`

3. Manifest Files  
   - EXE's can use a manifest file to require an application to run as admin. The manifest file will be found with the EXE, and will be the name of the exe with the .manifest extension. So notepad.exe would have notepad.exe.manifest.

   - and example manifest file is shown below:

   ```xml
   <!--?xml version="1.0" encoding="utf-8" standalone="yes"?-->
   <?xml version="1.0" encoding="utf-8" standalone="yes"?>  
   <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">  
   <assemblyIdentity version="1.0.0.0"  
      processorArchitecture="X86"  
      name="Myobp.exe"  
      type="win32" />  
   <description>Manifest for Premier</description>  
   <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">  
      <security>  
      <requestedPrivileges>  
         <requestedExecutionLevel  
            level="RUNASADMIN"  
            uiAccess="false"/>  
      </requestedPrivileges>  
      </security>  
   </trustInfo>  
   </assembly>
   ```

   - I have had luck simply deleting the file, though manifest files can also point to older versions of DLL's. In that case, You may have better luck replacing `RUNASADMIN` with `ASINVOKER`

4. Installer detection  
   - `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\EnableInstallerDetection` => Set from `1` to `0`

5. Runas.exe  

   - One way we can stop someone from running as admin is to also supply admin credentials for the applications that request them. For example, accounting users may need to open Excel as admin for certain plugins to work. You would then do:

   ```powershell
   runas.exe /savecred /user:domain\localadmin "C:\Program Files (x86)\Microsoft Office\Root\Office16\EXCEL.EXE"
   ```

6. Download and install the ACT ([Application Compatibility Toolkit](https://blogs.technet.microsoft.com/yongrhee/2015/08/11/download-application-compatibility-toolkit-act-for-windows-10/)). Run it with your program and see what keys changed and relax the permissions on those paths. I haven't tested this yet, but it seems to be the correct way to do this.

7. Another tool to look into would the be the [LUA Buglight Application](https://blogs.msdn.microsoft.com/aaron_margosis/2015/06/30/lua-buglight-2-3-with-support-for-windows-8-1-and-windows-10/) from Microsoft. If you prefer third party, I've heard good things about [CyberArks](https://www.cyberark.com/privileged-identity-management/) product.