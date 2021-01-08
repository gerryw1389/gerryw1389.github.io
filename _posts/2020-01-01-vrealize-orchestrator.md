---
title: 'vRealize Orchestrator'
date: 2020-01-01T07:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/vrealize-orchestrator/
categories:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

vRealize Orchestrator which will often be shorthanded as VRO is an orchestration tool part of vCenter that is used for the creation of workflows. The product is mainly designed for VM automation like provisioning tasks but you can have it automate all sorts of tasks since you can schedule workflows as needed. In order to get started, complete each of the following:
   - [Part 1](https://docs.hol.vmware.com/HOL-2019/hol-1921-05-cmp_html_en/)
   - [Part 2](http://docs.hol.vmware.com/HOL-2019/hol-1921-06-cmp_html_en/)
   - [Youtube Playlist](https://www.youtube.com/playlist?list=PL1JSSDnw-d0ETv0GM6KOUoVKg_M-IFwzi)

I had initially planned to make a separate post for each lab but decided instead to just start with real world examples. Below is just an overview of VRO:

### To Resolve

1. UI:

   - My Orchestrator - Summarizes the most recent activities on the Orchestrator server, such as recently modified elements, pending and running workflows, running policies, completed workflows, and workflows that are waiting for user interaction. You can use the My Orchestrator view to perform common administrative tasks such as running a workflow, importing a package, and setting root access rights.

   - Scheduler - Displays a list of all scheduled workflows. The workflows are sorted by name or date, together with their status. You can use the Scheduler view to create, edit, suspend, resume, and cancel scheduled workflows

   - Policies - Displays existing policies. You can use the Policies view to create and apply policies. Policies in vRealize Orchestrator are a series of rules, gauges, thresholds, and event filters that run certain workflows or scripts when specific predefined events occur either in Orchestrator or in the platforms that Orchestrator can access through plug-ins.

   - Workflows - Provides access to the Orchestrator workflow library. You can use the Workflows view to view information about each workflow. You can also use this view to create, edit, run and interact with workflows.

   - Inventory - Displays the objects of the plug-ins that are enabled in Orchestrator. You can use the Inventory view to run workflows on an inventory object.

2. Definitions:

   - Workflows - Provides access to the Orchestrator workflow library. You can use the Workflows view to view information about each workflow, create, edit, and run workflows, as well as to interact with the workflows.

   - Actions - Provides access to the libraries of predefined actions. You can use the Actions view to duplicate actions, export them to a file, or move them to a different module in the actions hierarchical list.

   - Resources - Provides access to the list of resource elements. You can use the Resources view to import external objects such as images, sysprep files, HTML templates, XML templates, and custom scripts. In turn, you can then use these as resource elements within workflows.

   - Configurations - Provides access to the available configuration elements. You can use the Actions view to create configuration elements to define common attributes across an Orchestrator server.

   - Packages - Displays a list of the available packages and where a selected package is used. You can use the Packages view to add, import, export, and synchronize packages.

   - Inventory - Displays the objects of the plug-ins that are enabled in Orchestrator. You can use the Inventory view to run workflows on an inventory object. 

3. Parameters

   - Parameters within vRealize Orchestrator are basically input and output variables of a workflow in the simplest of terms.

   - Input parameters are needed for most workflows and are values that are passed into the workflow when it starts via a user, application, another workflow, or even an action. A good example of this might be a workflow that is used to snapshot a virtual machine.  An input parameter for such a workflow may be the virtual machine name. Another thing to note about input parameters is that they are read-only, and cannot be changed during workflow execution.

   - Output parameters represent the result of the workflow and can be passed on to other elements when the workflow has completed. For that same virtual machine snapshot workflow, the output parameter is the resulting snapshot. Output parameters are write-only; to read the value of a parameter within a workflow, it cannot be an output parameter. However, this output parameter value is readable for any workflows chained after this one.

4. Workflow Attributes

   - Workflow attributes are one of the key constructs used to carry values between elements in a workflow. Attributes are variables that are generally read/write, and they can be used to transfer data between the elements of a workflow. An attribute can be locked so it is read-only across all workflow elements. This is very useful to define a static value that is needed in several elements of a workflow. Read-only workflow attributes act as global constants for a workflow. Writeable attributes act as a workflow’s global variables. Values of attributes can be set and modified as follows:
     -  Set attribute value in a workflow
     - Assign attribute value from a configuration element
     - Attribute linked to the output parameter of a workflow element

   ```escape
   Example, go to workflow => General tab => scroll down and there will be attributes. If you click on the checkbox next to one, it becomes read-only.
      Click on the General tab
      Scroll down to the bottom of the General tab
   Here are the attributes listed.  They can be blank or have a default value, and like Parameters, they have a type.
      Click on the checkbox near attribute2
   By doing this, the attribute is now read-only, and can be used by any workflow element only as IN.
      Double-click into the value field for the attribute1 attribute and type in my value 1
   This would set the attribute's default value to my value 1.  It will remain read/write and can used by any workflow element as IN and/or OUT. 
   ```

5. Actions

   - Actions in vRealize Orchestrator are generally pieces of code that can be reused often.  In another language they could be referred to as functions. The main difference between an Action and a workflow is that Actions can only return one variable and a workflow can return many.  Actions are also built entirely using JavaScript, and there is no visual programming like with a workflow.  
