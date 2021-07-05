---
title: Renewing SSL Certificates
date: 2017-10-28T06:01:24+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/10/renewing-ssl-certificates/
categories:
  - WindowsServer
tags:
  - Certificates
---
<!--more-->

### Description:

Follow these steps to renew a SSL Cert. Also, take a look at Digicert's site: [Renewal FAQ](https://www.digicert.com/ssl-certificate-renewal/#renewal-faq)

Q: Why Do I Need to Install a New Certificate if I Am Only Renewing My Existing Certificate?

ANSWER: It is not possible to extend the life of a certificate because certificate expiration dates are hard-coded into the certificates themselves. So, technically, when you 'renew' a certificate you are purchasing an entirely new certificate, just for the same company/domain. Because of this, DigiCert must issue a new SSL Certificate to replace the existing one on your server and you must install the certificate just like you did before.

Because it can be difficult to remember all the company and domain information for your expiring certificate, DigiCert automatically includes some of this information in our renewal request wizard. If you need to update this information you can do so during the request process. Note that if any of your organization's information has changed (location, etc.) you may need to provide new documentation to verify the changes. You should also change the information in the CSR.

Q: Do I Need to Create a New CSR to Renew My SSL Certificate?

ANSWER: Depending on your server type, you may also have to generate a new CSR. Many servers, including Apache servers, allow you to install a new certificate without generating a new CSR. However, the following servers require that you generate a new CSR:

Windows servers

Tomcat servers

Java-based servers

Most applications, such as firewalls, load balancers, etc.

If you have any of the above server platforms, you must generate a new CSR before you submit your renewal. Note that if you have a Windows server you can use the free DigiCert Certificate Utility for Windows which has an easy CSR generator for Windows servers.


### To Resolve:

1. Get old order number.

2. Add funds to account.

3. [Submit a CSR](https://docs.digicert.com/manage-certificates/renew-ssltls-certificate/) (Certificate Signing Request) => Two options: Submit a new request (what I usually do) or if renewing the same cert, resubmit the original CSR.

4. Submit domain verification => just reply to email the CA sends you.

5. Once they get the order, you can download the new cert or wait for them (the CA) to email it. Either way, you just go

Copying the text as you probably don't need screenshots:

### How to Generate an SSL Certificate Renewal CSR in Microsoft IIS 8 and IIS 8.5

Open Internet Information Services (IIS) Manager.  
From the Start screen, type and click Internet Information Services (IIS) Manager.  
In Internet Information Services (IIS) Manager, under Connections, click your server's Hostname.  
In the center menu, in the IIS section, double-click the Server Certificates icon.

In the Actions menu, click Create Certificate Request to open the Request Certificate wizard.

On the Distinguished Name Properties page, enter the following information:  
Common name Enter the name that will be used to access the certificate. This name is usually the fully-qualified domain name.  
For example, www.domain.com or mail.domain.com.  
Organization Enter the legally registered name of your organization/company.  
Organizational Unit Enter the name of your department within the organization. For example, you can enter IT or Web Security.  
You can also leave the text box blank.  
City/locality Enter the city in which your organization/company is located.  
State/province Enter the state/province in which your organization/company is located.  
Country/region Type or select your two-digit country code from the drop-down list.  
If necessary, you can find your two-digit country code in our SSL Certificate Country Codes list.

Click Next.  
On the Cryptographic Service Provider Properties page, enter the following information:  
Cryptographic service provider In the drop-down list, select Microsoft RSA SChannel&#8230;, unless you have a specific cryptographic provider.  
Bit length In the drop-down list, select 2048.

Click Next.  
On the File Name page, click the … box to browse to a location where you want to save the CSR file, enter the filename, and then click Open.

If you only enter the filename without selecting a location, your CSR file is saved to the following location: C:\Windows\System32.  
Make sure to note the filename and the location where you saved your CSR file. You need to open this file as a text file, copy the entire body of the text file (including the Begin New Certificate Request and End New Certificate Request tags), and paste it into the online order process when you are prompted.  
Click Finish.  
Next, log into the DigiCert® Management Console.  
Under Order next to the order that you want to renew, click + to expand the options for the order and then, click Renew.

Follow the instructions to place the order with DigiCert to renew your SSL Certificate.

### SSL Certificate Renewal Installation: Microsoft IIS 8 and IIS 8.5

Installation Instructions to Renew your SSL Certificate: Windows 2012 Server  
Save your certificate file to the IIS server from which the CSR was generated.  
Open Internet Information Services (IIS) Manager.  
From the Start screen, type and then click Internet Information Services (IIS) Manager.  
In Internet Information Services (IIS) Manager, under Connections, click your server's Hostname.  
In the center menu, in the IIS section, double-click the Server Certificates icon.

In the Actions menu, click Complete Certificate Request to open the Complete Request Certificate wizard and complete your request.

On the Specify Certificate Authority Response page, under File name containing the certification authority's response, click the … box to browse to the .cer certificate file that DigiCert sent you, select the file, and then click Open.

Next, enter the following information:  
Friendly name Enter a friendly name for the certificate. You will use this name to identify this certificate.  
We recommend that you add DigiCert and the expiration date to the end of your friendly name, for example: yoursite-DigiCert-Nov2015.  
This information helps identify the issuer and expiration date for each certificate. It also helps distinguish multiple certificates with the same domain name.  
Select a certificate store&#8230; In the drop-down list, select a certificate store.  
Click OK.  
In Internet Information Services (IIS) Manager, under Connections, expand your server's name, expand Sites, and then select the site on which you want to enable SSL.

In the Actions menu, under Edit Site, click Bindings.  
In the Site Bindings window, select binding for https, and then click Edit.

In the Edit Site Binding window, in the SSL certificate drop-down list, select your newly installed SSL Certificate by its friendly name, and then click OK.

Your new SSL Certificate should now be installed to your server.