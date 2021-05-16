---
title: Logic Apps Calling Other Logic Apps
date: 2021-01-26T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/01/logic-apps-calling-logic-apps/
categories:
  - Azure
tags:
  - Cloud
  - Azure-LogicApps
---
<!--more-->

### Description:

Short post here, just wanted to write out that you can use Logic Apps to call other Logic Apps

### To Resolve:

1. Set the trigger for the 'parent' Logic App to Reoccurrence.

2. Obviously add the action 'Choose A Logic App Workflow' and point to the child Logic App which consists of HTTP Request as trigger and contains a HTTP Response as an action.
   - Set payload to be blank like `{}` or pass in data if needed. Just make sure the child can parse the payload correctly by setting the HTTP trigger's json definition.

3. What can make this interesting is that your organization can get to a point where you can have Logic Apps that make reoccurring calls to various workflows in your environment.

   - For example, if you have automation that isn't event based, this setup could allow a Logic App to query an API at periodic intervals by having the child Logic App query and the parent call multiple children in succession.
   - This setup could allow for branching in the children Logic Apps where they return [different return codes](https://cloudinfoworld.home.blog/2019/07/27/welcome-to-logic-apps/) in their `Response` actions that can trigger various other automation.
   - This setup can get developers in the practice of passing HTTP payloads around and parsing responses which can be crucial for all sorts of automation.
