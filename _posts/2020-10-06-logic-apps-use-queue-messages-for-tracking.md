---
title: 'Logic Apps: Using Queue Messages For Tracking'
date: 2020-10-06T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/10/logic-apps-use-queue-messages-for-tracking
categories:
  - Azure
tags:
  - Azure-LogicApps
  - Azure-StorageAccounts
---
<!--more-->

### Description:

So if you have a chain of Logic Apps and you want to be able to track where they are in the chain, one method you can use is having each one write to a queue storage queue and then having the final Logic App clear it.

### To Resolve:

1. As stated, have each Logic App [add a message](https://docs.microsoft.com/en-us/connectors/azurequeues/#put-a-message-on-a-queue)
   - Ensure value is `completed`

2. Add a new Logic App as the last step in the chain that looks like:
   - Trigger: When HTTP Request is Received
   - Response: 200 code
   - [Get Messages](https://docs.microsoft.com/en-us/connectors/azurequeues/#get-messages) Max is 32
   - Initialize Variable - boolTerminate to 'false' (data type is boolean)
   - For Each 
	   - QueueMessage
	   - If Message contains 'completed'
		   - True: Delete Message
  		   - False: Set Variable boolTerminate to 'true'
	- If Variable boolTerminate is equal to 'true'
	   - True: Terminate
	   - False: Empty

3. Source code is [here](https://github.com/gerryw1389/gerryw1389.github.io/blob/main/assets/code/logic-apps/queue-storage.json)

4. Be sure to find/replace for `{{ some text }}` to set your own values. Also keep in mind I had to make many changes to sanitize it so it is just a general idea of how the Logic App will work, you might have to tweak it.

5. Pics

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2020/12/queue1.jpg){:class="img-responsive"}

   - ![image-title-here](https://automationadmin.com/assets/images/uploads/2020/12/queue2.jpg){:class="img-responsive"}