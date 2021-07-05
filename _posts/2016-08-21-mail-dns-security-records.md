---
title: Mail DNS Security Records
date: 2016-08-21T17:02:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/mail-dns-security-records/
categories:
  - SysAdmin
  - Security
---
<!--more-->

### Description:

This post is meant to consolidate the different email securities that are common practice for organizations that host their own mail. Essentially, in order to not be marked as spam to other email servers, you need to setup and configure multiple records for your email server on your DNS server.

### To Resolve:

1. The most common initial email security check to setup is **SPF records**. These records are used to prevent fake emails to appear to be sent by you. I describe the setup for this record in my [DNS Records post](https://automationadmin.com/2016/05/dns-records-overview/) but for convenience:

   - SPF Record Setup Example: `v=spf1 a mx ip4:12.218.xxx.xxx ip4:66.128.xxx.xxx/27 ~all`
   - `V=spf1` = Means it's defining a SPF record  
   - `A` = Look at all my A records and allow those  
   - `MX` = Look at all my MX records and allow those.  
   - `Ip4: 12.218.xxx.xxx` = Trust emails from this ip  
   - `Ip4: 66.128.xxx.xxx/27` = Trust all hosts between 66.128.xxx.xx0 – 191  
   - `~all` = soft fail. Trust us, but use your own filtering rules if necessary
   - Statement => Result => Meaning  
   - `+all` => pass => Allow all mail  
   - `-all` => fail => Only allow mail that matches one of the parameters (IPv4, MX, etc) in the record  
   - `~all` => softfail => Allow mail whether or not it matches the parameters in the record  
   - `?all` => neutral => No policy statement
   - SPF Record Implementation: On your DNS provider interface (or local server if you don't have an external DNS provider), create a TXT file similar to:  
`v=spf1 a mx ip4:12.218.xxx.xxx ip4:66.128.xxx.xxx/27 ~all`

1. **Sender ID** => Similar to SPF, but is not the same. This is used to verify senders => but is not used often and is considered obsolete.

2. **DKIM** => DomainKeys Identified Mail ([DKIM](https://wiki.zimbra.com/wiki/Best_Practices_on_Email_Protection:_SPF,_DKIM_and_DMARC)), is a method to associate the domain name and the email, allowing to a person or company assume the responsibility of the email. Follow [this](https://support.rackspace.com/how-to/create-a-dkim-txt-record/) guide for an example setup.

   - DKIM Record Setup Example: `v=DKIM1;k=rsa;p=randChars`
   - `V=DKIM1` = Means it's defining a DKIM record  
   - `K=rsa` = Encryption type  
   - `P= (key)` = Your public key
   - DKIM Record Implementation: On your DNS provider interface (or local server if you don't have an external DNS provider), create a TXT file similar to:

   ```escape
   Name = randChars_domainkey  
   TTL = 14400  
   Type = TXT  
   Data = "v=DKIM1;k=rsa;p=randChars"
   ```

3. **FCrDNS** is used to [make sure that PTR/A records match for a domain](http://www.itworld.com/article/2833006/networking/how-to-setup-reverse-dns-and-ptr-records.html).

   - Why Forward Confirmed rDNS is Important => FCrDNS helps prevent others from spoofing your hosts. If I'm the bad guy and I control the reverse lookup for my IP addresses I can put anything in there. I could pretend to be your bank and try to trick you into giving up your account information. However what I can't spoof is if you do a lookup on the fake name I return and it either doesn't resolve or resolves to a different IP address then you know it's not genuine. If it does resolve to the same IP address then you know it's good. This is because only the domain owner can make FCrDNS work correctly. This is a very important tool in detecting email phishing scams.
   - Here's how it's suppsed to work. Suppose your IP is 1.2.3.4:
   - 1.2.3.4 => PTR Record => hostname.example.com  
   - hostname.example.com => A Record => 1.2.3.4
   - The name that is returned by the rDNS lookup needs to point back to the same IP address. [Source](http://ipadmin.junkemailfilter.com/rdns.php)

4. **Demarc records** => Specify how mail servers should handle messages from your domain that don't have proper SPF and DKIM setup. I used these two guides [here](http://www.inmotionhosting.com/support/email/fighting-spam/dmarc-setup) and [here](http://www.zytrax.com/books/dns/ch9/dmarc.html). The main thing to note is that you need to setup DKIM and SPF before setting up Demarc records.

   - Demarc Record Setup Example: `v=DMARC1; p=quarantine; sp=none; ruf=mailto:tech@domain.com; rf=afrf; pct=100; ri=86400`

   - Where  
   - Tag Name Purpose Sample  
   - `v` Protocol version v=DMARC1  
   - `pct` Percentage of messages subjected to filtering pct=20  
   - `ruf` Reporting URI for forensic reports ruf=mailto:authfail@example.com  
   - `rua` Reporting URI of aggregate reports rua=mailto:aggrep@example.com  
   - `p` Policy for organizational domain p=quarantine  
   - `sp` Policy for subdomains of the OD sp=reject  
   - `adkim` Alignment mode for DKIM adkim=s  
   - `aspf` Alignment mode for SPF aspf=r  
   - [Source](https://dmarc.org/overview/)
   - Following that same guide as SPF records,it is best to go from None => Quarantine => Reject to get tighter controls.  
   - The None record would be: `v=DMARC1; p=quarantine; sp=none; ruf=mailto:user@example.com; rf=afrf; pct=100; ri=86400`
   - Demarc Record Implementation: On your DNS provider interface (or local server if you don't have an external DNS provider), create a TXT file similar to:

   ```escape
   Name = _demarc  
   TTL = 14400  
   Type = TXT  
   Data = "v=DMARC1; p=quarantine; sp=none; ruf=mailto:tech@domain.com; rf=afrf; pct=100; ri=86400"
   ```
