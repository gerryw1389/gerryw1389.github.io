---
title: 'PS: Logic Statements And Loops'
date: 2016-05-30T05:57:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/ps-logic-statements-and-loops/
tags:
  - Windows
tags:
  - Powershell
---
<!--more-->

### Description:

This is a collection of PowerShell logic statements and loops.

### The If-Then Statement:

1. Setup:

   ```escape
   If (condition) {Do stuff}  
   # Another explanation would be  
   If (test) {  
   "Execute when true"  
   }
   ```

2. Example:

   ```powershell
   $Status=(Get-service -name bits).status
   If ($Status -eq "Running") {
   Clear-Host
   Write-Output "Service is being stopped"
   Stop-Service -name bits
   } Else {
   Clear-Host
   Write-Output "Service is already stopped"
   }
   ```

### The Switch Statement:

1. Setup:

   ```escape
   Switch (pipeline) {  
   Pattern 1 {Statement block}  
   Pattern 2 {Statement block}  
   Pattern n {Statement block}  
   }
   ```

2. Example:

   ```powershell
   Switch ($status) {
   0 { $status_text = 'ok' }
   1 { $status_text = 'error' }
   2 { $status_text = 'jammed' }
   3 { $status_text = 'overheated' }
   4 { $status_text = 'empty' }
   default { $status_text = 'unknown' }
   }
   ```

3. Another Example:

   ```powershell
   $status = 3
   $status_text = switch ($status) {
   0 { 'OK' }
   1 { 'overheating' }
   2 { 'jammed' }
   3 { 'empty' }
   default { 'unknown' }
   }
   $status_text
   ```

### The Do-Until Loop:

1. Setup:

   ```escape
   Do  
   {

   command_block

   } until (condition)

   NOTE: The logic of this loop is to execute the Do {block} until (the condition is true).
   ```

2. Example:

   ```powershell
   Clear-Host
   $strPassword ="123"
   $strQuit = "Not yet"
   Do {
   $Guess = Read-Host "`n Guess the Password"
   if($Guess -eq $StrPassword)
   {" Correct guess"; $strQuit ="n"}
   else{
   $strQuit = Read-Host " Wrong `n Do you want another guess? (Y/N)"
   }
   } # End of 'Do'
   Until ($strQuit -eq "N")
   "`n Ready to do more stuff..."
   ```

### The Do-While Loop:

1. Setup:

   ```escape
   Do  
   {

   command_block

   } while (condition)

   NOTE: The logic of Do-While is the opposite of the Do Until. {Execute the block statement} while the (condition is true)
   ```

2. Example:

   ```powershell
   $a = 1
   DO
   {
   "Starting Loop $a"
   $a
   $a++
   "Now `$a is $a"
   } While ($a -le 5)
   # Do loop
   $i= 1
   ```

### The ForEach Loop:

1. Setup:

   ```escape
   ForEach (item In collection) {ScriptBlock}
   ```

2. Example:

   ```powershell
   $services = Get-Service
   ForEach ($service in $services) {
   $service.Displayname
   }
   ```

### The For Loop:

1. Setup:

   ```escape
   for (init; condition; repeat)
   {command_block}
   ```

2. Examples:

   ```powershell
   # You can use carriage returns instead of semi-colons:
   for($i=1; $i -le 10; $i++){
   Write-Host $i
   }
   ```

### References:

["PowerShell Basics: Loops – Do… Until, Do…While"](http://www.computerperformance.co.uk/powershell/powershell_loops_do_while.htm)  