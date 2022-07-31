---
title: Google Sheets Formulas
date: 2022-05-16T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/05/google-sheets-formulas/
categories:
  - WebSoftware
tags:
  - Tweaks
---
<!--more-->

### Description:

Let me start by saying I'm not an Excel/Sheets guru by any means. This post is just for reference for things I have done with Google Sheets so I can search on my blog if I forget :)

### To Resolve:

1. Creating an `if` statement. In this case `if month is January, take the values of (J25+$G2) and subtract 12000, else don't subtract 12000`:

   - `=IF(MONTH(A26)=1,((J25+$G$2)-12000),(J25+$G$2))`

   - Same logic but for `year` instead :

   - `=IF(YEAR(A26)=2025, (F26-700), F26-1430)`


1. Here is a multiple `ifs` statement similar to a `switch` or `case` statement in other languages:

   `=IFS(MONTH(K17)=1,(1000), MONTH(K17)=2,(2000), MONTH(K17)=3,(3000), MONTH(K17)=4,(4000), MONTH(K17)=5,(5000), MONTH(K17)=6,(6000), MONTH(K17)=7,(7000), MONTH(K17)=8,(8000), MONTH(K17)=9,(9000), MONTH(K17)=10,(10000), MONTH(K17)=11,(11000), MONTH(K17)=12,(12000) )`

   - It is basically saying, `give me the value of the month in K17 and I will set my cell to whatever the lookup is. So 1 = 1000, 3 = 3000, ect.`

1. To reference another sheets cell, you just use `=MySheet1!J16` for example.

1. If you want to reference a cell's value all the way down a column, you must do an absolute reference instead of a regular reference:

   - Regular: `=D8+C4`

   - Absolute: `=D8+$C$4`

1. To create a column with dates that are one month from today, just use the formula: `=EDATE(A28,1)` where `A28` is `=TODAY()`. The EDATE function will just add the number of months in second parameter.

1. For compound interest, I usually do something like : `=((D54+E54)*H54)+D54+E54` if the D column is an initial balance, the E column is a yearly add balance, and the H column is the interest like .07 for example.

   - So if `D54` was `21,779.79`, `E54` was `600`, and `H54` was `.07` I would:
   - Put this formula in `D55` and set the formula above. It would go in this order:
   - 1: Add 21,779.79 + 600
   - 2: Take that result (22,379.79) and multiply it by the interest rate, .07 = 1566.58
   - 3: The value from previous step is the amount of compound interest gained for the year. You then just add it to the first step once again to get your final result:
   - 4: 1,566.58 + 22,379.79 = 23,946.37
   - 5: The real power of this is you can drag the formula down over the years and see the interest gaining interest as the name implies, compound interest.

1. In addition to formulas, I have found that conditional formatting is super helpful as well. You can set all sorts of `if` statements there as well:

   - If the `date` in this column is before today, make it yellow and faded.
   - If the `value` in this column is above `2800`, mark it red.
   - If the value starts with `2021` mark it red. If for example you want to highlight a year or something.
   - Obviously tons of possibilities here.