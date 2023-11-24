---
title: 'VRO: Run Jenkins PS Script Pt 2'
date: 2020-01-20T09:39:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/vro-run-jenkins-pt-2/
tags:
  - LocalSoftware
tags:
  - Orchestration
  - CICD
---
<!--more-->

### Description:

This post is a continuation of my previous post where I use [VRO and Jenkins](https://automationadmin.com/2019/12/vro-run-jenkins-ps/) to execute jobs. In this one I take it one step further and use [VRO](https://automationadmin.com//2020/01/vrealize-orchestrator/) to pass a workflow with input parameters to Jenkins and then capture the output back in VRO. 

### To Resolve

1. Side-note: Before I started, I wanted to find a way to trigger builds remotely without anonymous users being able to read the job screen. I was able to after installing the plugin 'Build Authorization Token Root Plugin' which works if you give anonymous users 'build' permission only. The problem was then that I could not retrieve the job information from Jenkins to plug back into VRO logs so I just reverted and instead used the local firewall to only allow port 443 from a specific subnet range.

2. Ok, so we want to configure Jenkins first with an example job that takes parameters. I was able to accomplish this with:
   
   - Create a new pipeline project: powershell-with-parameters
   - General => Check the box 'this project is parameterized' => String parameter => name = number; Default value = 5
   - Build Triggers => Check the box 'Trigger Builds Remotely' => Auth Token = 954c2e51-a9d2-4600-9cb2-5d99942716392b
   - Pipeline => Pipeline script
   - Value:

   ```escape
   pipeline {
      agent any 
      stages {
            stage('Stage 1') {
               steps {
               pwsh ('''
            $text = ((Invoke-Webrequest -Uri "https://uinames.com/api/?amount=$env:number" -UseBasicParsing).content | ConvertFrom-Json).name
   Write-Output "$text"
   ''')
               }
            }
      }
   }
   ```

3. Go ahead and run it a few times locally to make sure it works. Next use something like POSTman to send a GET to the URL and see if it kicks off the job.

4. So now go into VRO and run the workflow 'Add A Rest Operation' and choose your existing Jenkins server. Set it up like:
   - Name: jenkinsParameter
   - TemplateURL: `https://jenkins.domain.com/job/pwsh-with-parameter/buildWithParameters?number={number}&token=954c2e51-a9d2-4600-9cb2-5d99942716392b`
   - HTTP Method: GET
   - NOTE: You are literally placing `{number}` in the template URL. This is how VRO will treat input variables.

5. Now go clone your previous workflow and create one like:
   - Variables tab = `jenkinsNumber` with a type of 'REST:RESTOperation' and pointing to the operation from the previous step
   - Inputs/Outputs tab = `number` that is just an input with a type of 'string'
   - Schema Tab:
     - Make sure to bind `jenkinsNumber` and `number` to the Input/Outputs section on the scriptable task screen.
     - On the actual scripting pane, just comment out `var objRESTRequest = getFact.createRequest(null,null);` (line 11) on previous post under step 4.
     - Add a new line under it with: `var objRESTRequest = jenkinsNumber.createRequest([number],null);`
   - Run the job, it should return as many names as you put in the input. Login to Jenkins web UI and verify if needed.

6. In case you were wondering for two parameters, you follow the same steps and:

   - When it gets to the rest operation workflow, just put it in like: `https://example-jenkins.domain.com/job/example/buildWithParameters?UserEmail={UserEmail}&GroupName={GroupName}&token=954c2e51-a9d2-4600-9cb2-5d99942716392b`
   - And then in your scripting pane, use `var objRESTRequest = restOperationName.createRequest([UserEmail, GroupName], null);`