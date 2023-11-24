---
title: Protocols Per Layer
date: 2016-05-22T06:22:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/protocols-per-layer/
tags:
  - Networking
  - SysAdmin
---
<!--more-->

### Description:

Protocols are methods that computers use to talk to each other. Throughout your IT career you will learn different ones and how they relate to the OSI model.

   - You can view common ports on the home page or [here](http://packetlife.net/media/library/23/common_ports.pdf)  
   - I recommend you download all the cheat sheets from the site [here](http://packetlife.net/library/cheat-sheets/)

### Popular Protocols:

|Port Number| Protocol Name | Description |
|:---|:---|:---|:---|
| 21 | FTP  | File Transfer Protocol  
| 22 | SSH/ SCP  | Used for secure connections  
| 25 | SMTP  | Used to send emails |   
| 53 | DNS | Used to translate IP to domain names |
| 80 | HTTP  | Protocol used to browse the web. More info [here](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)  |  
| 110 | POP3 | Email Protocol | 
| 143| IMAP4 | Email Protocol |
| 161-162 | SNMP | Network device communication protocol |  
| 443 | HTTPS | Secure HTTP |
| 989-990 | FTP over SSL | Secure FTP |  
| 993 | IMAP4 over SSL | Secure IMAP |  
| 995 | POP3 over SSL | Secure POP |

### Layer 1 Protocols: The Physical Layer

   - ADSL => Asymmetric digital subscriber line  
   - ISDN => Integrated Services Digital Network  
   - PDH => Plesiochronous Digital Hierarchy  
   - T-carrier => (T1, T3, etc.)  
   - E-carrier => (E1, E3, etc.)  
   - RS-232 => a serial line interface originally developed to connect modems and computer terminals  
   - SDH => Synchronous Digital Hierarchy  
   - SONET Synchronous Optical NETworking  
   - Modem standards/ITU V-Series Protocols used to communicate between analog modems over voice telephone lines.  
   - Various Ethernet physical layers

### Layer 2 Protocols: Data Link Layer

   - ARCnet  
   - CDP Cisco Discovery Protocol  
   - DCAP Data Link Switching Client Access Protocol  
   - Dynamic Trunking Protocol  
   - Econet  
   - Ethernet  
   - FDDI Fiber Distributed Data Interface  
   - Frame Relay  
   - HDLC High Level Data Link Control  
   - IEEE 802.11  
   - IEEE 802.16  
   - LocalTalk  
   - L2F Layer 2 Forwarding Protocol  
   - L2TP Layer 2 Tunneling Protocol  
   - LAPD Link Access Procedures on the D channel  
   - LLDP Link Layer Discovery Protocol  
   - LLDP-MED Link Layer Discovery Protocol => Media Endpoint Discovery  
   - PPP Point-to-Point Protocol  
   - PPTP Point-to-Point Tunneling Protocol  
   - Q.710 Simplified Message Transfer Part  
   - NDP Neighbor Discovery Protocol  
   - SLIP Serial Line Internet Protocol (obsolete)  
   - StarLan  
   - STP Spanning Tree Protocol  
   - Token ring  
   - VTP VLAN Trunking Protocol

### Layer 2+3 Protocols:

   - ATM Asynchronous Transfer Mode  
   - Frame relay, a simplified version of X.25  
   - MPLS Multi-protocol label switching  
   - X.25  
   - ARP Address Resolution Protocol  
   - RARP Reverse Address Resolution Protocol

### Layer 1+2+3 Protocols:

   - MTP Message Transfer Part  
   - NSP Network Service Part

### Layer 3 Protocols: Network Layer

   - CLNP Connectionless Networking Protocol  
   - EGP Exterior Gateway Protocol  
   - EIGRP Enhanced Interior Gateway Routing Protocol  
   - ICMP Internet Control Message Protocol  
   - IGMP Internet Group Management Protocol  
   - IGRP Interior Gateway Routing Protocol  
   - IPv4 Internet Protocol version 4  
   - IPv6 Internet Protocol version 6  
   - IPSec Internet Protocol Security  
   - IPX Internetwork Packet Exchange  
   - MPLS Multiprotocol Label Switching  
   - SCCP Signalling Connection Control Part

### Layer 3 Protocols: Network Layer management

   - IS-IS Intermediate system to intermediate system  
   - OSPF Open Shortest Path First  
   - BGP Border Gateway Protocol  
   - RIP Routing Information Protocol

### Layer 3.5 protocols

   - HIP Host Identity Protocol

### Layer 3+4 protocols

   - Xerox Network Services

### Layer 4 Protocols: Transport Layer

   - AHAH Authentication Header over IP or IPSec  
   - ESPESP Encapsulated Security Payload over IP or IPSec  
   - GRE Generic Routing Encapsulation for tunneling  
   - IL Originally developed as transport layer for 9P  
   - SCTP Stream Control Transmission Protocol  
   - Sinec H1 for telecontrol  
   - SPX Sequenced Packet Exchange  
   - TCP Transmission Control Protocol  
   - UDP User Datagram Protocol

### Layer 5 Protocols: Session Layer

   - 9P Distributed file system protocol developed originally as part of Plan 9  
   - NCP NetWare Core Protocol  
   - NFS Network File System  
   - SMB Server Message

### Layer 7 Protocols: Application Layer

   - AFP, Apple Filing Protocol  
   - BACnet, Building Automation and Control Network protocol  
   - BitTorrent, A peer-to-peer file sharing protocol  
   - BOOTP, Bootstrap Protocol  
   - Diameter, an authentication, authorization and accounting protocol  
   - DICT, Dictionary protocol  
   - DNS, Domain Name System  
   - DHCP, Dynamic Host Configuration Protocol  
   - ED2K, A peer-to-peer file sharing protocol  
   - FTP, File Transfer Protocol  
   - Finger, which gives user profile information  
   - Gnutella, a peer-to-peer file-swapping protocol  
   - Gopher, a hierarchical hyperlinkable protocol  
   - HTTP, HyperText Transfer Protocol  
   - IMAP, Internet Message Access Protocol  
   - IRC, Internet Relay Chat protocol  
   - ISUP, ISDN User Part  
   - Jabber, an instant-messaging protocol  
   - LDAP Lightweight Directory Access Protocol  
   - MIME, Multipurpose Internet Mail Extensions  
   - MSNP, Microsoft Notification Protocol (used by Windows Live Messenger)  
   - MAP, Mobile Application Part  
   - NetBIOS, File Sharing and Name Resolution protocol => the basis of file sharing with Windows.  
   - NNTP, News Network Transfer Protocol  
   - NTP, Network Time Protocol  
   - NTCIP, National Transportation Communications for Intelligent Transportation System Protocol  
   - POP3 Post Office Protocol Version 3  
   - RADIUS, an authentication, authorization and accounting protocol  
   - Rlogin, a UNIX remote login protocol  
   - rsync, a file transfer protocol for backups, copying and mirroring  
   - RTP, Real-time Transport Protocol  
   - RTSP, Real-time Transport Streaming Protocol  
   - SSH, Secure Shell  
   - SISNAPI, Siebel Internet Session Network API  
   - SIP, Session Initiation Protocol, a signaling protocol  
   - SMTP, Simple Mail Transfer Protocol  
   - SNMP, Simple Network Management Protocol  
   - SOAP, Simple Object Access Protocol  
   - TUP, Telephone User Part  
   - Telnet, a remote terminal access protocol  
   - TCAP, Transaction Capabilities Application Part  
   - TFTP, Trivial File Transfer Protocol, a simple file transfer protocol  
   - WebDAV, Web Dist Authoring and Versioning

### References:

["List of Protocols - on different layers of OSI model"](http://euphoricpranav.blogspot.com/2008/11/list-of-protocols-on-different-7-layer.html)