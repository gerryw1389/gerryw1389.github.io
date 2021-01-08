---
title: 'Common Workflow: Get Email Addresses For All Users On A Share'
date: 2018-11-22T07:03:04+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/11/common-workflow-get-email-addresses-for-all-users-on-a-share/
categories:
  - SysAdmin
tags:
  - Scripting-Powershell
  - ActiveDirectory
---
<!--more-->

### Description:

For example, we want to get the emails for all users who access shares on a file server.

### To Resolve:

1. First, remote into the file server and run the following:

   ```powershell
   Get-ChildItem e: -Recurse |
   Where-Object { $_.psiscontainer } |
   Get-Acl |
   Select-Object @{Name='Path';Expression={Convert -Path $_.Path}},Owner,AccessToString |
   out-file c:\scripts\shares.csv
   ```

2. Now copy that CSV locally and open it up.

   <img class="alignnone size-full wp-image-5590" src="https://automationadmin.com/assets/images/uploads/2018/11/groups-1.jpg" alt="" width="748" height="729" srcset="https://automationadmin.com/assets/images/uploads/2018/11/groups-1.jpg 748w, https://automationadmin.com/assets/images/uploads/2018/11/groups-1-300x292.jpg 300w" sizes="(max-width: 748px) 100vw, 748px" /> 

3. Use Excel's &#8220;Text to columns&#8221; feature on the Data tab in the ribbon to convert the text to columns.

4. Paste the &#8220;Owner&#8221; column into [dedupelist.com](http://www.dedupelist.com)  

5. Take those results and copy to notepad++

6. Press Ctrl+H and choose "Regular expression" in the replace dialog. We then do the following to replace the first character with a single quote and the last characters as a single quote and a comma. This is so essentially building an array in powershell.

   ```escape
   Find: $  
   Replace: ',  
   # Replace all  
   
   Find: ^  
   Replace: '  
   # Replace all
   ```

   - This part takes discretion and sometimes you might have other data you need to remove. For example, I had to switch to regular find/replace and remove `domainName\` from each line, just replace with `(blank)` <- Don't type anything and then click "Replace all" in normal find/replace mode.

   - Now on line one, just type: `$users = @(` and press enter:

   <img class="alignnone size-full wp-image-5591" src="https://automationadmin.com/assets/images/uploads/2018/11/groups-2.jpg" alt="" width="452" height="521" srcset="https://automationadmin.com/assets/images/uploads/2018/11/groups-2.jpg 452w, https://automationadmin.com/assets/images/uploads/2018/11/groups-2-260x300.jpg 260w" sizes="(max-width: 452px) 100vw, 452px" /> 

   - Now go to the last line and delete the comma and place a closing parenthesis to close the array.

   <img class="alignnone size-full wp-image-5592" src="https://automationadmin.com/assets/images/uploads/2018/11/groups-3.jpg" alt="" width="293" height="383" srcset="https://automationadmin.com/assets/images/uploads/2018/11/groups-3.jpg 293w, https://automationadmin.com/assets/images/uploads/2018/11/groups-3-230x300.jpg 230w" sizes="(max-width: 293px) 100vw, 293px" /> 

7. Now that you have an array, you can do just about anything you need to do. For example:

   ```powershell
   Import-Module activedirectory
   $UserArray = [System.Collections.Generic.List[PSObject]]@()
   $EmailArray = [System.Collections.Generic.List[PSObject]]@()
   ForEach ($u in $users)
   {
   $User = Get-ADUser -Identity $u
   [void]$UserArray.Add($($User.Name))
   [void]$EmailArray.Add($($user.UserPrincipalName))
   }
   ```

   - This will import AD module and initialize two new arrays. It will then loop through each member in the first array and pull their username and email and put them in different arrays. You can then take $EmailArray and export it to CSV or something. Or just copy and paste the results from the screen into an email.

8. Many tasks will follow this same workflow so remember it!