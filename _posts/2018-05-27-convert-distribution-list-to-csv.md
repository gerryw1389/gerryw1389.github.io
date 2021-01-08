---
title: Convert Distribution List To CSV
date: 2018-05-27T03:32:22+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/convert-distribution-list-to-csv/
categories:
  - LocalSoftware
tags:
  - MSOffice
---
<!--more-->

### Description:

If you don't have access to Powershell or on-premise Exchange/O365, it can be really tedious to convert a distribution list to a CSV. Here is how to do it client side.

### To Resolve:

1. Open Outlook and start a new email.

2. In the &#8220;To&#8221; field, type in the distribution group you want to expand.

3. Click the plus + sign to expand the members.

4. Select all members of the distribution list and copy them.

5. You can close the email as you do not need it anymore.

6. Navigate to Home => New items => More items => Contact group.

7. In the Contact group, go to Add members => From Address book.

8. Paste the names and email addresses into the Members field.

9. Go to File => Save as and save your contact group as a TXT file.

10. Open the txt file you just created and remove the first lines from it and replace all tabs with commas in the txt.

11. Save the TXT file as CSV file. You need to select All files and add manually .csv at the end of its title.