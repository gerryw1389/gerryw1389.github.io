---
title: AD Best Practices
date: 2017-11-08T17:27:54+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/11/ad-best-practices/
tags:
  - SysAdmin
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

For AD DS' DNS domain name, use a subdomain of the main web domain (internal.example.com) or use a dedicated web domain (example.net) owned by the organisation.

Always assume that users will roam.

Ensure that the PDC is syncing time from an external source, not its hardware / host.

Operate according to the Principle of Least Privilege.

If certain users require administrative permissions, issue them with a seperate, dedicated administrator  
accounts.

Use very long passwords on service accounts.

Set ACLs using security groups.

Use SSO whenever possible. If native / direct isn't possible, maybe via something like JumpCloud.

Use the central store for policies.

Use Microsoft LAPS.

Don't be afraid to use advanced features of Group Policy (loopback, preferences, item-level targeting, etc).

Don't modify the default domain policy => create a new GPO and move it higer in the linking priority.

Use Group Policy to enforce Windows' defaults settings for UAC, firewall, etc.

Set DC servers' DNS servers to others and itself last.

Rename the &#8220;administrator&#8221; account.

Don't let users use generic / shared user accounts (&#8220;reception&#8221;, &#8220;goodsin&#8221;, &#8220;meetingroom&#8221;, etc).

Have at least 2 domain controllers and schedule their Windows updates so they don't both reboot at the same  
time.