---
title: Use AWS CLI With Azure SSO
date: 2020-04-23T08:06:24-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/04/use-aws-cli-with-azure-sso
categories:
  - Windows
tags:
  - Cloud
---
<!--more-->

### Description:

Using AWS CLI is pretty straight forward and you can just follow the guides to setup and use, but what if your organization uses Azure SSO and you need to administer AWS? Well, here are the steps I have done to get through authentication. Many thanks to [a reddit comment from /u/myron-semack/](https://www.reddit.com/r/aws/comments/9ezp3u/aws_cli_with_azure_ad_as_idp/) for getting me started.

### To Resolve:

1. Install AWS CLI, Node, and aws-azure-login:

   - [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html)
   - [Node](https://nodejs.org/en/download/) - Make sure to add it to your PATH during the install wizard
   - Open PowerShell and run: `npm install -g aws-azure-login`
   - You should run `npm update -g aws-azure-login` from time to time to make sure you have the latest version.

2. Configure your profile

   - Open Powershell and run: `aws-azure-login --configure`
   - If you want to setup multiple profiles, you can run `aws-azure-login --configure --profile profilename`

   ```escape
   Configuring profile 'default'
   ? Azure Tenant ID: some-guid-for-your-organization
   ? Azure App ID URI: https://signin.aws.amazon.com/saml
   ? Default Username: yourEmail@domain.com
   ? Stay logged in: skip authentication while refreshing aws credentials (true|false) true
   ? Default Role ARN (if multiple): get-your-arn-based-on-role (maybe you can leave blank? format is normally arn:aws:iam::############:role/role-name)
   ? Default Session Duration Hours (up to 12): 1
   Profile saved.
   ```

3. Login:

   - Open Powershell and run: `aws-azure-login`
   - After a period of time, your credentials will expire and you will have to run aws-azure-login again. The time period will vary depending on inactivity, but it is typically several hours or days.

4. Now you can run things like `aws ec2 describe-instances` and so on and it should be authenticated.
