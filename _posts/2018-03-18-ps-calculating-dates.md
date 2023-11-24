---
title: 'PS: Calculating Dates'
date: 2018-03-18T16:04:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/ps-calculating-dates/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

It is common to need to compare dates or do date calculations in Powershell. The following is how I would go about it:

### To Resolve:

1. This is used in my [Credit Balance](https://automationadmin.com/2018/02/ps-send-me-my-credit-balance/) script:

   ```powershell
   # Generate all paydays for the year
   [DateTime] $StartDate = "2018-01-05"
   [Int]$DaysToSkip = 14
   [DateTime]$EndDate = "2018-12-31"
   $Arr = @()
   while ($StartDate -le $EndDate) 
   {
   $Arr += $StartDate 
   $StartDate = $StartDate.AddDays($DaysToSkip)
   }

   # Remove all paydays that have passed and place remaining in new array
   $NewArr = @()
   ForEach ($Ar in $Arr)
   {
      $s = (Get-Date)
      $e = $Ar
      $Difference = New-TimeSpan -Start $s -End $e
      If ( $Difference -ge 1)
      {
      $NewArr += $Ar
      }
   }

   # Select the first one
   $ClosestPayday = $NewArr[0].ToString("yyyy-MM-dd")

   # Calculate how many days from now until payday
   $Span = New-TimeSpan -Start (Get-Date) -End $NewArr[0]

   # Round up one because there is always a whole number and some change
   $DaysTilPayday = ($Span.Days + 1).ToString()
   ```

2. What do you do if you want to calculate a certain day of the month though? That doesn't always line up to every 30 days. Well, I did some research and this is how I would do &#8220;Calculate how many days until the 5th of the month:

   ```powershell
   $CurrentMonth = $((Get-Date).Month)
   $CurrentDay = $((Get-Date).Day)
   [datetime]$Date = Get-Date -Month $CurrentMonth -Day $CurrentDay
   $ThisFifth = Get-Date -Month $CurrentMonth -Day 5

   If ($CurrentMonth -eq 12)
   {
      $CurrentMonthPlusOne = 1
   }
   Else
   {
      $CurrentMonthPlusOne = $($Date.Month) + 1
   }
   [Datetime]$NextFifth = Get-Date -Month $CurrentMonthPlusOne -Day 5

   $CurrentYearPlusOne = $($Date.Year) + 1
   [Datetime]$NextFifthIfDecember = Get-Date -Month 1 -Day 5 -Year $CurrentYearPlusOne

   $Span = New-TimeSpan -Start $Date -End $ThisFifth
   If ($Span.Days.tostring().startswith('-'))
   {
      If ($CurrentMonth -eq 12)
      {
         $Span = New-TimeSpan -Start $Date -End $NextFifthIfDecember
      }
      Else
      {
         $Span = New-TimeSpan -Start $Date -End $NextFifth
      }

   }
   Else
   {
      If ($CurrentMonth -eq 12)
      {
         $Span = New-TimeSpan -Start $Date -End $NextFifthIfDecember
      }
      Else
      {
         # Do nothing as the date is already correct
      }
   }
   Write-Output "The fifth is $($Span.Days) days away!"
   ```

