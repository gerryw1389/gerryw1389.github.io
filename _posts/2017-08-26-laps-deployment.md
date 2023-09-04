---
title: LAPS Deployment
date: 2017-08-26T05:54:19+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/laps-deployment/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

Microsoft is offering the Local Administrator Password Solution ([LAPS](https://technet.microsoft.com/en-us/library/security/3062591.aspx)) that provides a solution to the issue of using a common local account with an identical password on every computer in a domain. LAPS resolves this issue by setting a different, random password for the common local administrator account on every computer in the domain. Domain administrators using the solution can determine which users, such as helpdesk administrators, are authorized to read passwords.

Compromised identical local account credentials could allow elevation of privilege if an attacker uses them to elevate from a local user/administrator to a domain/enterprise administrator. Local administrator credentials are needed for occasions when logon is required without domain access. In large environments, password management can become  
complex, leading to poor security practices, and such environments greatly increase the risk of a Pass-the-Hash (PtH) credential replay attack.

LAPS simplifies password management while helping customers implement recommended defenses against cyberattacks. In particular, the solution mitigates the risk of lateral escalation that results when customers use the same administrative local account and password combination on their computers.

First, follow the link in the references to download the program and the Operations guide. Then, follow the steps in the guide to install.

### To Resolve:

1. Download the .msi

   - Install only the management tools on the DC

   - Run the same msi on clients, but install only the CSE

   - What it does = installs two extended attributes to AD:  
     - `ms-Mcs-AdmPwd` – Stores the password in clear text  
     - `ms-Mcs-AdmPwdExpirationTime` – Stores the time to reset the password

3. On the DC:  

   ```powershell
   Import-module AdmPwd.PS  
   Update-AdmPwdADSchema
   ```

   - To see rights: `Find-AdmPwdExtendedrights -identity :<OU name> | Format-Table`

   - To remove rights:  
     - Open ADSIEdit  
     - Right Click on the OU that contains the computer accounts that you are installing this solution on and select Properties.  
     - Click the Security tab  
     - Click Advanced  
     - Select the Group(s) or User(s) that you don't want to be able to read the password and then click Edit.  
     - Uncheck All extended rights

4. Adding machine rights: `Set-AdmPwdComputerSelfPermission -OrgUnit <name of the OU to delegate permissions>` 

   - Example: `Set-AdmPwdComputerSelfPermission -OrgUnit Workstations`

5. Adding user rights: `Set-AdmPwdReadPasswordPermission -OrgUnit <name of the OU to delegate permissions> -AllowedPrincipals <users or groups>`  

   - Example: `Set-AdmPwdReadPasswordPermission -OrgUnit Workstations -AllowedPrincipals contoso\Administrator,contoso\HelpDesk,contoso\PwdAdmins`

6. Most important step = Deploy the GPO that sets the policy. The settings are located under `Computer Configuration\Administrative Templates\LAPS`.

   - Not showing up? Mine didn't either thanks to my [Central Store](https://automationadmin.com/2017/05/creating-a-central-store-for-gpos/)  
     - Open `C:\Windows\PolicyDefinitions\admpwd.admx` to `C:\Windows\SYSVOL\domain\Policies\PolicyDefinitions\admx`  
     - And `C:\Windows\PolicyDefinitions\en-us\admpwd.adml` to `C:\Windows\SYSVOL\domain\Policies\PolicyDefinitions\en-us\`

7. Done. Wait for GPO's to push to clients or run `gpupdate /force` to start testing!

8. Post Config: Clients must have the CSE installed and the GPO applied in order for LAPS to work!

9. Viewing the password using Powershell: `Get-AdmPwdPassword -ComputerName <computername>`

10. Viewing the password using GUI: ADUC => Right Click => Attribute Editor tab => ms-Mcs-AdmPwd

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2017/08/laps.jpg){:class="img-responsive"} 

11. If you have a Helpdesk Team with the required rights from step 5, you can have them install the management tools which includes the LAPS UI application:

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2017/08/laps-2.jpg){:class="img-responsive"}