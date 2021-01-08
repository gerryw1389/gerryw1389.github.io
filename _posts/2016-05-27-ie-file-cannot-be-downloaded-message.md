---
title: IE File Cannot Be Downloaded Message
date: 2016-05-27T22:13:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ie-file-cannot-be-downloaded-message/
categories:
  - Windows
---
<!--more-->

### Description:

If you get a &#8220;File could not be downloaded&#8221; when downloading an applet in IE, there are a couple steps you can do to fix.

### To Resolve:

1. &#8220;Reset&#8221; the Internet settings via Internet Properties. Run => inetcpl.cpl => &#8220;Advanced&#8221; Tab => &#8220;Reset&#8221; => Make sure to leave the &#8220;Delete Personal Settings&#8221; unchecked. This should be one of the first steps for most IE issues. Firefox and Chrome have similar functions.

2. If this doesn't work, create a new Windows profile and try to download the file from there. There is some cases where a corrupt profile may be the reason for this error.

3. In IE go to Internet Options => Security tab- Trusted Sites => Add whichever site you are on. This is common on Windows 8 machines and cannot be fixed by resetting IE.

4. In IE go to Security tab => Internet => Custom Level => Download => File Download and see if it is set to &#8220;disabled&#8221;. I've seen this a couple times.

  <img class="alignnone size-full wp-image-653" src="https://automationadmin.com/assets/images/uploads/2016/09/file-cannot-be-downloaded.png" alt="file-cannot-be-downloaded" width="847" height="459" srcset="https://automationadmin.com/assets/images/uploads/2016/09/file-cannot-be-downloaded.png 847w, https://automationadmin.com/assets/images/uploads/2016/09/file-cannot-be-downloaded-300x163.png 300w, https://automationadmin.com/assets/images/uploads/2016/09/file-cannot-be-downloaded-768x416.png 768w" sizes="(max-width: 847px) 100vw, 847px" />

5. Most often, this is a sign of an infection. See &#8220;General Troubleshooting&#8221; in the virus section to remove the virus.