---
title: Workstation Cannot Login To Domain
date: 2016-05-29T03:47:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/workstation-cannot-login-to-domain/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

You will have a message that says, &#8220;&#8221;the trust relationships between the workstation and the primary domain failed&#8221; at Windows login. The underlying problem when you see this error is that the machine you are trying to access can no longer communicate securely with the Active Directory domain to which it is joined. The machine's private secret is not set to the same value store in the domain controller. You can think of this secret as a password but really it's some bits of cryptographic data called a Kerberos keytab stored in the local security authority. When you try to access this machine using a domain account, it fails to verify the Kerberos ticket you receive from Active Directory against the private secret that it stores locally. I think you can also come across this error if for some reason the system time on the machine is out of sync with the system time on the domain controller.

You will need to leave and re-join the domain in order to gain access or reset the computer password object in AD.

### To Resolve:

1. Unplug the ethernet cable from the back of the workstation.

2. Login as a local user instead of the domain profile your used to. Make sure you are selecting (This computer). Use the local `administrator` account if you can't remember yours, you will need administrator privileges.

   - To force a local login with a computer on a domain, use `.\username` as the username if you don't know the computer name. If you do know the computer name, obviously, do the standard `computername\username` to login as a local user instead of a domain user.

3. Once in Windows, plug the ethernet cable back in.

4. Use the keyboard shortcut `Win+PauseBreak` to bring up the System Properties box. Under the Computer Name tab, take note of the domain name and change the computer from a Domain to a Workgroup (choose any name you want for the workgroup). Use whatever credentials you want to change to a workgroup, it doesn't matter.

5. Restart the workstation and log back in the `Administrator` account or whichever account you were on with Administrator rights.

6. Go back to they System Properties (Run => `sysdm.cpl`) and change the computer from a Workgroup back to a Domain. Here, make sure you enter the local administrator account's username/ password to the server.

7. Restart the machine again. Now login to the domain. If it still doesn't work, you need to login to the DC (Domain Controller) and check your user's account settings under Start => Administrative Tools => Active Directory Users and Computers.

### From Powershell (Preferred):

1. If you get the primary trust error, login to the local computer administrator account. Do this once the computer can "see" the domain controller (internal or over VPN with a remote connection established).

2. Run => Powershell =>

3. Type:

   ```powershell
   Reset-ComputerMachinePassword -server (domain controller) -credential (domain account with the ability to reset a computer password)
   ```

4. Log out and log back in to the domain account.


### From CMD:

   ```powershell
   netdom.exe resetpwd /s:<server> /ud:<user> /pd:*
   ```

   - server = a domain controller in the joined domain
   - user = DOMAIN\User format with rights to change the computer password