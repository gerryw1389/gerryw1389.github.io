---
title: Office Install Tasks
date: 2018-03-31T23:49:42+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/office-install-tasks/
categories:
  - LocalSoftware
tags:
  - MSOffice
---
<!--more-->

### Description:

Follow these steps to help with uninstalling, reactivating, or installing Office.

### To Resolve:

### To Uninstall All Versions Of Office From Machine:

1. Download the [Office Deployment Tool](https://www.microsoft.com/en-us/download/details.aspx?id=49117)

2. Extract to `c:\scripts` and rename `setup.exe` to `odt.exe`

3. Configure a configuration file (XML): [XML Editor](https://officedev.github.io/Office-IT-Pro-Deployment-Scripts/XmlEditor.html)

   - I create `uninstall.xml` at `c:\scripts` with the following value:

   ```powershell
   <Configuration>
      <Remove All="TRUE"/>
   </Configuration>
   ```

4. Open Powershell in `C:\scripts` and run:

   ```powershell
   & .\odt.exe /configure .\uninstall.xml
   ```

### To Change A Product Key:

1. Get new key and copy to a text file so we can copy and paste from.

2. Run each line one by one in elevated CMD or Powershell:

   ```powershell
   cd C:\Program Files (x86)\Microsoft Office\Office16
   cscript ospp.vbs /dstatus
   :: shows XQBQ9
   cscript ospp.vbs /unpkey:XQBQ9
   cscript ospp.vbs /inpkey:XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
   cscript ospp.vbs /act
   :: Open office, should be activated!
   ```

### To Deploy Office 365:

1. Create a [ProPlusInstallGenerator](https://officedev.github.io/Office-IT-Pro-Deployment-Scripts/XmlEditor.html) to create a .msi. Alternatively, see about [github.com/OfficeDev/Office-IT-Pro-Deployment-Scripts](https://github.com/OfficeDev/Office-IT-Pro-Deployment-Scripts) under the deployment section. More details:  

   - [Automating the Removal of Old Office Versions to Upgrade to 2016](https://joshheffner.com/automate-removal-old-office-versions-upgrade-2016/)  
   - [Deploy Office 2016 using SCCM 2012 – Click-to-Run Version](https://www.systemcenterdudes.com/sccm-2012-office-2016-deployment/)

2. Deploy the MSI as part of a task sequence in MDT (imaging), as a GPO, or manually.