---
title: 'MS Excel: Formatting Tasks'
date: 2016-08-20T04:22:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/ms-excel-formatting-tasks/
tags:
  - LocalSoftware
tags:
  - MSOffice
---
<!--more-->

### Description:

In my current position, I find myself needing to take list and convert them into tables in Excel. These are some things I have done:

### To Resolve:

1. Using Notepad++, we first want to remove the white space:
   - Copy and paste text from whatever source into Notepad++
   - Use `ALT+SHIFT` and the arrow keys to select empty regions and then the up or down arrow to remove empty characters at the beginning of lines.

2. Next, capitalize every word: Launch Find and Replace, change the Search Mode radio button to "Regular Expression" and then fill in the following in the what/with text boxes:

   ```escape
   find: w+  
   Replace: u$0
   ```

3. Once copied and pasted from Notepad++ to Excel, I sometimes have to cross compare two columns of data. The easiest way I have found to do this is using conditional formatting.

   - Highlight column A. Click Conditional Formatting => Create New Rule => Use this formula to determine which cells to format => Enter the formula: `=countif($B:$B, $A1)` => Click the Format button and change the Font color to something you like.
   - Repeat the same for column B, except use this formula and try another font color `=countif($A:$A, $B1)` Using a Separate Column
   - In column C, enter the ff. formula into the first cell and then copy it down `=if(countif($B:$B, $A1)<>0, "-", "Not in B")`
   - In column D, enter the ff. formula into the first cell and then copy it down `=if(countif($A:$A, $B1)<>0, "-", "Not in A")`
   - Both of these should help you visualize which items are missing from the other column.

4. To get columns to match text lists:

   - I copy and paste from Notepad++ to Excel.
   - Go to Data tab => Text to columns => Delimeter: Space for each word. This gives me many columns with one word each.
   - Lastly, you just combine column data by following [this MS article](https://support.office.com/en-us/article/Combine-text-from-two-or-more-cells-into-one-cell-81ba0946-ce78-42ed-b3c3-21340eb164a6).
   Essentially, next open cell type `=(A1&" "&B1&" "&C1)`
   - Replace A1, B1, C1 with whatever cells you want to combine. Also note that you are adding a white space in this case, feel free to remove it by just using `&` by itself or using a comma, like this: `&","&`


### References:

["How to compare two columns and find differences in Excel?"](http://superuser.com/questions/289650/how-to-compare-two-columns-and-find-differences-in-excel)