---
title: Azure Function Apps Get Secrets
date: 2021-01-22T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/01/function-apps-get-secrets/
categories:
  - Azure
tags:
  - Cloud
  - Azure-KeyVault
  - Azure-FunctionApps
  - Scripting-Python
---
<!--more-->

### Description:

This is currently how I have my Function Apps getting secrets.

### To Resolve:

1. Let's look at the following functions declared in our standard `shared/helpers.py` found in many of my python [Github Repos](https://github.com/gerryw1389/python/tree/main/scripts) ([for example](https://github.com/gerryw1389/python/blob/main/scripts/azure-durable-functions-basic/shared/helpers.py)):

   ```python
   def import_creds():
   '''
   Gets secrets from Azure Keyvault as an application
   Secret values are stored in the Function App under Configuration

   Example of how to call from main():
   keyvault_creds = import_creds()
   logging.info(f"client_id: { keyvault_creds['client_id'] }")
   logging.info(f"client_secret: { keyvault_creds['client_secret'] }")
   logging.info(f"tenant: { keyvault_creds['tenant'] }")
   logging.info(f"vault_name: { keyvault_creds['vault_name'] }")
   '''

   try:
      creds = {}
      creds["client_id"] = os.environ["client_id"]
      creds["client_secret"] = os.environ["client_secret"]
      creds["tenant"] = os.environ["tenant"]
      creds["vault_name"] = os.environ["vault_name"]
   except KeyError:
      logging.error("Unable to get env vars")
   except Exception as e:
      logging.error(f"Generic Catch: {str(e)}")

   return creds


   def get_oauth(tenant, client_id, client_secret):
   '''
   Gets an Oauth token from Graph API as an application
   See the scope in the payload where the application is scoped to just Key Vault

   Example of how to call from main():
   token = get_oauth( 
      tenant = keyvault_creds['tenant'], 
      client_id = keyvault_creds['client_id'], 
      client_secret = keyvault_creds['client_secret'] 
   )
   '''
   url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
   payload = "grant_type=client_credentials"\
      f"&client_id={client_id}"\
      f"&client_secret={client_secret}"\
      "&scope=https%3A%2F%2Fvault.azure.net%2F.default"
   headers = {'Content-Type': 'application/x-www-form-urlencoded'}
   response = requests.request("POST", url, headers=headers, data=payload)
   r = response.json()
   return r


   def get_secret(token, vault_name, secret_name):
   '''
   Using an Oauth token, gets the latest version of a secret

   Example of how to call from main():
   secret = get_secret(
      token = token["access_token"], 
      vault_name = keyvault_creds['vault_name'],
      secret_name = 'test'
   )
   logging.info(f"Secret value is : {secret['value']}")
   '''
   # Gets the latest version of a secret
   url = f"https://{vault_name}.vault.azure.net/secrets/{secret_name}?api-version=7.1"

   # for a specific version of the secret, replace {version}
   # version = "aadsfasdfasdfasdf"
   # url = f"https://{vault_name}.vault.azure.net/secrets/test/{version}?api-version=7.1"

   payload = {}
   headers = {"Authorization": f"Bearer {token}"}
   response = requests.request("GET", url, headers=headers, data=payload)
   r = response.json()
   return r


   def get_sn_username():
   '''
   Using a combination of get_oauth() and get_secret() functions, 
   This will get an oauth token and retrieve the latest version of a secret

   Example of how to call from main():
   sn_username = get_sn_username()
   logging.info(f"Secret value is : {sn_username}")
   '''
   keyvault_creds = import_creds()
   token = get_oauth(tenant=keyvault_creds['tenant'],
                     client_id=keyvault_creds['client_id'],
                     client_secret=keyvault_creds['client_secret'])
   secret = get_secret(token=token["access_token"],
                     vault_name=keyvault_creds['vault_name'],
                     secret_name='ServiceNow-Username')
   return secret['value']
   ```

2. First, notice the `get_sn_username` function which will get the username for an API user for Service Now.

   - It first creates `keyvault_creds` by querying the Function App's environmental variables. It is crucial that certain values are set in the `Configuration` blade in Azure for this to work as dicussed in my [Function App post](https://automationadmin.com/2021/01/function-app-source-control-pt-2/)
   - It then calls `get_oauth` which relies on those credentials to be correct to get an Oauth token.
   - It then passes that token to the Azure Keyvault to get a secret.
   - Finally, it returns the plain text version of the secret to whatever calls it.
