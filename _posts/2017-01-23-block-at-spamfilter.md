---
title: Block At SpamFilter
date: 2017-01-23T17:42:19+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/01/block-at-spamfilter/
tags:
  - Security
---
<!--more-->

### Description:

For those of you with local spam filters or the ability to add custom extensions to block, here is a list of extensions you may consider blocking in your spam filter policy

### To Resolve:

1. Block these attachment types at the spam filter.

   ```escape
   *.ade  
   *.adp  
   *.arj  
   *.asx  
   *.bas  
   *.bat  
   *.cab  
   *.chm  
   *.cmd  
   *.com  
   *.cpl  
   *.crt  
   *.hlp  
   *.hta  
   *.inf  
   *.ins  
   *.jar  
   *.js  
   *.jse  
   *.jsp  
   *.lib  
   *.lnk  
   *.mdb  
   *.mde  
   *.msi  
   *.msp  
   *.nsc  
   *.pcd  
   *.pif  
   *.pptm  
   *.ps1  
   *.reg  
   *.rwa  
   *.scr  
   *.sct  
   *.shs  
   *.vb  
   *.vbe  
   *.vbs  
   *.wmd  
   *.wsc  
   *.wsf  
   *.wsh
   ```

2. Additionally you may consider scanning these closer, quarantining, or blocking:

   ```escape
   *.rar (block any that are encrypted/can not be scanned)  
   *.zip (block any that are encrypted/can not be scanned)  
   *.pdf (block any that are encrypted/can not be scanned)  
   *.xlsm (macro enabled xls)  
   *.docm (macro enabled docs)  
   *.doc (block any that are macro enabled if possible)
   ```