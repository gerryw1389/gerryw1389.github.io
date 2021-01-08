---
title: WDS With MDT
date: 2016-05-29T04:35:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/wds-with-mdt/
categories:
  - WindowsServer
tags:
  - WindowsServer-Roles
  - ComputerImaging
---
<!--more-->

### Description:

WDS stands for Windows Deployment Services and it is how Administrators push images throughout an organization. Follow these steps to deploy WDS (Windows Deployment Services => Windows Role) with MDT (Microsoft Deployment Tool => Standalone Installer). This assumes you have AD, DNS, and DHCP already setup in your environment. Download the Microsoft Deployment Toolkit 2010 and WAIK for Windows 7 prior to starting this process.

NOTE: You will see that when it comes to imaging, MDT does 80%+ of the work and WDS does the rest.

### To Resolve:

1. Install the WDS role and reboot. Then install MDT and WAIK and reboot again. NOTE: WAIK will require .NET 2.0 to be installed. Add the feature through Server Manager if it is not installed.

2. Open up &#8220;Deployment Workbench&#8221; and right click Deployment Shares => New Share => Follow the wizard to set what you want up => Finish.

3. Go to Deployment Shares => Operating Systems => Import Operating System. You will need to point to a .wim file. What I did was transferred over an ISO and then installed 7zip to extract the ISO. I then pointed to the extractedFoldersourcesinstall.wim file.

4. Go to Out of Box Drivers => add the drivers to the deployment. See [here](https://blogs.msdn.microsoft.com/alex_semi/2013/11/05/harvesting-drivers-from-running-computer-cleaner-better-works-on-windows-7/) if you need help getting drivers for your computer. NOTE: I haven't tried that since I have been hoarding an 8GB driver folder for years. You can download a CAB driver bundle on the system's support/driver page on Dell's site for Dell computers.

5. Next you would add applications. For simplicity, I didn't want to at this point in time. The idea is to get a fresh Windows deployment and then build on that. You just need the media and you need to know what the parameter [switch] to do a quiet install.

6. Next you add a Task Sequence. Right click Task Sequence => New. Name is something unique like &#8220;W7x64Pro&#8221; or &#8220;Default&#8221;. Click Next => Standard Client Task Sequence => Put your Organizations name in the Owner => Put in the password for the default administrator account.

7. You should now see the Task Sequence in the list. Right click it => Properties => Task Sequence Tab => State Restore => Windows Update. Uncheck the &#8220;disable this step&#8221; in the options tab. Scroll down two more and do the same thing.

   - If you don't plan to use WDS (such as for using a thumb drive deployment) : Go back up to the MDT Deployment Share node and right click your share name. Go to Properties => Windows PE tab => General tab => Select &#8220;Generate a LiteTouch bootable ISO image&#8221; => OK.

8. Go back up to the MDT Deployment Share node and click the option to &#8220;Update Deployment Share&#8221;. This might take a while. This creates your WIM and ISO files based on the configuration from above.

9. Now import the WIM to WDS. Open up &#8220;Windows Deployment Services&#8221; (different from Deployment Workbench) and drill down to your server and then Boot Images. Here, Right click => Add => Point to: `\\severname\deplymentshare$\bootLiteTouchPE_x64.wim`.

**From here we have two options:**

1. Boot a computer using PXE boot, it will find the WDS Server and present you with a screen with the only option to &#8220;Capture Computer&#8221;. Click Next and it will ask for credentials. I'm sure I messed this step up but what I did was create a local admin account on my WDS Server called &#8220;test&#8221; and so when it got to this screen I used:

   ```escape
   username: test  
   password: myPasswordForTest  
   Domain: .
   ```

   - It will then bring you to a wizard of options, I just chose the defaults and it deployed W7 Ultimate.

2. The Preferred Option: Capture a reference computer and then sys prep it and deploy that:

   - Create a Windows VM in VirtualBox/HyperV or whatever you use. Do Windows updates and create a snapshot of it. Shut it down.

   - PXE boot this VM by setting Network first in the boot settings and pressing `F12` on startup. Follow MDT to create a capture of it.

   - On the WDS Sever, open up &#8220;Deployment Workbench&#8221; and go to Operating Systems => Import Operating System => Change to &#8220;custom wim&#8221; => Select from `\\ServerName\DeploymentShare$\Captures`

   - Redo step 10 above with the captured computers WIM instead of the Litetouch one we created earlier.

   - NOTE: In my lab I have done through step 10 and then created an empty W7 VM with no OS and PXE booting and got the OS installed. That is it! I am still working on following the preferred option and also want to see how to automate the entire thing from once you PXE launch the target computer. So this is just a general rough step 1.

### References:

["Deploy Windows 7 The Easy Way: Using WDS, MDT and AIK – Step-By-Step Video"](https://blogs.technet.microsoft.com/danstolts/2010/03/deploy-windows-7-the-easy-way-using-wds-mdt-and-aik-step-by-step-video/)  
["MDT 2012 Guide"](https://msadministrator.com/guides/mdt-2012-step-by-step-guide/)