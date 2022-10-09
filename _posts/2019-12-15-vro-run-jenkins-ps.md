---
title: 'VRO: Run Jenkins Powershell Script On Linux Host'
date: 2019-12-15T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/12/vro-run-jenkins-ps/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - Orchestration 
  - Scripting-RestAPI
  - CICD
---
<!--more-->

### Description:

This post will be following [Ben's post](https://ben.neise.co.uk/2016/09/05/vro-jenkins.html) but instead of having a Windows Jenkins server, we will be using our [Jenkins Server](https://automationadmin.com/2019/12/rhel7-deploy-jenkins/) which runs on RHEL 7. The post describes using [vRealize Orchestrator](https://automationadmin.com//2020/01/vrealize-orchestrator/) to call a Jenkins job and collect the results.

### To Resolve:

1. Install Powershell on the Jenkins server:

   ```shell
   curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo
   yum install powershell -y
   ```

2. Login to Jenkins web UI and:

   - New Item => 'pwsh-facts' (Pipeline) => Check the box 'Trigger builds remotely (e.g., from scripts)' and enter a random GUID (generate on your own)
   - Next, in the pipeline definition, enter:

   ```escape
   pipeline {
     agent any 
     stages {
         stage('Stage 1') {
             steps {
             pwsh ('''
         $text = ((Invoke-Webrequest -Uri "https://uselessfacts.jsph.pl/random.json?language=en" -UseBasicParsing).content | ConvertFrom-Json).text
         Write-Output "$text"
   ''')
             }
         }
     }
   }
   ```

   - source: [https://jenkins.io/blog/2017/07/26/powershell-pipeline/](https://jenkins.io/blog/2017/07/26/powershell-pipeline/)

   - Test your build => Success:

   ```escape
   Started by user username
   Running in Durability level: MAX_SURVIVABILITY
   [Pipeline] Start of Pipeline
   [Pipeline] node
   Running on Jenkins in /var/lib/jenkins/workspace/pwsh-facts@2
   [Pipeline] {
   [Pipeline] stage
   [Pipeline] { (Stage 1)
   [Pipeline] pwsh

   Caesar salad has nothing to do with any of the Caesars. It was first concocted in a bar in Tijuana, Mexico, in the 1920`s.
   [Pipeline] }
   [Pipeline] // stage
   [Pipeline] }
   [Pipeline] // node
   [Pipeline] End of Pipeline
   Finished: SUCCESS
   ```

   - I still haven't found out how to run a script, but I do know you can include a whole bunch of things between `pwsh ('''` and `''')`
   - For example, all the output streams will record in your logs:

   ```escape
   pipeline {
     agent any 
     stages {
         stage('Stage 1') {
             steps {
             pwsh ('''
         # Enable streams 3-6
         $WarningPreference = 'Continue'
         $VerbosePreference = 'Continue'
         $DebugPreference = 'Continue'
         $InformationPreference = 'Continue'

         Write-Output 'Hello, World!'
         Write-Error 'Something terrible has happened!'
         Write-Warning 'Warning! There is nothing wrong with your television set'
         Write-Verbose 'Do not attempt to adjust the picture'
         Write-Debug 'We will control the horizontal.  We will control the vertical'
         Write-Information 'We can change the focus to a soft blur or sharpen it to crystal clarity.'
     ''')
             }
         }
     }
   }
   ```

3. Anyhow, back on topic. Inside vRealize Orchestrator, run the workflow `Add A Rest Host` to add your Jenkins server:
   - Name: My Jenkins Server
   - URL: `http://server.domain.com:8080/jenkins/` (use the URL and port of your Jenkins server)
   - Connection timeout (seconds): 30.0 (you may wish to tune this for your specific requirements, but I'm leaving it as the default for now)
   - Operation timeout (seconds): 60.0 (you may wish to tune this for your specific requirements, but I'm leaving it as the default for now)
   - Configure Proxy settings
   - Use Proxy: No (Unless you have a proxy!)
   - Configure Host Authentication
   - Host authentication type: NONE
   - Now run the workflow `Add a REST Operation`:
   - Parent host: Select your new REST host My Jenkins Server (or whatever you called it)
   - Name: Generate useless fact
   - Template URL: This should be the URL to your job. You should be able to see this below the Trigger builds remotely (e.g., from scripts) section in the Jenkins job configuration. It will look something like /job/Generate%20Cat%20Fact/build?token=xxxxxxxxxxxxxxxxxxxxxxxxx
   - HTTP Method: GET
   - You can test this operation by right-clicking, then selecting Run workflow > Invoke a REST operation > Submit. It should run without errors (but it won't wait for the Jenkins job to complete, or give you any output)

4. Create the vRO Workflow which will run the Jenkins job, and get the results

   - Now we need an Orchestrator workflow which runs the operation, waits for it to complete and displays the status and output.
   - Using the Orchestrator client, create a new workflow. I'm going to call mine useless-fact
   - The workflow needs a single variable of type REST:RESTOperation, this should be set to your REST operation. My operation is `getFact`.
   - The workflow needs a single scriptable task, the REST:Operation attribute named `getFact` should be bound as an input. The script should be something like this:

   ```js
   #replace line 10 with your variable
   var jenkinsPollingIntervalMS = 1000;
   var buildURL = "";
   var buildResult = null;

   /*
   Create the request object. The two paramaters are:-
   - An array of values for the URL template paramaters. We have none, so this is null
   - Any content for POST or PUT operations. Ours is a GET, so this is also nulll
   */
   var objRESTRequest = getFact.createRequest(null,null);
   // Execute the REST operation
   var objRESTResponse = objRESTRequest.execute();
   System.debug("Status code: " + objRESTResponse.statusCode);
   // The location property gives us the URL of the queue item
   System.debug("Location: " + objRESTResponse.getAllHeaders().get("Location"));

   // Wait for job to be queued by looking for an "executable" property on the response
   while (buildURL === ""){
   var url = objRESTResponse.getAllHeaders().get("Location") + "api/json";
   var urlObject = new URL(url);
   result = urlObject.getContent() ;
   //System.debug(result);
   var objResult = JSON.parse(result);
   if (objResult.hasOwnProperty("executable")){
   System.debug(objResult.executable.url);
   buildURL = objResult.executable.url;
   }
   System.sleep(jenkinsPollingIntervalMS);
   }

   // Now that the job's queued, we need to wait for it to be completed
   while (buildResult === null){
   url = buildURL + "api/json";
   var urlObject = new URL(url);
   var result = urlObject.getContent() ;
   var objResult = JSON.parse(result);
   System.debug(result);
   System.debug("Build result:" + buildResult);
   buildResult = objResult.result;
   System.sleep(jenkinsPollingIntervalMS);
   }

   url = objResult.url + "consoleText";
   var urlObject = new URL(url);
   result = urlObject.getContent();
   // The result is the actual console output.
   System.log(result);
   System.debug("Build Result: " + buildResult);
   ```

5. I kept getting error:

   ```escape
   vro HTTP GET error : sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
   ```

6. The fix was a `reboot` after one of these changes:

   - Running workflow 'Import certificate from URL' = `https://jenkins.domain.com`
   - Running workflow 'Import a certificate from URL with certificate alias' = `https://jenkins.domain.com`
   - Navigate to `https://jenkins.domain.com` in a browser and download its cert locally as domain.cer. Then upload using workflows:
   - Running workflow 'Import a trusted certificate from a file' => domain.cer

7. After it was all said and done, this is what it looks like in the logs:

   - ![fact](https://automationadmin.com/assets/images/uploads/2019/12/fact.jpg){:class="img-responsive"}