---
title: 'MS Outlook: User Unable To See Full Details'
date: 2016-06-10T14:09:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/ms-outlook-user-unable-to-see-full-details/
categories:
  - LocalSoftware
tags:
  - MSOffice
---
<!--more-->

### Description:

So we use hosted Exchange for email and we commonly have users that share out their calendars for others to access. I ran into an issue the other day where the manager shared his calendar, added the employee with &#8220;editor&#8221; permissions, and sent the share request. When she got it, all she could see was &#8220;Availability Only&#8221;. We spent forever working on the issue and I actually had to put in a support case in order to get it fixed.

### To Resolve:

1. Long story short, when sending a share request, in the &#8220;To:&#8221; field, choose the user from the GAL (Global Address List) in Exchange. In this instance, his Outlook was resolving the name to a contact that he had in his local address book.

This particular user was first hired as a temp and put on our internal IMAP accounts that we host for other employees. Even though the email addresses are the same (due to an alias trick), Outlook I guess was pointing to the now non-existent IMAP account instead of the user's Exchange account. We move employees over from IMAP to Exchange when they go from temp to full time so the actual mailbox is migrated.

TLDR: Go through every step, one at a time to double check yourself when troubleshooting. In this case, I was simply typing the user's name and trusting that it resolved to the Exchange account when it was in fact resolving to a contact in the local address book.