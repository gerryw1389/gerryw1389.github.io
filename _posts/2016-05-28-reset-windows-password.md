---
title: Reset Windows Password
date: 2016-05-28T06:28:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/reset-windows-password/
tags:
  - Windows
tags:
  - Regedit
---
<!--more-->

### Description:

Sometimes, you will be locked out of an account due to not knowing the password, here are some things to try:


### Preferred Method - Native Windows:

1. Boot from the Windows 10 DVD. Make sure that your PC setup is configured to boot from a DVD and that UEFI and Secure Boot are disabled.

2. At some point in the beginning of the wizard, Press `SHIFT + F10` to open a command prompt.

3. Replace the file `utilman.exe` with `cmd.exe`. Before you do this, you should make a copy of `utilman.exe` so that you can restore it later. Note that you can only restore this file if you boot again from the Windows DVD. Windows 10 is usually installed on drive D: if you boot from a DVD. You can verify this with `dir d:\windows\system32\utilman.exe` If the system can't find `utilman.exe`, try other drive letters.

   ```powershell
   move d:\windows\system32\utilman.exe d:\windows\system32\utilman.exe.bak
   copy d:\windows\system32\cmd.exe d:\windows\system32\utilman.exe
   ```

4. After you have replaced `utilman.exe` successfully, you can remove the DVD and restart your problematic Windows 10 installation:

5. On the Windows 10 sign-in page, click the Utility Manager icon. Since we replaced the Utility Manager with the `cmd.exe`, a command prompt should open now. Don't worry about the error message. You can now add a new user with the commands below. Here we are creating a new user and adding to the administrators group.

   ```powershell
   net user (username) (password) /add
   net localgroup administrators (username) /add
   ```

6. Click the screen to make the sign-in page appear again. Your new account should show up, and you can sign in without a password.

   - NOTE: You will obviously want to do seps 1-3 again but putting files back where they belong.

### Hirens Boot CD

1. Download the ISO image of Hiren's BootCD from its official website (about 593 MB). Burn the ISO file to your CD (or USB stick) using the freeware ISO2Disc.

2. After getting Hiren's BootCD ready, Boot your Windows 10 computer from CD (Change boot order on BIOS to set CD/DVD-ROM as the first boot device). Remember to change UEFI boot with Legacy and disable Secure Boot temporarily in BIOS.

3. You will be prompted with the Hiren's CD Menu, from there select Offline NT/2000/XP/Vista/7 Password Changer and press Enter. Don't use Kon-Boot as it doesn't support Windows 10/8 password bypass.

4. Hit Enter when you see the boot prompt.

5. The screen will list all your partitions and you need to select the partition where Windows is installed. It's usually the larger one. Type 2 and press Enter.

6. Now it will ask to confirm the registry path (Windows/System32/config). The default registry path will be correct so just press Enter.

7. We're going to reset forgotten Windows password, so choose the default choice Password reset [sam system security] by pressing Enter.

8. Choose the default choice Edit user data and passwords and press Enter again.

9. You will now see the user accounts on you computer. Type the username whose password you want to change and press Enter.

   - Type 1 and press Enter. This will clear/remove the password of your selected account.
   - Now type ! And hit Enter to quit the User Editor menu.
   - Enter q to exit chntpw Main Interactive Menu and press Enter.

10. Important step! Here must type y so it saves your password reset changes!

### Sticky Keys Trick:

1. Boot from Windows PE or Windows RE and access the command prompt. NOTE: You can also boot to any Linux Live CD and access a Windows system.

2. Find the drive letter of the partition where Windows is installed. In Vista and Windows XP, it is usually C:, in Windows 7, it is D: in most cases because the first partition contains Startup Repair. To find the drive letter, type C: (or D:, respectively) and search for the Windows folder. Note that Windows PE (RE) usually resides on X:.

3. Type the following command (replace "c:" with the correct drive letter if Windows is not located on C:):

   - Type: `copy c:\windows\system32\sethc.exe c:\` (This creates a copy of `sethc.exe` to restore later.)

4. Type this command to replace `sethc.exe` with `cmd.exe`:

   - Type: `copy /y c:\windows\system32\cmd.exe c:\windows\system32\sethc.exe`

5. Reboot your computer and start the Windows installation where you forgot the administrator password.

6. After you see the logon screen, press the SHIFT key five times.

7. You should see a command prompt where you can enter the following command to reset the Windows password:

   - Type: `net user gerry pa$$w0rd /add` and then `net user localgroup administrators gerry /add`

8. After you login and do whatever you need to do it's advised to:

9. Replace `sethc.exe` with the copy you stored in the root folder of your system drive in step 3. For this, you have to boot up again with Windows PE or RE because you can't replace system files while the Windows installation is online. Then you have to enter this command:

   -Type: `copy /y c:\sethc.exe c:\windows\system32\sethc.exe`

10. Either delete the newly created account or hide it from the login/Control Panel users by:

   - Run => `regedit` => Navigate to: `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList` 
   - Create the subkeys if they are not there.
   - In that directory, right click => New DWORD (32 bit) => Name it the name of your user account and set its value to `0`.
   - Reboot for it to apply as with any reg trick.
