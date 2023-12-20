---
title: 'PS: Module Commands'
date: 2016-06-02T20:52:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/ps-module-commands/
tags:
  - Windows
tags:
  - Powershell
  - Powershell-Modules
  - OneLiners-Powershell
---
<!--more-->

### Description:

This section is for server roles, modules, or external modules. Almost all command prompt commands work just as well in Powershell. Search the &#8220;batch&#8221; label to see examples of them.

#### To See What Roles Are Installed:

   ```powershell
   Import-Module Servermanager ; Get-Windowsfeature | Where-Object {$_.Installed -Eq $True} | Format-List Displayname
   ```

#### To just return True or False if a specific role or feature is installed, you can use this (which uses the Hyper-V role as an example):

   ```powershell
   Import-module servermanager ; (Get-WindowsFeature -name hyper-v).Installed
   ```

#### To install .NET 3.5

   ```powershell
   Install-WindowsFeature Net-Framework-Core -source \\networkshare\sxs
   ```

   - or D:\sources\sxs as the source. Run get-windowsfeature afterwards to make sure it installed.

#### To Get A List of All Computer Names On Your Network (AD Module):

   ```powershell
   Get-Adcomputer -Filter * | Select -Property Name, @{Name='Computername'; Expression={$_.Name}}
   ```

   - The `@{}` Just Creates A Custom Column Name.

#### To Get Last Password Change For A User (AD Module):

   ```powershell
   Get-ADUser 'UserName' -properties PasswordLastSet | format-list

   # Actually that won't quite do it. Try (Replace $Account with the AD Account)
   Get-ADUser -filter {Name -like $Account } –Properties "DisplayName", "msDS-UserPasswordExpiryTimeComputed" |
   Select-Object -Property "Displayname",@{Name="ExpiryDate";Expression={[datetime]::FromFileTime($_."msDS-UserPasswordExpiryTimeComputed")}}
   ```

#### To Get the SID for an Account or get a name from SID

   ```powershell
   wmic useraccount where sid="S-1-5-21-1180699209-877415012-3182924384-1004" get name
   wmic useraccount get name,sid
   ```

#### To get the OS version and Service Pack level for all your Windows systems in a certain OU? (AD Module):

   ```powershell
   Get-ADComputer -SearchScope Subtree -SearchBase "OU=PCs,DC=DOMAIN,DC=LAB" –Filter {OperatingSystem -Like "Windows*"} -Property * | Format-Table Name, OperatingSystem, OperatingSystemServicePack
   ```

#### To see which servers hold which FSMO roles (AD Module):

   ```powershell
   Get-ADDomain | Select-Object InfrastructureMaster, RIDMaster, PDCEmulator
   ```

#### To Find Which Users In the Domain Have Their Account Passwords Set To Never Expire? (AD Module):

   ```powershell
   Search-ADAccount -PasswordNeverExpires | Select-Object Name, Enabled
   ```

#### To Get A List Of All Active AD-Accounts With Password Expirations (AD Module):

   ```powershell
   Get-ADUser -filter {Enabled -eq $True -and PasswordNeverExpires -eq $False} –Properties * |
   Select-Object -Property "Displayname", @{n="ExpiryDate";e={$_.PasswordLastSet.AddDays((Get-ADDefaultDomainPasswordPolicy).MaxPasswordAge.Days)}}
   ```

#### To reset a domain account lockout (AD Module):

   ```powershell
   Reset-ComputerMachinePassword -server (domain controller) -credential (domain account with the ability to reset a computer password)
   ```

#### To See How Long A VM Has Been Running (Hyper-V Module):

   ```powershell
   (Get-VM | ?{$_.State -eq "Running"} | Select -ExpandProperty Uptime | Measure-Object -Average -Property TotalHours).Average
   ```

#### To convert a vhd to vhdx (Hyper-V Module):

   ```powershell
   Convert-VHD myserver.vhd myserver.vhdx
   ```

#### To convert vmdk to vhdx (Install MS Virtual Machine Converter):

   ```powershell
   Import-Module 'C:Program FilesMicrosoft Virtual Machine ConverterMvmcCmdlet.psd1'
   ConvertTo-MvmcVirtualHardDisk -SourceLiteralPath C:\myserver.vmdk -VhdType DynamicHardDisk -VhdFormat vhdx -Destination c:\myserver
   ```

