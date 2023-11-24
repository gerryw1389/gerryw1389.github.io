---
title: Apply CIS Benchmarks
date: 2019-12-05T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/12/apply-cis-benchmarks/
tags:
  - Linux
tags:
  - ConfigManagement
---
<!--more-->

### Description

The goal of this project was to use Puppet Enterprise to apply a "Base CIS" class to both windows and linux servers in our organization that will accomplish [level 1](https://www.cisecurity.org/cis-benchmarks/cis-benchmarks-faq/) controls on our servers. This was accomplished and is maintained at [My Github Repo](https://github.com/gerryw1389/base_cis)

Overview:

- Step 1: Download Microsoft GPO's for Baseline config
- Step 2: Create Testlab
- Step 3: Setup Puppet Enterprise and Capture Settings
- Substep: Apply GPO's from Baseline and use Puppet to capture settings
- Step 4: Download Assesor and check settings - Should show everything as failing.
- Step 5: Correct Settings and Create Classes in Puppet - Note that for Windows we wanted to apply settings using Local Security Policy instead of GPOs so that settings can be managed via Puppet. We will eventually move to [DSC](https://docs.microsoft.com/en-us/powershell/scripting/dsc/overview/overview?view=powershell-6) for this.
- Step 6: Functional Testing - Show everything as passing
- Step 7: Project Handoff

### To Resolve

1. For Windows Servers, download [GPO's](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-baselines)

2. [Create a Test Lab](https://automationadmin.com/2016/12/setting-up-a-lab-using-only-virtual-box/) with:

   - Windows Server 2012r2 Domain Controller and member server
   - Windows Server 2016v1604 Domain Controller and member server
   - Centos 7.6.1810
   - RHEL 7.6 Maipo
   - PFSense firewall VM

3. Setup Puppet Enterprise free VM (up to 10 nodes):

   - `wget --content-disposition https://pm.puppet.com/cgi-bin/download.cgi?dist=el&rel=7&arch=x86_64&ver=latest`
   - `curl -JLO '<DOWNLOAD_URL>'`
   - Master: <https://pm.puppet.com/cgi-bin/download.cgi?dist=el&rel=7&arch=x86_64&ver=latest>
   - Agents:
   - RHEL7: <https://pm.puppet.com/puppet-agent/2019.1.0/6.4.2/repos/el/7/puppet6/x86_64/puppet-agent-6.4.2-1.el7.x86_64.rpm>
   - Windows: <https://pm.puppet.com/puppet-agent/2019.1.0/6.4.2/repos/windows/puppet-agent-6.4.2-x64.msi>

   - Download the tarball appropriate to your operating system and architecture.
   - curl -JLO <https://pm.puppet.com/cgi-bin/download.cgi?dist=el&rel=7&arch=x86_64&ver=latest>
   - or
   - wget --content-disposition <https://pm.puppet.com/cgi-bin/download.cgi?dist=el&rel=7&arch=x86_64&ver=latest>
   - NOTE: This didn't appear to be making progress so I went to the actual server and ran the command in the GUI and watched the tar.gz download. - I think it may have just been because the installer is half a GB.

   - Import the Puppet public key.
   - wget -O - <https://downloads.puppetlabs.com/puppet-gpg-signing-key.pub> | gpg --import
   - Print the fingerprint of the key.
   - gpg --fingerprint 0x7F438280EF8D349F
   - gpg --verify puppet-enterprise-<version>-<platform>.tar.gz.asc
   - Download and install:
   - tar -xf <TARBALL_FILENAME>
   - cd puppet....
   - sudo ./puppet-enterprise-installer
   - Got error:

   ```escape
   Could not prefetch pe_node_group provider 'ruby': Received 5 server error responses from the Node Manager service at https://puppet.williamsg.test:4433/classifier-api: 500 {"kind":"application-error","msg":"Connection refused"}
   [Error]: Failed to apply catalog: Received 5 server error responses from the Node Manager service at https://puppet.williamsg.test:4433/classifier-api: 500 {"kind":"application-error","msg":"Connection refused"}
   ```

   - Fix:
   - Add more memory, reboot and run the command again
   - It then gave me a link to reset my password. I copied and pasted into a browser and it worked. Sign in = login to web gui using admin/pass

   ```shell
   puppet infra console_password --password=<MY_PASSWORD>
   puppet agent -t

   firewall-cmd --get-active-zone
   #public
   firewall-cmd --zone=public --add-port=443/tcp --permanent
   firewall-cmd --zone=public --add-port=8140/tcp --permanent
   firewall-cmd --reload
   ```

   - Now install the puppet agent on nodes:

   - Centos: `curl -k https://puppet.williamsg.test:8140/packages/current/install.bash | sudo bash`
   - Windows: Download <https://pm.puppet.com/puppet-agent/2019.1.0/6.4.2/repos/windows/puppet-agent-6.4.2-x64.msi> on admin.williamsg.test
   - Then use a script to push and install it:

   - $servers is a propulated variable with each server in our environment

   - so...

   ```powershell
   Foreach ($server in $servers)
   {
      Invoke-Command -Computername $server -ArgumentList $server -Scriptblock {
      param($server)
         If ((-not (Test-Path "c:\scripts")))
         {
         New-Item -ItemType Directory -Path "c:\scripts" | Out-Null
         Write-output "created c:scripts on $server"
         }
         Write-output "downloading script on $server"
         [System.Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
         [Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
         $webClient = New-Object System.Net.WebClient
         $webClient.DownloadFile('https://puppet.williamsg.test:8140/packages/current/install.ps1', 'c:\scripts\install.ps1')
         Write-output "installing script on $server"
         c:\scripts\install.ps1
         }
   }
   ```

   - Login to the web GUI - Go to unsigned certs - Accept all

   - On the puppet master, install modules:

   ```shell
   cd /etc/puppetlabs/code/environments/production/modules
   puppet module install kpn-local_security_policy --version 3.1.1
   # if that one doesn't work, try https://forge.puppet.com/ayohrling/local_security_policy
   ```

   - Lastly, apply the GPO's from Step 1 and run `puppet resource local_security_policy > c:\scripts\server.txt` on each server and copy the settings displayed to a text file. These files will be the foundation for puppet classes.
  
4. Now we setup an initial baseline scan by downloading the client tool which will be ran on each system to get us a "score" of the systems current security level - [CIS Workbench Assessor-CLI-v4.0.7](https://workbench.cisecurity.org/files/2151)

   - Install the server software by following [Dashboard Deployment Guide for Windows](https://cis-cat-pro-dashboard.readthedocs.io/en/stable/source/Dashboard%20Deployment%20Guide%20for%20Windows/)
   - We start on Windows because it will be harder to fix than linux where everything can be fixed by shell scripts.
   - Here are the initial results:

   - ![assesment-results](https://automationadmin.com/assets/images/uploads/2019/12/assesment-results.jpg){:class="img-responsive"}

   - To increase the scores, Go to CIS Benchmark website – Search the benchmark - Download the 'Remediation Kits' for them.
   - For Windows, these are new GPO's to be applied. So we do that.

   - ![assesment-results-2](https://automationadmin.com/assets/images/uploads/2019/12/assesment-results-2.jpg){:class="img-responsive"}

   - On each client: Run `gpupdate /force`, reboot, then run `gpresult /scope computer /h c:\scripts\computer.html; gpresult /scope user /h c:\scripts\user.html`
   - Open the files and ensure that policies were inherited correctly. Ignore errors.
   - Now go to `c:\scripts\Assesor-CLI` and run the report again
   - Much better!
   - ![assesment-results-3](https://automationadmin.com/assets/images/uploads/2019/12/assesment-results-3.jpg){:class="img-responsive"}
   - Now run: `puppet resource local_security_policy > c:\scripts\2016dc_updated.txt`

   - This fixed Windows pretty well, but what about Centos/RHEL? Well out of the box they are not doing so good:

   - LinuxServer
   - ![assesment-results-4](https://automationadmin.com/assets/images/uploads/2019/12/assesment-results-4.jpg){:class="img-responsive"}
   - RHEL
   - ![assesment-results-5](https://automationadmin.com/assets/images/uploads/2019/12/assesment-results-5.jpg){:class="img-responsive"}

   - Run remediation (shell scripts) and I get better results (around 87%).

5. Now that we have an idea of remediation, we need to find a way to convert these to puppet classes. This is obviously the hardest part of the project as you have to find a way to have puppet apply a default class to each kind of server that will remediate most of the issues.

   - This is too complicated to list here, but if you know how to read puppet classes, start with [init.pp](https://github.com/gerryw1389/base_cis/blob/main/manifests/init.pp) and work your way downwards.

   - For Windows, the main fixes are two fold:
   - On one hand, puppet just sets a ton of registry settings. These are my preferred way to manage settings:

   ```puppet
   # rule_2.3.1.4_L1_Ensure_Accounts_Limit_local_account_use_of_blank_passwords_to_console_logon_only_is_set_to_Enabled
   registry_value { 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\LimitBlankPasswordUse':
   ensure => present,
   type   => dword,
   data   => 1,
   }
   ```

   - On the other hand, Windows is managed by `LGPO.exe` (with CSV files for audit policies and inf files for local security policies) , `laps.msi`, and others. See [2012](https://github.com/gerryw1389/base_cis/blob/main/manifests/base_windows/twentytwelve_template.pp) and [2016](https://github.com/gerryw1389/base_cis/blob/main/manifests/base_windows/twentysixteen_template.pp)

   - For linux, I just used a series of shell scripts that will [test settings on the first run, and then execute scripts if something fails](https://github.com/gerryw1389/base_cis/blob/main/manifests/base_rhel/rhel_cis.pp)

6. [Final result](https://github.com/gerryw1389/base_cis/blob/main/files/benchmarks/proof/proof.md)
