---
title: 'Github Actions: Using AKV To Get Secrets'
date: 2023-11-05T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/11/using-akv-to-get-secrets
tags:
  - Azure
  - Github
  - Terraform
  - Azure-KeyVault
---
<!--more-->

### Description:

A key goal I wish to accomplish with Github Actions is to set all the secrets I can in an Azure Key Vault and then only get them at run time to populate all the other secrets needed. I have been doing this for years with [Function Apps](https://automationadmin.com/2021/01/function-apps-get-secrets/) and other Azure services and wish to continue this strategy. Basically, the strategy works like this: `"Only store Azure Credentials as Env secrets and use those at runtime to populate more secrets"`. This way you can create a Service Principal with limited rights like ["Key Vault Secrets User"](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#key-vault-secrets-user) at the AKV level and then monitor it in Azure Active Directory to ensure it is only being used to access AKVs. Here is how I do just this:

### To Resolve:

1. The only secrets needed for [OIDC Auth](https://automationadmin.com/2023/08/setting-oidc-auth) are `${/{ secrets.CLIENT_ID }}`, `${/{ secrets.TENANT_ID }}`, and `${/{ secrets.SUB_ID }}` so I put each of these in the Repo as secrets. 

   - NOTE: [Jekyll Liquid Filters](https://jekyllrb.com/docs/liquid/filters/) clash with [Github Variables](https://docs.github.com/en/actions/learn-github-actions/variables#using-contexts-to-access-variable-values) so replace all instances of `${/{` by removing the forward slash :)

   - Then I need to add `${/{ secrets.REPO_BOT_PEM }}` as discussed [here](https://automationadmin.com/2023/07/create-repo-bot-for-tf-modules) for access to my module repos.

   - I would have that one come from a Key Vault, but I had issues reading secrets from AKV that are private keys as explained [here](https://automationadmin.com/2023/09/unable-to-load-priv-key-from-akv).

1. Once those secrets are added, we then just need to do 2 things: Populate our AKV with all possible secrets and then add a task in our pipeline that will update the worfklow and "switch" based on the **needed** variables.

1. [Here](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/.github/workflows/main.yml#L69) is the action that will switch based on the specific workflow :

   ```yaml
   - name: "Parse Workflow TF Folder From Matrix"
      id: parse
      run: |
         cd $GITHUB_WORKSPACE
         chmod +x ./.github/scripts/parse.sh
         ./.github/scripts/parse.sh
      env:
         CURRENT_DIRECTORY: ${/{ matrix.directories }}
   ```

   - And [here](https://github.com/AutomationAdmin-Com/sic.template/blob/main/.github/scripts/parse.sh) is the script.

1. You will notice a few important things about this script.

   - First, it makes use of [Github Outputs](https://docs.github.com/en/actions/using-jobs/defining-outputs-for-jobs#overview) context which is critical to how workflows work in Github Actions.
   - I used to think it only worked with Inline bash so I would have long workflows but I found that shell scripts will inherit the `$GITHUB_OUTPUT` [env var](https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables).
   - Second, the script mostly works by looking at the current matrix item and then setting outputs based on the value of it. Just a like a powershell switch statement but using bash.

1. Lastly, after the parsing script, you just reference any output key value pair by the `key's name` in subsequent steps. For example:
   - `TF_VAR_subscription_id: ${/{ steps.azure-keyvault-secrets-spoke.outputs.spoke-subscription-id }}`
   - `TF_VAR_hub_subscription_id: ${/{ steps.azure-keyvault-secrets-hub.outputs.hub-subscription-id }}`
   - In these examples the steps name is `azure-keyvault-secrets` as seen [here](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/.github/workflows/main.yml#L112) and the secrets we are setting are `spoke-subscription-id` and `hub-subscription-id` as seen in various spots of the parse script above ( look for any lines with `>>$GITHUB_OUTPUT` ).

1. In the previous step we get the subscription ID and hub subscription ID needed dynamically so that we can [build providers](https://github.com/AutomationAdmin-Com/sic.mgmt/blob/4ad7fee18f3032ad14d011affb69e3fcb44c4498/config/prd/hub/scus/stage1/none/backend.tf#L61) in our calling workflows. See my [lab](https://automationadmin.com/lab/) section for how this works.

1. Also, I have recently added a random [up to 45 second delay](https://github.com/AutomationAdmin-Com/sic.template/blob/484737f27f67780c6a35a5c7288a230efec4d5c7/.github/workflows/main.yml#L101) because I might have multiple parrallel workflows running and the AKV needs to only whitelist at run time so it would often error out with '(Forbidden) Client address is not authorized' like so:

   ```escape
   Run az account set --subscription "prd-hub"
   ERROR: (Forbidden) Client address is not authorized and caller is not a trusted service.
   Client address: 20.81.159.17
   Caller: appid=***;oid=fe62cc9a-b71b-46ae-93b3-d154327f57a4;iss=https://sts.windows.net/***/
   Vault: aa-prd-scus-hub-akv-v1;location=southcentralus
   Code: Forbidden
   Message: Client address is not authorized and caller is not a trusted service.
   Client address: 20.81.159.17
   Caller: appid=***;oid=fe62cc9a-b71b-46ae-93b3-d154327f57a4;iss=https://sts.windows.net/***/
   Vault: aa-prd-scus-hub-akv-v1;location=southcentralus
   Inner error: {
      "code": "ForbiddenByFirewall"
   }
   Error: Process completed with exit code 1.
   ```

   - The fix is to simply click the `rerun failed jobs` button. This happens due to concurrency that the 45 second delay is supposed to fix.
