---
title: General Settings For MS Outlook
date: 2016-05-23T18:20:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/general-settings-for-ms-outlook/
categories:
  - LocalSoftware
tags:
  - MSOffice
---
<!--more-->

### Description:

If you are having issues with a Yahoo or Hotmail &#8220;Free&#8221; email account working with Outlook, this is a known issue and the only fix is to buy the full version (Pro version) for it to work. Gmail and ISP email servers usually do not have any issues with Outlook. Also, you should use the &#8220;Hotmail to Outlook Connector&#8221; with the full version of Outlook for Hotmail accounts, they will not work with Outlook Express. Here is common solutions to many issues.

### To Resolve:

1. Verify the user name and password for the email account.

2. ALWAYS Test the account settings using the built in Test. Use this to determine the point of failure.

3. Normal setup for POP3 ports:

Incoming: 110 (by default) try changing to 995 (IMAP is 993)

Outgoing: 25 (by default) try changing to 465

Add SSL Encryption on both

4. Find out, what's the email service? Gmail, hotmail, Exchange server? Try deleting and re-adding the account. If POP3 and it don't work, create a new account with IMAP settings and vice versa.

5. If you are using a web based client, log in to it there and see if you can send / receive emails from there. If so, continue troubleshooting other causes. If not, call the provider to further troubleshoot.

6. Here are some common sign in pages:

GoDaddy Emails (NOTE: These usually seem like they are on an Exchange server because of their personalized domain name): [https://login.secureserver.net/index.php?app=wbe](https://sso.secureserver.net/?realm=pass&app=email)

Google: mail.google.com

Hotmail: login.live.com

Yahoo: mail.yahoo.com

### Outlook Attachment Storage Path:

`%localappdata%\Microsoft\Windows\Temporary Internet Files\content.outlook`

I've only seen this once, but someone got an error saying that Outlook couldn't open an attachment. Found out that Outlook has a limit to the number of attachments it can open in preview, each time it does => it creates the file in this location. The fix was to simply delete everything out of this folder.