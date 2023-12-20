---
title: 'VRO: Function Return Issue'
date: 2020-02-08T08:31:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/vro-function-return-issue
tags:
  - LocalSoftware
tags:
  - Orchestration
  - Javascript
---
<!--more-->

### Description:

So I ran into an issue today where I was trying to put my code into functions and return objects, but it kept saying it was `undefined`. Here goes:

### To Resolve:

1. First, I have this already working fine with my `getAccessToken()` function where it parses the response from a `POST`:

   ```javascript
   contentAsString = response.contentAsString
   //System.log("Content As String: " + contentAsString)
   var json = JSON.parse(contentAsString)
   var tokenID = json["access_token"]
   var refreshID = json["refresh_token"]
   //System.log("This is the token: " + tokenID)
   var token = {
      "access_token": tokenID,
      "refresh_token": refreshID
   };
   return token
   ```

   - and later, it's just a simple object value lookup:

   ```javascript
   var strToken2 = getAccessToken();
   var strToken2Access = strToken2["access_token"];
   var strToken2Refresh = strToken2["refresh_token"];
   var authVar = "Bearer " + strToken2Access
   // somewhere attach `authVar` to next request
   ```

2. That works great for strings, but gives errors if you want to return an integer. Unfortunately you can't force cast like you can in Powershell like `[int]$someVar = 3`. So let's say you have this function :

   ```javascript
   function getTimeDifference(strEpoch) {

      var epoch = new Date(strEpoch).toISOString();
      date = new Date(epoch);
      var year = date.getFullYear();
      var month = date.getMonth()
      var day = date.getDate();
      var hours = date.getHours();
      var minutes = date.getMinutes();
      var seconds = date.getSeconds();
      var dateToday = new Date(year, month, day, hours, minutes, seconds);
      System.log("Request submitted date: " + dateToday.toString());

      // Get todays date
      var today = new Date();
      var day = today.getDate();
      var month = today.getMonth()
      var year = today.getFullYear();
      var hours = today.getHours();
      var minutes = today.getMinutes();
      var seconds = today.getSeconds();
      var dateToday2 = new Date(year, month, day, hours, minutes, seconds);
      System.log("Todays date: " + dateToday2.toString());

      // Compare the two
      var diff = dateToday2.getTime() - dateToday.getTime();
      var diffDays = Math.floor(diff / (1000 * 60 * 60 * 24));
      diff -= diffDays * (1000 * 60 * 60 * 24);
      var diffHours = Math.floor(diff / (1000 * 60 * 60));
      diff -= diffHours * (1000 * 60 * 60);
      var diffMins = Math.floor(diff / (1000 * 60));
      diff -= diffMins * (1000 * 60);
      var diffSeconds = Math.floor(diff / (1000));
      diff -= diffSeconds * (1000);
      System.log("Difference between Request Date and today: " + diffDays + " days, " + diffHours + " hours, " + diffMins + " minutes, " + diffSeconds + " seconds");

   }
   ```

   - So at this point `diffDays, diffHours, diffMins, and diffSeconds` are all defined and working perfectly. The problem is how do you return them? Well logically you would put them in an object and return that by adding this below the last line before the function ends:

   ```javascript
   var strDateDiff {
      "diff_Days": diffDays,
      "diff_Hours": diffHours,
      "diff_Mins": diffMins,
      "diff_Seconds": diffSeconds
   }
   return strDateDiff
   ```

   - Then, later in code, you would reference like:

   ```javascript
   var strEpoch = 1581354527172;
   var strTimeDiff = getTimeDifference(strEpoch);

   System.log("diff days: " + strTimeDiff[diff_Days])
   System.log("diff hours: " + strTimeDiff[diff_Hours])
   System.log("diff min: " + strTimeDiff[diff_Mins])
   System.log("diff secs: " + strTimeDiff[diff_Seconds])
   ```

   - The problem is, of course, that doesn't work! It throws an error saying `strTimeDiff[diff_Days] is undefined`.

3. Well I knew this issue had something to do with the values being integers instead of strings and so I tried various things like removing quotes and trying to cast them to strings like `diffDays.toString();` but no matter what, it kept throwing the same error. So frustrating. I then found [a SO post](https://stackoverflow.com/questions/2917175/return-multiple-values-in-javascript) and found two different solutions that worked! Here goes:

   - First solution which I didn't like because of the dot notation is:

   ```javascript
   return {
      diff_Days: diffDays,
      diff_Hours: diffHours,
      diff_Mins: diffMins,
      diff_Seconds: diffSeconds
   };
   ```

   - Then, later in code, you would reference like:

   ```javascript
   var strEpoch = 1581354527172;
   var strTimeDiff = getTimeDifference(strEpoch);

   System.log("diff days: " + strTimeDiff.diff_Days)
   System.log("diff hours: " + strTimeDiff.diff_Hours)
   System.log("diff min: " + strTimeDiff.diff_Mins)
   System.log("diff secs: " + strTimeDiff.diff_Seconds)
   ```

   - The second solution which I chose is:

   ```javascript
   return [diffDays, diffHours, diffMins, diffSeconds];
   ```

   - Then, later in code, you would reference like:

   ```javascript
   var strEpoch = 1581354527172;
   var strTimeDiff = getTimeDifference(strEpoch);

   System.log("diff days: " + strTimeDiff[0])
   System.log("diff hours: " + strTimeDiff[1])
   System.log("diff min: " + strTimeDiff[2])
   System.log("diff secs: " + strTimeDiff[3])
   ```


   