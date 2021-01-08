---
title: Setting Up Barracuda Archiver
date: 2016-05-21T05:03:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/setting-up-barracuda-archiver/
categories:
  - Hardware
tags:
  - Setup
---
<!--more-->

### Description:

An email archiver is a hardware device that stores older copies of emails for reference that is placed on the network usually with a spam filter hardware device. We purchased one of these the other day and I was tasked to set it up.

### To Resolve:

1. We use MailEnable as our email server software, so I followed the guide [here](http://www.mailenable.com/kb/content/article.asp?ID=ME020395) to setup a mailbox for all mail to be copied to.

2. I setup the archiver on our DMZ subnet by following [this](https://campus.barracuda.com/product/messagearchiver/article/BMA/GetStarted2/) guide.

   - Added the device to our internal DNS server.
   - Added to our external DNS server since it was placed in the DMZ.
   - Made sure a DHCP reservation was created so that we wouldn't use the same IP on the internal subnet.

2. Created an unlimited space mailbox called `archiver@domain.com`.

3. Copied MESNOOP to `C:\Program Files (x86)\MailEnable\bin`. Double click to launch, say &#8220;yes&#8221; to message filtering and point to a mailbox I created in the previous step.

4. Open MailEnable and go to Messaging Manager => Filters.

5. Create a new one called &#8220;ArchiveAllMail&#8221; and double click it to edit it. Under &#8220;use standard criteria&#8221; select the option that says &#8220;All messages => Process this filter action for all messages&#8221; and then under the actions panel, click &#8220;Add Actions&#8221; and &#8220;forward to Address&#8221; and type in `archiver@domain.com`.

6. Lastly, login to BarracudaArchiver, go to Mail Sources => Journal Accounts. Make sure the polling frequency is 30 seconds.

   - Add the mailbox info:  
   - Server = Server IP address or hostname  
   - Protocol = POP3  
   - Username = email address  
   - Password = email password  
   - Encryption = SSL  
   - Port = 993
   - Then click Add

7. Update firmware on the device.

8. Lastly, if you purchased the license for Cloud Backup, you have to register for an account at [https://techlib.barracuda.com/BCC/CreateAccount](https://campus.barracuda.com/product/cloudcontrol/article/BCC/CreateAccount/).

9. Once a Cloud Control Account is created which is tied to an order number and serial number of a product, then you can connect the account under Advanced => Backup and Advanced => Cloud Control tabs just by signing in.