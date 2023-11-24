---
title: Misc Networking Concepts
date: 2018-04-07T04:12:32+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/04/misc-networking-concepts/
tags:
  - Networking
  - Windows
---
<!--more-->

### Description:

Various little things I've picked up regarding networking in Windows => rarely used.

### To Resolve:

1. Native Packet capture - Netsh: On anything 2008R2 and newer => if you need to capture a trace, `netsh trace start capture=yes traceFile=(path/to/file.etl)` , reproduce issue, then `netsh trace stop`  and copy the ETL file off. It can even be converted in Message Analyzer to a Wireshark-compatible cap format if you want to use Wireshark for analysis. I would not ever recommend installing a TCPIP leaf driver (winpcap) in Windows when you can capture right down at the NDIS level (netsh) natively. Plus the ETL trace command can add providers and scenarios to show you more of what happened when a packet was generated or received as well, aiding troubleshooting.

2. Windows port forwarding:

   ```powershell
   netsh interface portproxy add v4tov4 listenport=fromport listenaddress=fromip connectport=toport connectaddress=toip
   ```

   - where
   - fromport: the port number to listen on, e.g. 80  
   - fromip: the ip address to listen on, e.g. 192.168.1.1  
   - toport: the port number to forward to  
   - toip: the ip address to forward to

3. You can list the active port mappings using:

   ```powershell
   netsh interface portproxy show v4tov4
   ```

3. Netbios Alias => NetBIOS aliases are alternative names for your CIFS server that SMB clients can use when connecting to the CIFS server. Configuring NetBIOS aliases for a CIFS server can be useful when you are consolidating data from other file servers to the CIFS server and want the CIFS server to respond to the original file servers' names.

   - On the server, open regedit and go to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters` 
   - Add multi string key `OptionalNames` and add the name. Reboot the server.

4. To create a hidden share:  

   - Add a `$` to the end of the share name. If you it is already shared, you will need to unshare it, back out, and then reshare it with the dollar sign on the end. NOTE: This does little to nothing for security and is not as common as it was in the Windows XP/ Server 2003 days.