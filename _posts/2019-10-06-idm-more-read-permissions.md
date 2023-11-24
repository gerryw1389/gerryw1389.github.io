---
title: IDM More Read Permissions
date: 2019-10-06T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/10/idm-more-read-permissions
tags:
  - LocalSoftware
---
<!--more-->

### Description:

[Netiq Identity Manager](https://www.microfocus.com/en-us/products/netiq-identity-manager/overview)is a LDAP based directory software. In this example, I had a service account that need to perform LDAP lookups but wasn't returning all the properties for a user. I did the following steps to give the account more rights so that it would return all properties instead of a subset of properties:


### To Resolve:

1. Sign into web GUI of iManager => Roles and Tasks => Rights => Rights to Other Objects

2. Trustee Name: $PathToServiceAccount

3. Context to search from: `[root]`

4. Click okay => Next screen should be blank. 

5. Now click 'Add Object' => (select your tree root) => click 'assigned rights'

6. Click the Property Name and make sure the following are checked:
   - `[All Attributes Rights] - Compare, Read`
   - `[Entry Rights] - Browse`

7. Test by signing into Apache Directory Studio before and after and doing a quick search on your LDAP tree. You should see more properties afterwards!