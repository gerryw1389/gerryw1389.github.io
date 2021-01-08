---
title: Network Knowledge Quiz
date: 2018-05-27T04:09:03+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/network-knowledge-quiz/
categories:
  - SysAdmin
---
<!--more-->

  
This is part of a three part series:  
[General Knowledge Quiz](https://automationadmin.com/2018/05/general-knowledge-quiz/)  
Network Knowledge Quiz  
[AD Knowledge Quiz](https://automationadmin.com/2018/05/ad-knowledge-quiz/)

**What is an IP Address?**  
It is 32 Bits binary number (or any brief answer you can come up with)

**What is the difference between a subnet and a VLAN?**

If they are used interchangeably then they are used incorrectly. Subnet refers to particular IP network, such as 192.0.2.0/28  
VLAN refers to 802.1Q standard, in which you can essentially give each port unique MAC address table, effectively separating them from each other.  
VLAN may transport one or more subnet (but does not have to, it may be transporting something else than IP entirely). Subnet may be configured for VLAN, but does not have to be, it could be without 802.1Q or over some completely different L2 technology than ethernet.

**What is Subnet Mask and what does subnet mask do?**  
A 32 bit number that divides IP address into two distinct parts, Network and Host portion.

**Provide full subnet mask for /27**  
255.255.255.224  
/27 means 27 bits turned on,  
8 bits = 255  
24 bits = 255.255.255  
3 bits 128 + 64 + 32 = 224  
Therefore, full SB mask for /27 is 255.255.255.224  
If you did not get this STOP. You need to go back and learn basic subnetting.  
You cannot screw up with such easy question on the interview, so take your time to study.

**Now it is rare in the AD Interview but incase, you could be asked /27 how many network and how many hosts in each network?**  
Going back to basic, /27 255.255.255.0  
3 bits for network  
5 bits for Hots  
2X2X2 = 8 Networks  
2x2x2x2x2 = 30 Hosts in each Networks (32 -2 = 30) we need one IP for each Network and another one for Broadcast.

**What is the difference in between TCP /UDP Protocols?**  
TCP is connection oriented, whereas UDP is connectionless

**How many Bytes TCP Header?**  
Size of TCP Header (without any options) => 20 Bytes

**How many Bytes UDP Header?**  
Size of UDP header => 8 bytes

**Size of Total empty TCP datagram**  
Total size of empty TCP datagram => 24 + 20 + 20 = 64 bytes  
Size of Ethernet frame => 24 Bytes  
Size of IPv4 Header (without any options) => 20 bytes  
Size of TCP Header (without any options) => 20 Bytes

Size of Total empty UDP datagram  
Total size of empty UDP datagram => 24 + 20 + 8 = 52 bytes  
Size of UDP header => 8 bytes  
Size of Ethernet frame => 24 Bytes  
Size of IPv4 Header (without any options) => 20 bytes

**What Is VOIP?**  
VOIP – Short for Voice Over Internet Protocol, a category of hardware and software that enables people to use the Internet as the transmission medium for telephone calls by sending voice data in packets using IP rather than by traditional circuit transmissions.

**What is loop back?**  
Loopback address is 127.0.0.1; An address that sends outgoing signals back to the same computer for testing.

### DNS

**Define DNS**  
Domain Name System, DNS is an Internet service that translates domain names into IP addresses. Because domain names are alphabetic, they're easier to remember.

**What are the two types of lookup in DNS?**  
Forward lookup : it converts Domain name to ip address.  
Reverse lookup: it converts ip address to Domain name.

**How many zone types are there?**  
Three types of zone. Primary zone, Secondary zone and stub zone.

**What is the port number of DNS?**  
UDP and port number – 53

**What is NSlookup.**  
Nslookup.exe is a command-line administrative tool for testing and troubleshooting DNS servers. This tool is installed along with the TCP/IP protocol through Control Panel. MS-DOS utility that enables a user to look up an IP address of a domain or host on a network.

**In Which directory partition DNS information is kept?**  
Domain Partition

**What is an A record, when I open A record what do I see inside?**  
Host name mapping to IPV4 record

**What is an AAA record, when I open A record what do I see inside?**  
Host name mapping to IPV6 record

**What is Glue record, when I open A record what do I see inside?**  
Simply Host name mapping to IP address (same as A record)

**What is PTR record, when I open A record what do I see inside?**  
Pointer record, IP address map to Host name

**What is CNAME record, when I open A record what do I see inside?**  
Chomical Name record, Multiple names mapping to same IP address

**What is Alias record, when I open A record what do I see inside?**  
Another name for CNAME record, Multiple names mapping to same IP address

**What is a SRV record?**  
Service record, which provides information about service and port information

**How many reverse lookup zone, is available with default DNS installation?**  
None, DNS does not rely on reverse DNS zone to work properly. It is optional to crate reverse DNS zone, and many administrators will recommend creating one for various reasons (security etc.)

**How many forward lookup zone, is available with default DNS Installation?**  
Single forward lookup zone gets created with default installation of DNS services on a Domain Controller.

### DHCP

**How DHCP work?**  
DHCP Stands for Dynamic host configuration protocol. DHCP is a protocol used for automatic configuration IP address in client computers connected to IP networks. DHCP operates on a client server model in four phases.

> Discover: A client broadcasts DHCP Discover message when it comes alive on the network.  
> Offer: When a DHCP server receives the DHCP Discover message from the client, it reserves an I P address for the client and sends a DHCP Offer message to the client offering the reserved IP address.  
> Request: The client receives the DHCP offer message and broadcasts a DHCP request message to show its consent to accept the offered IP address.  
> Acknowledge: When the DHCP server receives the DHCP Request message from the client, it sends a DHCP Ack packet to the client. At this point the IP configuration process is complete.

**What is DHCP Scope.**  
A range of IP address that the DHCP server can assign to clients that are on one subnet.

**What protocol and port does DHCP use.**  
UDP protocol and 67 port in client and 68 port in server.

**What is a DHCP lease.**  
A DHCP lease is the amount of time that the DHCP server grants to the DHCP client permission to use a particular IP address. A typical server allows its administrator to set the lease time.

**Can DHCP support statically defined addresses.**  
Yes.

**Define Dora Process & why it is used.**  
Discover, Offer, request and acknowledgement. it is used to assign ip address automatically to client systems.

**What is Authorizing DHCP Servers in Active Directory.**  
If a DHCP server is to operate within an Active Directory domain (and is not running on a domain controller) it must first be authorized to Active directory.

**How to Backup and Restore DHCP in Windows Server 2008**  
In Windows Server 2008, backup of DHCP database and settings has gotten simpler. You may want to backup your DHCP server from time to time to prepare for disaster recovery scenarios or when migrating DHCP server role to a new hardware.  
Backup DHCP Server  
1. Open Server Manager > DHCP role  
2. Right click server name, choose Backup..  
3. Choose a location for backup, click OK  
Restore DHCP Server  
1. Open Server Manager > DHCP role  
2. Right Click server name, choose Restore  
3. Choose the location of the backup, click OK  
4. Restart the DHCP Service

**DHCP Databse location?**  
C:\WINDOWS\System32\DHCP directory.