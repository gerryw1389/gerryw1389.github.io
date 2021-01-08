---
title: 'PS: Call C Sharp Code'
date: 2016-12-27T08:11:49+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/ps-call-c-sharp-code/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - OneLiners-Powershell
---
<!--more-->

### Description:

From [Microsoft](https://blogs.technet.microsoft.com/stefan_gossner/2010/05/07/using-csharp-c-code-in-powershell-scripts/), this is how you call C Sharp code into PS scripts:

### To Resolve:

1. Use the following template:  

   ```powershell
   $Assem = (
   …add referenced assemblies here…
   )
   $Source = @"
   …add C# source code here…
   "@
   Add-Type -ReferencedAssemblies $Assem -TypeDefinition $Source -Language CSharp
   ```

2. Example:

   ```powershell
   $Assem = (
   "Microsoft.SharePoint, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c" ,
   "Microsoft.SharePoint.Publishing, Version=14.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c"
   )
   $Source = @"
   using Microsoft.SharePoint.Publishing.Administration;
   using System;
   namespace StefanG.Tools
   {
   public static class CDRemoteTimeout
   {
   public static void Get()
   {
   ContentDeploymentConfiguration cdconfig = ContentDeploymentConfiguration.GetInstance();
   Console.WriteLine("Remote Timeout: "+cdconfig.RemoteTimeout);
   }
   public static void Set(int seconds)
   {
   ContentDeploymentConfiguration cdconfig = ContentDeploymentConfiguration.GetInstance();
   cdconfig.RemoteTimeout = seconds;
   cdconfig.Update();
   }
   }
   }
   "@
   Add-Type -ReferencedAssemblies $Assem -TypeDefinition $Source -Language CSharp
   [StefanG.Tools.CDRemoteTimeout]::Get()
   [StefanG.Tools.CDRemoteTimeout]::Set(600)
   # The last lines in the above listed sample demonstrates how to call the C# methods from Powershell.
   ```