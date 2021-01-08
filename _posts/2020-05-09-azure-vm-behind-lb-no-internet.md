---
title: Azure VM Behind LB No Internet
date: 2020-05-09T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/azure-vm-behind-lb-no-internet
categories:
  - Azure
tags:
  - Cloud
  - Azure-NATGateways
---
<!--more-->

### Description:

So one of the first tasks we had to do in Azure is load balance some VMs. Since this was an internal LB, I assumed that VM's would still have internet access but I was wrong.

### To Resolve:

1. If you place VM's behind an internal LB with the Standard SKU, they will not have internet access. The only way is if you:

   - Give each VM a public IP address
   - Change the LB to a public LB
   - Move them to a NAT Gateway - see [here](https://docs.microsoft.com/en-us/azure/virtual-network/quickstart-create-nat-gateway-portal)

### References:

["Azure Standard Internal Load Balancer backend machines partial internet access"](https://stackoverflow.com/questions/49979793/azure-standard-internal-load-balancer-backend-machines-partial-internet-access)

["Allow Internal Load Balancer Internet Access "](https://feedback.azure.com/forums/217313-networking/suggestions/37768234-allow-internal-load-balancer-internet-access)

["Generic search"](https://www.google.com/search?sxsrf=ALeKk00Z5TtdlBtkZR-y5gj-NSnWKwGr7A:1588971813646&q=azure+internal+load+balancer+vm+doesn%27t+get+internet&spell=1&sa=X&ved=2ahUKEwinkYqklaXpAhUBKKwKHd8IA-0QBSgAegQIDRAn&biw=1920&bih=938)

