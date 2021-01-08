---
title: Azure Serverless SFTP
date: 2020-11-20T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/11/azure-serverless-sftp
categories:
  - Azure
tags:
  - Azure-StorageAccounts
  - Azure-ContainerInstances
---
<!--more-->

### Description:

Following [this template](https://github.com/Azure/azure-quickstart-templates/tree/master/201-aci-sftp-files-existing-storage) I was able to create a powershell script that when ran in the portal would deploy new instances of SFTP by connecting to our storage account and creating one share per user. This works great as a one off solution to have user's send you files and each user is to have their own chroot.This will be maintained at Github [here](https://github.com/gerryw1389/powershell/tree/master/azure/serverless-sftp).

### To Resolve:

1. First, create `run.ps1` in cloud shell and paste in:

   ```powershell
   $params = @{
   "ResourceGroupName"= "Storage-Account-Resource-Group"
   "TemplateFile"= "t.json"
   "TemplateParameterFile"= "p.json"
   "Tag" = @{"Department"="IT"; "Email"="me@company.com";}
   }
   New-AzResourceGroupDeployment @params
   ```

2. Create the `t.json` template file:

   ```json
   {
      "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
      "contentVersion": "1.0.0.0",
      "parameters": {
         "existingStorageAccountResourceGroupName": {
               "type": "string",
               "metadata": {
                  "description": "Resource group for existing storage account"
               }
         },
         "existingStorageAccountName": {
               "type": "string",
               "metadata": {
                  "description": "Name of existing storage account"
               }
         },
         "existingFileShareName": {
               "type": "string",
               "metadata": {
                  "description": "Name of existing file share to be mounted"
               }
         },
         "sftpUser": {
               "type": "string",
               "metadata": {
                  "description": "Username to use for SFTP access"
               }
         },
         "sftpPassword": {
               "type": "securestring",
               "metadata": {
                  "description": "Password to use for SFTP access"
               }
         },
         "location": {
               "type": "string",
               "metadata": {
                  "description": "Primary location for resources"
               }
         },
         "dnsLabel": {
               "type": "string",
               "metadata": {
                  "description": "URL prefix for .southcentralus.azurecontainer.io"
               }
         },
         "containerGroupName": {
               "type": "string",
               "metadata": {
                  "description": "Ensure this does not currently exist"
               }
         }
      },
      "variables": {
         "sftpContainerName": "sftp",
         "sftpContainerGroupName": "[parameters('containerGroupName')]",
         "sftpContainerImage": "atmoz/sftp:latest",
         "sftpEnvVariable": "[concat(parameters('sftpUser'), ':', parameters('sftpPassword'), ':1001')]",
         "storageAccountId": "[resourceId(parameters('existingStorageAccountResourceGroupName'), 'Microsoft.Storage/storageAccounts', parameters('existingStorageAccountName'))]"
      },
      "resources": [
         {
               "type": "Microsoft.Resources/deployments",
               "name": "pid-18f281fe-d1e1-502c-8b87-d945383dc75b",
               "apiVersion": "2019-09-01",
               "properties": {
                  "mode": "Incremental",
                  "template": {
                     "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
                     "contentVersion": "1.0.0.0",
                     "resources": []
                  }
               }
         },
         {
               "type": "Microsoft.ContainerInstance/containerGroups",
               "name": "[variables('sftpContainerGroupName')]",
               "apiVersion": "2019-12-01",
               "location": "[parameters('location')]",
               "properties": {
                  "containers": [
                     {
                           "name": "[variables('sftpContainerName')]",
                           "properties": {
                              "image": "[variables('sftpContainerImage')]",
                              "environmentVariables": [
                                 {
                                       "name": "SFTP_USERS",
                                       "value": "[variables('sftpEnvVariable')]"
                                 }
                              ],
                              "resources": {
                                 "requests": {
                                       "cpu": 2,
                                       "memoryInGB": 1
                                 }
                              },
                              "ports": [
                                 {
                                       "port": 22
                                 }
                              ],
                              "volumeMounts": [
                                 {
                                       "mountPath": "[concat('/home/', parameters('sftpUser'), '/upload')]",
                                       "name": "sftpvolume",
                                       "readOnly": false
                                 }
                              ]
                           }
                     }
                  ],
                  "osType": "Linux",
                  "ipAddress": {
                     "ports": [
                           {
                              "protocol": "TCP",
                              "port": 22
                           }
                     ],
                     "type": "Public",
                     "dnsNameLabel": "[parameters('dnsLabel')]"
                  },
                  "restartPolicy": "OnFailure",
                  "volumes": [
                     {
                           "name": "sftpvolume",
                           "azureFile": {
                              "readOnly": false,
                              "shareName": "[parameters('existingFileShareName')]",
                              "storageAccountName": "[parameters('existingStorageAccountName')]",
                              "storageAccountKey": "[listKeys(variables('storageAccountId'),'2018-02-01').keys[0].value]"
                           }
                     }
                  ]
               }
         }
      ],
      "outputs": {
         "containerIPv4Address": {
               "type": "string",
               "value": "[reference(resourceId('Microsoft.ContainerInstance/containerGroups/', variables('sftpContainerGroupName'))).ipAddress.ip]"
         }
      }
   }
   ```

3. Create the `p.json` parameters file that fits your organization:

   ```json
   {
      "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#",
      "contentVersion": "1.0.0.0",
      "parameters": {
         "existingStorageAccountResourceGroupName": {
         "value": "My-Storage-Account-RG"
         },
         "existingStorageAccountName": {
         "value": "My-Storage-Account"
         },
         "existingFileShareName": {
         "value": "My-Share"
         },
         "sftpUser": {
         "value": "sftp-user-name"
         },
         "sftpPassword": {
         "value": "some-long-password"
         },
         "location": {
         "value": "southcentralus"
         },
         "dnsLabel": {
         "value": "my-transfer-group-name"
         },
         "containerGroupName": {
         "value": "my-transfer-group-name"
         }
      }
   }
   ```

4. What I do is keep these three files in a folder, and when needed copy the folder, rename it, tweak parameters, and deploy again.

