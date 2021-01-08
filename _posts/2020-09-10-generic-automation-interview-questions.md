---
title: Generic Automation Interview Questions
date: 2020-09-10T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/09/generic-automation-interview-questions
categories:
  - SysAdmin
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

Here are some interview questions we might ask for a candidate.

### To Resolve:

1. What automation tool you have been using for your last project? 

2. Tell me about a time you had multiple assignments with conflicting goals or deadlines, and how you completed each of them. 

3. How are Python arrays and Python lists different from each other? 
   - A: Looking for how arrays cannot be modified once declared

4. Describe a process you have automated. What were the steps? 

5. You write a function:  

   ```powershell
   Reboot-servers { 
      Invoke-Command -ComputerName 'computer1.domain.com' -ScriptBlock {  
         Restart-computer -Force 
      } 
      Invoke-Command -ComputerName 'computer2.domain.com' -ScriptBlock {  
         Restart-computer -Force 
      } 
   } 
   ```

   - And save it as the file `reboot-servers.ps1`. You then run it by typing `.\reboot-servers.ps1` but it does nothing. Why is that? 
   - Hint: Is there a way to confirm the commands were ran? 
   - A: You declared a function but never called it. 

6. When is an okay time to hard code passwords in scripts? 
   - A: Never 

7. How would you define a trigger in regards to automation? 
   - A: Looking for scheduled time => start script or "when $x happens, start this process" 

8. In regards to object oriented programming, what is an object? 
   - A: Looking for something regarding properties (characteristics) and methods (actions) 

9. What protocols are used to run scripts remotely for Windows and Linux? 
   - A: WSMan and SSH are most common nowadays.
   - Bonus: What ports?
     - WMAN: 5985/tcp 
     - WSMAN over HTTPS: 5986/tcp
     - SSH: 22/tcp 

 