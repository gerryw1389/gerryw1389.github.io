---
title: 'PS: Deploy RHEL In Azure'
date: 2020-03-05T07:18:46-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/03/ps-deploy-rhel-in-azure
tags:
  - Azure
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

So I had to deploy a set of RHEL 8 boxes in Azure but I kept being told to destroy them and move them between subnets. After the second time, I decided it would be better to script the installation. The following script will:

   - Deploy RHEL 8 box to the Resource Group and Subnet of your choosing
   - Attach an extra 80 GB disk to the VM
   - Set the IP assigned to it as static (you will need to know the subnet and available IP Addresses before hand)
   - Requires [MS Az module](https://docs.microsoft.com/en-us/powershell/azure/new-azureps-module-az?view=azps-3.7.0)

### To Resolve:

1. Use the following script and set your variables in the `Variables for each` section:


   ```powershell
   ################################
   # Run once
   Import-Module Az
   Connect-AzAccount
   ################################
   # Variables for each

   $vmName = 'myRHEL8'
   $vmSize = 'Standard_D2_v3'
   $staticIP = "10.20.20.102"

   $resourceGroupName = 'RHEL8-Instances'
   $location = 'southcentralus'
   $vnetName = 'Linux_VNET'
   $vnetSubnetName = 'RHEL8_Subnet'
   $nsgName = "nsg_rhel"

   $adminUsername = 'seeKeepass'
   $adminPassword = 'seeKeepass'

   # OS image
   $publisherName = 'RedHat'
   $offerName = 'RHEL'
   $skuName = '8'
   # if you want Windows, just change to:
   # per https://docs.microsoft.com/en-us/azure/virtual-machines/windows/cli-ps-findimage
   # $publisherName = 'MicrosoftWindowsServer'
   # $offerName = 'WindowsServer'
   # $skuName = '2019-Datacenter'


   ################################

   # start
   $resourceGroup = Get-AzResourceGroup -Name $resourceGroupName
   $rgName = $resourceGroup.ResourceGroupName

   # Set the network card info
   $vnet = Get-AzVirtualNetwork -Name $vnetName -ResourceGroupName $rgName
   $subnetid = (Get-AzVirtualNetworkSubnetConfig -Name $vnetSubnetName -VirtualNetwork $vnet).Id
   $nsg = Get-AzNetworkSecurityGroup -ResourceGroupName $rgName -Name $nsgName
   $nic = New-AzNetworkInterface -Name "$($vmName)$(Get-Random)" -ResourceGroupName $rgName -Location $location -SubnetId $subnetid -NetworkSecurityGroupId $nsg.Id

   # Set the Azure Marketplace image
   $adminCreds = New-Object PSCredential $adminUsername, ($adminPassword | ConvertTo-SecureString -AsPlainText -Force)
   # Set the disk info
   $dataDiskName = $vmName + '_datadisk1'
   $storageType = 'StandardSSD_LRS'
   $diskConfig = New-AzDiskConfig -SkuName $storageType -Location $location -CreateOption Empty -DiskSizeGB 80
   $dataDisk1 = New-AzDisk -DiskName $dataDiskName -Disk $diskConfig -ResourceGroupName $rgName

   # Set OS info / create VM
   $vmSize = 'Standard_D2_v3'
   $vmConfig = New-AzVMConfig -VMName $vmName -VMSize $vmSize
   Add-AzVMNetworkInterface -VM $vmConfig -Id $nic.Id
   Set-AzVMOperatingSystem -VM $vmConfig -Linux -ComputerName $vmName -Credential $adminCreds
   Set-AzVMSourceImage -VM $vmConfig -PublisherName $publisherName -Offer $offerName -Skus $skuName -Version 'latest'
   Set-AzVMOSDisk -VM $vmConfig -Name "$($vmName)_OsDisk_1_$(Get-Random)" -CreateOption "FromImage"
   Set-AzVMBootDiagnostic -VM $vmConfig -Disable
   New-AzVM -ResourceGroupName $rgName -Location $location -VM $vmConfig

   # Attach disk
   $vm = Get-AzVM -Name $vmName -ResourceGroupName $rgName 
   $vm = Add-AzVMDataDisk -VM $vm -Name $dataDiskName -CreateOption Attach -ManagedDiskId $dataDisk1.Id -Lun 1
   Update-AzVM -VM $vm -ResourceGroupName $rgName

   # Set static IP
   $postInstallNic = Get-AzNetworkInterface -ResourceGroupName $rgName -Name $nic.Name
   $postInstallNic.IpConfigurations[0].PrivateIpAddress = $staticIP
   $postInstallNic.IpConfigurations[0].PrivateIpAllocationMethod = "Static"
   $postInstallNic.Tag = @{Name = "Name"; Value = "Value" }
   Set-AzNetworkInterface -NetworkInterface $postInstallNic
   ```

