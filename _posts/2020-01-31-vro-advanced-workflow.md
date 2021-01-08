---
title: 'VRO: Advanced Workflow'
date: 2020-01-31T10:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: 2020/01/vro-advanced-workflow/
categories:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

This post will cover each of my previous posts about [vRealize Orchestrator](https://automationadmin.com//2020/01/vrealize-orchestrator/) so far. It combines all of them into an advanced workflow that does the following:

### To Resolve:

1. Add [REST hosts and operations](https://automationadmin.com/2020/01/vro-add-rest-host-and-ops/) to VRO.

2. Scan SN response into variables.

3. Send REST API call to a software to get a users identity information.

4. [Parse the response](https://automationadmin.com/2020/01/vro-parsing-responses/) and send the request to a different endpoint on that software.

5. Update the Service Now request to ["waiting"](https://automationadmin.com/2020/01/vro-read-write-service-now/).

6. Write the information [to an attachment](https://automationadmin.com/2020/01/vro-attachments/).

7. Workflow 1 ends with the following JSON being created and stored in VRO itself as a resource element:

   ```json
   {
      "REQ0000006": [{
         "12_Comment": "Permission = CompanyEmployee, Status = Waiting",
         "12": "waiting",
         "11_Comment": "Permission = CompanyEmployee-Dev, Status = Waiting",
         "11": "waiting",
         "User_Email": ["user1@domain.com"],
         "User_ID": "122365465",
         "User_GroupsRequested": ["CompanyEmployee", "CompanyEmployee-Dev"],
         "SN_RequestNumber": "REQ0000006",
         "SN_Reason": "Test 2/3",
         "SN_SysID": "71141da7dbae08140ed7dbf0ce9615645645115572",
         "Company_RequestNumberArray": [12, 11],
         "LastUpdatedDate": "2020-1-30",
         "LastUpdatedTime": "14:42:21 PM"
      }],
      "REQ0000007": [{
         "14_Comment": "Permission = CompanyEmployee, Status = Waiting",
         "14": "waiting",
         "13_Comment": "Permission = CompanyEmployee-Test, Status = Waiting",
         "13": "waiting",
         "User_Email": ["user2@domain.com"],
         "User_ID": "122365465",
         "User_GroupsRequested": ["CompanyEmployee", "CompanyEmployee-Test"],
         "SN_RequestNumber": "REQ0000007",
         "SN_Reason": "test 3/3",
         "SN_SysID": "71141da7dbae08140ed7dbf0ce9615645645115572",
         "Company_RequestNumberArray": [14, 13],
         "LastUpdatedDate": "2020-1-30",
         "LastUpdatedTime": "14:43:20 PM"
      }]
   }
   ```

8. Now a different workflow (workflow 2) will [Parse attachment](https://automationadmin.com/2020/01/vro-attachments/) and for each request ...

   - And for each item in the request ...

   - Do a lookup  to external approval system via REST call and if the item is completed, do nothing. If the item is approved, call another workflow to perform an operations and mark the item as completed.

   - Once all items are completed under a request, close the request in Service Now

9. Workflow 3: Exists only to be called from workflow two. It consists of a [Jenkins job](https://automationadmin.com/2020/01/vro-run-jenkins-ps-2/) that takes multiple input parameters.

