---
title: Email Being Blocked
date: 2017-07-23T04:30:40+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/email-being-blocked/
tags:
  - Networking
---
<!--more-->

### Description:

If you face problems sending out mail, but only to a handful of domains, please run through the following checks / tests and make sure your environment is setup properly:

### To Resolve:

1. Reverse DNS:

   - Check your domain on &#8220;DNS Goodies&#8221; and see if you have a Reverse DNS pointer setup with a proper FQDN, not an ISP generic one. If you do not have one setup => call your Internet Service Provider (ISP) and ask them to set one up to match the Fully Qualified Domain Name (FQDN) that your mail server responds as e.g., mail.yourcompany.com. Also, your mailserver FQDN should also be setup with something like mail.yourcompany.com. Any FQDN ending in .local or .internal or anything that is not a valid Internet Domain Name is not correct and should be changed otherwise you may experience problems sending out emails to some domains.

   - To get your ISP to setup Reverse DNS on your Fixed IP Address, there must be a corresponding A record configured in your DNS records (at your Domain Registrar) that resolves the name you want added, to the IP Address. If such a record doesn't exist, then the ISP won't set it up for you!

   - A simple test from a DOS Prompt (Command Prompt) will help here:

   ```escape
   nslookup mail.yourdomain.com
   # This should return your Public IP Address e.g., 123.123.123.123
   # Then if you run the following command:
   nslookup 123.123.123.123
   # It will return your Reverse DNS record. If it says mail.yourdomain.com (or at least if it matches what you type in the first time) then you are good to go.
   ```

   NOTE: It is not uncommon for a company to host their mail out of another site, the best way to resolve this is to have that site use a SUBDOMAIN of the main domain.
   {: .notice--success}

2. Blacklists:

   - Check that your IP address is not listed on any Blacklists on [mxtoolbox](http://www.mxtoolbox.com/blacklists.aspx) and [blacklistalert.org](http://www.blacklistalert.org/) => If you appear on any blacklists, then you may have problems sending mail to some domains who check against blacklists (not everyone does, but a lot do). Follow the links on the results page to the particular blacklist site to find out the reason why you are listed (you may have an infected computer sending out spam that you are not aware of) and then deal with the issue before requesting removal from those blacklists (if you don't deal with the problem, such as an infected computer, you will get removed from the blacklist, but will only re-appear again as more spam is sent out). Once you know what you are facing, you can resolve the problem.

   - If you are blacklisted => configure your firewall / router to block all traffic on TCP Port 25 Outbound from all IP addresses apart from your Mail Server. This should reduce the possibility of an infection from getting you blacklisted further and will help prevent getting listed again once you have cleaned up your network.

3. IP Reputation:

   - Check your IP reputation on Talos [talosintelligence.com](https://talosintelligence.com/) or MXToolbox. You will either be Good, Neutral or Poor. If your reputation is Poor => then you may have problems sending out mail and are most likely appearing on a blacklist or two somewhere. If you are Neutral, then you may have had a problem in the recent past and are still recovering your reputation. If you have a Good reputation, you should have no problems sending out emails.

4. SPF Record (Sender Policy Framework):

   - Check to see if you have an SPF (Sender Policy Framework) record setup on [mxtoolbox.com/spf](http://www.mxtoolbox.com/spf.aspx) => If you do not have a record setup, visit (site invalid), run through the various options carefully and then you should see your SPF record in the final box at the bottom of the screen. Once you have an SPF record, you have to publish this record in your Domains DNS records by adding a TXT record with the SPF record as the data e.g., Type=TXT Record=(output from (site invalid)).

   - It is far better not to have an SPF record, than it is to have an incorrect one. Not having an SPF record won't get your emails rejected, but a badly configured on will.

   - SPF records essentially tell the world which IP Address(es) / Mail Server(s) are permitted to send out mail on behalf of your domain. If you send out mail from an IP Address that isn't permitted / included in your SPF record, don't be surprised if your emails get rejected and don't blame the recipient server for rejecting you.

5. General: If you send out mail from a different IP address to the advertised MX record IP Address, please check that the Reverse DNS entry for this IP Address is also configured properly and that it resolves correctly to the same IP address on [dnsgoodies.com](http://www.dnsgoodies.com/). As an example, if you send mail out via IP 123.123.123.123 and the Reverse DNS entry setup on this IP address by your ISP is mail.yourcompany.com then mail.yourcompany.com should also resolve in DNS back to the same 123.123.123.123 IP Address.

### References:

["Problems sending mail to one or more external domains"](https://www.experts-exchange.com/articles/2427/Problems-sending-mail-to-one-or-more-external-domains.html)