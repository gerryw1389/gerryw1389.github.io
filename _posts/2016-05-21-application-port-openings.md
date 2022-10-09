---
title: Application Port Openings
date: 2016-05-21T22:03:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/application-port-openings/
categories:
  - Networking
  - SysAdmin
---
<!--more-->

### Description:

Computers these days are meant to be networked. Applications and services run on many ports so it's not really feasible to block all ports and open only the ones you need due to dynamic addressing. That being said, there are some cases, such as when a computer is placed in your DMZ, that you want to do just that, block all ports except for the ones that need to be opened. I use this page as a reference for such devices. 

Note that when setting up firewall rules you simply use the syntax `Allow $port from this $IPRange only` so that you restrict who can connect. The only ports you open to the world (0.0.0.0/0) should normally just be 80 (HTTP) or 443 (HTTPS), everything else should be restricted to your internal IP's only. You should work with your organization to ensure that as few ports as possible are open to the world.


### To Resolve:

1. To view your dynamic ranges for a client computer, you can use the below commands:

   ```powershell
   netsh int ipv4 show dynamicport tcp  
   netsh int ipv4 show dynamicport udp  
   netsh int ipv6 show dynamicport tcp  
   netsh int ipv6 show dynamicport udp
   ```

2. See the following table for most ports:

   |Application|TCPPorts|UDPPorts|
   |:---|:---|:---|
   |AD|25|-|
   |AD|42|-|
   |AD|135|-|
   |AD|137|-|
   |AD|139|-|
   |AD|389|389|
   |AD|636|-|
   |AD|3268|-|
   |AD|3269|-|
   |AD|88|88|
   |AD|53|53|
   |AD|445|445|
   |AD|9389|-|
   |AD|5722|-|
   |AD|464|464|
   |AD|-|123|
   |AD|-|137|
   |AD|-|138|
   |AD|-|67|
   |AD|-|2535|
   |AD|1024-5000|1024-5000|
   |MSSQL|1433|-|
   |MSSQL|1434|-|
   |MSSQL|2383|-|
   |MSSQL|2382|-|
   |MSSQL|135|-|
   |MSSQL|80|-|
   |MSSQL|443|-|
   |MSSQL|4022|-|
   |MSSQL|-|1434|
   |MSSQL|1433|-|
   |SMB(Server Message Block)|445|-|
   |RPC(Remote Procedure Call)|135|-|
   |RPC(Remote Procedure Call)|5722|-|
   |File Transfer Protocol(FTP)(RFC959)|20|-|
   |File Transfer Protocol(FTP)(RFC959)|21|-|
   |Secure Shell(SSH)(RFC4250-4256)|22|-|
   |Telnet(RFC854)|23|-|
   |Simple Mail Transfer Protocol(SMTP)(RFC5321)|25|-|
   |Domain Name System(DNS)(RFC1034-1035)|53|53|
   |Dynamic Host Configuration Protocol(DHCP)(RFC2131)|-|67|
   |Dynamic Host Configuration Protocol(DHCP)(RFC2131)|-|68|
   |Trivial File Transfer Protocol(TFTP)(RFC1350)|-|69|
   |Hypertext Transfer Protocol(HTTP)(RFC2616)|80|-|
   |Post Office Protocol(POP)version3(RFC1939)|110|-|
   |Network Time Protocol(NTP)(RFC5905)|-|123|
   |NetBIOS(RFC1001-1002)|137|137|
   |NetBIOS(RFC1001-1002)|138|138|
   |NetBIOS(RFC1001-1002)|139|139|
   |Internet Message Access Protocol(IMAP)(RFC3501)|143|-|
   |Simple Network Management Protocol(SNMP)(RFC1901-1908,3411-3418)|161|161|
   |Simple Network Management Protocol(SNMP)(RFC1901-1908,3411-3418)|162|162|
   |Border Gateway Protocol(BGP)(RFC4271)|179|-|
   |Lightweight Directory Access Protocol(LDAP)(RFC4510)|389|389|
   |Hypertext Transfer Protocol over SSL/TLS(HTTPS)(RFC2818)|443|-|
   |Lightweight Directory Access Protocol over TLS/SSL(LDAPS)(RFC4513)|636|636|
   |FTP over TLS/SSL(RFC4217)|989|-|
   |FTP over TLS/SSL(RFC4217)|990|-|
   |MySQL|3306|-|
   |MySQL|33060|-|
   |MySQL|33061|-|
   |MySQL|33062|-|
   |MySQL|6446|-|
   |MySQL|6447|-|
   |MySQL|6448|-|
   |MySQL|6449|-|

   - NOTE: If the server has Netbios (NBT) enabled, it listens on UDP ports 137, 138, and on TCP ports 139, 445. If it has NBT disabled, it listens on TCP port 445 only.
   {: .notice--success}

   - **In addition to this list, feel free to check my [Protocols per Layer](https://automationadmin.com/2016/05/protocols-per-layer/) post.**

### References:

["What Ports Are Used For File Sharing"](http://superuser.com/questions/764623/what-port-or-ports-are-used-for-file-sharing-in-windows)  

["Active Directory Firewall Ports"](https://blogs.msmvps.com/acefekay/2011/11/01/active-directory-firewall-ports-let-s-try-to-make-this-simple/)  

["Microsoft Ports"](https://technet.microsoft.com/en-us/library/dd772723(v=ws.10).aspx)  

["Minimum Number of Ports.."](http://serverfault.com/questions/565775/minimum-number-of-port-need-to-open-between-windows-client-domain-controller-o)  

["MySQL Port Reference"](https://dev.mysql.com/doc/mysql-port-reference/en/mysql-ports-reference-tables.html)  