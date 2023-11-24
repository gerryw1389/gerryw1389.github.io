---
title: 'GPO: Software Restriction Policy'
date: 2017-10-10T17:13:18+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/10/gpo-software-restriction-policy/
tags:
  - WindowsServer
  - Security
tags:
  - GroupPolicy
  - WindowsServer-Roles
---
<!--more-->

### Description:

This was somewhat covered in [CryptoPrevention](https://automationadmin.com/2016/05/gpo-cryptolocker-block/) but here is a more generic post on SRP's

### To Resolve:

1. Create a GPO and go to: `Computer Configuration\Policies\WindowsSettings\SecuritySettings\SoftwareRestrictionPolicies`

   - Right click => create a new default
   - Enforcement => all users
   - Designated file types => remove url/lnk
   - Next Security Levels => Disallowed => Set as default => click okay on warning
   - Right click on additional rules => add path rule
   - Now just add paths like `c:\windows`, `c:\program files`, `c:\program files (x86)`, and so on. These require admin rights for executable files to run so they should be safe.
   - Make sure to add any shares to file servers if users run portable programs from them.
   - As per my post linked, you would also want to blacklist certain paths:  
     - `%AppData%\*.exe` => Disallowed => Prevent programs from running in AppData.  
     - `%AppData%\*\*.exe` => Disallowed => Prevent virus payloads from executing in subfolders of AppData  
     - `%LocalAppData%\Temp\Rar\*\\*.exe` => Disallowed => Prevent un-WinRARed executables in email attachments from running in the user space  
     - `%LocalAppData%\Temp\7z\*\\*.exe` => Disallowed => Prevent un-7Ziped executables in email attachments from running in the user space  
     - `%LocalAppData%\Temp\wz\*\\*.exe` => Disallowed => Prevent un-WinZIPed executables in email attachments from running in the user space  
     - `%LocalAppData%\Temp\*.zip\*.exe` => Disallowed => Prevent unarchived executables in email attachments from running in the user space


2. Whitelist any applications going forward. Check event ID 875 for blocked software (windows logs => application)