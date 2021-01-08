---
title: DNS Records Overview
date: 2016-05-23T12:31:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/dns-records-overview/
categories:
  - SysAdmin
---
<!--more-->

### Description:

DNS records are a very important part of networking. I put this under the email server section though because you will most likely not have to mess with DNS records once they are setup unless you host your own email, then you might have to change MX records and SPF records.

A great comb-through resource for understanding DNS records can be found here.

### To Resolve:

1. In a nutshell:

   - `A and AAAA`: Specifies an IP for a specific host (forward lookup).  
   - `CNAME`: Specifies a domain name that has to be queried in order to resolve the original DNS query.  
   - `MX`: Specifies a mail exchange server for a DNS domain name.  
   - `NS`: Specifies an authoritive name server for a given host.  
   - `PTR`: Specifies a domain name based off an IP address (reverse lookup).  
   - `SOA`: Specifies core information about a DNS zone, including the primary name server, the email of the domain admin, the domain serial number, and several timers  - related to refreshing the zone.  
   - `TXT`: These can hold an arbitrary non-formatted string. These are where SPF records are used to prevent fake emails to appear to be sent by you.

2. We once had a spammer that was sending from our CEO's email address (spoofed email issue). In order to tighten security, we changed our SPF record from `~all` on the end of the CNAME record to a `-all`.
   - Our DNS provider warned us that if we had multiple email servers, we would need to specify them in the record change.

3. The best way to understand SPF records is to break them down. For example:

   - `v=spf1 a mx ip4:12.218.xxx.xxx ip4:66.128.xxx.xxx/27 ~all`
   - `V=spf1` = Means it's defining a SPF record  
   - `A` = Look at all my A records and allow those  
   - `MX` = Look at all my MX records and allow those.  
   - `Ip4: 12.218.xxx.xxx` = Trust emails from this ip  
   - v`Ip4: 66.128.xxx.xxx/27` = Trust all hosts between 66.128.xxx.xx0 – 191  
   - `~all` = Soft fail. Trust us, but use your own filtering rules if necessary

4. Statement => Result => Meaning  
   - `+all` => pass => Allow all mail  
   - `-all` => fail => Only allow mail that matches one of the parameters (IPv4, MX, etc) in the record  
   - `~all` => softfail => Allow mail whether or not it matches the parameters in the record  
   - `?all` => neutral => No policy statement

5. In practice I have only seen `~` all and `-` all used. Please take a look at the following links for more info:  
   ["Authenticating SPF"](https://wordtothewise.com/2014/06/authenticating-spf)  
   ["Syntax"](http://www.openspf.org/SPF_Record_Syntax)
