---
title: Exchange Appointments Not Showing On iPhone
date: 2016-06-25T01:10:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/06/exchange-appointments-not-showing-on-iphone/
categories:
  - Hardware
---
<!--more-->

### Description:

My current organization uses hosted Exchange like many others so I don't have to deal so much with the back end of Exchange as much as dealing with users (yay me). Anyways, we had an issue the other day where a user created an appointment in Outlook but it didn't show up on their iPhone/ iPad.

Here are the general rules with Exchange/ Apple products:

1. Run the same version of Outlook on all of your computers, at work and at home.  Mailbox owners and any delegates should be using the same version of Outlook with the latest service pack and updates on all computers that are used for calendaring. If you are in a mixed environment of Windows, Mac or mobile devices, each platform should use the same version and each device should have the latest service pack and updates.

2. Only one person should process meeting requests. Other people, computers or devices that recieve the meeting request should ignore them, i.e. leave them be, do not delete them do not process them.  Have no more than two delegates.

3. Manage your calendar exclusively from Outlook or OWA. Don't accept, decline, modify or invite others to appointments from your mobile device.  You can, however, create new appointments on your mobile device, (e.g., add one while checking out at a doctor's office).

4. Make sure your mobile device has the latest OS/iOS version.  Often new devices do not, so be sure to check for updates, and do so BEFORE adding your Exchange account to the device.

5. To change an entire series of meetings, cancel the original meeting and create a new one.  To change one instance, cancel just that meeting and create a new one to replace it.  Always put an end date on a recurring meeting.

6. A "corrupt" meeting will remain that way until you delete it.  If it is a recurring appointment, delete all occurences and reschedule it.

7. When scheduling a recurring meeting, Microsoft recommends setting the end date no more than 6 months.  If you need to schedule a meeting for a longer period, start a new recurring meeting.

### To Resolve:

1. In this case I had the user delete the appointment and recreate it. It still did not show on the phone until I went to Calendar => Day view => Clicked on Calendars (at the bottom) => Unchecked all of them => then re-checked Exchange. After it showed the appointment that was missing, I then went back and did "all calendars".

2. Another thing I have seen fix the issue is to re-enter the user's email password under Settings => Mail. This re-authenticates that user.

3. Last thing I would check is to make sure the user has enough "Active Sync" licenses in Exchange. Since ours is hosted, I login to the admin console, go to the user, and look at the number of devices. If they have close to 10, I start deleting devices from a couple years ago (as I assume they don't own them anymore). This would present itself much sooner if it was an issue though as ActiveSync is what enables cell phones to sync with Exchange.

### References:

["Best Practices for Office 365 Calendar Users"](https://its.uiowa.edu/support/article/3521)