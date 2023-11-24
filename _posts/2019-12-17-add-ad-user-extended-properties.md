---
title: 'Add AD User Extended Properties To Azure User'
date: 2019-12-17T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/12/add-ad-user-extended-properties/
Tags:
  - Azure
tags:
  - Scripting-RestAPI
---
<!--more-->

### Description:

Let's say you have an AD extended attribute on prem called 'companyEmployeeID' and you want this to be an extended attribute for the same user with the Azure AD user, this post will get that information added using RestAPI's mostly following [this](https://docs.microsoft.com/en-us/previous-versions/azure/ad/graph/howto/azure-ad-graph-api-directory-schema-extensions#WriteAnExtensionValue) guide.



### To Resolve:

1. In the Azure Portal, [create an application](https://automationadmin.com/2020/01/azure-create-ps-app/) in Azure AD and get its `applicationID`. We have `269fc2f7-6420-4ea4-be90-9e1f93a87a64`

2. Create a POST request with the name you want the object to be. It can only have a data type of String or Byte I believe. 

   ```json
   POST
   https://graph.microsoft.com/v1.0/applications/269fc2f7-6420-4ea4-be90-9e1f93a87a64/extensionProperties
   {
      "name": "companyEmployeeID",
      "dataType": "String",
      "targetObjects": [
         "User"
      ]
   }
   ```

   - Response:

   ```json
   {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#applications('269fc2f7-6420-4ea4-be90-9e1f93a87a64')/extensionProperties/$entity",
      "id": "5d0a80ec-125a-4ea3-96d8-0094ea115d77",
      "deletedDateTime": null,
      "appDisplayName": "custom class attributes",
      "dataType": "String",
      "isSyncedFromOnPremises": false,
      "name": "extension_b5cfcf360940477da1b4bb2042c2b585_companyEmployeeID",
      "targetObjects": [
         "User"
      ]
   }
   ```

3. Just to verify, do a GET request to your application and see if it shows the extensions `name` value

   ```escape
   GET
   https://graph.microsoft.com/v1.0/applications/269fc2f7-6420-4ea4-be90-9e1f93a87a64/extensionProperties
   # Looks good = extension_b5cfcf360940477da1b4bb2042c2b585_companyEmployeeID
   ```

4. Now let's write a value to a user:

   ```json
   PATCH
   https://graph.microsoft.com/v1.0/users/gerry@domain.com

   {
      "extension_b5cfcf360940477da1b4bb2042c2b585_companyEmployeeID": "015645645612"
   }
   ```

5. Verify:

   ```json
   GET
   https://graph.microsoft.com/v1.0/users/gerry@domain.com?$select=extension_b5cfcf360940477da1b4bb2042c2b585_companyEmployeeID
   ```

   - At this point, you can script something that writes each on-prem value to Azure!
    
6. If you ever want to remove the extension value for a user: 

   ```json
   PATCH
   https://graph.microsoft.com/v1.0/users/gerry@domain.com

   {
      "extension_b5cfcf360940477da1b4bb2042c2b585_companyEmployeeID": null
   }
   ```

7. If you don't even want it as an option, you need to un-register the extension (get the ID first from step 2):

   ```json
   DELETE
   https://graph.microsoft.com/v1.0/applications/{applicationID}/extensionProperties/{extensionIDFromStep2}
   # https://graph.microsoft.com/v1.0/applications/269fc2f7-6420-4ea4-be90-9e1f93a87a64/extensionProperties/5d0a80ec-125a-4ea3-96d8-0094ea115d77
   ```



