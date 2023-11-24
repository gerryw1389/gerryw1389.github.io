---
title: System32 Files
date: 2016-05-26T22:34:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/system32-files/
tags:
  - Windows
---
<!--more-->

### Description:

This is a list of files that reside in the &#8220;C:\Windows\System32&#8221; directory (NOTE: Many of these are from XP):

acctres.dll => Microsoft Internet Account Manager Resources => Needed to open Outlook Express. If you do not want users to be able to use Outlook Express, it is an easy way to delete this file.

aclui.dll => Security Descriptor Editor => Needed to enable Registry Editor.

activeds.dll => ADs Router Layer DLL => Needed to open the Event viewer and Services Viewer.

actxprxy.dll => ActiveX Interface Marshaling Library => Essential to Internet Explorer. This DLL keeps track on Active X modules.

advapi32.dll => Advanced Windows 32 Base API => Needed to boot to Windows. Provides access to the fundamental resources available to a Windows system. Included are things like file systems, devices, processes and threads, access to the Windows registry, and error handling.

advpack.dll => Advpack Library => Needed by Microsoft Update. This DLL builds up the Windows Update menu and accesses the updates list in the registry.

apphelp.dll => Application Compatibility Client Library => This DLL came with service pack 3 and it enables the Microsoft management console to work.

asycfilt.dll => Allows applications to communicate between each other using Object Linking and Embedding (OLE).

atl.dll => ATL Module for Windows XP (Unicode) => Needed by Microsoft Update. Also needed to open Event and Services Viewers. And needed by Outlook Express. Without this file Outlook Express will not open. You will receive this message when you click on the Outlook Express shortcut: Outlook Express could not be started because MSOE.DLL could not be found. Outlook Express may not be installed correctly.

attrib.exe => Attribute Utility => Displays or changes file attributes (read-only, archive, hidden, or system).

audiosrv.dll => Windows Audio Service => Needed to hear sound on your computer. Main Service file for Windows Audio.

authz.dll => Authorization Framework => Needed to boot to Windows.

autochk.exe => Auto Check Disk => Needed to boot to Windows. Launches automatically during Windows XP bootup if a volume is marked with bad clusters, error blocks, or otherwise damaged.

avifil32.dll => Microsoft AVI File support library.

basesvr.dll => Windows NT BASE API Server DLL => Needed to boot to Windows.

batmeter.dll => Battery Meter Helper DLL => Power Options in Control Panel.

bootvid.dll => VGA Boot Driver => Needed to boot to Windows.

browselc.dll => Shell Browser UI Library => IE Toolbar will look messed up without it, and you cannot right-click access &#8220;Customize&#8221; without it.

browseui.dll => Shell Browser UI Library => Needed to boot to Windows.

cabinet.dll => Microsoft® Cabinet File API => Microsoft Update. Also needed to access Properties of Devices in Device Manager.

cabview.dll => Cabinet File Viewer Shell Extension => Needed to view inside .cab files.

cdm.dll => Windows Update CDM Stub.

certcli.dll => Microsoft® Certificate Services Client => Display Properties of devices in Device Manager.

cfgmgr32.dll => Configuration Manager Forwarder DLL => Part of CHKDSK.

chkdsk.exe => Check Disk => Part of CHKDSK. A disk inspection tool that can search for and repair disk errors.

clb.dll => Column List Box => Needed to open Registry Editor.

clusapi.dll => Cluster API Library => Needed to access Disk Management in Computer Management. Also needed by Microsoft Update to install February 20, 2006 update for Windows Media Player 10. An application programming interface (API) is the interface that a computer system, library or application provides in order to allow requests for service to be made of it by other computer programs, and/or to allow data to be exchanged between them.

cmd.exe => Command Prompt => Enables execute of a batch file. An executable that provides the command prompt (MS-DOS shell interpreter) for Windows NT.

comctl32.dll => Common Controls Library => Needed to boot to Windows. Provides the functionality to create and manage screen windows and most basic controls, such as buttons and scrollbars, receive mouse and keyboard input, and other functionality associated with the GUI part of Windows. Gives applications access to some advanced controls provided by the operating system. These include things like status bars, progress bars, toolbars and tabs.

comdlg32.dll => Common Dialogs DLL => Needed to boot to Windows. Provides applications the standard dialog boxes for opening and saving files, choosing color and font, etc.

corpol.dll => Microsoft COM Runtime Execution Engine => Microsoft Update.

crypt32.dll => Crypto API32 => Needed to boot to Windows.

cryptdll.dll => Cryptography Manager => Needed to boot to Windows.

cryptsvc.dll => Cryptographic Services => Cryptographic Services, which is needed by Microsoft Update. Also needed to access Properties of Disk Drives.

cryptui.dll => Microsoft Trust UI Provider => Needed to boot to Windows.

csrsrv.dll => Client Server Runtime Process => Needed to boot to Windows.

csrss.exe => Client-Server Runtime Server Subsystem => Needed to boot to Windows. Used to maintain the Win32 system environment console and other essential functions.

d3d8thk.dll => Microsoft Direct3D OS Thunk Layer => Needed by ConvertXtoDVD.

d3d9.dll => Microsoft Direct3D => If you update to NVIDIA display drivers version 93.71, the d3d9.dll is used by NVIDIA so that you can manually adjust Brightness, Contrast, Gamma and Image sharpening in Display Properties => Settings => Advanced => NVIDIA Unknown (or your designated graphics card, depending upon whether or not you've chosen to delete the nvapi.dll) => select Color Correction => under &#8220;Apply color changes to:&#8221; click on the drop arrow to the right of the box and select &#8220;Overlay&#8221;.

dbghelp.dll => Windows Image Helper => Windows Media Player 11. Without it, when you click on something to play, a message tells you to re-install Windows Media Player. Also needed to install WMP11.

dciman32.dll => DCI Manager => Websites with streaming media.

ddraw.dll => Microsoft DirectDraw => DVD Playback with Windows Media Player and NVDVD Player.

ddrawex.dll => Direct Draw Ex

desk.cpl => Desktop Control Panel => Display Properties Control Panel applet.

devenum.dll => Device enumeration => Needed by Windows Media Player and NVDVD Player.

devmgmt.msc => Computer Management Console => Needed to access Device Manager.

devmgr.dll => Device Manager MMC Snapin => Needed to access Device Manager.

dhcpcsvc.dll => DHCP Client Service => Needed for Internet connectivity. Main Service file for DHCP Client.

dinput.dll => Microsoft DirectInput => Needed by ffdshow.

dmocx.dll => TreeView OCX => Needed to access Device Manager.

dnsapi.dll => DNS Client API DLL Needed to boot into Windows.

dolbyhph.dll => Dolby Headphone Engine => Installed and needed by NVDVD Player.

dpcdll.dll => Dpcdll Module => Needed to boot to Windows. Product Code activation.

dsound.dll => DirectSound => Needed by Windows Media Player and NVDVD Player.

dssenh.dll => Microsoft Enhanced DSS and Diffie-Hellman Cryptographic Provider => Needed by Internet Explorer. Also needed by Microsoft Update.

duser.dll => Windows DirectUser Engine => Needed by Add/Remove Module. Also, if you delete this file Windows will display the classic logoff and logon prompts. However, you can boot to Windows without it.

dxtmsft.dll => DirectX Media => Image DirectX Transforms

dxtrans.dll => DirectX Media => DirectX Transform Core

els.dll => Event Viewer Snapin => Needed by Event Viewer.

esent.dll => Server Database Storage Engine => Microsoft Update. Also needed to access Properties of Disk Drives.

eventlog.dll => Event Logging Service => Needed by Event Viewer. Without this file present it will take a very long time for your system to boot to Windows.

eventvwr.exe => Event Viewer Microsoft Management Console => Needed by Event Viewer. Main Service file for Event Log.

eventvwr.msc => Event Viewer Microsoft Management Console => Needed by Event Viewer.

filemgmt.dll => Services and Shared Folders => Needed by Services Viewer.

fmifs.dll => FM IFS Utility DLL => Part of CHKDSK.

fntcache.dat => Font Cache => If deleted, Windows will rebuild a new FNTCACHE.DAT the next time you reboot your system. If you use SVS or SWV, and you copied fonts from a layer to the base, delete this file. Next boot it will be rebuilded and that solves a lot of the fonts problems. (Added to DinamiQs software to keep fonts in the layers without the need to rebuild everytime)

fontext.dll => Windows Font Folder => Needed to maintain selected view of Font Folder, and also needed to display the default icon for .TTF Fonts

framebuf.dll => Framebuffer Display Driver => Needed so graphics in Safe Mode don't look all screwed up.

gdi32.dll => GDI Client DLL => Needed to boot to Windows. Provides the functionality for outputting graphical content to monitors, printers and other output devices.

grpconv.exe => Group Convert => Needed for some programs to install. Converts Microsoft Windows 3.x and Microsoft Windows for Workgroups Program Manager groups into Start Menu items.

hal.dll => Hardware Abstraction Layer => Needed to boot to Windows.

hccoin.dll => USB Coinstaller => Needed by Intel Chipset INF Update Utility.

hid.dll => Hid User Library => Needed by Sound and Video Card driver installations. HID stands for Human Interface Device, a type of computer device that interacts directly with and takes input from humans.

html.iec => Microsoft HTML Converter => Needed to be able to copy text from a Webpage and paste it to Wordpad.

icmp.dll => ICMP DLL => Needed in order to install the PCPitStop Utility for computer checkup and diagnostics on the PC Pitstop Website. Also needed by TCPOptimizer. ICMP (Internet Control Message Protocol) is used when networking. It ensures the integrity of information being sent across a network.

ieframe.dll => Internet Explorer => Essential to Internet Explorer 7. (Installed by Internet Explorer 7.)

ieframe.dll.mui => Internet Explorer => Needed by Internet Explorer 7 Toolbar. (Installed by Internet Explorer 7.)

iepeers.dll => Internet Explorer Peer Objects => Needed to watch Yahoo Movie Trailers.

iertutil.dll => Run time utility for Internet Explorer => Needed to start explorer.exe with Internet Explorer 7 installed on your system. The explorer.exe (located in the C:\Windows folder), manages the Windows Graphical Shell including the Start Menu, Taskbar, Desktop, and File Manager. Without it running, the graphical interface for Windows will disappear. (The iertutil.dll is installed by Internet Explorer 7.)

ieui.dll => Internet Explorer UI Engine => Essential to Internet Explorer 7. (Installed by Internet Explorer 7.)

ifsutil.dll => IFS Utility DLL => Part of CHKDSK.

imagehlp.dll => Windows NT Image Helper => Needed to boot to Windows.

imgutil.dll => IE plugin image decoder support DLL => Belongs to Internet Explorer => Needed so you don't see red x's in place of some images.

imm32.dll => Windows XP IMM32 API Client DLL => You cannot enter System Properties without the imm32.dll or the usp10.dll present.

inetcomm.dll => Microsoft Internet Messaging API => Without this file Outlook Express will not open. You will receive this message when you click on the Outlook Express shortcut: Outlook Express could not be started because MSOE.DLL could not be found. Outlook Express may not be installed correctly. Additionally, the inetcomm.dll is needed in order to save a Webpage as an offline Webpage with an .mht extension. Also needed to save an offline Webpage with an .mht extension are the inetres.dll and the MSOERT2.DLL (Outlook Express files), and the MSHTML.TLB (Internet Explorer file).

inetcpl.cpl => Internet Control Panel => Internet Options Control Panel applet.

inetcplc.dll => Internet Control Panel => Needed to access Internet Options.

inetres.dll => Microsoft Internet Messaging API Resources => Without this file Outlook Express will not open. You will receive this message when you click on the Outlook Express shortcut: Outlook Express could not be started because MSOERES.DLL could not be found. Outlook Express may not be installed correctly. Additionally, the inetres.dll is needed in order to save a Webpage as an offline Webpage with an .mht extension. Also needed to save an offline Webpage with an .mht extension are the inetcomm.dll and the MSOERT2.DLL (Outlook Express files), and the MSHTML.TLB (Internet Explorer file).

iphlpapi.dll => IP Helper API => Needed to boot to Windows.

iuengine.dll => Windows Update Control Engine => Needed by Microsoft Update.

jscript.dll => Microsoft ® JScript => Needed by Microsoft Update. Also needed by Services Viewer.

kbdus.dll => United States Keyboard Layout => Needed to boot to Windows. You may need a different KBD*.DLL depending on your system.

kdcom.dll => Kernel Debugger HW Extension DLL => Needed to boot to Windows.

kernel32.dll => Windows NT BASE API Client DLL => Needed to boot to Windows. Provides access to the fundamental resources available to a Windows system. Included are things like file systems, devices, processes and threads, access to the Windows registry, and error handling.

ksproxy.ax => Installed by Sound Card driver installations from either the XP installation CD, or a cab file in C:\WindowsDriver Cachei386. The installation will ask for the &#8220;ksuser.dll.&#8221; Once located, the &#8220;ksproxy.ax&#8221; will be installed along with the &#8220;ksuser.dll to C:\Windows\System32.

ksuser.dll => User CSA Library => Needed by Windows Media Player and NVDVD Player. Installed by Sound Card driver installations from either the XP installation CD, or a cab file in C:\WindowsDriver Cachei386. The installation will ask for the &#8220;ksuser.dll.&#8221; Once located, the &#8220;ksuser.dll&#8221; will be installed along with the &#8220;ksproxy.ax&#8221; to C:\Windows\System32.

l3codeca.acm => MPEG Layer-3 Audio Codec for MSACM => Needed by Windows Media Player to play .mp3 music files, and also needed to be able to rip music CDs to the .mp3 format.

l3codecp.acm => MPEG Audio Layer-3 Codec for MSACM => Needed by Windows Media Player to be able to rip music CDs to the .mp3 format.

legitcheckcontrol.dll => Windows Genuine Advantage Validation => Needed by Microsoft Update. This file is replaced once or twice a year to check for piracy key's

licdll.dll => Licdll Module => Needed by Windows Update.

logonui.exe => Windows Logon User Interface => The user interface that appears when Windows XP first starts => If you delete this file, Windows will display the classic logoff and logon prompts. However, you can boot up to Windows without it. With resourcehacker this executable can be customised to create custom ctrl-alt-del menu's

lsasrv.dll => LSA Server DLL => Needed to boot to Windows.

lsass.exe => LSA Security Service => Needed to boot to Windows. The Local Security Authority server process.

lz32.dll => LZ Expand/Compress API DLL => Needed to properly display the default icon for .ttf extension fonts.

mcicda.dll => MCI driver for cdaudio devices => Needed by Windows Media Player burning and ripping processes.

mfc42.dll => MFCDLL Shared Library => Retail Version

mfc42u.dll => MFCDLL Shared Library => Retail Version => Needed to open Event and Services Viewers. Needed to access Device Manager. And also needed by Wordpad.

mfplat.dll => Media Foundation Platform => To even open Windows Media Player 11.

mlang.dll => Multi Language Support DLL => Essential to Internet Explorer.

mmc.exe => Microsoft Management Console => Needed to open Event and Services Viewers. Also needed to access Device Manager.

mmcbase.dll => MMC Base DLL => Needed by Event and Services Viewers. Also needed to access Device Manager.

mmcndmgr.dll => MMC Node Manager DLL => Needed by Event and Services Viewers. Also needed to access Device Manager.

mpg4dmod.dll => Corona Windows Media MPEG-4 S Video Decoder => Needed to be able to adjust the brightness in Windows Media Player for certain videos.

mpr.dll => Multiple Provider Router DLL => Needed to boot to Windows.

mprapi.dll => Windows NT MP Router Administration DLL => After installing Internet Explorer 7, this file is one of five system32 files needed to open Internet Options: MPRAPI.DLL, msrating.dll, rasapi32.dll, rasdlg.dll and rasman.dll. Additionally needed to open Network Connections in Control Panel.

msacm32.dll => Microsoft ACM Audio Filter => Needed to open Audio tab in Sound and Audio Device properties. You cannot view or change multimedia properties without this file. Also needed to hear sound in Windows Pinball Game.

msacm32.drv => Microsoft Sound Mapper => Needed to hear sound in Windows Pinball Game.

msasn1.dll => ASN.1 Runtime APIs => Needed to boot to Windows.

msconfig.exe => System Configuration Utility => Designed to help you troubleshoot problems with your computer. MSCONFIG can also be used to ensure that your computer boots faster and crashes less => In PART 5 I moved msconfig.exe to the system32 folder from C:\Windowspchealthhelpctrbinaries before I deleted the pchealth folder and its contents.

msctfime.ime => Microsoft Text Frame Work Service IME => Installed with Internet Explorer 7 => If this file is not present your system could lockup while working at your Desktop.

msdmo.dll => DMO Runtime => Without the msdmo.dll present, Windows Media Player will not play&#8230;anything. Also, the msdmo.dll is very much needed by Websites with streaming media.

msdxm.ocx => Windows Media Player 2 ActiveX Control => Needed by too many Websites with streaming media to not keep this file installed on my system. The msdxm.ocx (DirectX file) and the wmpdxm.dll (Windows Media Player file) work together. The msdxm.ocx is also needed to start Media Player 6.4 (mplayer2.exe).

msftedit.dll => Rich Text Edit Control, v4.1 => Needed by Wordpad. Contains functions for the Rich Text Edit control version 4.1.

msgina.dll => Windows NT Logon GINA DLL => Needed to boot to Windows. Loads Logon User Interface.

mshtml.dll => Microsoft ® HTML Viewer => Needed by Internet Explorer.

mshtml.tlb => Microsoft ® MSHTML Typelib => Needed in order to save a Webpage as an offline Webpage with an .mht extension. Also needed to save an offline Webpage with an .mht extension are the inetcomm.dll, the inetres.dll and the MSOERT2.DLL (Outlook Express files).

mshtmled.dll => Microsoft ® HTML Editing Component => Gives you the ability to edit HTML. An example of this would be when you edit one of your posts on some forums. You wouldn't be able to do that without this file.

mshtmler.dll => Microsoft ® HTML Editing Component's Resource DLL => Needed to insert a picture in E-mail using Outlook Express.

msi.dll => Windows Installer => Needed by Windows Installer. Also needed by PerfectDisk 6. (PerfectDisk 8 does not need the MSI.DLL.)

msident.dll => Microsoft Identity Manager => Needed by Outlook Express.

msidle.dll => User Idle Monitor => Needed by Microsoft Update.

msidntld.dll => Microsoft Identity Manager => Needed by Outlook Express.

msiexec.exe => Windows Installer => Main Service File for Windows Installer. Windows Installer uses the information within .MSI files that are provided with some applications, and installs, repairs, or removes software using this information. Note: You can view these .MSI (Windows Installer File) files within the C:\WindowsInstaller folder.

msihnd.dll => Needed by Windows Installer.

msimg32.dll => GDIEXT Client DLL => Without this file present, upon booting to Windows, you will need to click OK on a Logon Message in order to enter Windows.

msisip.dll => MSI Signature SIP Provider => Windows Installer file. SIP stands for Session Initiation Protocol.

msls31.dll => Microsoft Line Services library file => Essential to Internet Explorer.

msoeacct.dll => Microsoft Internet Account Manager => Needed by Outlook Express.

msoert2.dll => Microsoft Outlook Express RT Lib => Needed by Outlook Express. Additionally, the MSOERT2.DLL is needed in order to save a Webpage as an offline Webpage with an .mht extension. Also needed to save an offline Webpage with an .mht extension are the inetcomm.dll and the inetres.dll (Outlook Express files), and the MSHTML.TLB (Internet Explorer file).

mspaint.exe => Microsoft Paint => A basic graphics creation and viewing tool.

mspatcha.dll => Microsoft® Patch Engine => Needed by Microsoft Update.

msprivs.dll => Microsoft Privilege Translations => Needed to boot to Windows.

msrating.dll => Internet Ratings and Local User Management DLL => After installing Internet Explorer 7, this file is one of five system32 files needed to open Internet Options: MPRAPI.DLL, msrating.dll, rasapi32.dll, rasdlg.dll and rasman.dll.

msv1_0.dll => Microsoft Authentication Package v1.0 => Needed to boot to Windows.

msvbvm60.dll => Visual Basic Virtual Machine => Contains program code used to run programs that are written in the Visual Basic programming language. As one example, CCleaner, a very popular program needs this file.

msvcp60.dll => Microsoft ® C++ Runtime Library => Needed to boot to Windows.

msvcp71.dll => Microsoft® C++ Runtime Library => Installed by Acronis True Image 10.

msvcr71.dll => Microsoft® C Runtime Library => Installed by Acronis True Image 10.

msvcrt.dll => Windows NT CRT DLL => Needed to boot to Windows.

msvfw32.dll => Microsoft Video for Windows DLL => Needed to open Windows Media Player.

mswsock.dll => Microsoft Windows Sockets 2.0 Service Provider => Essential to Internet Explorer.

msxml3.dll => MSXML 3.0 SP 5 => Needed by Event and Services Viewers. Also needed to access Device Manager.

msxml3r.dll => XML Resources => Needed by Event and Services Viewers. Also needed to access Device Manager.

muweb.dll => Microsoft Update Web Control => Installed by Microsoft Update Software.

mydocs.dll => My Documents Folder UI => Needed to properly display the My Documents Icon.

ncobjapi.dll => Needed to boot to Windows.

nddeapi.dll => Network DDE Share Management APIs => Needed to boot to Windows.

netapi32.dll => Net Win32 API DLL => Needed to boot to Windows.

newdev.dll => Add Hardware Device Library => Needed by Sound and Video Card driver installations. I'm sure other hardware device driver installations need it too.

normaliz.dll => Unicode Normalization DLL => Needed to start explorer.exe with Internet Explorer 7 installed on your system. The explorer.exe (located in the C:\Windows folder), manages the Windows Graphical Shell including the Start Menu, Taskbar, Desktop, and File Manager. Without it running, the graphical interface for Windows will disappear. (The normaliz.dll is installed by Internet Explorer 7.)

notepad.exe => Notepad => Notepad text-editing utility.

ntdll.dll => NT Layer DLL => Needed to boot to Windows.

ntdsapi.dll => NT5DS Library => Needed to boot to Windows

ntoskrnl.exe => NT Kernel & System => Windows XP operating system Kernel => Needed to boot to Windows

nv4_disp.dll => NVIDIA Compatible Windows 2000 Display driver => Essential for Display Adapter. And needed to boot to Windows.

nvcod.dll => NVIDIA Driver Co-Installer

nvcpl.dll => NVIDIA Display Properties Extension

nvdisp.nvu => NVIDIA Extension

nvshell.dll => NVIDIA Desktop Explorer

nvudisp.exe => NVIDIA Uninstaller Utility => Needed by NVIDIA to uninstall older drivers before installing new drivers during the updating process.

occache.dll => Object Control Viewer => Needed to view icon for ActiveX objects in Downloaded Program Files. Otherwise the ActiveX objects show up as .ini files.

odbc32.dll => Microsoft Data Access => ODBC Driver Manager => Needed to boot to Windows.

odbcint.dll => Microsoft Data Access => ODBC Resources => Needed to boot to Windows.

ole32.dll => Microsoft OLE for Windows => Needed to boot to Windows.

oleacc.dll => Active Accessibility Core Component

oleaccrc.dll => Active Accessibility Resource DLL

oleaut32.dll => Needed to boot to Windows.

oledlg.dll => Microsoft Windows™ OLE 2.0 User Interface Support => Needed to open NVDVD Player. Also needed by Wordpad.

olepro32.dll => Needed to open NVDVD Player.

olethk32.dll => Microsoft OLE for Windows => Needed by Nero.

pdboot.exe => PerfectDisk Boot Time Defragmentation => Needed by PerfectDisk.

pidgen.dll => Pid3.0 generation => Needed by Microsoft Update. During Windows setup the pidgen.dll produces a PID (Product Identification) from the serial number entered.

pngfilt.dll => IE PNG plugin image decoder => Belongs to Internet Explorer => Needed so you don't see red x's in place of some images.

powrprof.dll => Power Profile Helper DLL => Along with the powercfg.cpl, needed to enter Power Options where you can adjust how you want your computer to power down. Without this file present, you will receive an error when opening Properties for your Keyboard. However, the Properties for Keyboard will eventually open.

profmap.dll => Userenv => Needed to boot to Windows.

psapi.dll => Process Status Helper => Needed to boot to Windows.

qasf.dll => DirectShow ASF Support => Needed to play WMA music files and WMV video files with Media Player Classic, a third-party media player. GASF stands for Advanced Systems Format (formerly Advanced Streaming Format), Microsoft's proprietary digital audio/digital video container format, especially meant for streaming media. The most common file types contained within an ASF file are Windows Media Audio (WMA) and Windows Media Video (WMV).

qdvd.dll => DirectShow DVD Playback Runtime => Needed For DVD Playback with Windows Media Player and NVDVD Player.

qmgr.dll => Background Intelligent Transfer Service => Needed by Microsoft Update. Main Service file for Background Intelligent Transfer.

rasdlg.dll => Remote Access Common Dialog API

rasman.dll => Remote Access Connection Manager

regapi.dll => Registry Configuration API => Needed to boot to Windows.

regsvr32.exe => Microsoft© Register Server => You can use the Regsvr32 tool (Regsvr32.exe) to Register and UnRegister object linking and embedding (OLE) controls such as dynamic-link library (DLL) or ActiveX Controls (OCX) files that are self-registerable.

riched20.dll => Rich Text Edit Control, v3.0 => Needed by Event Viewer. Contains functions for the Rich Text Edit control versions 2.0 and 3.0.

riched32.dll => Wrapper Dll for Richedit 1.0 => Needed by Event Viewer. Contains functions for the Rich Text Edit control version 1.0.

rpcrt3.dll => Remote Procedure Call Runtime => Needed to boot to Windows.

rpcss.dll => Distributed COM Services => Needed to boot to Windows. Main Service file for Remote Procedure Call (RPC).

rsaenh.dll => Microsoft Enhanced Cryptographic Provider => Needed to boot to Windows. The RSAENH.DLL is needed to accurately check license for Windows.

rshx32.dll => 1Security Shell Extension => The Rshx32.dll controls the Security tab in Properties of files and folders. (To be able to see the Security tab in XP Home Edition you must be in Safemode.)

rtutils.dll => Routing Utilities => Needed by Websites with streaming media.

rundll32.exe => Run DLL => Used to run DLL files from a command line.

runonce.exe => Run Once => Used to perform tasks as defined in the RunOnce Registry key.

samlib.dll => SAM Library DLL => Needed to boot to Windows.

samsrv.dll => SAM Server DLL => Needed to boot to Windows.

sc.exe => A tool to aid in developing services for Windows NT => Communicates with the Service Controller and installed services. The SC.exe retrieves and sets control information about Services.

scesrv.dll => Windows Security Configuration Editor Engine => Needed to boot to Windows.

schannel.dll => TLS / SSL Security Provider => Needed by Internet Explorer. Also needed by Microsoft Update.

secur32.dll => Security Support Provider Interface => Needed to boot to Windows.

sendmail.dll => Send Mail => The sendmail.dll is a library file used for sending mail via Websites.

services.exe => Services and Controller app => Needed to boot to Windows. Main Service file for Plug and Play.

services.msc => Services Viewer => Needed by Services Viewer.

setupapi.dll => Windows Setup API => Needed to boot to Windows.

sfc.dll => Windows File Protection => Needed by Microsoft Update.

sfc\_os.dll => Windows File Protection => You can boot to Windows without this file, but not without first having to click OK on an error that appears telling you the SFC\_OS.DLL cannot be found.

sfcfiles.dll => Windows 2000 System File Checker => Needed to display Properties button in Control Panel > Keyboard > Hardware without receiving an error.

shdoclc.dll => Shell Doc Object and Control Library => Needed to be able to access right-click options while right-clicking on a Webpage.

shdocvw.dll => Shell Doc Object and Control Library => Needed to boot to Windows.

shell32.dll => Windows Shell Common Dll => Needed to boot to Windows.

shellstyle.dll => Windows Shell Style Resource Dll => If you choose to use the Windows Classic theme, and delete the Themes folder and its contents, you will still need the shellstyle.dll that is in the system32 folder in order to gain access to the Add or Remove Programs panel.

shfolder.dll => Shell Folder Service => Needed by Microsoft Update.

shgina.dll => Windows Shell User Logon => Needed to restart your computer from your Desktop. Further, once you delete or move this file from the system32 folder=>even if you put it back=>you still won't be able to restart from your Desktop.

shimgvw.dll => Windows Picture and Fax Viewer => Needed to display saved image files.

shlwapi.dll => Shell Light-weight Utility Library => Needed to boot to Windows. Allows applications to access the functionality provided by the operating system shell, as well as change and enhance it.

shsvcs.dll => Windows Shell Services Dll => Main Service file for Shell Hardware Detection.

shutdown.exe => Remote Shutdown Tool => Allows shutdowns and restarts on local or remote PCs.

smss.exe => Windows NT Session Manager => Needed to boot to Windows. Used to establish the Windows XP environment during bootup.

snapapi.dll => Acronis Snapshot Dynamic Link Library => Installed by Acronis True Image.

sndvol32.exe => Volume Control => A GUI (Graphical User Interface) volume application.

stdole2.tlb => Microsoft OLE 3.50 for Windows NT™ and Windows 95™ Operating Systems => After deleting the stdole2.tlb and rebooting your system, you may be unable to launch the Search Assistant.

stdole32.tlb => Microsoft OLE 2.1 for Windows NT™ Operating System => When you delete one or both the stdole32.tlb or the stdole2.tlb from the system32 folder, when installing a program that uses InstallShield, you may receive the following error message: The install Shield engine &#8220;ikernel.exe&#8221; could not be launched -Error loading type library /dll.

storprop.dll => Property Pages for Storage Devices => Needed to view Advanced Settings tab in Primary IDE Channel and Secondary IDE Channel under IDE ATA/ATAPI controllers in Device Manager.

svchost.exe => Generic Host Process for Win32 Service => Needed to boot to Windows.

sxs.dll => Fusion 2.5 => Needed to boot to Windows.

sysdm.cpl => System Applet for the Control Panel => System Properties Control Panel applet.

syssetup.dll => Windows NT System Setup => Needed to display Properties button in Control Panel > Keyboard > Hardware without receiving an error.

tapi32.dll => Microsoft® Windows™ Telephony API Client DLL => TAPI32.DLL is needed by streaming media on many sites.

taskmgr.exe => Task Manager => The Task Manager application.

themeui.dll => Windows Theme API => Needed by Display Properties.

timedate.cpl => Time Date Control Panel Applet => Date and Time Properties Control Panel applet.

ulib.dll => File Utilities Support DLL => Part of CHKDSK.

umpnpmgr.dll => User-mode Plug-and-Play Service => Needed to boot to Windows.

untfs.dll => NTFS Utility DLL => Part of CHKDSK.

url.dll => Internet Shortcut Shell Extension DLL => Displays default &#8220;e&#8221; icon for Internet Shortcuts and the one displayed in your Explorer Toolbar Address Bar.

urlmon.dll => OLE32 Extensions for Win32 => Essential to Internet Explorer.

usbui.dll => USB UI Dll => Needed to display Advanced tab in USB Universal Host Controller Properties, and Power tab in USB Root Hub Properties in Device Manager.

user32.dll => Windows XP USER API Client DLL => Needed to boot to Windows.

userenv.dll => Userenv => Needed to boot to Windows.

userinit.exe => User Initialization => Needed to boot to Windows. Used to establish the operating environment for a user after logon.

usp10.dll => Unicode script processor => You cannot enter System Properties without the usp10.dll or the imm32.dll present.

uxtheme.dll => Microsoft UxTheme Library => Needed to boot to Windows. Main Service file for Themes.

vbscript.dll => Microsoft ® VBScript => Needed by some Websites with streaming media. Also needed by Yahoo Chat.

vdmdbg.dll => Needed to access Task Manager.

version.dll => Version Checking and File Installation Libraries => Needed to boot to Windows.

watchdog.sys => Watchdog Driver => Needed to boot to Windows.

wdmaud.drv => WDM Audio driver mapper => Needed by Windows Media Player. Also needed to hear sound in Windows Pinball Game.

webcheck.dll => Web Site Monitor => Needed by Microsoft Update. You will need the webcheck.dll to install the new Microsoft Update software.

win32k.sys => Multi-User Win32 Driver => Needed to boot to Windows.

winhttp.dll => Windows HTTP Services => Needed by Microsoft Update. In Vista this DLL is needed to open Wireless configuration dialogbox

wininet.dll => Internet Extensions for Win32 => Needed to boot to Windows. Internet Explorer file.

winlogon.exe => Windows NT Logon Application => Needed to boot to Windows. Windows logon manager. Handles the login and logout procedures. With resourcehacker this file can be altered to control logon procedures and to alter the tasks that it follows.

winmm.dll => MCI API DLL => Needed by Windows Media Player.

winscard.dll => Microsoft Smart Card API => Needed by Microsoft Update.

winspool.drv => Windows Spooler Driver.

winsrv.dll => Windows Server DLL => Needed to boot to Windows.

winsta.dll => Winstation Library => Needed to boot to Windows.

wintrust.dll => Microsoft Trust Verification APIs => Needed to boot to Windows.

wldap32.dll => Win32 LDAP API DLL => Needed to boot to Windows.

wlnotify.dll => Common DLL to receive Winlogon notifications => Needed by Microsoft Update.

wmadmod.dll => Windows Media Audio Decoder => Needed by Windows Media Player to play .WMA music files.

wmadmoe.dll => Windows Media Audio Encoder/Transcoder => Needed by Windows Media Player ripping process.

wmasf.dll => Windows Media ASF DLL => Needed by Windows Media Player.

wmi.dll => WMI DC and DP functionality) => Needed to access Device Manager.

wmnetmgr.dll => Windows Media Network Plugin Manager DLL => Needed to watch Yahoo Movie Trailers.

wmp.dll => Windows Media Player Core => Needed to open Windows Media Player.

wmpdxm.dll => Windows Media 6.4 Player Shim => Needed by too many Websites with streaming media to not keep this file installed on my system.

wmpeffects.dll => Windows Media Player Effects => Needed for visual effects while playing music with Windows Media Player 11.

wmploc.dll => Windows Media Player => Needed to open Windows Media Player.

wmpps.dll => Windows Media Player Proxy Stub Dll => Needed to rip music CDs using Windows Media Player 11 with file-name information intact, such as the name of the artist, album, song title. Without the wmpps.dll file present, the file-name information it will read and write as &#8220;01 Unknown Artist Track 1&#8221;. Also needed to burn .WMA files to a CD using WMP11.

wmpshell.dll => Windows Media Player Launcher => Without the wmpshell.dll present WMP cannot remember that it's supposed to open your media files. The Open With dialog box will open instead, asking you to choose a program you want to use to open the file.

wmvcore.dll => Windows Media Playback/Authoring DLL => Needed to watch Yahoo Movie Trailers.

wmvdecod.dll => Windows Media Video Decoder => Needed to watch MSNBC videos online, and to watch Yahoo Movie Trailers with Windows Media Player 11 installed on your system.

wpa.dbl => Windows Product Activation (WPA) => Needed to boot to Windows.

ws2_32.dll => Windows Socket 2.0 32-Bit DLL => Needed to boot to Windows.

ws2help.dll => Windows Socket 2.0 Helper for Windows NT => Needed to boot to Windows.

wshtcpip.dll => Windows Sockets Helper DLL => Essential to Internet Explorer

wsock32.dll => Windows Socket 32-Bit DLL => Needed for Internet Connectivity. Winsock (short for Windows Sockets) is a specification that defines how Windows network software should access network services, especially TCP/IP.

wtsapi32.dll => WTSAPI32.DLL (Windows Terminal Server SDK APIs) => Needed both to view the Automatic Updates tab in System Properties, and by Microsoft Update. Also needed to enter System Properties by right-clicking on My Computer and selecting Properties without receiving this error: This application has failed to start because WTSAPI32.DLL was not found. Re-installing the application may fix this. However, System Properties will open after clicking OK on the error message even without this file present.

wuaucpl.cpl => Automatic Updates Control Panel => Automatic Updates Control Panel applet => Needed by Microsoft Update.

wuapi.dll.mui => Windows Update Client API => Needed by Microsoft Update.

wuauclt.exe => Windows Update => An auto-update client => Needed by Microsoft Update.

wuauclt1.exe => Windows Update AutoUpdate Client => Needed by Microsoft Update.

wuaucpl.cpl => Automatic Updates Control Panel applet => Needed by Microsoft Update.

wuaucpl.cpl.mui => Automatic Updates Control Panel => Needed by Microsoft Update.

wuaueng.dll => Windows Update AutoUpdate Engine => Needed by Microsoft Update.

wuaueng.dll.mui => Windows Update Agent => Needed by Microsoft Update.

wuaueng1.dll => Windows Update AutoUpdate Engine => Needed by Microsoft Update.

wuauserv.dll => Windows Update AutoUpdate Service => Needed by Microsoft Update. Main Service file for Automatic Updates.

wucltui.dll => Windows Update Client UI Plugin => Needed by Microsoft Update.

wucltui.dll.mui => Windows Update Client UI Plugin => Needed by Microsoft Update.

wupdmgr.exe => Windows Update Manager for NT => Needed by Microsoft Update.

wups.dll => Windows Update client proxy stub => Needed by Microsoft Update.

wups2.dll => Windows Update client proxy stub 2 => Needed by Microsoft Update.

wuweb.dll => Windows Update Web Control => Needed by Microsoft Update.

xmllite.dll => Microsoft XmlLite Library => Needed by Internet Explorer 7 Toolbar. (Installed by Internet Explorer 7.)

xpsp1res.dll => Service Pack 1 Messages => Needed to open Add/Remove Programs from the Control Panel.

xpsp2res.dll => Service Pack 2 Messages => Needed to boot to Windows.

zipfldr.dll => Compressed (zipped) Folders => Needed to package files in Compressed (zipped) form.This is a list of files that reside in the &#8220;C:\Windows\System32&#8221; directory (NOTE: Many of these are from XP):

acctres.dll => Microsoft Internet Account Manager Resources => Needed to open Outlook Express. If you do not want users to be able to use Outlook Express, it is an easy way to delete this file.

aclui.dll => Security Descriptor Editor => Needed to enable Registry Editor.

activeds.dll => ADs Router Layer DLL => Needed to open the Event viewer and Services Viewer.

actxprxy.dll => ActiveX Interface Marshaling Library => Essential to Internet Explorer. This DLL keeps track on Active X modules.

advapi32.dll => Advanced Windows 32 Base API => Needed to boot to Windows. Provides access to the fundamental resources available to a Windows system. Included are things like file systems, devices, processes and threads, access to the Windows registry, and error handling.

advpack.dll => Advpack Library => Needed by Microsoft Update. This DLL builds up the Windows Update menu and accesses the updates list in the registry.

apphelp.dll => Application Compatibility Client Library => This DLL came with service pack 3 and it enables the Microsoft management console to work.

asycfilt.dll => Allows applications to communicate between each other using Object Linking and Embedding (OLE).

atl.dll => ATL Module for Windows XP (Unicode) => Needed by Microsoft Update. Also needed to open Event and Services Viewers. And needed by Outlook Express. Without this file Outlook Express will not open. You will receive this message when you click on the Outlook Express shortcut: Outlook Express could not be started because MSOE.DLL could not be found. Outlook Express may not be installed correctly.

attrib.exe => Attribute Utility => Displays or changes file attributes (read-only, archive, hidden, or system).

audiosrv.dll => Windows Audio Service => Needed to hear sound on your computer. Main Service file for Windows Audio.

authz.dll => Authorization Framework => Needed to boot to Windows.

autochk.exe => Auto Check Disk => Needed to boot to Windows. Launches automatically during Windows XP bootup if a volume is marked with bad clusters, error blocks, or otherwise damaged.

avifil32.dll => Microsoft AVI File support library.

basesvr.dll => Windows NT BASE API Server DLL => Needed to boot to Windows.

batmeter.dll => Battery Meter Helper DLL => Power Options in Control Panel.

bootvid.dll => VGA Boot Driver => Needed to boot to Windows.

browselc.dll => Shell Browser UI Library => IE Toolbar will look messed up without it, and you cannot right-click access &#8220;Customize&#8221; without it.

browseui.dll => Shell Browser UI Library => Needed to boot to Windows.

cabinet.dll => Microsoft® Cabinet File API => Microsoft Update. Also needed to access Properties of Devices in Device Manager.

cabview.dll => Cabinet File Viewer Shell Extension => Needed to view inside .cab files.

cdm.dll => Windows Update CDM Stub.

certcli.dll => Microsoft® Certificate Services Client => Display Properties of devices in Device Manager.

cfgmgr32.dll => Configuration Manager Forwarder DLL => Part of CHKDSK.

chkdsk.exe => Check Disk => Part of CHKDSK. A disk inspection tool that can search for and repair disk errors.

clb.dll => Column List Box => Needed to open Registry Editor.

clusapi.dll => Cluster API Library => Needed to access Disk Management in Computer Management. Also needed by Microsoft Update to install February 20, 2006 update for Windows Media Player 10. An application programming interface (API) is the interface that a computer system, library or application provides in order to allow requests for service to be made of it by other computer programs, and/or to allow data to be exchanged between them.

cmd.exe => Command Prompt => Enables execute of a batch file. An executable that provides the command prompt (MS-DOS shell interpreter) for Windows NT.

comctl32.dll => Common Controls Library => Needed to boot to Windows. Provides the functionality to create and manage screen windows and most basic controls, such as buttons and scrollbars, receive mouse and keyboard input, and other functionality associated with the GUI part of Windows. Gives applications access to some advanced controls provided by the operating system. These include things like status bars, progress bars, toolbars and tabs.

comdlg32.dll => Common Dialogs DLL => Needed to boot to Windows. Provides applications the standard dialog boxes for opening and saving files, choosing color and font, etc.

corpol.dll => Microsoft COM Runtime Execution Engine => Microsoft Update.

crypt32.dll => Crypto API32 => Needed to boot to Windows.

cryptdll.dll => Cryptography Manager => Needed to boot to Windows.

cryptsvc.dll => Cryptographic Services => Cryptographic Services, which is needed by Microsoft Update. Also needed to access Properties of Disk Drives.

cryptui.dll => Microsoft Trust UI Provider => Needed to boot to Windows.

csrsrv.dll => Client Server Runtime Process => Needed to boot to Windows.

csrss.exe => Client-Server Runtime Server Subsystem => Needed to boot to Windows. Used to maintain the Win32 system environment console and other essential functions.

d3d8thk.dll => Microsoft Direct3D OS Thunk Layer => Needed by ConvertXtoDVD.

d3d9.dll => Microsoft Direct3D => If you update to NVIDIA display drivers version 93.71, the d3d9.dll is used by NVIDIA so that you can manually adjust Brightness, Contrast, Gamma and Image sharpening in Display Properties => Settings => Advanced => NVIDIA Unknown (or your designated graphics card, depending upon whether or not you've chosen to delete the nvapi.dll) => select Color Correction => under &#8220;Apply color changes to:&#8221; click on the drop arrow to the right of the box and select &#8220;Overlay&#8221;.

dbghelp.dll => Windows Image Helper => Windows Media Player 11. Without it, when you click on something to play, a message tells you to re-install Windows Media Player. Also needed to install WMP11.

dciman32.dll => DCI Manager => Websites with streaming media.

ddraw.dll => Microsoft DirectDraw => DVD Playback with Windows Media Player and NVDVD Player.

ddrawex.dll => Direct Draw Ex

desk.cpl => Desktop Control Panel => Display Properties Control Panel applet.

devenum.dll => Device enumeration => Needed by Windows Media Player and NVDVD Player.

devmgmt.msc => Computer Management Console => Needed to access Device Manager.

devmgr.dll => Device Manager MMC Snapin => Needed to access Device Manager.

dhcpcsvc.dll => DHCP Client Service => Needed for Internet connectivity. Main Service file for DHCP Client.

dinput.dll => Microsoft DirectInput => Needed by ffdshow.

dmocx.dll => TreeView OCX => Needed to access Device Manager.

dnsapi.dll => DNS Client API DLL Needed to boot into Windows.

dolbyhph.dll => Dolby Headphone Engine => Installed and needed by NVDVD Player.

dpcdll.dll => Dpcdll Module => Needed to boot to Windows. Product Code activation.

dsound.dll => DirectSound => Needed by Windows Media Player and NVDVD Player.

dssenh.dll => Microsoft Enhanced DSS and Diffie-Hellman Cryptographic Provider => Needed by Internet Explorer. Also needed by Microsoft Update.

duser.dll => Windows DirectUser Engine => Needed by Add/Remove Module. Also, if you delete this file Windows will display the classic logoff and logon prompts. However, you can boot to Windows without it.

dxtmsft.dll => DirectX Media => Image DirectX Transforms

dxtrans.dll => DirectX Media => DirectX Transform Core

els.dll => Event Viewer Snapin => Needed by Event Viewer.

esent.dll => Server Database Storage Engine => Microsoft Update. Also needed to access Properties of Disk Drives.

eventlog.dll => Event Logging Service => Needed by Event Viewer. Without this file present it will take a very long time for your system to boot to Windows.

eventvwr.exe => Event Viewer Microsoft Management Console => Needed by Event Viewer. Main Service file for Event Log.

eventvwr.msc => Event Viewer Microsoft Management Console => Needed by Event Viewer.

filemgmt.dll => Services and Shared Folders => Needed by Services Viewer.

fmifs.dll => FM IFS Utility DLL => Part of CHKDSK.

fntcache.dat => Font Cache => If deleted, Windows will rebuild a new FNTCACHE.DAT the next time you reboot your system. If you use SVS or SWV, and you copied fonts from a layer to the base, delete this file. Next boot it will be rebuilded and that solves a lot of the fonts problems. (Added to DinamiQs software to keep fonts in the layers without the need to rebuild everytime)

fontext.dll => Windows Font Folder => Needed to maintain selected view of Font Folder, and also needed to display the default icon for .TTF Fonts

framebuf.dll => Framebuffer Display Driver => Needed so graphics in Safe Mode don't look all screwed up.

gdi32.dll => GDI Client DLL => Needed to boot to Windows. Provides the functionality for outputting graphical content to monitors, printers and other output devices.

grpconv.exe => Group Convert => Needed for some programs to install. Converts Microsoft Windows 3.x and Microsoft Windows for Workgroups Program Manager groups into Start Menu items.

hal.dll => Hardware Abstraction Layer => Needed to boot to Windows.

hccoin.dll => USB Coinstaller => Needed by Intel Chipset INF Update Utility.

hid.dll => Hid User Library => Needed by Sound and Video Card driver installations. HID stands for Human Interface Device, a type of computer device that interacts directly with and takes input from humans.

html.iec => Microsoft HTML Converter => Needed to be able to copy text from a Webpage and paste it to Wordpad.

icmp.dll => ICMP DLL => Needed in order to install the PCPitStop Utility for computer checkup and diagnostics on the PC Pitstop Website. Also needed by TCPOptimizer. ICMP (Internet Control Message Protocol) is used when networking. It ensures the integrity of information being sent across a network.

ieframe.dll => Internet Explorer => Essential to Internet Explorer 7. (Installed by Internet Explorer 7.)

ieframe.dll.mui => Internet Explorer => Needed by Internet Explorer 7 Toolbar. (Installed by Internet Explorer 7.)

iepeers.dll => Internet Explorer Peer Objects => Needed to watch Yahoo Movie Trailers.

iertutil.dll => Run time utility for Internet Explorer => Needed to start explorer.exe with Internet Explorer 7 installed on your system. The explorer.exe (located in the C:\Windows folder), manages the Windows Graphical Shell including the Start Menu, Taskbar, Desktop, and File Manager. Without it running, the graphical interface for Windows will disappear. (The iertutil.dll is installed by Internet Explorer 7.)

ieui.dll => Internet Explorer UI Engine => Essential to Internet Explorer 7. (Installed by Internet Explorer 7.)

ifsutil.dll => IFS Utility DLL => Part of CHKDSK.

imagehlp.dll => Windows NT Image Helper => Needed to boot to Windows.

imgutil.dll => IE plugin image decoder support DLL => Belongs to Internet Explorer => Needed so you don't see red x's in place of some images.

imm32.dll => Windows XP IMM32 API Client DLL => You cannot enter System Properties without the imm32.dll or the usp10.dll present.

inetcomm.dll => Microsoft Internet Messaging API => Without this file Outlook Express will not open. You will receive this message when you click on the Outlook Express shortcut: Outlook Express could not be started because MSOE.DLL could not be found. Outlook Express may not be installed correctly. Additionally, the inetcomm.dll is needed in order to save a Webpage as an offline Webpage with an .mht extension. Also needed to save an offline Webpage with an .mht extension are the inetres.dll and the MSOERT2.DLL (Outlook Express files), and the MSHTML.TLB (Internet Explorer file).

inetcpl.cpl => Internet Control Panel => Internet Options Control Panel applet.

inetcplc.dll => Internet Control Panel => Needed to access Internet Options.

inetres.dll => Microsoft Internet Messaging API Resources => Without this file Outlook Express will not open. You will receive this message when you click on the Outlook Express shortcut: Outlook Express could not be started because MSOERES.DLL could not be found. Outlook Express may not be installed correctly. Additionally, the inetres.dll is needed in order to save a Webpage as an offline Webpage with an .mht extension. Also needed to save an offline Webpage with an .mht extension are the inetcomm.dll and the MSOERT2.DLL (Outlook Express files), and the MSHTML.TLB (Internet Explorer file).

iphlpapi.dll => IP Helper API => Needed to boot to Windows.

iuengine.dll => Windows Update Control Engine => Needed by Microsoft Update.

jscript.dll => Microsoft ® JScript => Needed by Microsoft Update. Also needed by Services Viewer.

kbdus.dll => United States Keyboard Layout => Needed to boot to Windows. You may need a different KBD*.DLL depending on your system.

kdcom.dll => Kernel Debugger HW Extension DLL => Needed to boot to Windows.

kernel32.dll => Windows NT BASE API Client DLL => Needed to boot to Windows. Provides access to the fundamental resources available to a Windows system. Included are things like file systems, devices, processes and threads, access to the Windows registry, and error handling.

ksproxy.ax => Installed by Sound Card driver installations from either the XP installation CD, or a cab file in C:\WindowsDriver Cachei386. The installation will ask for the &#8220;ksuser.dll.&#8221; Once located, the &#8220;ksproxy.ax&#8221; will be installed along with the &#8220;ksuser.dll to C:\Windows\System32.

ksuser.dll => User CSA Library => Needed by Windows Media Player and NVDVD Player. Installed by Sound Card driver installations from either the XP installation CD, or a cab file in C:\WindowsDriver Cachei386. The installation will ask for the &#8220;ksuser.dll.&#8221; Once located, the &#8220;ksuser.dll&#8221; will be installed along with the &#8220;ksproxy.ax&#8221; to C:\Windows\System32.

l3codeca.acm => MPEG Layer-3 Audio Codec for MSACM => Needed by Windows Media Player to play .mp3 music files, and also needed to be able to rip music CDs to the .mp3 format.

l3codecp.acm => MPEG Audio Layer-3 Codec for MSACM => Needed by Windows Media Player to be able to rip music CDs to the .mp3 format.

legitcheckcontrol.dll => Windows Genuine Advantage Validation => Needed by Microsoft Update. This file is replaced once or twice a year to check for piracy key's

licdll.dll => Licdll Module => Needed by Windows Update.

logonui.exe => Windows Logon User Interface => The user interface that appears when Windows XP first starts => If you delete this file, Windows will display the classic logoff and logon prompts. However, you can boot up to Windows without it. With resourcehacker this executable can be customised to create custom ctrl-alt-del menu's

lsasrv.dll => LSA Server DLL => Needed to boot to Windows.

lsass.exe => LSA Security Service => Needed to boot to Windows. The Local Security Authority server process.

lz32.dll => LZ Expand/Compress API DLL => Needed to properly display the default icon for .ttf extension fonts.

mcicda.dll => MCI driver for cdaudio devices => Needed by Windows Media Player burning and ripping processes.

mfc42.dll => MFCDLL Shared Library => Retail Version

mfc42u.dll => MFCDLL Shared Library => Retail Version => Needed to open Event and Services Viewers. Needed to access Device Manager. And also needed by Wordpad.

mfplat.dll => Media Foundation Platform => To even open Windows Media Player 11.

mlang.dll => Multi Language Support DLL => Essential to Internet Explorer.

mmc.exe => Microsoft Management Console => Needed to open Event and Services Viewers. Also needed to access Device Manager.

mmcbase.dll => MMC Base DLL => Needed by Event and Services Viewers. Also needed to access Device Manager.

mmcndmgr.dll => MMC Node Manager DLL => Needed by Event and Services Viewers. Also needed to access Device Manager.

mpg4dmod.dll => Corona Windows Media MPEG-4 S Video Decoder => Needed to be able to adjust the brightness in Windows Media Player for certain videos.

mpr.dll => Multiple Provider Router DLL => Needed to boot to Windows.

mprapi.dll => Windows NT MP Router Administration DLL => After installing Internet Explorer 7, this file is one of five system32 files needed to open Internet Options: MPRAPI.DLL, msrating.dll, rasapi32.dll, rasdlg.dll and rasman.dll. Additionally needed to open Network Connections in Control Panel.

msacm32.dll => Microsoft ACM Audio Filter => Needed to open Audio tab in Sound and Audio Device properties. You cannot view or change multimedia properties without this file. Also needed to hear sound in Windows Pinball Game.

msacm32.drv => Microsoft Sound Mapper => Needed to hear sound in Windows Pinball Game.

msasn1.dll => ASN.1 Runtime APIs => Needed to boot to Windows.

msconfig.exe => System Configuration Utility => Designed to help you troubleshoot problems with your computer. MSCONFIG can also be used to ensure that your computer boots faster and crashes less => In PART 5 I moved msconfig.exe to the system32 folder from C:\Windowspchealthhelpctrbinaries before I deleted the pchealth folder and its contents.

msctfime.ime => Microsoft Text Frame Work Service IME => Installed with Internet Explorer 7 => If this file is not present your system could lockup while working at your Desktop.

msdmo.dll => DMO Runtime => Without the msdmo.dll present, Windows Media Player will not play&#8230;anything. Also, the msdmo.dll is very much needed by Websites with streaming media.

msdxm.ocx => Windows Media Player 2 ActiveX Control => Needed by too many Websites with streaming media to not keep this file installed on my system. The msdxm.ocx (DirectX file) and the wmpdxm.dll (Windows Media Player file) work together. The msdxm.ocx is also needed to start Media Player 6.4 (mplayer2.exe).

msftedit.dll => Rich Text Edit Control, v4.1 => Needed by Wordpad. Contains functions for the Rich Text Edit control version 4.1.

msgina.dll => Windows NT Logon GINA DLL => Needed to boot to Windows. Loads Logon User Interface.

mshtml.dll => Microsoft ® HTML Viewer => Needed by Internet Explorer.

mshtml.tlb => Microsoft ® MSHTML Typelib => Needed in order to save a Webpage as an offline Webpage with an .mht extension. Also needed to save an offline Webpage with an .mht extension are the inetcomm.dll, the inetres.dll and the MSOERT2.DLL (Outlook Express files).

mshtmled.dll => Microsoft ® HTML Editing Component => Gives you the ability to edit HTML. An example of this would be when you edit one of your posts on some forums. You wouldn't be able to do that without this file.

mshtmler.dll => Microsoft ® HTML Editing Component's Resource DLL => Needed to insert a picture in E-mail using Outlook Express.

msi.dll => Windows Installer => Needed by Windows Installer. Also needed by PerfectDisk 6. (PerfectDisk 8 does not need the MSI.DLL.)

msident.dll => Microsoft Identity Manager => Needed by Outlook Express.

msidle.dll => User Idle Monitor => Needed by Microsoft Update.

msidntld.dll => Microsoft Identity Manager => Needed by Outlook Express.

msiexec.exe => Windows Installer => Main Service File for Windows Installer. Windows Installer uses the information within .MSI files that are provided with some applications, and installs, repairs, or removes software using this information. Note: You can view these .MSI (Windows Installer File) files within the C:\WindowsInstaller folder.

msihnd.dll => Needed by Windows Installer.

msimg32.dll => GDIEXT Client DLL => Without this file present, upon booting to Windows, you will need to click OK on a Logon Message in order to enter Windows.

msisip.dll => MSI Signature SIP Provider => Windows Installer file. SIP stands for Session Initiation Protocol.

msls31.dll => Microsoft Line Services library file => Essential to Internet Explorer.

msoeacct.dll => Microsoft Internet Account Manager => Needed by Outlook Express.

msoert2.dll => Microsoft Outlook Express RT Lib => Needed by Outlook Express. Additionally, the MSOERT2.DLL is needed in order to save a Webpage as an offline Webpage with an .mht extension. Also needed to save an offline Webpage with an .mht extension are the inetcomm.dll and the inetres.dll (Outlook Express files), and the MSHTML.TLB (Internet Explorer file).

mspaint.exe => Microsoft Paint => A basic graphics creation and viewing tool.

mspatcha.dll => Microsoft® Patch Engine => Needed by Microsoft Update.

msprivs.dll => Microsoft Privilege Translations => Needed to boot to Windows.

msrating.dll => Internet Ratings and Local User Management DLL => After installing Internet Explorer 7, this file is one of five system32 files needed to open Internet Options: MPRAPI.DLL, msrating.dll, rasapi32.dll, rasdlg.dll and rasman.dll.

msv1_0.dll => Microsoft Authentication Package v1.0 => Needed to boot to Windows.

msvbvm60.dll => Visual Basic Virtual Machine => Contains program code used to run programs that are written in the Visual Basic programming language. As one example, CCleaner, a very popular program needs this file.

msvcp60.dll => Microsoft ® C++ Runtime Library => Needed to boot to Windows.

msvcp71.dll => Microsoft® C++ Runtime Library => Installed by Acronis True Image 10.

msvcr71.dll => Microsoft® C Runtime Library => Installed by Acronis True Image 10.

msvcrt.dll => Windows NT CRT DLL => Needed to boot to Windows.

msvfw32.dll => Microsoft Video for Windows DLL => Needed to open Windows Media Player.

mswsock.dll => Microsoft Windows Sockets 2.0 Service Provider => Essential to Internet Explorer.

msxml3.dll => MSXML 3.0 SP 5 => Needed by Event and Services Viewers. Also needed to access Device Manager.

msxml3r.dll => XML Resources => Needed by Event and Services Viewers. Also needed to access Device Manager.

muweb.dll => Microsoft Update Web Control => Installed by Microsoft Update Software.

mydocs.dll => My Documents Folder UI => Needed to properly display the My Documents Icon.

ncobjapi.dll => Needed to boot to Windows.

nddeapi.dll => Network DDE Share Management APIs => Needed to boot to Windows.

netapi32.dll => Net Win32 API DLL => Needed to boot to Windows.

newdev.dll => Add Hardware Device Library => Needed by Sound and Video Card driver installations. I'm sure other hardware device driver installations need it too.

normaliz.dll => Unicode Normalization DLL => Needed to start explorer.exe with Internet Explorer 7 installed on your system. The explorer.exe (located in the C:\Windows folder), manages the Windows Graphical Shell including the Start Menu, Taskbar, Desktop, and File Manager. Without it running, the graphical interface for Windows will disappear. (The normaliz.dll is installed by Internet Explorer 7.)

notepad.exe => Notepad => Notepad text-editing utility.

ntdll.dll => NT Layer DLL => Needed to boot to Windows.

ntdsapi.dll => NT5DS Library => Needed to boot to Windows

ntoskrnl.exe => NT Kernel & System => Windows XP operating system Kernel => Needed to boot to Windows

nv4_disp.dll => NVIDIA Compatible Windows 2000 Display driver => Essential for Display Adapter. And needed to boot to Windows.

nvcod.dll => NVIDIA Driver Co-Installer

nvcpl.dll => NVIDIA Display Properties Extension

nvdisp.nvu => NVIDIA Extension

nvshell.dll => NVIDIA Desktop Explorer

nvudisp.exe => NVIDIA Uninstaller Utility => Needed by NVIDIA to uninstall older drivers before installing new drivers during the updating process.

occache.dll => Object Control Viewer => Needed to view icon for ActiveX objects in Downloaded Program Files. Otherwise the ActiveX objects show up as .ini files.

odbc32.dll => Microsoft Data Access => ODBC Driver Manager => Needed to boot to Windows.

odbcint.dll => Microsoft Data Access => ODBC Resources => Needed to boot to Windows.

ole32.dll => Microsoft OLE for Windows => Needed to boot to Windows.

oleacc.dll => Active Accessibility Core Component

oleaccrc.dll => Active Accessibility Resource DLL

oleaut32.dll => Needed to boot to Windows.

oledlg.dll => Microsoft Windows™ OLE 2.0 User Interface Support => Needed to open NVDVD Player. Also needed by Wordpad.

olepro32.dll => Needed to open NVDVD Player.

olethk32.dll => Microsoft OLE for Windows => Needed by Nero.

pdboot.exe => PerfectDisk Boot Time Defragmentation => Needed by PerfectDisk.

pidgen.dll => Pid3.0 generation => Needed by Microsoft Update. During Windows setup the pidgen.dll produces a PID (Product Identification) from the serial number entered.

pngfilt.dll => IE PNG plugin image decoder => Belongs to Internet Explorer => Needed so you don't see red x's in place of some images.

powrprof.dll => Power Profile Helper DLL => Along with the powercfg.cpl, needed to enter Power Options where you can adjust how you want your computer to power down. Without this file present, you will receive an error when opening Properties for your Keyboard. However, the Properties for Keyboard will eventually open.

profmap.dll => Userenv => Needed to boot to Windows.

psapi.dll => Process Status Helper => Needed to boot to Windows.

qasf.dll => DirectShow ASF Support => Needed to play WMA music files and WMV video files with Media Player Classic, a third-party media player. GASF stands for Advanced Systems Format (formerly Advanced Streaming Format), Microsoft's proprietary digital audio/digital video container format, especially meant for streaming media. The most common file types contained within an ASF file are Windows Media Audio (WMA) and Windows Media Video (WMV).

qdvd.dll => DirectShow DVD Playback Runtime => Needed For DVD Playback with Windows Media Player and NVDVD Player.

qmgr.dll => Background Intelligent Transfer Service => Needed by Microsoft Update. Main Service file for Background Intelligent Transfer.

rasdlg.dll => Remote Access Common Dialog API

rasman.dll => Remote Access Connection Manager

regapi.dll => Registry Configuration API => Needed to boot to Windows.

regsvr32.exe => Microsoft© Register Server => You can use the Regsvr32 tool (Regsvr32.exe) to Register and UnRegister object linking and embedding (OLE) controls such as dynamic-link library (DLL) or ActiveX Controls (OCX) files that are self-registerable.

riched20.dll => Rich Text Edit Control, v3.0 => Needed by Event Viewer. Contains functions for the Rich Text Edit control versions 2.0 and 3.0.

riched32.dll => Wrapper Dll for Richedit 1.0 => Needed by Event Viewer. Contains functions for the Rich Text Edit control version 1.0.

rpcrt3.dll => Remote Procedure Call Runtime => Needed to boot to Windows.

rpcss.dll => Distributed COM Services => Needed to boot to Windows. Main Service file for Remote Procedure Call (RPC).

rsaenh.dll => Microsoft Enhanced Cryptographic Provider => Needed to boot to Windows. The RSAENH.DLL is needed to accurately check license for Windows.

rshx32.dll => 1Security Shell Extension => The Rshx32.dll controls the Security tab in Properties of files and folders. (To be able to see the Security tab in XP Home Edition you must be in Safemode.)

rtutils.dll => Routing Utilities => Needed by Websites with streaming media.

rundll32.exe => Run DLL => Used to run DLL files from a command line.

runonce.exe => Run Once => Used to perform tasks as defined in the RunOnce Registry key.

samlib.dll => SAM Library DLL => Needed to boot to Windows.

samsrv.dll => SAM Server DLL => Needed to boot to Windows.

sc.exe => A tool to aid in developing services for Windows NT => Communicates with the Service Controller and installed services. The SC.exe retrieves and sets control information about Services.

scesrv.dll => Windows Security Configuration Editor Engine => Needed to boot to Windows.

schannel.dll => TLS / SSL Security Provider => Needed by Internet Explorer. Also needed by Microsoft Update.

secur32.dll => Security Support Provider Interface => Needed to boot to Windows.

sendmail.dll => Send Mail => The sendmail.dll is a library file used for sending mail via Websites.

services.exe => Services and Controller app => Needed to boot to Windows. Main Service file for Plug and Play.

services.msc => Services Viewer => Needed by Services Viewer.

setupapi.dll => Windows Setup API => Needed to boot to Windows.

sfc.dll => Windows File Protection => Needed by Microsoft Update.

sfc\_os.dll => Windows File Protection => You can boot to Windows without this file, but not without first having to click OK on an error that appears telling you the SFC\_OS.DLL cannot be found.

sfcfiles.dll => Windows 2000 System File Checker => Needed to display Properties button in Control Panel > Keyboard > Hardware without receiving an error.

shdoclc.dll => Shell Doc Object and Control Library => Needed to be able to access right-click options while right-clicking on a Webpage.

shdocvw.dll => Shell Doc Object and Control Library => Needed to boot to Windows.

shell32.dll => Windows Shell Common Dll => Needed to boot to Windows.

shellstyle.dll => Windows Shell Style Resource Dll => If you choose to use the Windows Classic theme, and delete the Themes folder and its contents, you will still need the shellstyle.dll that is in the system32 folder in order to gain access to the Add or Remove Programs panel.

shfolder.dll => Shell Folder Service => Needed by Microsoft Update.

shgina.dll => Windows Shell User Logon => Needed to restart your computer from your Desktop. Further, once you delete or move this file from the system32 folder=>even if you put it back=>you still won't be able to restart from your Desktop.

shimgvw.dll => Windows Picture and Fax Viewer => Needed to display saved image files.

shlwapi.dll => Shell Light-weight Utility Library => Needed to boot to Windows. Allows applications to access the functionality provided by the operating system shell, as well as change and enhance it.

shsvcs.dll => Windows Shell Services Dll => Main Service file for Shell Hardware Detection.

shutdown.exe => Remote Shutdown Tool => Allows shutdowns and restarts on local or remote PCs.

smss.exe => Windows NT Session Manager => Needed to boot to Windows. Used to establish the Windows XP environment during bootup.

snapapi.dll => Acronis Snapshot Dynamic Link Library => Installed by Acronis True Image.

sndvol32.exe => Volume Control => A GUI (Graphical User Interface) volume application.

stdole2.tlb => Microsoft OLE 3.50 for Windows NT™ and Windows 95™ Operating Systems => After deleting the stdole2.tlb and rebooting your system, you may be unable to launch the Search Assistant.

stdole32.tlb => Microsoft OLE 2.1 for Windows NT™ Operating System => When you delete one or both the stdole32.tlb or the stdole2.tlb from the system32 folder, when installing a program that uses InstallShield, you may receive the following error message: The install Shield engine &#8220;ikernel.exe&#8221; could not be launched -Error loading type library /dll.

storprop.dll => Property Pages for Storage Devices => Needed to view Advanced Settings tab in Primary IDE Channel and Secondary IDE Channel under IDE ATA/ATAPI controllers in Device Manager.

svchost.exe => Generic Host Process for Win32 Service => Needed to boot to Windows.

sxs.dll => Fusion 2.5 => Needed to boot to Windows.

sysdm.cpl => System Applet for the Control Panel => System Properties Control Panel applet.

syssetup.dll => Windows NT System Setup => Needed to display Properties button in Control Panel > Keyboard > Hardware without receiving an error.

tapi32.dll => Microsoft® Windows™ Telephony API Client DLL => TAPI32.DLL is needed by streaming media on many sites.

taskmgr.exe => Task Manager => The Task Manager application.

themeui.dll => Windows Theme API => Needed by Display Properties.

timedate.cpl => Time Date Control Panel Applet => Date and Time Properties Control Panel applet.

ulib.dll => File Utilities Support DLL => Part of CHKDSK.

umpnpmgr.dll => User-mode Plug-and-Play Service => Needed to boot to Windows.

untfs.dll => NTFS Utility DLL => Part of CHKDSK.

url.dll => Internet Shortcut Shell Extension DLL => Displays default &#8220;e&#8221; icon for Internet Shortcuts and the one displayed in your Explorer Toolbar Address Bar.

urlmon.dll => OLE32 Extensions for Win32 => Essential to Internet Explorer.

usbui.dll => USB UI Dll => Needed to display Advanced tab in USB Universal Host Controller Properties, and Power tab in USB Root Hub Properties in Device Manager.

user32.dll => Windows XP USER API Client DLL => Needed to boot to Windows.

userenv.dll => Userenv => Needed to boot to Windows.

userinit.exe => User Initialization => Needed to boot to Windows. Used to establish the operating environment for a user after logon.

usp10.dll => Unicode script processor => You cannot enter System Properties without the usp10.dll or the imm32.dll present.

uxtheme.dll => Microsoft UxTheme Library => Needed to boot to Windows. Main Service file for Themes.

vbscript.dll => Microsoft ® VBScript => Needed by some Websites with streaming media. Also needed by Yahoo Chat.

vdmdbg.dll => Needed to access Task Manager.

version.dll => Version Checking and File Installation Libraries => Needed to boot to Windows.

watchdog.sys => Watchdog Driver => Needed to boot to Windows.

wdmaud.drv => WDM Audio driver mapper => Needed by Windows Media Player. Also needed to hear sound in Windows Pinball Game.

webcheck.dll => Web Site Monitor => Needed by Microsoft Update. You will need the webcheck.dll to install the new Microsoft Update software.

win32k.sys => Multi-User Win32 Driver => Needed to boot to Windows.

winhttp.dll => Windows HTTP Services => Needed by Microsoft Update. In Vista this DLL is needed to open Wireless configuration dialogbox

wininet.dll => Internet Extensions for Win32 => Needed to boot to Windows. Internet Explorer file.

winlogon.exe => Windows NT Logon Application => Needed to boot to Windows. Windows logon manager. Handles the login and logout procedures. With resourcehacker this file can be altered to control logon procedures and to alter the tasks that it follows.

winmm.dll => MCI API DLL => Needed by Windows Media Player.

winscard.dll => Microsoft Smart Card API => Needed by Microsoft Update.

winspool.drv => Windows Spooler Driver.

winsrv.dll => Windows Server DLL => Needed to boot to Windows.

winsta.dll => Winstation Library => Needed to boot to Windows.

wintrust.dll => Microsoft Trust Verification APIs => Needed to boot to Windows.

wldap32.dll => Win32 LDAP API DLL => Needed to boot to Windows.

wlnotify.dll => Common DLL to receive Winlogon notifications => Needed by Microsoft Update.

wmadmod.dll => Windows Media Audio Decoder => Needed by Windows Media Player to play .WMA music files.

wmadmoe.dll => Windows Media Audio Encoder/Transcoder => Needed by Windows Media Player ripping process.

wmasf.dll => Windows Media ASF DLL => Needed by Windows Media Player.

wmi.dll => WMI DC and DP functionality) => Needed to access Device Manager.

wmnetmgr.dll => Windows Media Network Plugin Manager DLL => Needed to watch Yahoo Movie Trailers.

wmp.dll => Windows Media Player Core => Needed to open Windows Media Player.

wmpdxm.dll => Windows Media 6.4 Player Shim => Needed by too many Websites with streaming media to not keep this file installed on my system.

wmpeffects.dll => Windows Media Player Effects => Needed for visual effects while playing music with Windows Media Player 11.

wmploc.dll => Windows Media Player => Needed to open Windows Media Player.

wmpps.dll => Windows Media Player Proxy Stub Dll => Needed to rip music CDs using Windows Media Player 11 with file-name information intact, such as the name of the artist, album, song title. Without the wmpps.dll file present, the file-name information it will read and write as &#8220;01 Unknown Artist Track 1&#8221;. Also needed to burn .WMA files to a CD using WMP11.

wmpshell.dll => Windows Media Player Launcher => Without the wmpshell.dll present WMP cannot remember that it's supposed to open your media files. The Open With dialog box will open instead, asking you to choose a program you want to use to open the file.

wmvcore.dll => Windows Media Playback/Authoring DLL => Needed to watch Yahoo Movie Trailers.

wmvdecod.dll => Windows Media Video Decoder => Needed to watch MSNBC videos online, and to watch Yahoo Movie Trailers with Windows Media Player 11 installed on your system.

wpa.dbl => Windows Product Activation (WPA) => Needed to boot to Windows.

ws2_32.dll => Windows Socket 2.0 32-Bit DLL => Needed to boot to Windows.

ws2help.dll => Windows Socket 2.0 Helper for Windows NT => Needed to boot to Windows.

wshtcpip.dll => Windows Sockets Helper DLL => Essential to Internet Explorer

wsock32.dll => Windows Socket 32-Bit DLL => Needed for Internet Connectivity. Winsock (short for Windows Sockets) is a specification that defines how Windows network software should access network services, especially TCP/IP.

wtsapi32.dll => WTSAPI32.DLL (Windows Terminal Server SDK APIs) => Needed both to view the Automatic Updates tab in System Properties, and by Microsoft Update. Also needed to enter System Properties by right-clicking on My Computer and selecting Properties without receiving this error: This application has failed to start because WTSAPI32.DLL was not found. Re-installing the application may fix this. However, System Properties will open after clicking OK on the error message even without this file present.

wuaucpl.cpl => Automatic Updates Control Panel => Automatic Updates Control Panel applet => Needed by Microsoft Update.

wuapi.dll.mui => Windows Update Client API => Needed by Microsoft Update.

wuauclt.exe => Windows Update => An auto-update client => Needed by Microsoft Update.

wuauclt1.exe => Windows Update AutoUpdate Client => Needed by Microsoft Update.

wuaucpl.cpl => Automatic Updates Control Panel applet => Needed by Microsoft Update.

wuaucpl.cpl.mui => Automatic Updates Control Panel => Needed by Microsoft Update.

wuaueng.dll => Windows Update AutoUpdate Engine => Needed by Microsoft Update.

wuaueng.dll.mui => Windows Update Agent => Needed by Microsoft Update.

wuaueng1.dll => Windows Update AutoUpdate Engine => Needed by Microsoft Update.

wuauserv.dll => Windows Update AutoUpdate Service => Needed by Microsoft Update. Main Service file for Automatic Updates.

wucltui.dll => Windows Update Client UI Plugin => Needed by Microsoft Update.

wucltui.dll.mui => Windows Update Client UI Plugin => Needed by Microsoft Update.

wupdmgr.exe => Windows Update Manager for NT => Needed by Microsoft Update.

wups.dll => Windows Update client proxy stub => Needed by Microsoft Update.

wups2.dll => Windows Update client proxy stub 2 => Needed by Microsoft Update.

wuweb.dll => Windows Update Web Control => Needed by Microsoft Update.

xmllite.dll => Microsoft XmlLite Library => Needed by Internet Explorer 7 Toolbar. (Installed by Internet Explorer 7.)

xpsp1res.dll => Service Pack 1 Messages => Needed to open Add/Remove Programs from the Control Panel.

xpsp2res.dll => Service Pack 2 Messages => Needed to boot to Windows.

zipfldr.dll => Compressed (zipped) Folders => Needed to package files in Compressed (zipped) form.