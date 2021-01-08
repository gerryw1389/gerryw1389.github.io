---
title: 'Logic App Expressions'
date: 2020-05-15T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/logic-app-expressions
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
---
<!--more-->

### Description:

This post will be a reference post for different expressions you can create with Logic Apps.

### To Resolve:

1. Expression to convert to local time zone: `convertTimeZone(utcnow(),'UTC','Central Standard Time','yyyy_MM_dd_HH_mm_ss_tt')`

2. To do a `Start-Sleep`, insert a Delay element and set it up accordingly. I like to test Conditions by having `if true...delay` just to see if the IF statement will fire.

3. A common tactic is to take a HTTP Response or something similar and put it in a `Compose` element. Logic Apps will dynamically put it in a `For each` element. When using this strategy, it is best to rename the element ( for example: `Get-FileContent` ) and then access it later by something like `outputs('Get-FileContent')`. This will create an object that you can reference.

4. I usually follow `Compose` elements with:
   - A string variable named `longDescription` with the expression `json( first(outputs('Get-FileContent')))` if the `Get-Content` element outputs something like `[{'key':'value', 'key2':'value2'}]`
   - An array variable named `DescArray` with the expression `split(variables('longDescription'),',')`
   - Another string variable named `key` with the expression of `split(variables('DescArray')[0],':')[1]`. This will have the value of `value`
   - Another string variable named `key2` with the expression of `split(variables('DescArray')[0],':')[1]`. This will have the value of `value2`
   - What those string are doing is splitting on ':' and grabbing the second element 1 (first element is 0).

5. To split something = `split(` + `variables('myVarName')` or `outputs('myComposeElementTitle')` + `,',')`

6. To get an array count: `sub(length(outputs('Convert-ToArray')),1)` coming from a compose element. Length will get the number of elements, but you need to subtract one because arrays are 0 value so you use `sub( length, 1)` to subtract the length - 1.

7. To access the last element in array: `variables('stringArray')[variables('count')]` assuming you have a variable named `count` using the step above.

8. Working with substrings:

   ```escape
   $test = "Some info: Some value

   Some info2: Some value2

   Some info3: Some value3

   Response successful. Response info4: 12345678"
   ```

   - Syntax: `substring ( string to modify, starting index, integer you want past the index)`
   - So if I wanted to get:
   - `: 12345678` stored in variable `$substring`
   - I would use expression: `substring(variables('test'),lastIndexOf(variables('test'),':'),sub(length(variables('test')),lastIndexOf(variables('test'),':')))`

   ```escape
   substring
   (
      variables('test'), #string to modify
      lastIndexOf(variables('test'),':'), # starting index = get the position of last colon = 210
      sub(length(variables('test')),lastIndexOf(variables('test'),':')) # integer you want past the index = subtract the position of last colon 210 from length of $test 216, so 6
   )
   ```

   - Which is nice, but let's substring again to get the first two characters removed:

   ```escape
   # Now we do this again
   substring
   ( 
      variables('substring'), #string to modify
      2, # starting index
      sub(length(variables('substring')),2)) # integer you want past the index = subtract 2 from the length of $substring
   )
   ```


