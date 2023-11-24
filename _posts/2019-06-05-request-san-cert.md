---
title: Request SAN Cert
date: 2019-06-05T23:56:46-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/request-san-cert/
tags:
  - WindowsServer
tags:
  - Certificates
---
<!--more-->

### Description:

So the general flow for getting a HTTPS cert is straight-forward. You run a cert request on the server, you upload the request to your third party Certificate Authority (CA), you download their response, and then you import it using `certlm.msc` under the personal store. You then use whatever application software to bind the cert to the listener.

But for SAN certs (servers that are load balanced), the way I do it is I `add` a new domain under the CSR that the server will respond on in addition to the servers hostname and send that in the CSR Request. Then when processing the cert, I make sure the third party CA includes it in the SAN Cert which is different than a regular cert. Here is how:

### To Resolve:

1. In the actual request, add/modify this section:

   ```escape
   [RequestAttributes]
   SAN="dns=loadbalanced.domain.com"
   ```

   - If you have multiple domains you want it to listen on, add them like so: `SAN="dns=not.server2008r2.com&dns=stillnot.server2008r2.com&dns=meh.2003server.com"`

2. Then in the web GUI for your third party CA, choose `MultiDomain SSL`

3. You would do this for each server behind the load balancer by replacing `loadbalanced.domain.com` with the front end DNS entry for your load balancer.
