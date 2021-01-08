---
title: Creating A Central Store For GPOs
date: 2017-05-23T14:50:34+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/05/creating-a-central-store-for-gpos/
categories:
  - WindowsServer
tags:
  - GroupPolicy
---
<!--more-->

### Description:

Follow these steps to enable a central location for your organization's GPO's.

### To Resolve:

1. Create a folder called &#8220;PolicyDefinitions&#8221; at `C:\Windows\sysvol\domain\Policies\`

2. Copy everything from `C:\Windows\PolicyDefinitions` to that location.

3. Install ADMX templates to that location => copy all .admx to that locations root, copy your language *.adml to that location under the correct folder (for example en-us)

4. Now if you look at a GPO's settings you should see Policy definitions (ADMX files) retrieved from the central store.

5. Someone on /r/sysadmin was saying something about an error they were having so I'm just copying/pasting the fix here:

   - `Error: resource '$(string.Win7Only)';…`
   - Fix: I had the same problem. 
   - I don't see a new SearchOCR.admx file in the new 1803 templates and the version in my PolicyDefinitions was from 2010.  
   - Found this post from someone who solved it.   
   - Basically I downloaded the 1511 templates, extracted and just copied the SearchOCR.admx to the sysvol PolicyDefinitions root.  
   - However this alone didn't fix it for me. 
   - Then I looked at the 1803 version SearchOCR.adml located in en-US folder, compared it with the 1511 version and noticed it was missing a line underneath of  
   - `<string id='OCR'>OCR</string>`  
   - I added this underneath it and saved it:  
   - `<string id='Win7Only'>Microsoft Windows 7 or later</string>`  
