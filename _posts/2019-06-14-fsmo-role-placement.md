---
title: FSMO Role Placment
date: 2019-06-14T23:13:34-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/fsmo-role-placement
categories:
  - WindowsServer
  - SysAdmin
tags:
  - ActiveDirectory
---
<!--more-->

### Description:

The following is a best practice type advice regarding FSMO placements in your domain.

### General Rules

- Schema Master Enterprise - Schema Master/ Domain Naming Master should be on the same server, the root server (PDC) of the multi domain.
- Domain Naming Master Enterprise - Schema Master/ Domain Naming Master should be on the same server, the root server of the multi domain.
- Primary Domain Controller Domain - PDC and RID should be same server
- RID Domain - PDC and RID should be same server
- Infrastructure Master DomainApplication partition - Doesn't matter if all DC's are Global Catalogs. 

### To Resolve:

1. For a single domain forest: Simply separate the enterprise level roles from the domain level roles (there is no work for the Infrastructure Master role in a single domain forest, so it can be on any DC whether it hosts the global catalog or not).

   - SGLDMDC01 – Schema, Domain Naming
   - SGLDMDC02 – PDC, RID, Infrastructure

2. Multi domain: So, for our forest root domain, we have two DC's with FSMO roles (we may have many other replicas):

   - RTDMDC01 – PDC, Schema, Domain Naming
   - RTDMDC02 – RID, Infrastructure

3. Child domain: So, in our child domains, we have a single DC with FSMO roles (we may have many other replicas).

   - CHLDMDC01 – PDC, RID, Infrastructure

### References:

["FSMO Roles Separation Best Practices"](https://nyuktech.wordpress.com/2014/06/16/fsmo-roles-separation-best-practices/)
