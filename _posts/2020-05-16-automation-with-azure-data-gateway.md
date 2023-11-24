---
title: Automation With Azure Data Gateway
date: 2020-05-20T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/automation-with-azure-data-gateway
tags:
  - Azure
tags:
  - Azure-On-premisesDataGateways
---
<!--more-->

### Description:

So I have used [MS Flow](https://automationadmin.com/2019/10/connect-ms-flow-to-on-prem) in the past to connect on-prem, here is how you do it with Azure.

### To Resolve:

1. Create a new server in Azure that connects to your network

2. Install [required Software](https://docs.microsoft.com/en-us/azure/logic-apps/logic-apps-gateway-install)

3. Make sure you have a service account user that has contributor access to your Resource Group that you want the Gateway to appear at.

4. Follow the installation from above and sign in to your Service Account on the server when you get to that step. Also, pay very close attention to the location during the gateway install because you basically have to reinstall it for it to show up - in my case I was wanting `southcentralus` and it kept trying to give me `centralus`. If this happens, you can reinstall it to point to the correct location. Name it something you will recognize. Lastly, I would advise running the gateway as an on-prem user that you specify so that you can automate things within the environment - this is pretty easy to do as there is a page for it in the configuration.

5. Once completed, go inside Azure and search for `on-premises Data Gateways` and click New => Enter your information and it should find them in the dropdown. If this doesn't work, try waiting an hour or so and try again. See step 6 [here](https://www.codit.eu/blog/installing-and-configuring-on-premise-data-gateway-for-logic-apps/) for examples.
