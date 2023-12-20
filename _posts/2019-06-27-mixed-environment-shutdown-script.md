---
title: Mixed Environment Shutdown Script
date: 2019-06-27T00:49:32-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/mixed-environment-shutdown-script/
tags:
  - Windows
  - Linux
tags:
  - Powershell
  - Bash
---
<!--more-->

### Description:

So for my VMWare lab, I have quite a few servers:
4 Windows VMs
1 RHEL 7 VM
2 Centos VMs
1 PFSense VM
1 W10 VM with WSL installed that I used as my 'admin' machine so I could PS remote to the Windows Servers and WSL ssh into the Linux/PFSense VMs.

My goal was to create a simple way to shutdown my lab at the end of the day since it was on a laptop that I take home. 

I already had a startup script for Windows boots:

   ```escape
   @ echo off
   "C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" -T ws start "C:\scripts\vms\pfsense\pfsense.vmx" nogui
   "C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" -T ws start "C:\scripts\vms\2016dc\2016dc.vmx" nogui
   "C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" -T ws start "C:\scripts\vms\puppet\puppet.vmx" nogui
   "C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" -T ws start "C:\scripts\vms\2012dc\2012dc.vmx" nogui
   "C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe" -T ws start "C:\scripts\vms\2016client\2016client.vmx" nogui
   ```

I'm sure there is a simple VMWare way, but I wanted to initiate the shutdown of the lab from a single machine. Since I'm fairly good with Powershell, it was easy to write a function for the Windows VM's, but I needed to find a way to shutdown my linux/BSD machines.

### To Resolve

1. The way to do this is to setup PublicKeyAuthentication and then create a shell script that would shutdown my VMs

   - To do this, you first create your own key and send it to the servers:

   ```shell
   ssh-keygen -t rsa
   # cat /home/gerry/.ssh/id_rsa.pub - Copy this somewhere just in case, it is your public key. The same directory has your private key.
   ssh-copy-id gerry@puppet.williamsg.test

   # ssh in and then run
   sudo su
   vi /etc/ssh/sshd_config
   # Set 'PubkeyAuthentication' to 'yes' and 'PasswordAuthentication' to 'no'
   cat /home/gerry/.ssh/authorized_keys
   # make sure it matches
   systemctl restart sshd

   # Now it should work!
   ```

   - This worked easy enough. But I ran into an issue:

   ```shell
   ssh gerry@puppet.williamsg.test "sudo /usr/sbin/shutdown now"
   sudo: no tty present and no askpass program specified
   ```

   - fix:

   ```shell
   echo "pass" | ssh -t gerry@puppet.williamsg.test "sudo -S /usr/sbin/shutdown now"
   ```

2. Since that took care of my Linux VM's, I just had PFSense left. Here is what I did to set it up:

   - Login to web gui
   - System - Advanced - Enable SSH - Also check box to disable passwords
   - On admin box: cat ~/.ssh/id_rsa.pub - Copy to clipboard
   - Back in Web GUI, go to User Manager - YourUser - Paste in to authorized_keys file
   - Back on admin, create script: `ssh yourUser@10.12.12.254 'poweroff -p now'`

3. So now I have a function in my Powershell profile that will shutdown windows VMs and a bash script in my WSL tab that I run to shutdown the rest.

   - Here is Windows function:

   ```powershell
   # Encryption
   # $Key = (3,4,2,3,56,34,254,222,1,1,2,23,42,54,33,233,1,34,2,7,6,5,35,43)
   # Read-Host -Assecurestring | Convertfrom-Securestring -Key $Key | Out-File 'C:\Users\gerry.WILLIAMSG\Documents\WindowsPowershell\pw.xml'
    
   # Decryption
   $Key = (3, 4, 2, 3, 56, 34, 254, 222, 1, 1, 2, 23, 42, 54, 33, 233, 1, 34, 2, 7, 6, 5, 35, 43)
   $Password = Get-Content 'C:\Users\gerry.WILLIAMSG\Documents\WindowsPowershell\pw.xml' | Convertto-Securestring -Key $Key
   $Username = "williamsg.test\gerry"
   $Cred = New-Object -Typename System.Management.Automation.Pscredential -Argumentlist $Username, $Password

   Function Set-LabSessions
   {
       $2016dc = New-PSSession -ComputerName "2016dc" -Credential $cred
       $2012dc = New-PSSession -ComputerName "2012dc" -Credential $cred
       $2012client = New-PSSession -ComputerName "2012client" -Credential $cred
       $2016client = New-PSSession -ComputerName "2016client" -Credential $cred
   }

   $servers = @("2016dc", "2012dc", "2016client", "2012client")
   #Enter-pssession $2016dc

   Function Stop-Lab
   {
       invoke-command -ComputerName $servers -scriptblock { stop-computer -force }
   }
   ```

