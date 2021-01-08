---
title: 'GPO: Local Admin Password Reset'
date: 2016-05-29T04:14:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gpo-local-admin-password-reset/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

Follow these steps to update the a local administrator account via GPO. Note in GPO's: If you want to make a computer change, you need to apply the policy to computer OU's, if you want to make a user change, you need to make a policy for User OU's.

NOTE: This does NOT follow best practices. You should implement [LAPS](https://automationadmin.com/2017/08/laps-deployment/) instead.

### To Resolve:

1. Login to the Domain Controller and open up the Active Directory Users and Computers console to find the group of computers you want to make a change to.

2. Open up the Group Policy Management console and find the corresponding group. Then right click => &#8220;Create GPO in this domain and link it here&#8221;.

3. Name it something unique like &#8220;ResetLocalAdminPassword(departmentName)&#8221;.

4. Go to Computer ConfigurationPreferencesLocal Users and Groups and right click in the empty space and select &#8220;New Local User&#8221;. In there it brings up the Properties box. Make sure to select &#8220;Update&#8221; for the action and the select your administrator account as the user name. Set the new password and tick the appropriate boxes at the bottom. After that is done, the policy will be applied to the computers in the OU on the next refresh (usually 30 min to 4 hours depending on size of domain).

NOTE: This is version 1 of the GPO and will need to be replaced with a more secure version. The password for the admin account is not encrypted this way (but is scrambled) and can be de-scrambled using free tools off the Internet.