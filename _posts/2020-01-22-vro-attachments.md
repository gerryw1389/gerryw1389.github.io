---
title: 'VRO: Using Attachments'
date: 2020-01-22T10:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/vro-attachments/
tags:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

This post will cover how to use Resource Elements in [vRealize Orchestrator](https://automationadmin.com//2020/01/vrealize-orchestrator/). Resource Elements are essentially attachments that VRO holds that you can read/write to for workflows. I like to write JSON objects to a text file in one workflow and then have another workflow parse the file and update it in order to have different workflows pass information to each other.

### To Resolve

1. First, create a text file on your computer at `c:\scripts\` called `json.txt` with the value `{}`. Then upload this to VRO on the Resource elements tab.

   - Then attach it as a variable to a workflow. I called mine `rscTasks` or something like that with a data type of `ResourceElement`

   - Then, bind it to a scripting element and put your code like:

   ```javascript
   var tasksJson = rscTask
   var tasksJsonText = tasksJson.getContentAsMimeAttachment()
   rscObject = JSON.parse(tasksJsonText.content);
   ```

2. Now that it is imported as a JSON object, you can do all sorts of stuff and write it back

   - See [here](https://automationadmin.com/2020/01/vro-javascript-syntax/) to add a value, delete a value, test for a value, or modify a value.

   - To create a nested value do something like:

   ```javascript
   var reqNestedHash2 = {
      "User_Email": ["blah@domain.com"],
      "User_EmplID": someVar,
      "User_GroupsRequested": someArray,
      "SN_RequestNumber": strRequestNumber,
      "SN_Reason": strReason,
      "SN_SysID": sys_ID,
      "Software_RequestNumberArray": arrRequestIDs,
      "LastUpdatedDate": strDate,
      "LastUpdatedTime": strTime,
   }


   rscObject["REQ002"] = [reqNestedHash2]
   ```

3. Either way, when you are done, write it back to VRO

   ```javascript
   payload = JSON.stringify(rscObject);
   tasksJsonText.content = payload
   tasksJson.setContentFromMimeAttachment(tasksJsonText)
   ```

4. I usually start the second flow where it will import the resource element and then loop through each request and close the request if all items are completed:


   ```javascript
   var tasksJson = rscTask
   var tasksJsonText = tasksJson.getContentAsMimeAttachment()
   var rscObject = JSON.parse(tasksJsonText.content);

   for (var key in rscObject) {
      var reqKey = key
      var reqValue = rscObject[key]
      //var strValue = JSON.stringify(reqValue);
      System.log("Key: " + reqKey)
      //System.log("Value (doesnt work): " + reqValue)
      //System.log("Value (does work - stringified): " + strValue)

      // value is an array with one element
      for (var singleHash in reqValue) {

         var singleValue = reqValue[singleHash]
         //System.log("single value (just returns [object object] because its a hashtable): " + singleValue)

         // strings

         var strSNRequestNumber = singleValue["SN_RequestNumber"]
         ....

         // if request_number.item == completed { // do nothing } else { // do something }

      }  // End loop for each request value in resource file

      // If all items in request_number are completed, delete the Request from the resource element so that it will not run on next run
   } // End loop for each request key in resource file

   ```

