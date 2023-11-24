---
title: 'BSODs: Stop Error Codes'
date: 2016-05-26T22:40:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/bsods-stop-error-codes/
tags:
  - Windows
---
<!--more-->

### Description:

Computers will sometimes get the &#8220;Blue Screen of Death&#8221; or a BSOD for short. These are called &#8220;Stop Error Codes&#8221; and can be helpful in trying to determine the point of failure. If possible, disable automatic reboot in the system properties (`sysdm.cpl` => Advanced tab => Startup and Recovery => Settings => Uncheck &#8220;Automatically restart&#8221; under System Failure) so that you have time to write these down.

### `STOP 0x0000007B Error Message: INACCESSIBLE_BOOT_DEVICE`

1. These are caused by device driver issues (especially those related to hard drive and other storage controllers), viruses, data corruption, and sometimes even hardware failures.

2. Restart your computer if you haven't already done so. The STOP 0x0000007B blue screen error might be a one-off situation. I've seen it happen when someone plugged in a camera to a USB port.

3. Try to do a System Restore to revert back.

4. Rollback hard drive controller device driver to version prior to your driver update.

5. Verify that the hard drive is configured properly in BIOS. The STOP 0x0000007B error could occur if the hard drive settings in BIOS are incorrect.

6. Scan your computer for viruses. Certain viruses that infect the master boot record (MBR) or boot sector can cause STOP 0x0000007B errors. Clear the CMOS. Sometimes the

7. STOP 0x0000007B error is caused by a BIOS memory issue. Clearing the CMOS could solve that problem.

### Use These Steps To Further Diagnose BSODs:

1. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `verifier` => &#8220;delete existing settings&#8221; radio button.

2. Verifier - &#8220;Create standard settings&#8221; => &#8220;Automatically select all drivers installed on this computer&#8221; => reboot (`shutdown -f -r -t 00`)

3. Computer will reboot over and over producing blue screens.

4. After you have collected a few (I would say at least 3), get in to Safe mode w/ networking.

5. [run => cmd => ](https://automationadmin.com/2016/05/command-prompt-overview/) `verifier` => &#8220;delete existing settings&#8221; radio button (again) => reboot into normal mode

6. Now download [MS Debugging Tools](http://msdn.microsoft.com/en-us/library/windows/hardware/ff551063(v=vs.85).aspx) and run `Windbg(x64)` on the computer.

7. From &#8220;File&#8221; => Open Crash Dump (Ctrl+D) => Type in `%SystemRoot%MEMORY.DMP` to the filename. This will generate the BSOD Report.

8. From there go to the `!analyze -v` link inside to document to help identify which driver or system file that may be the cause of the BSOD.

9. Always run tools like &#8220;Blue Screen View&#8221; in conjunction with tools like these to determine faults, the more information the better.

10. Troubleshooting Steps Copied From A Forum Member:

   ```escape
   Blue screens are caused by faulty hardware or faulty hardware drivers.

   To See if a Fix is Available  
   In Control Panel (and select Classic view in the left hand pane) choose Problem Reports and Solutions (type problem in Start's search box), go to Problem History, right click your error and choose Check For Solution. You may also right click and choose Details for more info. Post those details here.

   To See if a Recent System Change Caused It  
   In Control Panel (and select Classic view in the left hand pane) choose Administrative Tools then chooseReliability and Performance Monitor and choose Monitoring Tools then Reliability Monitor (type Reliability in search on Start) . This list is a chart of software installs, uninstalls, Windows updates, and crashes by date (scroll left to see earlier dates). See if your crashes started happening after you installed or uninstalled something.

   First lets test what hardware we can.

   Standard Hardware Troubleshooting

   S.M.A.R.T  
   Click Start => All Programs => Accessories => Right click Command Prompt and choose Run As Administrator.

   Disk drives in Windows monitor themselves for impending failure. The feature is called S.M.A.R.T. It will detect impending failure 30% of the time. In an elevated command prompt type (it's one line)

   wmic /namespace:\rootwmi PATH MSStorageDriver_FailurePredictStatus get active,predictfailure,reason /format:List

   If it's on Active will be true, if not on turn it on in the computer's BIOS.

   Predict Failure should be False if everything's ok.

   In Vista and later if SMART predicts failure Windows prompts the user to run Backup.

   Run Chkdsk  
   In Computer right click all your drives and choose Properties, then Tools tab, then click Check Now. Tick BOTHcheckboxes then Start. Reboot. This will take overnight.

   Sfc  
   Check for file corruption by clicking Start => All Programs => Accessories => Right click Command Prompt and choose Run As Administrator. Type

   sfc /scannow  
   Memory Diagnostic  
   If you haven't run a memory diagnostic then please do so. Click Start => Control Panel => choose Classic View in left hand pane => choose Administrative Tools => then Memory Diagnostics Tool.

   For Chkdsk Results  
   Click Start => Control Panel (and select Classic view in the left hand pane) choose Administrative Tools thenEvent Viewer then look at both the Application and System logs (under Windows Logs) for entries.

   Look for EventID is 7 and Source is Disk  
   Look for EventID is 11 and Source is Disk  
   Look for EventID is 51 and Source is Disk  
   Look for EventID is 52 and Source is Disk  
   Look for EventID is 55 and Source is NTFS  
   Look for EventID is 130 and Source is NTFS  
   Look for EventID is 1001 and Source is Autochk  
   Look for EventID is 1001 and Source is Winlogon  
   Look for EventID is 1001 and Source is WinInit  
   Look for EventID is 1001 and Source is Chkdsk  
   Look for EventID is 26212 and Source is Chkdsk

   Double click the entry for details on that entry.

   P.S. 7 and 55 are the auto repair codes where windows repairs disk errors silently on the fly. 52 is the SMART warning.

   For SFC Results  
   Click Start => All Programs => Accessories => Right click Command Prompt and choose Run As Administrator. Type  
   findstr /c:&#8221;[SR] Cannot&#8221; %windir%\logs\cbscbs.log|more

   This will see which files are corrupted. We may be able to copy them from another computer.

   For Memory Diagnostic Results  
   Click Start => Control Panel (and select Classic view in the left hand pane) choose Administrative Tools thenEvent Viewer then look at both the Application and System logs (under Windows Logs) for entries.

   Look for EventID is 1201 or 1101 and Source is MemoryDiagnostic-Results

   Double click the entry for details on that entry.

   Dump Files

   Dump files are files containing the state of the machine when it crashed. We can analyse the file to identify the driver (or program) causing the crash.

   Analyse Dump Files  
   If you want to analyse your own dump files.

   You need to start Explorer as Administrator to access the files in C:\Windows\Minidump. Right click Explorer and choose Run As Administrator.

   Download and install Debugging Tools for Windows  
   http://msdn.microsoft.com/en-us/windows/hardware/hh852363  
   Install theWindows SDK but just choose the debugging tools.

   Create a folder called Symbols in C:

   Start Windbg. File menu => Symbol File Path and enter  
   srv\*C:symbols\*http://msdl.microsoft.com/download/symbols  
   Close and reopen WinDbg. File menu => Open Crash Dump

   This will analyse the crash dump. You need to close and reopen WinDbg for each dump file analysed. Because you are downloading symbols from the internet WinDbg will appear to be doing nothing. But it's downloading. Be patient.

   You are looking for a driver or system library that the crash occurred in at the end of the listing. Find the file, right click then Properties => Details tab. If it shows a driver you'll need to update the driver identified. Most drivers are in C:\Windows\System32\drivers. If it shows a system file see if you can get a program from analyze -v.

   Type in theWinDbg command prompt

   !analyze -v

   -v stands for Verbose and if the crash was originated by a program, as opposed to hardware or a driver, it will appear in the middle of the listing.

   Upload Them for Analysis

   Or upload the minidump files to your Public folder on Skydrive and copy the link from the address bar and I'll analyse them.

   Skydrive is Microsoft's Windows Live file upload site at https://skydrive.live.com/. Read about it athttp://explore.live.com/skydrive.

   If you have downloaded any of the Live applications or have a web based Live  
   mail account you already have access to your Skydrive.

   Put your event list in the Public folder and copy the link from the address bar.

   ```



