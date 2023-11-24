---
title: General Knowledge Quiz
date: 2018-05-27T03:39:46+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/general-knowledge-quiz/
tags:
  - SysAdmin
---
<!--more-->

  
This is part of a three part series:  
General Knowledge Quiz  
[Network Knowledge Quiz](https://automationadmin.com/2018/05/network-knowledge-quiz/)  
[AD Knowledge Quiz](https://automationadmin.com/2018/05/ad-knowledge-quiz/)

### General

**Differentiate between NTFS & FAT.**  
NTFS is the current file system used by Windows. It offers features like security permissions (to limit other users' access to folders), quotas (so one user can't fill up the disk), shadowing (backing up) and many other features that help Windows.  
FAT32 is the older Microsoft filesystem, primarily used by the Windows 9X line and Window could be installed on a FAT32 parition up to XP. In comparision, FAT32 offers none of what was mentioned above, and also has a maximum FILE (not folder) size of 4GB, which is kind of small these days, especially in regards to HD video.

**What is Proxy Server?**  
A proxy server is a computer that acts as a gateway between a local network (e.g., all the computers at one company or in one building) and a larger-scale network such as the Internet. Proxy servers provide increased performance and security. In some cases, they monitor employees' use of outside resources.

**Differentiate between FIREWALL/ANTIVIRUS.**  
Antivirus: The prime job of an anivirus is protect your system from computer viruses. Your computer may be standalone or part of network or connected to Internet you need an antivirus program. It actively monitors when you are using your system for any virus threat from different sources. if it found one it tries to clean or quarantine the virus ultimately keeping your system and data safe.  
Firewall: Firewall is in other hand a program which protects your system from outsider/intruder/hacker attacks. These attacks may not be virus type. In some cases hackers can take control of your system remotely and steal your data or important information from system. If your system is directly connected to internet or a large network than you can install a software firewall in your PC to protect your self from unauthorized access. Firewall is available either in software or in hardware form. For a single PC you may need a software firewall while a large corporate implements hardware firewall to protect all of their systems from such attacks.

**Differentiate between Frond end & Back End Server.**  
Backend server: A back end server is a computer resource that has not been exposed to the internet. In this regard the computing resource does not directly interact with the internet user. It can also be described as a server whose main function is to store and retrieve email messages.  
Frontend server: A frontend server is a computer resources that has exposed to the internet.

**What is APIPA.**  
Stands for Automatic Private IP Addressing; APIPA is a DHCP fail over mechanism for local networks. With APIPA, DHCP clients can obtain IP addresses when DHCP servers are non-functional. APIPA exists in all modern versions of Windows except Windows NT. When a DHCP server fails, APIPA allocates IP addresses in the private range 169.254.0.1 to 169.254.255.254.

**How Release and renew IP address from Command prompt.**  
Ipconfig / release  
ipconfig / renew

**What is wins server.**  
Windows Internet Name Service (WINS) servers dynamically map IP addresses to computer names (NetBIOS names). This allows users to access resources by computer name instead of by IP address. If you want this computer to keep track of the names and IP addresses of other computers in your network, configure this computer as a WINS server. If you do not use WINS in such a network, you cannot connect to a remote network resource by using its NetBIOS name.

**What is the Windows Registry.**  
The Windows Registry, usually referred to as "the registry," is a collection of databases of configuration settings in Microsoft Windows operating systems.

**What is the System Volume Information (SVI) Folder.**  
Windows XP includes a folder named System Volume Information on the root of each drive that remains hidden from view even when you choose to show system files. It remains hidden because it is not a normally hidden folder you can say it is a Super Hidden Folder. Windows does not shows Super Hidden Folders even when you select "Show Hidden Files."

**What is MBR.**  
Short form Master Boot Record, a small program that is executed when a computer boots up. Typically, the MBR resides on the first sector of the hard disk. The program begins the boot process by looking up the partition table to determine which partition to use for booting

**What is Bit Locker.**  
BitLocker is an encryption feature available in Ultimate and Enterprise versions of Windows 7 and Vista, to encrypt an entire drive, simply right-click on the drive and select Turn on BitLocker from the context menu.

**Main Difference Between Windows server 2008 and 2012**  
1) New Server Manager: Create, Manage Server Groups  
2) Hyper-V Replication : The Hyper-V Replica feature allows you to replicate a virtual machine from one location to another with Hyper-V and a network connection—and without any shared storage required. This is a big deal in the Microsoft world for disaster recovery, high availability and more. VMware does this, too, but the vendor charges new licensees extra for the capability.  
3) Expanded PowerShell Capabilities  
4)IIS 8.0 and IIS 7 in 2008  
5)Hyper-V 3.0  
6)PowerShell 3.0

**What happens when we type URL in browser.**  
First the computer looks up the destination host. If it exists in local DNS cache, it uses that information. Otherwise, DNS querying is performed until the IP address is found.  
Then, your browser opens a TCP connection to the destination host and sends the request according to HTTP 1.1 (or might use HTTP 1.0, but normal browsers don't do it any more).  
The server looks up the required resource (if it exists) and responds using HTTP protocol, sends the data to the client (=your browser)  
The browser then uses HTML parser to re-create document structure which is later presented to you on screen. If it finds references to external resources, such as pictures, css files, javascript files, these are is delivered the same way as the HTML document itself.

### Troubleshooting:

 **A user is unable to log into his desktop which is connected to a domain. What are the troubleshooting steps you will consider?**  
Check the network connection on the desktop. Try to ping to the domain controller. Run and check if name resolution is working. Check Active Directory for the computer account of the desktop. Compare the time settings on the desktop and Domain controller. Remove the desktop from domain and rejoin to domain.

**A Domain Controller called ABC is failing replication with XYZ. How do you troubleshoot the issue?**  
Active Directory replication issue can occur due to variety of reasons. For example, DNS issue, network problems, security issues etc. Troubleshooting can start by verifying DNS records. Then remove and recreate Domain Controller replication link. Check the time settings on both replication partners.

### Virtualization:

**Define virtualization.**  
Hyper-V virtualization will provide an environment in which we can run multiple operating systems at the same time on one physical computer, by running each operating system in its own virtual machine.

**What is a Hypervisor.**  
You can think of a Hypervisor as the kernel or the core of a virtualization platform. The Hypervisor is also called the Virtual Machine Monitor. The Hypervisor has access to the physical host hardware.

**What are a host, guest, and virtual machine.**  
A host system (host operating system) would be the primary & first installed operating system. If you are using a bare metal Virtualization platform like Hyper-V or ESX, there really isn't a host operating system besides the Hypervisor. If you are using a Type-2 Hypervisor like VMware Server or Virtual Server, the host operating system is whatever operating system those applications are installed into.  
A guest system (guest operating system) is a virtual guest or virtual machine (VM) that is installed under the host operating system. The guests are the VMs that you run in your virtualization platform.  
Some admins also call the host & guest the parent and child.

**Hyper v Snap shot:**  
How to create Hyper v Snap shot:  
Just select the Virtual machine in Hyper-V Manager and select Snapshot from the Actions pane. The status of the virtual machine will change to "Taking Snapshot" and show the progress of the action using a percentage value.  
File extension = .avhd  
Virtual Machine files  
The first thing to know is what files are used to create a virtual machine:  
.XML files  
These files contain the virtual machine configuration details. There is one of these for each virtual machine and each snapshot of a virtual machine. They are always named with the GUID used to internally identify the virtual machine or snapshot in question.  
.BIN files  
This file contains the memory of a virtual machine or snapshot that is in a saved state.  
.VSV files  
This file contains the saved state from the devices associated with the virtual machine.  
.VHD files  
These are the virtual hard disk files for the virtual machine  
.AVHD files  
These are the differencing disk files used for virtual machine snapshots