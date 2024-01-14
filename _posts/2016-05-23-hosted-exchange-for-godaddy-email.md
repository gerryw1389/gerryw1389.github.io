---
title: Hosted Exchange For GoDaddy Email
date: 2016-05-23T12:52:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/hosted-exchange-for-godaddy-email/
tags:
  - SysAdmin
---
<!--more-->

### Description:

I once had a client that wanted to convert from their business email account to a hosted Exchange account through GoDaddy. I did the following steps to complete the task:

### To Resolve:

1. Go to godaddy.com. In the top right, click on Sign In, then My Products.

2. There will be an existing &#8220;Workspace&#8221; section with a business email. Click on Manage => Select the account and delete it.

3. Go to the Office 365 section and select &#8220;Manage&#8221;. Here you will create your own account. I chose the account name of the office email. Since the account names were exactly the same, I was told to just leave the account in the Workspaces and they would automatically convert the email to an Office 365 account.

4. Once the conversion is complete, I went to email.(domainNameChosen).com and signed in => it brought up the online Office menu => great! The actual 365 account has been created, but it would take a little longer for the business email to migrate to the newly created 365 email.

5. Since the old IMAP account was deleted from GoDaddy's server, the local Outlook PST is the only survivor of all the emails/appointments/etc remaining. In Outlook, I went to File => Open => Import => Export to a file => Outlook Data File (.pst) => Create a file and export. NOTE: This may take a while but is well worth it. There is no way around it actually. NOTE: If you copy the &#8220;data file&#8221; while outlook is closed, you will get a read-only file that does not import even though the file properties will not specifically have the option checked for &#8220;read-only&#8221;. Learned this a long time ago.

6. You cannot add an exchange account while Outlook is open, you have to close it and Run => Control => Mail options. Here you create a new profile (I always choose &#8220;Default&#8221;) and then select the radio button that launches &#8220;Default&#8221; every time.

7. So now the Exchange account is created and you just need to import your IMAP emails, calandars, etc. Go back to File => Open => Import => Import from another file or program => Outlook Data File (.pst) => yourFilename. THIS MAY TAKE A WHILE. This is a good stage, at this point => you just have to wait for your email to sync between your client and the hosted exchange servers.

8. Once sync is complete, you should test by loading the email on multiple computers and then creating an appointment and verifying that it shows on all workstations at the same time.