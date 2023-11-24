---
title: Send Gmail Using Powershell
date: 2017-12-24T05:01:17+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/send-gmail-using-powershell/
tags:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

This script template will allow you to send emails from a Powershell script.

### To Resolve:

1. Script

   ```powershell
   $From = "from@gmail.com"
   $To = "to@gmail.com"
   $Subject = "Read this"
   $Body = "<HTML><HEAD><META http-equiv=""Content-Type"" content=""text/html; charset=iso-8859-1"" /><TITLE></TITLE></HEAD>"
   $Body += "<BODY bgcolor=""#FFFFFF"" style=""font-size: Small; font-family: TAHOMA; color: #000000""><P>"
   $Body += "Dear <b><font color=red>customer</b></font><br>"
   $Body += "This is an <b>HTML</b> email<br>"
   $Body += "Click <a href=http://www.google.com target=""_blank"">here</a> to open google <br>"
   $SMTPServer = "smtp.gmail.com"
   $SMTPPort = "587"
   # $Cc = "YourBoss@YourDomain.com"
   # $Attachment = "C:\temp\Some random file.txt"

   # Optionally include:
   # -Attachments $Attachment
   # -Cc $Cc

   Send-MailMessage -From $From -to $To -Subject $Subject `
     -BodyAsHTML -Body $Body -SmtpServer $SMTPServer -port $SMTPPort -UseSsl `
     -Credential (Get-Credential -Credential "from@gmail.com")
   ```

2. Source is maintained under [gwNetworking](https://github.com/gerryw1389/powershell/blob/main/gwNetworking/Public/Send-Gmail.ps1)