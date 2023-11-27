---
title: Enabling VM Insights For Ubuntu 22.04 Scale Sets
date: 2023-03-26T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/03/vm-insights-for-ubuntu-2204
tags:
  - Azure
  - Terraform
  - Azure-VMSS
---
<!--more-->

### Description

According to the [VM Insights Overview](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-enable-overview#agents) page, you need both the Dependency Agent and AMA (Azure Monitoring Agent) on VMs and Scale Sets in order to get "VM Insights". After a case was opened with Microsoft, we found you actually only need the AMA Agent only until they support Ubuntu 22.04. Here are the notes:

### Steps

1. I once opened a Microsoft because [this Github Issue](https://github.com/microsoft/OMS-Agent-for-Linux/issues/1458) indicated that Microsoft has no support for Ubuntu 22.04 for Dependency Agent despite it being 18 months old at this point and ultimately got a response like ( don't quote Microsoft on this!) : "Product Group is lookin get some minor update to potentially support Linux RH 8.6 and 8.7 as well as Ubuntu 20.04 Kernel 5.15, There is no other future support in the pipeline."

1. What we found out was that even though the VM Insights Overview page makes it clear that you need both the DependencyAgent + AMA agent, you actually don't. You just need the Dependency Agent for the "map feature" of VM Insights but that doesn't work with Ubuntu 22.04 and probably never will according to their response. We can [keep checking here](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-dependency-agent-maintenance#dependency-agent-linux-support) in the future if we want to enable it again but for now, we will go with just AMA Agent.

1. You can verify the AMA agent works alone by:

   - Going to the scale set `your-scale-set` => Insights blade. You should see metrics.

   - Going to Azure Monitor => Virtual Machines blade => Overview tab and under the section "Monitor Coverage" you should see `Enabled` 

   - Going to Log Analytics `your-log-analytics` and running a query like:

   ```escape
   InsightsMetrics 
   | summarize HB = count() by Computer, Namespace, Name, Val
   | where Computer startswith "ubuntu-hu"
   ```

   - Replace `ubuntu-hu` with whatever [prefix](https://registry.terraform.io/providers/hashicorp/azurerm/3.80.0/docs/resources/linux_virtual_machine_scale_set#computer_name_prefix) you chose for your scale sets.

   - I believe the AMA agent is writing to tables: `VMComputer` and `VMConnection` as well. Here is a [full list](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-log-query) of tables and properties though I only see a subset of computers when I run some of the queries?


1. Closing notes from the Support case:

   - VM insights requires AMA to collect performance metrics only.
   - Dependency agent is not mandatory to enable VM Insights. This agent collects discovered data about processes running on the virtual machine and external process dependencies, which are used by the Map feature in VM insights. But has no impact on performance data collection.
   - Regarding support for Ubuntu 22.04, at this time the developing team does not have plans to implement support for that distro in the near future, however, this might change as we move forward.
     
1. In the future, if we ever need to add it back in Terraform, add:

   ```terraform
   resource "azurerm_virtual_machine_scale_set_extension" "vmss_ext_dependency_agent" {
   virtual_machine_scale_set_id = azurerm_linux_virtual_machine_scale_set.vmss.id
   auto_upgrade_minor_version   = true
   # https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/agent-dependency-linux#extension-schema
   name                       = "DAExtension"
   publisher                  = "Microsoft.Azure.Monitoring.DependencyAgent"
   type                       = "DependencyAgentLinux"
   type_handler_version       = "9.5"
   provision_after_extensions = [azurerm_virtual_machine_scale_set_extension.ama_linux.name]
   automatic_upgrade_enabled  = true
   settings = jsonencode({
      "enableAMA" = true
   })
   }
   ```

   - And then inside `azurerm_monitor_data_collection_rule` add this block:

   ```terraform
   extension {
      extension_name = "DependencyAgent"
      name           = "DependencyAgentDataSource"
      streams        = ["Microsoft-ServiceMap"]
   }
   ```

