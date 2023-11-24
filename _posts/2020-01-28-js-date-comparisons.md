---
title: 'Javascript: Date Comparisons'
date: 2020-01-28T10:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/javascript-date-comparisons/
tags:
  - LocalSoftware
tags:
  - Scripting-Javascript
---
<!--more-->

### Description:

Here is how I compared dates in a [vRealize Orchestrator](https://automationadmin.com//2020/01/vrealize-orchestrator/) workflow:

### To Resolve

1. To get dates down to the milliseconds

   ```javascript
   function addZero(x, n) {
   while (x.toString().length < n) {
      x = "0" + x;
   }
   return x;
   }

   function sleep(milliseconds) {
      var timeStart = new Date().getTime();
      while (true) {
         var elapsedTime = new Date().getTime() - timeStart;
         if (elapsedTime > milliseconds) {
            break;
         }
      }
   }

   var d = new Date();
   var utc = d.getTime() + (d.getTimezoneOffset() * 60000);
   var offset = "-6.0"
   var nd = new Date(utc + (3600000*offset));
   var strTime = nd.toLocaleString();

   var today = new Date(strTime);
   var day = addZero( today.getDate(), 2);
   var month = addZero( (today.getMonth() + 1), 2);
   var year = today.getFullYear();
   var hours = addZero(today.getHours(), 2);
   var minutes = addZero(today.getMinutes(), 2);
   var seconds = addZero(today.getSeconds(), 2);
   var ms = addZero(d.getMilliseconds(), 3);
   var date3 = year + "-" + month + "-" + day + "T" + hours + ":" + minutes + ":" + seconds + "." + ms + "000-0600" 
   System.log("date3 is " + date3);

   //////

   sleep(200);

   var d = new Date();
   var utc = d.getTime() + (d.getTimezoneOffset() * 60000);
   var offset = "-6.0"
   var nd = new Date(utc + (3600000*offset));
   var strTime = nd.toLocaleString();

   var today = new Date(strTime);
   var day = addZero( today.getDate(), 2);
   var month = addZero( (today.getMonth() + 1), 2);
   var year = today.getFullYear();
   var hours = addZero(today.getHours(), 2);
   var minutes = addZero(today.getMinutes(), 2);
   var seconds = addZero(today.getSeconds(), 2);
   var ms = addZero(d.getMilliseconds(), 3);

   var date4 = year + "-" + month + "-" + day + "T" + hours + ":" + minutes + ":" + seconds + "." + ms + "000-0600" 
   System.log("date4 is " + date4);


   //////

   sleep(200);

   var d = new Date();
   var utc = d.getTime() + (d.getTimezoneOffset() * 60000);
   var offset = "-6.0"
   var nd = new Date(utc + (3600000*offset));
   var strTime = nd.toLocaleString();

   var today = new Date(strTime);
   var day = addZero( today.getDate(), 2);
   var month = addZero( (today.getMonth() + 1), 2);
   var year = today.getFullYear();
   var hours = addZero(today.getHours(), 2);
   var minutes = addZero(today.getMinutes(), 2);
   var seconds = addZero(today.getSeconds(), 2);
   var ms = addZero(d.getMilliseconds(), 3);

   var date5 = year + "-" + month + "-" + day + "T" + hours + ":" + minutes + ":" + seconds + "." + ms + "000-0600" 
   System.log("date5 is " + date5);
   ```

   - Produces these results:

   ```escape
   date3 is 2020-02-03T12:06:01.064000-0600
   date4 is 2020-02-03T12:06:01.270000-0600
   date5 is 2020-02-03T12:06:01.476000-0600
   ```


2. To get AM/PM

   ```javascript
   // Looks bad, but just returns the time in CST with AM or PM
   var d = new Date();
   var utc = d.getTime() + (d.getTimezoneOffset() * 60000);
   var offset = "-6.0"
   var nd = new Date(utc + (3600000*offset));
   var strTime = nd.toLocaleString();
   //System.log("strTime unformatted: " + strTime);
   var today = new Date(strTime);
   var day = today.getDate();
   var month = today.getMonth()
   var year = today.getFullYear();
   var hours = today.getHours();
   var minutes = today.getMinutes();
   var seconds = today.getSeconds();
   if ( hours >= 12) { var ampm ="PM" } else { var ampm = "AM"}
   var strTimeAMPM = hours + ":" + minutes + ":" + seconds + " " + ampm
   //System.log("Current Time: " + strTimeAMPM);
   ```

3. To compare two different times (one epoch calculated (used in REST API response) and the other today's date):

   ```javascript
   //  var specificRequestDate = "1580764746"
   var epoch = new Date(specificRequestDate).toISOString();
   date = new Date(epoch);
   var year = date.getFullYear();
   var month = date.getMonth()
   var day = date.getDate();
   var hours = date.getHours();
   var minutes = date.getMinutes();
   var seconds = date.getSeconds();
   var dateToday = new Date(year, month, day, hours, minutes, seconds);
   System.log("REST Response date: " + dateToday.toString());

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
   System.log("Difference between REST Response and today: " + diffDays + " days, " + diffHours + " hours, " + diffMins + " minutes, " + diffSeconds + " seconds");
   ```



