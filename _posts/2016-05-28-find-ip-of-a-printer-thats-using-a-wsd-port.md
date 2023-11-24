---
title: 'Find IP Of A Printer Thats Using A WSD Port'
date: 2016-05-28T06:35:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/find-ip-of-a-printer-thats-using-a-wsd-port/
tags:
  - Hardware
  - Windows
tags:
  - Printing
---
<!--more-->

### Description:

The WSD Port Monitor is a new printer port monitor in Windows Vista and Windows Server 2008. This port monitor supports printing to network devices that are designed to include Web Services for Devices (WSD) technology. Web Services for Devices allows network-connected IP-based devices to advertise their functionality and offer these services to clients by using the Web Services protocol. WSD-based devices and clients communicate over the network using a series of SOAP (Simple Object Access Protocol) messages over UDP and HTTP(S). WSD for Devices provides a network plug-and-play experience that is similar to installing a USB device. Web Services for Devices also defines a security profile that may be extended to provide additional protection and authentication using device-based certificates.

This is for WSD ports on printers: Most software that comes with network printers ( HP, Brother or Lemark ) add printers through a WDS Printer Port Interface. This is good when it works, because printers advertise themselves on networks so windows can find them as well as their device driver. Sometimes I find the WDS Service stops on local machines causing issues. Trying to diagnose whether the problem is communication related between the computer and the printer or an actual printer issue is hard through WDS. To troubleshoot issues with a printer that is using a WSD port, try re-adding the printer using an IP port.

### To Resolve:

1. Run => control printers => Right click the printer => Printer Properties => Web Services Tab => Bottom of the page should have the IP address.

2. If the Web Services tab is unavailable, see if you have the Services tab => Select that and go to the drop down and change it to "Device and Supplies Status" and then select "Go". Once this launches, it should have the printer's IP address with it.

3. As mentioned, remove the printer that is using the WSD port and re-add the printer using its IP Address instead.