---
title: Variato Software Install
date: 2017-07-23T04:13:43+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/07/variato-software-install/
categories:
  - LocalSoftware
---
<!--more-->

### Description:

Veriato is a company that specializes in Employee Monitoring software. You buy however many licenses for the clients you want to monitor and the server software comes free. Follow these steps to setup/install their software:

### To Resolve:

1. First we need to install the server software:

   - Disable your antivirus completely
   - Install the software => Pretty straightforward
   - Add Exclusions now that the software is installed : `C:\Program Files(x86)\Veriato\*` and `C:\Windows\*`
   - Now Re-enable your AV

2. Now that the software is installed, double click the &#8220;Management Server&#8221; icon to launch the setup wizard

   - Create an application password => uses only number/letters. Special characters is broken.
   - Supply local admin creds to connect to client computers
   - Import computers => I chose to import the computers for Active Direc  - 

3. Once you have the licenses for the clients, you can follow these steps to install on the client:

   - On the client, disable AV.
   - On the server, right click the computer and choose the option to install the software. It will do it automatically and the client will reboot (!)
   - Once the client comes back up, add the C:\Windows\* exclusion, this is all that is needed in your AV.
   - Re-enable your AV.

4. Done. At this point, your client is being recorded and will send information to the server however long you have it configured for. On the server, you have to wait 15+ minutes or so and then go to the Recordings tab to see recordings of the client.

5. For the `Adobe Bad Image` Issue:

   - Computers => Mange Recorder Versions => Check for updates => Ensure you are on 7.6.45024 and have it as the default.
   - Computers => Manage Recording Profiles => Add a new Windows Profile.
   - Skip over to General Options Tab and: Name = Method1, Description = Bad Image Issue => Advanced Button (okay on message) => File Protection (dropdown) = None, OK. Now click Application => Advanced (bottom right, select yes on pop up again) => Uncheck the box &#8220;Capture elevated applications&#8221; and its childitem => Change &#8220;Network Initialization&#8221; from 0 to 10 => Click OK and exit.
   - Uninstall the recorder on the users computer, select this new profile, and then re-install.


### References:

["Veriato Investigator overview video"](https://www.youtube.com/watch?v=ZD_r6L4-_n4&feature=youtu.be)  