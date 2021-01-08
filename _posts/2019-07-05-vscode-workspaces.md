---
title: VSCode Workspaces
date: 2019-07-05T01:19:05-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/07/vscode-workspaces/
categories:
  - LocalSoftware
---
<!--more-->

### Description:

Short post here - Just wanted to mention that if you have issues connecting to different repos (work / home) like Gitlab and Github, it might be best to setup Workspaces in VSCode. I have been using the following setup for a couple months and I think I found my way:

### To Resolve:

1. Workspace `notes` is the default workspace I open when I launch VScode, I setup it up by changing the properties in the VSCode launcher to `"C:\Program Files\Microsoft VS Code\Code.exe" c:\google\apps\vscode\notes.code-workspace`

2. I then have other `.code-workspace` files in `c:\google\apps\vscode\` that point to different things:
   
   - work-powershell - For working with Gitlab
   - work-puppet - For working with Gitlab
   - home-powershell - for updating my Github scripts at home
   - home-website - For updating this site

3. I even went as far as creating a function in my $Profile in Powershell so that if I open code and am too lazy to `Open New Window - Open Workspace` I can just run the function from within VSCode and it will open the windows for me:

   ```powershell
   Function Start-Workspaces {
   [Cmdletbinding()]
   Param
   (
      [Parameter(Position = 0, Mandatory = $False)]
      [Switch]$Powershell
   )
   If ( $Powershell)
   {
   code C:\google\apps\vscode\home-powershell.code-workspace
   code C:\google\apps\vscode\work-powershell.code-workspace
   }
   Else
   {
   code C:\google\apps\vscode\home-powershell.code-workspace
   code C:\google\apps\vscode\home-website.code-workspace
   code C:\google\apps\vscode\work-powershell.code-workspace
   code C:\google\apps\vscode\work-puppet.code-workspace
   }
   }
   ```