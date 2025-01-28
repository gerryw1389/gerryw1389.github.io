---
permalink: /about/
title: "About"
layout: single
classes: wide
---

Hello, my name is Gerry and I wrote this blog to store information about lessons I have learned over time through my career from Tech Support => SysAdmin => Cloud Engineer => Eventually Cloud Architect. I'm mostly following [the standard devops path](https://roadmap.sh/devops). You will find these days it mostly covers deploying resources in Azure using Terraform with Github Actions. Every now and then I get to use my [Powershell](https://automationadmin.com/tags/#powershell) experience as well!

Many people who write blogs are highly skilled in their domain and speak at conferences, travel the world to enlighten others, and are generally seen as an "authority" on their content. This blog is not that. I simply write posts that help me remember the steps I took when researching and deploying an automation solution. I take what I did on my job, sanitize it, and then publish here for me to search later. If others find it useful -- great! If not, no worries! This blog is not meant to be a main source of revenue (though I do use Google Ads - see [terms](https://automationadmin.com/terms/)). I do accept [donations](https://www.paypal.com/paypalme/gerryw1389) and I have setup [Utterances](https://mmistakes.github.io/minimal-mistakes/docs/configuration/#utterances-comments) to be more engaging in the communinity, but I certainly expect that most readers will just pick up a few things from my simple to-the-point style of posting unlike most other blogs. Thanks for stopping by!

### My Interests Over Time:

1. Cloud Engineer:
   - Post Tags/Categories:
     - [**Terraform**](https://automationadmin.com/tags/#terraform)
     - [Azure](https://automationadmin.com/tags/#azure)
     - [Azure Devops/Github Actions](https://automationadmin.com/tags/#cicd)
     - [Git](https://automationadmin.com/tags/#versioncontrol) 
   - My major focus has been "Deploying of all Azure Services using Azure Devops/Github Actions + Terraform". Everything is done through IaC instead of Azure Portal. Challenge mode on!
   - AKS deployment/management. Will post more on this in the future but for now just learning how to use [kubectl and k9s](https://automationadmin.com//2022/07/kubectl-k9s) for interacting with deployed clusters. Stay tuned.
   - Powershell + Python scripting to be ran by [Azure Devops Scheduled Tasks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/scheduled-triggers?view=azure-devops&tabs=yaml)/Azure Automation/Logic Apps/Function Apps. This will never change as scripting is an [incredibly valuable skill](https://automationadmin.com/2020/02/importance-of-learning-scripting/) that can be used anywhere/anytime for automation.

2. Automation Engineer:
   - Post Tags:
     - [Azure-Automation](https://automationadmin.com/tags/#azure-automation)
     - [Azure-FunctionApps](https://automationadmin.com/tags/#azure-functionapps)
     - [Azure-KeyVault](https://automationadmin.com/tags/#azure-keyvault)
     - [Azure-LogAnalytics](https://automationadmin.com/tags/#azure-loganalytics)
     - [Azure-LogicApps](https://automationadmin.com/tags/#azure-logicapps)
     - [CICD](https://automationadmin.com/tags/#cicd)
     - [ConfigManagement](https://automationadmin.com/tags/#configmanagement)
     - [Powershell](https://automationadmin.com/tags/#powershell)
     - [Python](https://automationadmin.com/tags/#python)
     - [RestAPI](https://automationadmin.com/tags/#restapi)
     - [VersionControl](https://automationadmin.com/tags/#versioncontrol)
   - This position used Azure Services with a focus in Automation, but it didn't focus at all on Infrastructure as Code but instead used [serverless](https://automationadmin.com/2021/01/function-apps-with-logic-apps) automation.
   - This is where I shifted focus from on-prem automation to cloud automation specifically in Azure. Also, [this post](https://automationadmin.com/2018/11/aws-sysadmin-guide/) helped me change my mindset at that time.
   - Another great career changing post was [this](https://www.reddit.com/r/sysadmin/comments/cdlar7/psa_still_not_automating_still_at_risk/) one.

3. Systems Administrator:
   - Post Tags/Categories: [Powershell](https://automationadmin.com/tags/#powershell), [Windows Server](https://automationadmin.com/tags/#windowsserver), [Linux Server](https://automationadmin.com/tags/#linuxserver)
   - I was a Windows SysAdmin but tried at every job to use Linux instead (where it makes sense (not for Active Directory for example)):
     - [How to be a Linux SysAdmin](https://automationadmin.com/2016/05/how-to-become-a-linux-sysadmin/)  
     - [How to be a Windows SysAdmin](https://automationadmin.com/2016/06/how-to-be-a-windows-sysadmin/)
   - Having trouble breaking in? See [this post](https://automationadmin.com/2016/05/breaking-into-sa-jobs/) for my advice.
   - Already in? [How far in?](https://www.docs.google.com/spreadsheets/d/1FBr20VIOePQH2aAH2a_6irvdB1NOTHZaD8U5e2MOMiw/pub?output=html) Please don't be cocky, read [the wiki](https://www.reddit.com/r/sysadmin/wiki/bootcamp/) to always improve your skills.

4. Remote Support Tech:
   - Mostly break fix and learning to script.
   - Learning to troubleshoot.
   - Everyone should read this at [the beginning of your career](http://www.catb.org/esr/faqs/smart-questions.html) and really understand what it is saying. This is not to be condescending, but I refuse to help people who do not try to help themselves. 80% of people who ask me questions about something are doing it out of sheer laziness - no more, redirect them to this page and ask them "show me where you got stuck..."

### General Advice

1. For those that are new to the field of IT, my advice is to learn the following skills in the following order:
   - Foundational knowledge: Hardware, Software, Networking. These are the core of IT systems with Software being the largest. But at a minimum you should know:
     - [Hardware](https://automationadmin.com/tags/#hardware): What components go into a computer - from disk drives, to memory sticks (RAM), to Raid Arrays and on. This may get less and less relevant as time goes on where Cloud providers extract this away but it is still important as we may shift back on-prem in the future once vendor lockin is not as strong. Currently cloud providers such as GCP, AWS, and Azure have attractive pricing to bring companies to their platform but once they capture a large enough market there is nothing stopping them from increasing their pricing because they know it will take enterprises years to migrate back on-prem. And obviously being publically traded companies they actually have to do this to increase share holder value so keep this in mind.
     - Software: This goes from anything between what an Operating System is, to user installed programs, to Server Applications versus Client Applications. 
     - [Networking](https://automationadmin.com/tags/#networking): I personally feel that every person in IT should be CCNA certified at the beginning of their career no matter what path they choose. Not because I'm a Cisco shill, quite the opposite actually, I don't care what provider but you need to know the basics: Private IP verus Public IP, NAT, Firewall Rules, etc. At a minimum, you should try to [visualize a path](https://automationadmin.com/2020/08/basic-network-troubleshooting) networking traffic takes between two devices.
   - So you will never master everything in those categories as each are infinite in depth where you can spend your whole career getting deeper and deeper, so you should strive to have a SysAdmin level knowledge (hint: go for [level 50](https://www.docs.google.com/spreadsheets/d/1FBr20VIOePQH2aAH2a_6irvdB1NOTHZaD8U5e2MOMiw/pub?output=html) ) in each.
   - The best advice above all is to learn to troubleshoot. The way you troubleshoot something is you have to visualize how it works as deep as you can. Have you heard of the ["what happens when you google?"](https://github.com/alex/what-happens-when) repo? Do this but with **EVERYTHING** that you can.

2. How to Advance:
   - Look for a [new demanding job](https://thedailywtf.com/articles/Up-or-Out-Solving-the-IT-Turnover-Crisis) once you feel you have learned all you can and you don't see upwards mobility.
     - Make sure to [interview them](https://automationadmin.com/2016/04/interview-questions/) more than they interview you :)
     - Try to give your current position 3 years minimum, it can look bad if you jump ship too often.
   - Try to never be the smartest person the room.
     - I'm a fan of [skills checklists](https://roadmap.sh/devops) so that I'm always learning something new, see above.
   - Be a tinker by nature:
     - When you install programs, do you modify the themes, settings, sync options, encryption options? See my [tweaks](https://automationadmin.com/tags/#tweaks) tag for example. For example, it drives me crazy that people install vscode and don't know about `settings.json` [tweaks and extensions](https://github.com/gerryw1389/misc/blob/main/vscode/settings-sync.json).
     - Do you regularly go out of your way to learn how $x works? See [this list](https://github.com/Kickball/awesome-selfhosted) of things you can install in your [homelab](https://automationadmin.com/tags/#virtualizationsoftware) (newer version [here](https://automationadmin.com/lab)).
       - See my [setup](https://automationadmin.com/tags/#setup) tag for example.
       - After you stand something up, take notes of each step and then post them on [a blog](https://automationadmin.com/2019/06/wordpress-to-jekyll/) so you can showcase your skills.
         - This can be a self hosted Wordpress instance or preferably, Github Pages with many blog links pointing to your Github repos.
     - Last but not least, focus mostly on [scripting](https://automationadmin.com/2020/02/importance-of-learning-scripting/). I would do powershell for Windows and bash/python for linux servers.
       - I always explain scripting to be like legos - Super small chunks of things that you learn that build the foundation for any kind of automation you can think of. If you are interested in learning I would suggest Powershell or Python (or both)
         - See [this intro post on powershell](https://automationadmin.com/2018/02/new-to-powershell/).
         - See [this intro post on python](https://automationadmin.com/2020/11/new-to-python).
       - You will never not have an in-demand job if you know how to write scripts, especially if built on a SysAdmin foundational knowledge (how to build servers, how to [picture networking](https://automationadmin.com/2020/08/basic-network-troubleshooting), how to use [orchestration tools](https://automationadmin.com/tags/#orchestration) for example)
   - Work on your [people skills](https://automationadmin.com/2016/05/people-skills/) yo!
   - Get certifications with tech you plan to use the most, especially with cloud providers if you plan to work in cloud!
   - Create different Github Repos for different tech that you learn. This will help conceptualize the technologies based on categories. For example my Github has:
     - A [powershell](https://github.com/gerryw1389/powershell) repo
     - A [python](https://github.com/gerryw1389/python) repo
     - A couple [terraform](https://github.com/gerryw1389/terraform-examples) repos
     - Etc.

### My Certs:

1. 2021-10-02: Azure Solutions Architect
   - ![Solutions Architect](https://automationadmin.com/assets/images/uploads/certs/az303-az304.png){:class="img-responsive"}
   - 2021-10-02: Microsoft Azure Architect Design (AZ304)
   - 2021-08-01: Microsoft Azure Architect Technologies (AZ303) 
   - [Verify](https://learn.microsoft.com/api/credentials/share/en-us/gerryw1389/B5DCB300D654DA75?sharingId=2FE55661222C38FD)

1. 2020-05-16: Microsoft Azure Administrator (AZ103)
   - ![AZ103](https://automationadmin.com/assets/images/uploads/certs/az103.png){:class="img-responsive"}
   - [Verify](https://learn.microsoft.com/api/credentials/share/en-us/gerryw1389/C9927E497853FBAE?sharingId=2FE55661222C38FD)

1. 2016-06-17: Cisco Certified Network Associate: Routing and Switching (CCNA R&S)
   - ![CCNA](https://automationadmin.com/assets/images/uploads/certs/ccna.png){:class="img-responsive"}

1. 2015-05-02: Testout Network Pro
   - ![TestOut Network Pro](https://automationadmin.com/assets/images/uploads/certs/testout.png){:class="img-responsive"}

### Archived:

Looking for the older version of this page? Check [here](https://automationadmin.com/2016/01/archived-about-me).
