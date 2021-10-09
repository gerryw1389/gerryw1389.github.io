---
title: Creating Azure KeyVault Service Account
date: 2020-12-18T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/creating-azure-keyvault-service-account
categories:
  - Azure
tags:
  - Cloud
  - Scripting-Python
  - Azure-KeyVault
  - Scripting-RestAPI
---
<!--more-->

### Description:

Service Accounts are great! They allow you to connect services and limit access to a specific user at the same time. Here is an example of how I setup an Azure KeyVault user.

### To Resolve:

1. Create a user in Azure AD called `keyvault@domain.com` for example.
   - To create a user in Azure AD: Azure AD => Users => New
   - Give 30+ character password
   - Have it bypass MFA: Azure AD => Security => Conditional Access => Azure MFA => Exclude => Add user
   - Have password never expire: `Set-AzureADUser -ObjectId keyvault@domain.com -PasswordPolicies DisablePasswordExpiration`
     - We have an enterprise app that rotates passwords every 30 days so this is okay.

2. Create an application in Azure called `keyvault_access`
   - Go to Azure => App Registrations => Create new
   - Copy the ClientID from the Overview tab to notepad
   - Owners => add the user you just created (keyvault@domain.com)
   - Client Secrets => Copy to notepad

3. Add the user to the KeyVault policy

   - Go to Azure KeyVault => IAM => Role Assignments => contributor => Add user and application
   - Go to Azure KeyVault => Access Policies => Add user and application with "Key & Secret Management" Template (read/write to secrets)

4. Now that the user is added, I create a `.env` file in my python repo and fill with key value pairs mentioned in the next script.

   - Script:

   ```python
   #!/usr/bin/env python3

   ################################################################
   # Gets an Oauth token as an application and then attaches the token to another request.
   # Tested/working on 2021-01-05 
   ################################################################

   import requests
   import json
   from dotenv import load_dotenv
   import os
   import sys

   load_dotenv()

   try:
      ro_user = os.environ["user"]
      ro_password = os.environ["password"]
      client_id = os.environ["client_id"]
      client_secret = os.environ["client_secret"]
      tenant = os.environ["tenant"]
      vault_name = os.environ["vault_name"]
   except KeyError:
      print("unable to get env vars")
      sys.exit(1)
   except Exception as e:
      print("Generic Catch: unable to get env vars")
      sys.exit(1)


   def oauth(tenant, client_id, client_secret):
      url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
      payload = "grant_type=client_credentials"\
         f"&client_id={client_id}"\
         f"&client_secret={client_secret}"\
         "&scope=https%3A%2F%2Fvault.azure.net%2F.default"
      headers = {'Content-Type': 'application/x-www-form-urlencoded'}
      response = requests.request("POST", url, headers=headers, data=payload)
      r = response.json()
      return r

   def get_secret(token, vault_name):
      
      # Gets the latest version of a secret
      url = f"https://{vault_name}.vault.azure.net/secrets/test?api-version=7.1"
      
      # for a specific version of the secret, replace {version}
      # version = "someGuid"
      # url = f"https://{vault_name}.vault.azure.net/secrets/test/{version}?api-version=7.1"

      payload={}
      headers = { "Authorization": f"Bearer {token}" }
      response = requests.request("GET", url, headers=headers, data=payload)
      r = response.json()
      return r


   def main():
      
      token = oauth(tenant, client_id, client_secret)
      print(token)
      # print(f"My token is:\n{oauth_token['access_token']}")

      secret = get_secret(token=token["access_token"], vault_name=vault_name)
      print(secret)
      print(f"Secret value is : {secret['value']}")

   if __name__ == '__main__':
      main()
      ```

5. I ended up getting `... For help resolving this issue, please see https://go.microsoft.com/fwlink/?linkid=2125287", 'innererror': {'code': 'ForbiddenByPolicy'}}}`. To fix:

   - Inside the Azure KeyVault policy, remove the `Compound Identity` and add two policies - one for the user and one for the application separately.
   - After running again, I get the secret I was looking for.
