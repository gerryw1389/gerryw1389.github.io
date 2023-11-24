---
title: Create A SSL Certificate
date: 2016-05-29T04:30:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/create-a-ssl-certificate/
tags:
  - Security
tags:
  - Certificates
  - WebServer
---
<!--more-->

### Description:

Follow these steps to create a SSL Certificate in Windows Server 2012 with Digicert (a common CA(Certificate Authority)). Note you will need IIS v8 or 8.5 installed by installing the IIS Role under Server Roles.

### To Resolve:

1. Open IIS Manager => Select your server name on the top left => Server Certificates

2. After selecting it, click on &#8220;Create Certificate Request..&#8221;.

3. Fill it out the &#8220;Distinguished Name Properties&#8221; window accordingly:

   - Common Name = The name through which the certificate will be accessed (usually the fully-qualified domain name, e.g., www.domain.com or mail.domain.com).

   - Organization = The legally registered name of your organization/company.

   - Organizational unit = The name of your department within the organization (frequently this entry will be listed as &#8220;IT,&#8221; &#8220;Web Security,&#8221; or is simply left blank).

   - City, State, Country = Self Explanatory.

   <img class="alignnone size-full wp-image-641" src="https://automationadmin.com/assets/images/uploads/2016/09/create-a-ssl-cert.png" alt="create-a-ssl-cert" width="688" height="524" srcset="https://automationadmin.com/assets/images/uploads/2016/09/create-a-ssl-cert.png 688w, https://automationadmin.com/assets/images/uploads/2016/09/create-a-ssl-cert-300x228.png 300w" sizes="(max-width: 688px) 100vw, 688px" />
   
   
4. Click &#8220;Next&#8221; and then move on to the &#8220;Cryptographic Service Provider Properties&#8221; window. Select &#8220;Microsoft RSA Schannel..&#8221; and &#8220;2048&#8221; for bit length => Next => Save the file somewhere you will remember. You will need to open this file and copy and paste the entire file into the Online Order Request in the following steps.

5. Fill out the request on Digicerts website and they will email you the .cert file. Save it where you know how to get to it.

6. Open IIS Manager => Select your server name on the top left => Server Certificates.

7. Click on Server Certificates => Complete CSR Request => Upload the cert file (friendly name = used by server admin to distinguish) => Choose &#8220;Personal&#8221; cert store for a single cert.

8. The certificate is now installed. Note that for Multiple Certificates using SNI, you would do the same steps but choose &#8220;Web Hosting&#8221; store instead. Also, for your second site, when you &#8220;Add Site Binding&#8221; you MUST check the box that says &#8220;Require Server Name Indication&#8221;.

9. (Optional) If you requested the cert for a website, you would then open IIS Manager => Sites => (SiteName) => Bindings => Add => Add Site Bindings => Protocol: HTTPS/ Port: 443/ Cert: CertName from earlier.