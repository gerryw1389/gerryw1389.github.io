---
title: 'PS: Send Me My Credit Balance'
date: 2018-02-24T08:01:52+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/02/ps-send-me-my-credit-balance/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

I'm finally at a point with Powershell that I can write scripts that take longer than a day to complete. 

1. I recently created a script that:

   - Parses my Gmail every day for an automated message from my bank with my credit balance.
   - Takes the current balance and determines, based on my monthly bills, what my budget should be until the next payday.
   - The script also calculates all my paydays for the rest of the year and tells me how long until the next one.
   - The script also sends a text message with just the &#8220;Budget before payday&#8221; amount

2. How it works:
   - Section 1: Get the current balance of my credit cards from credit balance alerts sent to me from my bank daily  
   - Section 2: Generate all paydays for the year  
   - Section 3: Add in recurring bills.  
   - Section 4: Send email with all these results  
   - Section 5: Clean up

3. Overview:  
   - This script will take today's date, along with your current balance, and calculate in future bills and send you an email daily with how much you have left over until the next payday. For example, if today is the 20th: It will take today's current balance, say $1000 which is derived from both my credit cards and add in $473. The $473 comes from bills that will be charged automatically before my next payday. The script adjusts day by day until it finally gets to adding $0 amounts (because you have no bills left to pay and you pay your credit cards off, thus restarting the cycle). What's neat is you can hard code a budget. I use $2400 but you may use whatever you see fit. Anyways, it takes your budget, $2400 and removes your current balance + future bills and sends you THAT amount daily. This is good because it tells my wife and I when we can afford to splurge and when to cut back.

4. This is what it ends up looking like (Script is maintained [here](https://github.com/gerryw1389/powershell/blob/main/gwMisc/Public/Send-CreditBalance.ps1)):

   <img class="alignnone size-full wp-image-4994" src="https://automationadmin.com/assets/images/uploads/2018/02/credit-card.png" alt="" width="310" height="628" srcset="https://automationadmin.com/assets/images/uploads/2018/02/credit-card.png 310w, https://automationadmin.com/assets/images/uploads/2018/02/credit-card-148x300.png 148w" sizes="(max-width: 310px) 100vw, 310px" /> 

5. Assumptions:  

   - You get an automated email with your &#8220;Available Credit&#8221; daily. This is not to be confused with your &#8220;balance&#8221; as the available credit will usually include pending charges. The script will subtract your &#8220;Total Available Credit&#8221; from that day's &#8220;Available Credit&#8221; to give a more accurate picture of your expenses. Please see lines 136 and 141 and adjust accordingly.

     - To be clear, all I'm saying is that if you have a credit card with a total credit limit of $10,000 and the script finds that your current available credit is $9000, it will add $1000 to to the $Results variable which is used later. That $1000 is your current charges that will be due on payday.

   - This was setup because I have two credit cards => one for spending and one for bills that gets charged monthly.  
   - I pay my bills on the fifth each month even though I get paid bi-weekly. You can easily modify this to do twice a month, that's how I had it setup initially.

6. Let's get started. 

### To Resolve:

1. Suppose I have these bills:

   ```powershell
   Due Date - Bill - Amount
   01 - Internet - $105
   06 - Groceries - $200
   13 - Groceries - $200
   14 - Hulu - $13
   16 - Water - $90
   16 - ATT Cell - $45
   20 - Groceries - $200
   24 - Netflix - $11
   27 - Electric - $166
   27 - Groceries - $200
   28 - Auto Ins - $176
   ```

   - Arrange your bills with the day you will pay them first, not by the order of the day in the month. The example above was just my initial list of all my bills, I break these down into the correct order in the next step. Do this because if you get an alert on the 30th but you don't pay bills until the fifth, you need to save for any bills that come before the fifth.

2. The first thing I did was put them in a table like so (notice that I break between distinct groups that will help my code logic later): Column setup should be:

   - Amount to be added (aggregated value of bills up until that day). So if it is the 16th, I will have to add: Groceries ($200), Groceries ($200), Hulu ($13), Water ($90), and ATT Cell ($45) to get a total of $547. I list 0548 only because I wanted my columns to line up, no other reason.

   - Amount that needs to be reserved for future bills => This starts with the total amount of all your bills and goes down as bills gets paid. It should be the same as column one but in reverse. So Total Bills => Column 1.

   - Day of month

   - What bill is added to my total

   ```powershell
   $0000 - $1421- 05 - nothing

   $0200 - $1221- 06 - groceries
   $0200 - $1221- 08 - groceries
   $0200 - $1221- 07 - groceries
   $0200 - $1221- 09 - groceries
   $0200 - $1221- 10 - groceries
   $0200 - $1221- 11 - groceries
   $0200 - $1221- 12 - groceries

   $0400 - $1021- 13 - groceries, groceries

   $0413 - $1008- 14 - groceries, groceries, hulu
   $0413 - $1008- 15 - groceries, groceries, hulu

   $0548 - $0873- 16 - groceries, groceries, hulu, water, att cell
   $0548 - $0873- 17 - groceries, groceries, hulu, water, att cell
   $0548 - $0873- 18 - groceries, groceries, hulu, water, att cell
   $0548 - $0873- 19 - groceries, groceries, hulu, water, att cell

   $0748 - $0673- 20 - groceries, groceries, groceries, hulu, water, att cell
   $0748 - $0673- 21 - groceries, groceries, groceries, hulu, water, att cell
   $0748 - $0673- 22 - groceries, groceries, groceries, hulu, water, att cell
   $0748 - $0673- 23 - groceries, groceries, groceries, hulu, water, att cell

   $0759 - $0662- 24 - groceries, groceries, groceries, hulu, water, att cell, netflix
   $0759 - $0662- 25 - groceries, groceries, groceries, hulu, water, att cell, netflix
   $0759 - $0662- 26 - groceries, groceries, groceries, hulu, water, att cell, netflix

   $1140 - $0281- 27 - groceries, groceries, groceries, groceries, hulu, water, att cell, netflix, electric, plex

   $1316 - $0105- 28 - groceries, groceries, groceries, groceries, hulu, water, att cell, netflix, electric, plex, auto ins
   $1316 - $0105- 29 - groceries, groceries, groceries, groceries, hulu, water, att cell, netflix, electric, plex, auto ins
   $1316 - $0105- 30 - groceries, groceries, groceries, groceries, hulu, water, att cell, netflix, electric, plex, auto ins
   $1316 - $0105- 31 - groceries, groceries, groceries, groceries, hulu, water, att cell, netflix, electric, plex, auto ins

   $1421 - $0000- 01 - groceries, groceries, groceries, groceries, hulu, water, att cell, netflix, electric, plex, auto ins, internet
   $1421 - $0000- 02 - groceries, groceries, groceries, groceries, hulu, water, att cell, netflix, electric, plex, auto ins, internet
   $1421 - $0000- 03 - groceries, groceries, groceries, groceries, hulu, water, att cell, netflix, electric, plex, auto ins, internet
   $1421 - $0000- 04 - groceries, groceries, groceries, groceries, hulu, water, att cell, netflix, electric, plex, auto ins, internet
   ```

   - The main column we care about here is the second column. This tells us how much we need to save for future bills by referencing the day of the month until the next payday.

3. Now build the logic that if it is on this day (or range of days to make it easier), add this to my current balance using a If, ElseIf, Else construct:  

   - For example:

   ```powershell
   ElseIf (($DayofMonth -ge 16) -And ($DayofMonth -le 23))
   {
   	$ResultsWithBills = $Results + 473
   	$UpcomingBills = '24 - Netflix - $11<br>'
   	$UpcomingBills += '27 - Electric - $166<br>'
   	$UpcomingBills += '27 - Plex - $15<br>'
   	$UpcomingBills += '28 - Auto Ins. - $176'
   	$UpcomingBills += '1 - Internet - $105'
   }
   ```

   - This says that if today is between the 16th and the 23rd, take my current credit card balance and add 473 to it. This is because I haven't paid it since the fifth this month and I have this many bills currently charged ($Results) and this many bills (473) to be charged before I pay it again.

4. Now do this for each bracket that repeats in your table using a If, Elseif, Else construct. You will see a clear pattern and it will make sense.

