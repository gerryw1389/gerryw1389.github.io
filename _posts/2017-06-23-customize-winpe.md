---
title: Customize WinPE
date: 2017-06-23T18:25:22+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/06/customize-winpe/
categories:
  - Windows
---
<!--more-->

### Description:

I have not actually done this, but I copied someones comment on a reddit thread the other day and wanted to post it here in case it ever gets lost. They describe making a master WinPE boot.wim and using that as the basis to create any drive. Here is an overview of how to do it.

### To Resolve:

1. Download and install the ADK. Use it to create the [WinPE working source directory](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-mount-and-customize) by using the following:

   ```powershell
   copype amd64 C:\WinPE_amd64
   ```

2. Mount and customize the image:

   ```powershell
   Dism /Mount-Image /ImageFile:"C:\WinPE_amd64\media\sources\boot.wim" /index:1 /MountDir:"C:\WinPE_amd64\mount"
   ```

3. Modify the `startnet.cmd` from the mounted directory:

   ```powershell
   C:\WinPE_amd64\mount\Windows\System32\Startnet.cmd
   ```

   - In this file, I use the following method. Basically, I search for an `Images` folder in the PE Images partition. Inside of that folder, I have a `start.cmd` file [which is called](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-identify-drive-letters) from the `startnet.cmd`. 

   - After you're finished, unmount the image:

   ```powershell
   Dism /Unmount-Image /MountDir:"C:\WinPE_amd64\mount" /commit
   ```

4. You can now create a `start.cmd` for your `Images` folder on the Images partition and call whatever you want there. I typically have to make a drive that covers several different types of models, so I'll write a script that has a menu with selection items in it.

5. [Create your USB drive](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-create-usb-bootable-drive)

   - Don't forget to add the `Images` folder in the Images partition. Put your `start.cmd` in that folder and call your menu or Dism image apply call (or whatever you want) from there.

   - Added Fun: Bonus cookie points if you replace the WinPE background with [your company background](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-mount-and-customize#addwallpaper)

   - Notes: Don't forget to set the [power configuration to High Performance in your startnet.cmd](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-mount-and-customize#highperformance) (call this prior to calling your batch script start.cmd menu)

   - You can have better resolution in WinPE by using an `unattend.xml` file.

   - TLDR: Basically, I use `startnet.cmd` to call a `start.cmd` in an `Images` folder on the PE Images partition. That way I can automate things easily and can re-work this single `start.cmd` script in the future for any applicable image or process needed, as opposed to having to edit the `boot.wim` and change the `startnet.cmd` contents.

   - While the image is mounted, you may want to try the following PS commands:

6. To Remove images:

   ```powershell
   #Remove image indexes for Ent N, Pro/Pro N, and Edu/Edu N
   for ($i = 6; $i -ge 1; $i--) 
   {
      if ($i -eq 3) 
      {
         continue
      }
      else
      {
         Remove-WindowsImage -ImagePath $ImageFilename -Index $i
      }
   }
   ```

7. To Extract all but one image

   ```powershell
   Dism /Mount-Image /ImageFile:"D:\sources\install.wim" /index:1 /MountDir:"C:\temp\mount"
   dism /export-image /SourceImageFile:D:\sources\install.wim /SourceIndex:3 /DestinationImageFile:C:\W10\install.wim /Compress:max /CheckIntegrity
   ```

