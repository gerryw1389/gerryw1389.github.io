---
title: Export A Private Key
date: 2016-05-29T03:33:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/export-a-private-key/
categories:
  - Security
tags:
  - Certificates
---
<!--more-->

### Description:

Follow these steps to export a private key from one server to another. Note that by default, private keys are stored in the computer's certificate store.

### To Resolve:

1. Run => mmc => Add/Remove Snap In => Certificates => Add => My User Account.

2. Select Certificates => Current User => Personal => Certificates.

3. Select the cert you want => right click => Export => Yes, Export the Private Key => (Enter A Password) => Export.

4. On the other machine, repeat steps 1 and 2. Now you right click the certificate under the console root and select import. Enter the password from earlier, optionally select the check box that allows the key to be exportable again, and choose the personal store to complete the import.