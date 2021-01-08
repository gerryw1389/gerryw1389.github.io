---
title: IE Has Stopped Working
date: 2016-05-27T22:15:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ie-has-stopped-working/
categories:
  - Windows
---
<!--more-->

### Description:

If you get this error message &#8220;Internet explorer has stopped working&#8221;, that means, must be a 3rd party ".dll" file is conflicting with `iexplore.exe`, also Internet explorer getting lots of load of unwanted toolbars, BHO's, addon's, extensions, and some internet explorer security settings.

### To Resolve:

1. Follow the link to 9 methods to try:  
[http://www.techsupportall.com/how-to-fix-internet-explorer-has-stopped-working/](https://www.techsupportall.com/how-to-fix-internet-explorer-has-stopped-working/)

2. I just worked one of these the other day:
   - Reset IE: Run => `inetcpl.cpl` => Advanced tab => Reset => Reset. Did not fix.
   - Run [Ultra Adware Portable](http://www.majorgeeks.com/files/details/ultra_adware_killer.html) => Removed items and rebooted. Did not fix.
   - Run [Bleachbit](http://www.bleachbit.org/download) => Made sure to check all options regarding IE. Fixed
   - I think the issue had to do with some file in their `%localappdata%` or `%appdata%` directory. Bleachbit resolved the issue.