---
title: 'VRO: Javascript Syntax'
date: 2020-01-19T09:39:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/vro-javascript-syntax/
tags:
  - LocalSoftware
tags:
  - Orchestration
  - Javascript
---
<!--more-->

### Description:

[vRealize Orchestrator](https://automationadmin.com//2020/01/vrealize-orchestrator/) doesn't actually use Javascript [per se](https://docs.vmware.com/en/vRealize-Orchestrator/7.6/com.vmware.vrealize.orchestrator-dev.doc/GUID-2BDAC8BD-8A5D-4ACE-AD4B-45E3F24DE6DB.html), but most examples on the internet will work. Here are my notes on what I use:

### To Resolve

1. Replace contents of a string

   ```javascript
   var str1 = "'hello'" ; 
   var reg = new RegExp("(')", "g"); 
   var str2 = str1.replace(reg,"\\'") ; 
   System.log(""+str2) ; // result : \'hello\'
   ```

2. if - else if - else

   ```javascript
   if (specificEnvironment == "Dev") {
      //System.log("environment: Unique ID = 473f5496-6061-3f55-9330-ad1eeb5654e773");
      //System.log("environment: DisplayName = Dev");
      reqEnvironments["MyMavDev"] = "473f5496-6061-3f55-9330-ad1eeb5654e773"
   }
   else if (specificEnvironment == "Testing") {
      // do something
   }
   else {
      //System.log("environment: Could not match to any uniqueids ");
   }

   // if something matches "_" in the name example:
   var arrRequestIDs = []
   for (var property in rscObject) {
      var reqKey = property
      var reqValue = rscObject[property]
      // if something matches "_" in the name
      if (reqKey.match(/_/g)) {
         var reqKeySplit = reqKey.split("_")[1]
         var strReqNumber = reqKey.split("_")[0]
         // if something matches "$any3numbers" or "$any4numbers" in the name
         if ((reqKeySplit.match(/[0-9][0-9][0-9]/g)) || (reqKeySplit.match(/[0-9][0-9][0-9][0-9]/g))) {
            arrRequestIDs.push(reqKeySplit);
         }
      }
   }
   ```

3. Objects => Hashtables, Json, Resource Elements (I like to use text files that contain json objects as resource elements)

   ```javascript
   // Loop through hashtable:
   for (var property in rscObject) {
      var reqKey = property
      var reqValue = rscObject[property]
      System.log("Key: " + reqKey)
      System.log("Value: " + reqValue)
   }

   // Import from resource:
   // attach resource to workflow as 'rscTask'
   var tasksJson = rscTask
   var tasksJsonText = tasksJson.getContentAsMimeAttachment()
   rscObject = JSON.parse(tasksJsonText.content);

   // Add a new element or update existing:
   rscObject["last-updated-date"] = "2020-01-03"

   // To test a value, do the following:
   if (jsonObject["time"] == "02 AM") {
      //do something
      System.log("executed true that time was 02 AM");
      System.log("setting to 04 AM");
      jsonObject['time'] = "04 AM";
      System.log("new time: " + jsonObject["time"]);
   }
   else {
      System.log("executed false that time was 02 AM");
   }

   // To delete a key, do the following:
   jsonObject['newVar'] = "uniqueValue";
   delete jsonObject['newVar']

   // To test if a key exists, do the following:
   if (("time" in jsonObject) == false) {
      System.log("key does not exist: time");
   }
   else {
      System.log("key does exist: time");
   }

   // When you are done, write it back to the file
   payload = JSON.stringify(jsonObject);
   tasksJsonText.content = payload
   tasksJson.setContentFromMimeAttachment(tasksJsonText)

   // To create a new hashtable
   var reqEnvironments = {}
   ```

4. Arrays

   ```javascript
   // Loop through array:
   for (var RequestID in arrRequestIDs) {
      var strRequestID = arrRequestIDs[RequestID]
      System.log("Request ID: " + strRequestID)
   }

   // Add values to an array
   var arrRequestIDs = []
   for (i = 0; i < idgJson.requests.length; i++) {
      var specificRequestID = idgJson.requests[i].resourceRequestItemId
      arrRequestIDs.push(specificRequestID);
   }

   // Test value of array
   var specificRequestIDPermName = "bob"
   var arrPermsToRemove = ["gery", "jim"]
   var arrPermsToAdd = ["bob", "jim"]
   strValue = arrPermsToAdd.indexOf(specificRequestIDPermName)
   if (strValue == -1) {
      System.log("doesnt exist")
   }
   else {
      System.log("does exist: " + strValue)
   }
   // 0 = true?
   strValue2 = arrPermsToRemove.indexOf(specificRequestIDPermName)
   if (strValue == -1) {
      System.log("doesnt exist: " + strValue2)
   }
   else {
      System.log("does exist: " + strValue2)
   }
   // 0 is true and -1 is false
   ```

5. Send Email

   ```javascript
   var smtpHost = "smtp.office365.com"
   var smtpPort = "587"
   var username = "account@domain.com"
   var secPassword = password
   var fromName = "vRealize Orchestrator"
   var fromAddress = "account@domain.com"
   var toAddress = "me@domain.com"
   var subject = "hello from vro"
   var content = "test content 2:05 pm"

   var message = new EmailMessage();

   //message.useSsl = true;
   message.useStartTls = true;

   message.smtpHost = smtpHost;
   message.smtpPort = smtpPort;
   message.username = username;
   message.password = secPassword;
   message.fromName = fromName;
   message.fromAddress = fromAddress;

   message.toAddress = toAddress
   //message.ccAddress = convertToComaSeparatedList(ccList);
   //message.bccAddress = convertToComaSeparatedList(bccList);
   message.subject = subject;
   message.addMimePart(content, "text/html; charset=UTF-8");
   message.sendMessage();

   /*
   errorError in (Workflow:email / Scriptable task (item1)#97) Cannot send mail : 'Could not convert socket to TLS' Cause: 'Certificate is not in CA store.'

   Fix:
   Import a certificate
   go to smtp.office365.com and download / copy the pem chain and import to the library - didn't work

   reboot server

   Import a certificate from URL
   url
   smtp.office365.com

   Did work!
   */
   ```

6. Passwords

   ```javascript
   function setValueByID(value) {
      var result = "";
      for (i = 0; i < value.length; i++) {
         if (i < value.length - 1) {
            result += value.charCodeAt(i) + 10;
            result += "8tr2NeU78e";
         }
         else {
            result += value.charCodeAt(i) + 10;
         }
      }
      return result;
   }
   setValueByID("hunter1")
   // "1148tr2NeU78e1278tr2NeU78e1208tr2NeU78e1268tr2NeU78e1118tr2NeU78e1248tr2NeU78e59"

   function getValueByID(value) {
      var result = "";
      var array = value.split("8tr2NeU78e");

      for (i = 0; i < array.length; i++) {
         result += String.fromCharCode(array[i] - 10);
      }
      return result;
   }
   strValue = getValueByID("1148tr2NeU78e1278tr2NeU78e1208tr2NeU78e1268tr2NeU78e1118tr2NeU78e1248tr2NeU78e59")
   // hunter1
   ```

7. Write/Read A Text File locally on VRO appliance

   ```javascript
   var tempDir = System.getTempDirectory();
   var fileWriter = new FileWriter(tempDir + "/readme.txt");
   fileWriter.open();
   fileWriter.writeLine("File written at : " + new Date());
   fileWriter.writeLine("Another line");
   fileWriter.close()

   var tempDir = System.getTempDirectory();
   var fileReader = new FileReader(tempDir + "/readme.txt");
   fileReader.open();
   var fileContentAsString = fileReader.readAll();
   System.log("content: " + fileContentAsString)

   fileReader.close()
   ```

8. Run a local command - not working

   ```javascript
   var cmd = new Command("curl -v telnet://company.domain.com:443");
   cmd.execute(true);
   System.log(cmd.output); 

   // Error: You are not authorized to execute local process, to enable this feature set your system property 'com.vmware.js.allow-local-process' to true 
   ```

9. Networking

   ```javascript
   //Obtain Text from a URL
   //The following JavaScript example accesses a URL, obtains text, and converts it to a string.

   var url = new URL("http://www.vmware.com") ; 
   var htmlContentAsString = url.getContent() ;
   ```

10. Workflow

   ```javascript
   // Part 1 - Launch another workflow from an input variable:
   // First attach the workflow as an input to the Scriptable task called 'myWorkflow' and data type 'Workflow'
   var inputProperties = new Properties();  

   inputProperties.put("inputParameter1", inputParameter1);  
   inputProperties.put("inputParameter2", inputParameter2);  

   workflowToken = myWorkflow.execute(inputProperties);  
   workflowTokens = new Array();  
   workflowTokens.push(workflowToken);  
   System.getModule("com.vmware.library.workflow").waitAllWorkflowComplete(workflowTokens)

   // Part 2 - Launch workflow, wait for it to complete, and launch it again with different input params

   var inputParameter1 = "Employee"
   var inputParameter2 = "email@domain.com"
   var inputProperties = new Properties();

   inputProperties.put("GroupName", inputParameter1);
   inputProperties.put("UserEmail", inputParameter2);

   workflowToken = myWorkflow.execute(inputProperties);

   System.log("calling workflow: ")
   System.log("input 1: " + inputParameter1)
   System.log("input 2: " + inputParameter2)

   workflowTokens = new Array();
   workflowTokens.push(workflowToken);
   System.getModule("com.vmware.library.workflow").waitAllWorkflowComplete(workflowTokens)

   // Here the parent workflow will pause until the child is completed!!

   System.log("=======================")
   System.log("Workflow completed, now doing additional steps")

   function sleep(milliseconds) {
      var timeStart = new Date().getTime();
      while (true) {
         var elapsedTime = new Date().getTime() - timeStart;
         if (elapsedTime > milliseconds) {
            break;
         }
      }
   }

   sleep(4000);
   System.log("example of doing something")
   sleep(4000);
   System.log("example of doing something else")
   System.log("Completed doing something ")
   System.log("=======================")
   System.log("=======================Calling workflow again with new params=======================")

   var inputParameter1pt2 = "Test, Student"
   var inputParameter2pt2 = "example@domain.com"
   var inputPropertiespt2 = new Properties();

   inputPropertiespt2.put("GroupName", inputParameter1pt2);
   inputPropertiespt2.put("UserEmail", inputParameter2pt2);

   workflowTokenpt2 = myWorkflow.execute(inputPropertiespt2);

   System.log("calling workflow 3: ")
   System.log("input 1: " + inputParameter1pt2)
   System.log("input 2: " + inputParameter2pt2)

   workflowTokenspt2 = new Array();
   workflowTokenspt2.push(workflowTokenpt2);
   System.getModule("com.vmware.library.workflow").waitAllWorkflowComplete(workflowTokenspt2)

   System.log("=======================")
   System.log("Workflow completed, now doing additional steps")
   sleep(4000);
   System.log("example of doing something")
   sleep(4000);
   System.log("example of doing something else")
   System.log("Finally, completed everything ")
   System.log("=======================")

   // Part 3 - Don't even attach workflow, call it by ID! 
   // Launch workflow, wait for it to complete, and launch it again with different input params
   // In this case, I got the workflow ID of c2edc5eb-07f7-40b6-b803-17cbf99d38f3 from the `Workflow Runs` page in VRO web UI
   var wfObject = System.getModule("com.vmware.library.workflow").getWorkflowById("c2edc5eb-07f7-40b6-b803-17cbf99d38f3");
   // now run the same code as above replacing `myWorkflow` with `wfObject` and you are now good to delete the input variable!
   ```

1. Untested myself - Access XML Documents

   ```javascript
   The following JavaScript example allows you to access XML documents from JavaScript by using the ECMAScript for XML (E4X) implementation in the Orchestrator JavaScript API.
   Note: In addition to implementing E4X in the JavaScript API, Orchestrator also provides a Document Object Model (DOM) XML implementation in the XML plug-in. For information about the XML plug-in and its sample workflows, see the Using vCenter Orchestrator Plug-Ins.


   var people = <people>
                  <person id="1">
                        <name>Moe</name>
                  </person>
                  <person id="2">
                        <name>Larry</name>
                  </person>
               </people>;

   System.log("'people' = " + people);

   // built-in XML type
   System.log("'people' is of type : " + typeof(people)); 

   // list-like interface System.log("which contains a list of " +
   people.person.length() + " persons"); 
   System.log("whose first element is : " + people.person[0]);

   // attribute 'id' is mapped to field '@id'
   people.person[0].@id='47'; 
   // change Moe's id to 47 
   // also supports search by constraints
   System.log("Moe's id is now : " + people.person.(name=='Moe').@id);

   // suppress Moe from the list
   delete people.person[0];
   System.log("Moe is now removed.");

   // new (sub-)document can be built from a string 
   people.person[1] = new XML("<person id=\"3\"><name>James</name></person>");
   System.log("Added James to the list, which is now :");
   for each(var person in people..person)

   for each(var person in people..person){
      System.log("- " + person.name + " (id=" + person.@id + ")"); 
   }

   */
   ```

1. Untested - CSV Files? May work?

   ```javascript
   var i = 0;
   var csvFileName = "c:\\Orchestrator\\customer.csv";
   Server.log(csvFileName);

   var fileReader = new FileReader(csvFileName);
   fileReader.open();
   var line = fileReader.readLine();
   Server.log(line);

   while (line != null) {
      Server.log("loop Started");
      var lineValues = line.split(",");
      var linelength = lineValues.length
      var vmname = lineValues[0];
      var INPTemplateNameString = lineValues[1];
      var MyNoCPU = lineValues[2];
      var MyNoMemory = lineValues[3] * 1000;
      var MyNoNICS = lineValues[4];

      i = i + 1;
      Server.log("looping");
      line = fileReader.readLine();

      }
   fileReader.close; 
   ```
