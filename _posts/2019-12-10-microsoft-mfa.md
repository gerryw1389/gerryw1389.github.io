---
title: 'Microsoft MFA'
date: 2019-12-10T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/12/microsoft-mfa/
categories:
  - WebSoftware
tags:
  - Cloud
---
<!--more-->

### Description:

This post will serve as the foundation post for things I do within the Azure Web UI.


### Description:

1. To create a service account that is exempt from MFA (for Power Automate):
   - Create user in Azure AD
   - Open a new window and sign in as that user.
   - Now go back into AzureAD and look at sign-in's under that user. Under 'Conditional Access', it will list the policy that requires 2FA.
   - In our case, it was 'Baseline policy: Require MFA for Admins (preview)'
   - So now go back to Azure Active Directory => Conditional Access => $name of policy => Users => Exclude => Add your account there

2. If a user says they lost their phone and needs to activate MFA on a new one: 
   - Go to user in Azure => Authentication Methods => Select button `Require re-register MFA`
   - Tell user to go to [aka.ms/mfasetup](https://aka.ms/mfasetup) and reconfigure their phone number used for MFA