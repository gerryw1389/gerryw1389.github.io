---
title: Hosted Exchange Migration
date: 2016-11-15T03:06:43+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/hosted-exchange-migration/
categories:
  - SysAdmin
  - WindowsServer
tags:
  - Migration
  - MSOffice
---
<!--more-->

### Description:

So our department recently had the project of moving from one hosted Exchange company to another. This is a brief overview of the steps needed to prepare for in the migration. For this example, I will use &#8220;Exchange1&#8221; as the current provider and &#8220;Exchange2&#8221; as the company we are switching over to.

### To Resolve:

1. First, make note of all the things that normally will not transfer over: Rules, signatures, shared folders, Delegate Access settings, and appointments with no end dates. There may be others but these are the main ones for my environment.

2. Next, get a list of all the mailboxes, contacts, rooms, ect in Exchange1 and give them to an engineer at Exchange2 to set up. You will most likely need to include the size of the mailboxes and such so that they know the size before hand. Some of our accounts were 1-2 GB while others were around 20GB and they need to know what to setup initially for the first &#8220;push&#8221; from Exchange1 => Exchange2.

3. Once the accounts are setup in both systems and before you do the migration, setup a forward on your mail server that goes to both systems at the same time. So our setup was Mail Server => Forward emails to: Exchange1 and Exchange2 at the same time. MX record was hosted in house because we provide POP/IMAP mail for our customers while the corporate staff is on Exchange (a dual setup if you will).

4. On migration day, you need to have researched 3 DNS records that you will need to change before you can create the new Exchange mail profiles on end user's machines:

   - SRV record => This will be provided by Exchange2's tech's. Syntax: `_service._proto.name`. TTL class SRV priority weight port target. [Source](https://en.wikipedia.org/wiki/SRV_record)

   - Autodiscover record => This is just a CNAME of of Exchange2's servers that provide the autodiscover service. 
     - Add the dot on the end for the one on the domain controller. If you have hosted DNS, it may / may not be necessary => I would email their support just to make sure.

   - SPF Record => Make sure to check out the `include` section as all we had to do is add Exchange2's domain before the `-all` 
     - If you have issues after adding this, try adding a `?` after the include command, this will make it neutral. We didn't have to do this.

5. Once you cut over the DNS records, specifically the autodiscover, you have to wait for DNS to propagate in order for clients to hit the right server for auto-config => they just use email address and mailbox password to add their account in Outlook and on cell phones.

6. While you could theoretically just add a second exchange account to people's profiles, it is best practice to create a new profile and deal with the changes that come over afterwards. For us, it pulled over the signatures and rules, you just had to set them.

7. For clarity, here are some of the things we had to do after the migration:

   - File => Options => Mail => Signatures => You see they moved over, but you have redo the drop downs that make them active for new emails/ replies
   - Clear the autocomplete cache by either running &#8220;Outlook.exe /CleanAutoCompleteCache&#8221; or just going to File => Options => Mail => Empty AutoComplete list.
   - Setup Auto-archive settings again. If they had an archive folder, just re-add it under File => Account Settings => Data files tab => Add => path\to\archive.pst.
   - Add Delegate Access either via OWA or in Outlook under File => Account Settings => Delegate Access => Add => (person) => Click the appropriate radio button for your environment.

8. Done. This is all that I can think of if you still host accounts in house, will add to this once we have to change MX records.