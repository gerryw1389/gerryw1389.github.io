---
title: Drive Has Foreign State
date: 2016-05-21T04:50:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/drive-has-foreign-state/
tags:
  - Hardware
  - WindowsServer
tags:
  - Monitoring
---
<!--more-->

### Description:

Inside Dell OM, you have a drive seperated from the others that has a state of &#8220;foreign&#8221;.

   - ![drive-has-foreign-state](https://automationadmin.com/assets/images/uploads/2016/09/drive-has-foreign-state.png){:class="img-responsive"}

### To Resolve:

1. Navigate up to the controller properties (Perc 6/i Integrated => Information/Configuration Tab in this case). On &#8220;Controller Tasks&#8221; select &#8220;Foreign Configiration Operations&#8221; and then execute.

   - ![drive-has-foreign-state-2](https://automationadmin.com/assets/images/uploads/2016/09/drive-has-foreign-state-2.png){:class="img-responsive"}

2. Navigate back to the drive and select the option of &#8220;Assign Global Hot Spare&#8221; and select Execute. This will start the rebuild process automatically.

3. UPDATE: So apparently our server went down the next morning after doing this and would not boot into Windows! I want to say this is directly related but others have done this without what happened to me so YMMV. To fix, we chose the option to &#8220;Import previous RAID Config&#8221; by pressing &#8220;F&#8221; on boot up and then choosing the previous settings and rebooting.

4. I was always taught that if it is one drive you do &#8220;Clear config&#8221; and if the whole array is bad do &#8220;import previous&#8221;. Either way, after booting to the OS the next day, we replaced the drive that originally caused all of this and it rebuilt successfully.