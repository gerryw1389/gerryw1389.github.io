---
title: Connect MS Flow To On Prem
date: 2019-10-04T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/10/connect-ms-flow-to-on-prem
tags:
  - WebSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

Microsoft Flow is an automation tool that Admins can use to connect services in the cloud. Basically, a Microsoft version of the app [IFTTT](https://ifttt.com/). Anyhow, now there is a way to connect it on-prem so that your flows can automate things on prem as well. In this one, I will be writing a file to a server on-prem. You could then have a powershell script read that file and then do something!

### To Resolve:

1. Create a Server 2019 server and install the gateway package from [Gateway Server Install](https://docs.microsoft.com/en-us/azure/analysis-services/analysis-services-gateway-install)

2. For my organization, we had a 'cloud only' account which means even though we use AAD to sync on-prem to Azure, we still have some accounts that live directly in Azure and not on-prem AD. So when following this, I had to make sure to use two different accounts. Normally you can use a single account though. 
   - The idea is that you will need a local AD user to run the service on the server which will then execute flows. This account will need to have access to network shares and such if your automation will require it. 

3. After it installs, open the `On-premises data gateway` program and change the account that it runs as to the service account:
   - Make sure to add that account as a local admin on the server so that it can write to whatever directories it needs to:
   - NOTE: This goes for file shares in the environment as well. 

4. So at this point, the on-prem server is connected and ready for flows to connect to. I'm going to create an example flow that connects to the local server and writes a file:

   - Sign into O365 and go to [flow.microsoft.com](https://flow.microsoft.com) to get to your flows.
   - Go to Data => Connections => Create New. Search `File System` and choose `Create a file`. Create it like:
     - You can name the connection whatever you want, but it is advised to name it the same as the file path. You will see why shortly.
     - Create a flow and then choose the option `create a file`. This will then need to know which connection to use, use the local one. In my example, I have two connections, one for a local file on the gateway server `flow.domain.com` and one for `\\fileserver.domain.com\exampleShare` which is just an open share that the AD account can write to.
   - When I create a flow, I have to specify which one to connect to and which root path. For example, you can use the connection to `flow.domain.com` server to write a file called `test.txt` to the `c:\scripts` directory. 

5. At this point, the possibilities are up to you. The general idea is have MS Flow write a file with certain information to server, and then have a script that runs on a schedule pick up, process, and delete or move the file and do things without human intervention.
   - An example flow: When a sharepoint list is updated, take that information and write to to `c:\scripts\info.csv` on `flow.domain.com`. Then have a powershell script run every 5 minutes and look for `c:\scripts\info.csv`. It will then parse it, and do a REST API call to some service and process a transaction. Then have the script either move the file to another location or delete it. In addition, you can have flow give it a unique timestamp in the name of the file. 
   - I will probably write another post on this later.

### References

["Flow of the Week: Local code execution"](https://flow.microsoft.com/en-us/blog/flow-of-the-week-local-code-execution/)