---
title: 'GPO: Disable Clipboard In RDP'
date: 2016-05-29T04:16:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/gpo-disable-clipboard-in-rdp/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

Follow these steps to disable copy/paste in RDP Connections. We implemented this for our VPN clients.

To Resolve:

1. On the Domain Controller, open up Group Policy Management. Create a new GPO under your workstation and link a new policy. Name is something like &#8220;DisableClipboardInRdp&#8221; or something.

2. Navigate to: `Computer Configuration\Policies\Administrative Templates\Windows Components\Remote Desktop Services\Remote Desktop Session Host\Device` and Resource Redirection

3. Set the &#8220;Do not allow clipboard redirection&#8221; and &#8220;Do not allow drive redirection&#8221; to &#8220;Enabled&#8221;.

4. Update your workstations to receive the new policy by `gpupdate /force` from an admin cmd. Then run `rsop.msc`, or preferably `gpresult /h c:\scripts\report.html` to see if it has been applied.


   <img class="alignnone size-full wp-image-660" src="https://automationadmin.com/assets/images/uploads/2016/09/gpo-disable-clipboard-redirection.png" alt="gpo-disable-clipboard-redirection" width="1201" height="368" srcset="https://automationadmin.com/assets/images/uploads/2016/09/gpo-disable-clipboard-redirection.png 1201w, https://automationadmin.com/assets/images/uploads/2016/09/gpo-disable-clipboard-redirection-300x92.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/gpo-disable-clipboard-redirection-768x235.png 768w, https://automationadmin.com/assets/images/uploads/2016/09/gpo-disable-clipboard-redirection-1024x314.png 1024w" sizes="(max-width: 1201px) 100vw, 1201px" />

