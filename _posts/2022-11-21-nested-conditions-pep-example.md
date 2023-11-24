---
title: 'Terraform: Nested Conditional Example With Private Endpoint'
date: 2022-11-21T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/11/nested-conditions-pep-example
tags:
  - Azure
  - Terraform
---
<!--more-->

### Description:

Terraform doesn't have a `switch` statement like [powershell](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_switch?view=powershell-7.2) but it does have conditionals. If you want, you can actually nest conditionals though it might look ugly. One place I did this the other day is for the three radio buttons for public access for a resource with private endpoints.

Anyone who deals with public access to resources with [Private Endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints) in Azure is familiar with the Networking blade of resources that give you three radio buttons on the 'Firewalls and Virtual Networks' tab:

- "Allow public access from all networks" => Selecting this setting does not take away from private access if the resource has a private endpoint, it simply gives the `ability` of public to access the resource.
- "Allow public access from specific virtual networks and IP addresses" => This blocks all public traffic unless you specify IP addresses.
- "Disable public access" => This blocks all network traffic that is not coming through the Private Endpoint, should be the default.

### To Resolve:

1. So in our terraform code, let's assume we have `var.enable_pep` as a `bool` and `var.ip_rules` as a `list(string)` but optional, we could do the following to setup the three radio buttons:

   ```terraform
   resource "azurerm_key_vault" "kv" {
   name                        = "keyvault1"
   location                    = var.region
   resource_group_name         = var.resource_group
   enabled_for_disk_encryption = var.enabled_for_disk_encryption
   tenant_id                   = var.tenant_id

   # Keyvault => Networking => Firewalls and virtual networks Settings
   # if not enabling pep => "Allow public access from all networks" radio button selected
   # if enabling pep with ip rules => "Allow public access from specific virtual networks and IP addresses" radio button selected with ip rules defined. For this to work, public access must be true and the network_acls below will restrict.
   # if enabling pep with no ip rules => "Disable public access" radio button selected
   public_network_access_enabled = (var.enable_pep == true) && (length(var.ip_rules) > 0) ? true : ((var.enable_pep == true) && (length(var.ip_rules) == 0) ? false : true)

   # Only set Network ACLs if IP Rules are defined
   # NOTE 2022-10-21: I have noticed that even with this defined, sometimes it will choose the radio button "Disable public access". But.. if you move it up to "Allow public access from specific virtual networks and IP addresses" it will
   # have the IP addresses stored so it knows about them.
   # Also, if you add a single IP to the list and run another apply, it will move the radio button to the one you want. This has to be a glitch in the UI.
   dynamic "network_acls" {
      for_each = length(var.ip_rules) > 0 ? [1] : []
      content {
         bypass         = "AzureServices"
         default_action = "Deny"
         ip_rules       = var.ip_rules
      }
   }
   ```

1. So the first thing to do when you see a long conditional if you want to understand it is to copy it to notepad++ and dissect it (my opinion of course, you do you) :

   - `public_network_access_enabled = (var.enable_pep == true) && (length(var.ip_rules) > 0) ? true : ((var.enable_pep == true) && (length(var.ip_rules) == 0) ? false : true)`
   - First strip the final result, we know it's just the attribute [`public_network_access_enabled`](https://registry.terraform.io/providers/hashicorp/azurerm/3.20.0/docs/resources/key_vault#public_network_access_enabled)
   - Next let's add some line break to break it up:

   ```escape
   (var.enable_pep == true) && (length(var.ip_rules) > 0) ?  true
   : 
   ((var.enable_pep == true) && (length(var.ip_rules) == 0) ? false 
   :
   true)
   ```

   ```escape
   condition1: (var.enable_pep == true) && (length(var.ip_rules) > 0) 
   condition1_true_value: true
   condition1_false_value: ((var.enable_pep == true) && (length(var.ip_rules) == 0) 
   
   condition2: (var.enable_pep == true) && (length(var.ip_rules) == 0) 
   condition2_true_value: false
   condition2_false_value: true
   ```

   - So first, if enable_pep is `true` and the `ip_rules` have at least one value defined (they should default to an empty list `[]` which gives lenght `0` causing this to be `false`), then the true condition fires. It is set to `true`. According to my comments, this is because they have to be true for you to allow any public IPs and are dynamically listed below in the `dynamic "network_acls"` section.

   - OK, so what ifyou pass `enable_pep` is true but don't even pass `ip_rules` so they accept their default length of `0`? Well that would trigger the false condition of the first conditional. Let's look at it: `((var.enable_pep == true) && (length(var.ip_rules) == 0) ? false : true)`. So what this saying is "if `enable_pep` is true and `ip_rules` has a lenght of `0` (which is the case here), then trigger my true condition, else trigger my false".

   - So what is your true condition, well it is `false`. That means that `public_network_access_enabled` is set to false if we want to enable private endpoint but we don't want any public IPs to access the resource, makes sense.

   - So what is the false condition of the second conditional? Looks like it is set to `true`, when would that ever fire? Well, what if we pass `enable_pep` to false? The first condition says "if `enable_pep` true ..." and the second condition says "if `enable_pep` true ...", so both of those would trigger false if you set it to `false`, we need a "catch-all". In this case, we want `public_network_access_enabled` to be `true` for those rare cases that we don't have a private endpoint.

1. As mentioned in the comments, I have noticed a glitch in the Azure UI on resources with the middle radio button selected where if you set a list of public IP's, it will default to the bottom radio button but if you select the middle one they "magically" show up like it knew about them the whole time. In addition, in terraform if you add an IP and run an apply, it will move to the middle radio button as expected. Not sure why this happens but take note. Thankfully, I don't have to deal with the implications for this much because 99.99% of resources that have these options are set to the bottom radio button which disables all public network traffic.