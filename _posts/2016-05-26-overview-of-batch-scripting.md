---
title: Overview Of Batch Scripting
date: 2016-05-26T04:23:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/overview-of-batch-scripting/
tags:
  - Windows
tags:
  - Batch-Commands
---
<!--more-->

### Description:

A list of things to do regarding batch scripts. See &#8220;Command Prompt&#8221; for a list of CMD tricks you can include in batch files.

### To Start:

1. Create a `.bat` file => Right click on desktop and create a notepad document with the ext of `.bat` by changing the save as type to "all extensions" and typing it in.

Different commands to use:

   - TITLE => The Window name for the BAT file.  
   - ECHO => the "print" statement for BAT files. Anything following the word ECHO will be displayed in the command prompt as text, on its own line.  
   - ECHO OFF – BAT writers typically put this at the beginning of their files. It means that the program won't show the command that you told it to run while it's running – it'll just run the command. I'd recommend that after you run this test program, you try removing this line from your code to see what happens.  
   - PAUSE => This outputs the "press any key to continue…" message that you've seen all too many times. It's helpful because it pauses the BAT file execution until the user tells it to go again. If you don't put this in your program, everything will speed by and end before you can see it. People typically put this in BAT files to give the user a chance to review the material on the screen before continuing.  
   - CLS => Clears the DOS window.  
   - Windows run commands will be the most used in batch files. Ex: `Ipconfig /all`, `chkdsk`, `msinfo32`, `ping`, `tracert`, and `dir`.

2. Think about what you want it to do and edit your bat file to do it. Right click your BAT file and click "edit" to bring up Notepad. The whole document should be blank. Here is an example: (::TEXT is a comment and not a command)

   ```console
   ECHO OFF  
   ::CMD will no longer show us what command it's executing(cleaner)  
   ECHO As a network admin, I'm getting tired of having to type these commands in! Hopefully, this saves me some time in the long run.  
   :: Print some text  
   IPCONFIG /ALL  
   :: Outputs tons of network information into the command prompt  
   PAUSE  
   :: Lets the user read the important network information  
   PING www.google.com  
   :: Ping google to figure out if we've got internet!  
   ECHO All done pinging Google.  
   ::Print some text  
   PAUSE  
   :: Give the user some time to see the results. Because this is our last line, the program will exit and the command window will close once this line finishes.
   ```

