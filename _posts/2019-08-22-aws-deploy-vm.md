---
title: AWS Deploy VM
date: 2019-08-22T08:00:44-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/08/aws-deploy-vm/
categories:
  - WebSoftware
tags:
  - Cloud
---
<!--more-->

### Description:

Follow this guide to deploy a VM in AWS via GUI. Pretty basic, but still noted.

### To Resolve:

1.	Sign in to AWS, type `EC2` under services. Now `Launch Instance`.

2.	Choose with `Windows Base 2016` image

3.	Choose size – I chose T3.small

4.	On this screen, make sure to choose:
   - Subnet = Choose a subnet in your VPC.
   - IAM Role = Choose an IAM Role you have configured
   - Protect against accidental deletion = Checked
   - Enable Cloudwatch = Checked

5.	On the `Add Storage`, just keep defaults

6.	On `Add Tags`, enter `Owner` and `$Department who owns the server`

7.	For Security Groups, choose `Default` for now. We will eventually be breaking these out by groups like – Web servers, Domain Controllers, ect.

8.	Click `Review and Launch`. A screen will pop up and ask for you to use some keys. Click to `Create a new key pair` and enter your name. Now download the .pem file to your machine.

9.	After your server is created, go to `EC2 – Instances` and select your server and name it by clicking on the pencil icon.

10.	After selecting your machine, click on `View Inbound Rules`. Make sure that Source is `$yourPublic IP` for port `3389` and `ICMP – Protocol Version 4`. 

11. Lastly, choose `Connect` to connect to the machine. It will ask you to `Get Password`. Just point it to your pem file you downloaded earlier and you Copy/paste the password somewhere. Now go back and choose `Download RDP file` and RDP to your machine using `Administrator/$yourPassword`. 