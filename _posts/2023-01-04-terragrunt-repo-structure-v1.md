---
title: 'Terragrunt: Repo Structure V1'
date: 2023-01-04T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/terragrunt-repo-structure-v1
categories:
  - Azure
tags:
  - Cloud
  - InfrastructureProvisioning
---
<!--more-->

### Description:

So recently I have been looking at using [Terragrunt](https://terragrunt.gruntwork.io/) to manage my terraform code dynamically based on environment similar to my [Data Lookup module](https://automationadmin.com/2022/11/data-sources-module). This post is a list of the steps taken to get my my initial (working!) version of my repo using Github Actions/Terragrunt.

Note: You can see the code for this post on [my Github repo](https://github.com/gerryw1389/terraform-examples/tree/main/2023-01-04-terragrunt-repo-structure-v1). [Github Actions are here](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/2023-01-04-terragrunt-repo-structure-v1/)
{: .notice--success}

### To Resolve:

1. First, for readers unaware, please see my [subscription setup](https://automationadmin.com/2022/10/tf-new-subscription)

   - To setup Terragrunt initially, you just start with a file structure that is completely up to you. I chose environment => subscription => region => application. This sets my file structure like the following as seen [here](https://github.com/gerryw1389/terraform-examples/tree/main/2023-01-04-terragrunt-repo-structure-v1/infra-config):

   ```escape
   C:.
   │   global.hcl
   │   root.hcl
   │
   ├───nonprod
   │   │   env.hcl
   │   │
   │   ├───hub
   │   │   │   sub.hcl
   │   │   │
   │   │   ├───east
   │   │   │   │   region.hcl
   │   │   │   │
   │   │   │   └───deployment
   │   │   │           terragrunt.hcl
   │   │   │
   │   │   └───southcentral
   │   │       │   region.hcl
   │   │       │
   │   │       └───deployment
   │   │               terragrunt.hcl
   │   │
   │   └───spoke
   │       │   sub.hcl
   │       │
   │       ├───east
   │       │   │   region.hcl
   │       │   │
   │       │   └───deployment
   │       │           terragrunt.hcl
   │       │
   │       └───southcentral
   │           │   region.hcl
   │           │   
   │           └───deployment
   │                   terragrunt.hcl
   │
   └───prod
      │   env.hcl
      │
      ├───hub
      │   │   sub.hcl
      │   │
      │   ├───east
      │   │   │   region.hcl
      │   │   │
      │   │   └───deployment
      │   │           terragrunt.hcl
      │   │
      │   └───southcentral
      │       │   region.hcl
      │       │
      │       └───deployment
      │               terragrunt.hcl
      │
      └───spoke
         │   sub.hcl
         │
         ├───east
         │   │   region.hcl
         │   │
         │   └───deployment
         │           terragrunt.hcl
         │
         └───southcentral
               │   region.hcl
               │
               └───deployment
                     terragrunt.hcl
   ```

1. So after creating the files, it is best to see what is happening by breaking them down by the directory level:

   - Level 1: [global.hcl](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/global.hcl) => Defines some local variables that will be inherited downwards to all subscriptions, environments, regions, ect. as well as imports environmental vars.

   - Level 1: [root.hcl](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/root.hcl) => currently only has a `generate` block which is a Terragrunt native command that dynamically generates a `provider.tf` at run time. I'm sure there is more to this, this just my initial version. We will import this file later in the file structure.

   - Level 2: [env.hcl](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/nonprod/env.hcl) => These are placed in each sub folder and are environment level variables.

   - Level 3: [sub.hcl](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/nonprod/spoke/sub.hcl) => These are placed in each sub folder and are subscription level variables.

   - Level 4: [region.hcl](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/nonprod/spoke/southcentral/region.hcl) => These are placed in each sub folder and are region level variables.

   - Level 5: [terragrunt.hcl](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/nonprod/spoke/southcentral/deployment/terragrunt.hcl) => You will see this file placed 8 times - one for each environment, subscription, and region. The `deployment` is just an arbitrary name for an application deployment. I could have done `weather.io`, `bob`, or `my-app` if I wanted.

1. So we have level 5 terragrunt.hcl files in 8 places with the same code in each, I thought the point was to be DRY (Don't repeat yourself), sounds like you are! All I can say is "give me a break, I'm still learning! lol" But seriously, I think what is happening will reveal itself to be useful if we just continue on okay? UPDATE: This is fixed and covered in [Terragrunt Repo Structure V2](https://automationadmin.com/2023/01/terragrunt-repo-structure-v2).

1. OK, so let's break down the sections in [terragrunt.hcl](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/nonprod/spoke/southcentral/deployment/terragrunt.hcl). 

   - First, it creates a dictionary of all the locals in the file system above it. This is incredibly powerful already because we can have 1, 2, or 23 levels of folders above and extract them locally! We can then mix and match to make our own custom locals.

   - Next, we `include "root_config"` to import that root hcl file that dynmically generates our provider.tf. Then we generate our own backend.tf.

   - Something really cool about this section is the `path_relative_to_include()` function for the blob location. This will actually create your state file based on your file system tree in your storage account! Really:

   - ![terragrunt-tree](https://automationadmin.com/assets/images/uploads/2023/01/terragrunt-tree.jpg){:class="img-responsive"}

   - Anyways, the next section is the most important: You call terraform with a `source` path and then you call `inputs` which is where you inject those locals to pass to the module.

1. OK, so we are dynamically passing variables to modules, I want to see this in action! OK, let's look at the [build](https://github.com/gerryw1389/terraform-examples/blob/main/.github/workflows/2023-01-04-terragrunt-repo-structure-v1/) and see if we can dissect it:

   - First, we are using `autero1/action-terragrunt@v1.1.0` to install terragrunt after terraform, cool.

   - Next, we are running its [`run-all plan`](https://terragrunt.gruntwork.io/docs/reference/cli-options/#plan-all-deprecated-use-run-all) to pass environmental variables to Terragrunt which will then pass them to terraform later on.

   - In that same command we are doing something that is real important for you to understand, we are passing a directory for the `--terragrunt-working-dir`. This is important because if you don't pay attention here, you could run plans against all your subscriptions at the same time! Not a big deal since it is a plan but one of the main [selling points of terragrunt](https://terragrunt.gruntwork.io/docs/features/execute-terraform-commands-on-multiple-modules-at-once/). Let's just run this once for now to see what happens...

   - NOTE: Unfortunately, I have to paste the logs here because Github deletes them, sorry, just scroll!

   ```escape
   Prepare all required actions
   Getting action download info
   Download action repository 'actions/checkout@v3' (SHA:ac593985615ec2ede58e132d2e21d2b1cbd6127c)
   Download action repository 'hashicorp/setup-terraform@v2' (SHA:633666f66e0061ca3b725c73b2ec20cd13a8fdd1)
   Download action repository 'autero1/action-terragrunt@v1.1.0' (SHA:a99cd7d0443c46ba89b09d68a8db6bbcf8932ae0)
   Run ./.github/workflows/2023-01-04-terragrunt-repo-structure-v1/build
   Run actions/checkout@v3
   Syncing repository: gerryw1389/terraform-examples
   Getting Git version info
   Temporarily overriding HOME='/home/runner/work/_temp/15219c16-2bed-426f-9d25-2db8be9aa4cf' before making global git config changes
   Adding repository directory to the temporary git global config as a safe directory
   /usr/bin/git config --global --add safe.directory /home/runner/work/terraform-examples/terraform-examples
   /usr/bin/git config --local --get remote.origin.url
   https://github.com/gerryw1389/terraform-examples
   Removing previously created refs, to avoid conflicts
   Cleaning the repository
   Disabling automatic garbage collection
   Setting up auth
   Fetching the repository
   Determining the checkout info
   Checking out the ref
   /usr/bin/git log -1 --format='%H'
   '9811f927faa9adf513ab30272007fe68c70f3336'
   Run hashicorp/setup-terraform@v2
   /usr/bin/unzip -o -q /home/runner/work/_temp/aeca15f7-48be-4f9a-812f-61d0c68d91d9
   Run autero1/action-terragrunt@v1.1.0
   [INFO] TerragruntVersion: v0.42.7
   [INFO] Setting up Terragrunt version: 'v0.42.7'
   [INFO] Downloading from: 'https://github.com/gruntwork-io/terragrunt/releases/download/v0.42.7/terragrunt_linux_amd64'
   [INFO] Terragrunt version: 'v0.42.7' has been cached at /opt/hostedtoolcache/terragrunt/0.42.7/x64/terragrunt
   Warning: The `set-output` command is deprecated and will be disabled soon. Please upgrade to using Environment Files. For more information see: https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/
   Run cd 2023-01-04-terragrunt-repo-structure-v1
   time=2023-01-13T22:53:25Z level=info msg=The stack at infra-config/nonprod/hub/east/deployment will be processed in the following order for command plan:
   Group 1
   - Module /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra-config/nonprod/hub/east/deployment


   time=2023-01-13T22:53:26Z level=warning msg=No double-slash (//) found in source URL /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra. Relative paths in downloaded Terraform code may not work. prefix=[/home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra-config/nonprod/hub/east/deployment] 
   /home/runner/work/_temp/f5b30077-5be2-4d37-a73b-8dbd96e56e3c/terraform-bin init

   Initializing the backend...

   Successfully configured the backend "azurerm"! Terraform will automatically
   use this backend unless the backend configuration changes.

   Initializing provider plugins...
   - Finding hashicorp/azurerm versions matching "3.30.0"...
   - Installing hashicorp/azurerm v3.30.0...
   - Installed hashicorp/azurerm v3.30.0 (signed by HashiCorp)

   Terraform has created a lock file .terraform.lock.hcl to record the provider
   selections it made above. Include this file in your version control repository
   so that Terraform can guarantee to make the same selections by default when
   you run "terraform init" in the future.

   Terraform has been successfully initialized!

   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.

   If you ever set or change modules or backend configuration for Terraform,
   rerun this command to reinitialize your working directory. If you forget, other
   commands will detect it and remind you to do so if necessary.
   /home/runner/work/_temp/f5b30077-5be2-4d37-a73b-8dbd96e56e3c/terraform-bin plan -input=false

   Terraform used the selected providers to generate the following execution
   plan. Resource actions are indicated with the following symbols:
   + create

   Terraform will perform the following actions:

   # azurerm_resource_group.rg will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "eastus"
         + name     = "aa-dev-eus-mgmt-rg"
         + tags     = {
            + "App_Contact" = "gerry@automationadmin.com"
            + "CostCenter"  = "100"
            + "Description" = "Automation Admin Terraform POC"
            + "Environment" = "dev"
            + "Owner"       = "Automation Admin"
         }
      }

   Plan: 1 to add, 0 to change, 0 to destroy.

   ─────────────────────────────────────────────────────────────────────────────

   Note: You didn't use the -out option to save this plan, so Terraform can't
   guarantee to take exactly these actions if you run "terraform apply" now.
   -01-13T22:53:37Z level=info msg=[command]/home/runner/work/_temp/f5b30077-5be2-4d37-a73b-8dbd96e56e3c/terraform-bin init

   Initializing the backend...

   Successfully configured the backend "azurerm"! Terraform will automatically
   use this backend unless the backend configuration changes.

   Initializing provider plugins...
   - Finding hashicorp/azurerm versions matching "3.30.0"...
   - Installing hashicorp/azurerm v3.30.0...
   - Installed hashicorp/azurerm v3.30.0 (signed by HashiCorp)

   Terraform has created a lock file .terraform.lock.hcl to record the provider
   selections it made above. Include this file in your version control repository
   so that Terraform can guarantee to make the same selections by default when
   you run "terraform init" in the future.

   Terraform has been successfully initialized!

   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.

   If you ever set or change modules or backend configuration for Terraform,
   rerun this command to reinitialize your working directory. If you forget, other
   commands will detect it and remind you to do so if necessary.

   ```

   - OK, success! It is going to build a Resource Group according to the `inputs` I passed it in infra-config/nonprod/hub/east/deployment. Lets look at its [terragrunt.hcl](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/nonprod/hub/east/deployment/terragrunt.hcl)...

   - First, from the output, we can see it is creating a Resource Group called "aa-dev-eus-mgmt-rg". Is this right? 
   - According to [main.tf](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra/main.tf) the name expands `"aa-${var.env_stage_abbr}-${var.region_abbr}-mgmt-rg"`
   - Well `var.env_stage_abbr` is under the `./nonprod` folder so it should be `dev` as we [expect](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/nonprod/env.hcl) 
   - Well `var.region_abbr` is under the `./east` folder so it should be `eus` as we [expect](https://github.com/gerryw1389/terraform-examples/blob/main/2023-01-04-terragrunt-repo-structure-v1/infra-config/nonprod/hub/east/region.hcl)
   - OK so that is a lot of work for what it is, maybe not use Terragrunt?

2. Well hold on, first let's try a different environment/region and see what happens. Simply changing `--terragrunt-working-dir infra-config/nonprod/hub/east/deployment` to `--terragrunt-working-dir infra-config/prod/hub/southcentral/deployment` gives us `"aa-prod-scus-mgmt-rg"`, wowza, that's pretty cool!

3. OK, so let's talk about what will happen if we execute it from higher up? Well, let's try. Changing `--terragrunt-working-dir infra-config/prod/hub/southcentral/deployment` to `--terragrunt-working-dir infra-config/prod` shows it will create 4 Resource Groups at the same time in each subscription! NOTE: Unfortunately, I have to paste the logs here because Github deletes them, sorry, just scroll!

   ```escape
   Prepare all required actions
   Getting action download info
   Download action repository 'actions/checkout@v3' (SHA:ac593985615ec2ede58e132d2e21d2b1cbd6127c)
   Download action repository 'hashicorp/setup-terraform@v2' (SHA:633666f66e0061ca3b725c73b2ec20cd13a8fdd1)
   Download action repository 'autero1/action-terragrunt@v1.1.0' (SHA:a99cd7d0443c46ba89b09d68a8db6bbcf8932ae0)
   Run ./.github/workflows/2023-01-04-terragrunt-repo-structure-v1/build
   Run actions/checkout@v3
   Syncing repository: gerryw1389/terraform-examples
   Getting Git version info
   Temporarily overriding HOME='/home/runner/work/_temp/5e4c1666-90be-4607-81d3-ee6fba5d2f95' before making global git config changes
   Adding repository directory to the temporary git global config as a safe directory
   /usr/bin/git config --global --add safe.directory /home/runner/work/terraform-examples/terraform-examples
   /usr/bin/git config --local --get remote.origin.url
   https://github.com/gerryw1389/terraform-examples
   Removing previously created refs, to avoid conflicts
   Cleaning the repository
   Disabling automatic garbage collection
   Setting up auth
   Fetching the repository
   Determining the checkout info
   Checking out the ref
   /usr/bin/git log -1 --format='%H'
   '06e88633f924d9935a6c943810b95ddd43c05827'
   Run hashicorp/setup-terraform@v2
   /usr/bin/unzip -o -q /home/runner/work/_temp/c3831059-87ba-4596-8225-12dfd0aff9df
   Run autero1/action-terragrunt@v1.1.0
   [INFO] TerragruntVersion: v0.42.7
   [INFO] Setting up Terragrunt version: 'v0.42.7'
   [INFO] Downloading from: 'https://github.com/gruntwork-io/terragrunt/releases/download/v0.42.7/terragrunt_linux_amd64'
   [INFO] Terragrunt version: 'v0.42.7' has been cached at /opt/hostedtoolcache/terragrunt/0.42.7/x64/terragrunt
   Warning: The `set-output` command is deprecated and will be disabled soon. Please upgrade to using Environment Files. For more information see: https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/
   Run cd 2023-01-04-terragrunt-repo-structure-v1
   time=2023-01-14T00:25:31Z level=info msg=The stack at infra-config/prod will be processed in the following order for command plan:
   Group 1
   - Module /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra-config/prod/hub/east/deployment
   - Module /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra-config/prod/hub/southcentral/deployment
   - Module /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra-config/prod/spoke/east/deployment
   - Module /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra-config/prod/spoke/southcentral/deployment


   time=2023-01-14T00:25:33Z level=warning msg=No double-slash (//) found in source URL /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra. Relative paths in downloaded Terraform code may not work. prefix=[/home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra-config/prod/spoke/southcentral/deployment] 
   time=2023-01-14T00:25:33Z level=warning msg=No double-slash (//) found in source URL /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra. Relative paths in downloaded Terraform code may not work. prefix=[/home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra-config/prod/spoke/east/deployment] 
   time=2023-01-14T00:25:33Z level=warning msg=No double-slash (//) found in source URL /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra. Relative paths in downloaded Terraform code may not work. prefix=[/home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra-config/prod/hub/southcentral/deployment] 
   /home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin init
   /home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin init
   time=2023-01-14T00:25:34Z level=warning msg=No double-slash (//) found in source URL /home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra. Relative paths in downloaded Terraform code may not work. prefix=[/home/runner/work/terraform-examples/terraform-examples/2023-01-04-terragrunt-repo-structure-v1/infra-config/prod/hub/east/deployment] 

   Initializing the backend...

   Initializing the backend...
   /home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin init
   /home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin init

   Initializing the backend...

   Initializing the backend...

   Successfully configured the backend "azurerm"! Terraform will automatically
   use this backend unless the backend configuration changes.

   Successfully configured the backend "azurerm"! Terraform will automatically
   use this backend unless the backend configuration changes.

   Successfully configured the backend "azurerm"! Terraform will automatically
   use this backend unless the backend configuration changes.

   Successfully configured the backend "azurerm"! Terraform will automatically
   use this backend unless the backend configuration changes.

   Initializing provider plugins...
   - Finding hashicorp/azurerm versions matching "3.30.0"...

   Initializing provider plugins...
   - Finding hashicorp/azurerm versions matching "3.30.0"...

   Initializing provider plugins...
   - Finding hashicorp/azurerm versions matching "3.30.0"...

   Initializing provider plugins...
   - Finding hashicorp/azurerm versions matching "3.30.0"...
   - Installing hashicorp/azurerm v3.30.0...
   - Installing hashicorp/azurerm v3.30.0...
   - Installing hashicorp/azurerm v3.30.0...
   - Installing hashicorp/azurerm v3.30.0...
   - Installed hashicorp/azurerm v3.30.0 (signed by HashiCorp)

   Terraform has created a lock file .terraform.lock.hcl to record the provider
   selections it made above. Include this file in your version control repository
   so that Terraform can guarantee to make the same selections by default when
   you run "terraform init" in the future.

   Terraform has been successfully initialized!

   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.

   If you ever set or change modules or backend configuration for Terraform,
   rerun this command to reinitialize your working directory. If you forget, other
   commands will detect it and remind you to do so if necessary.
   - Installed hashicorp/azurerm v3.30.0 (signed by HashiCorp)

   Terraform has created a lock file .terraform.lock.hcl to record the provider
   selections it made above. Include this file in your version control repository
   so that Terraform can guarantee to make the same selections by default when
   you run "terraform init" in the future.

   Terraform has been successfully initialized!

   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.

   If you ever set or change modules or backend configuration for Terraform,
   rerun this command to reinitialize your working directory. If you forget, other
   commands will detect it and remind you to do so if necessary.
   /home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin plan -input=false
   /home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin plan -input=false
   - Installed hashicorp/azurerm v3.30.0 (signed by HashiCorp)

   Terraform has created a lock file .terraform.lock.hcl to record the provider
   selections it made above. Include this file in your version control repository
   so that Terraform can guarantee to make the same selections by default when
   you run "terraform init" in the future.

   Terraform has been successfully initialized!

   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.

   If you ever set or change modules or backend configuration for Terraform,
   rerun this command to reinitialize your working directory. If you forget, other
   commands will detect it and remind you to do so if necessary.
   - Installed hashicorp/azurerm v3.30.0 (signed by HashiCorp)

   Terraform has created a lock file .terraform.lock.hcl to record the provider
   selections it made above. Include this file in your version control repository
   so that Terraform can guarantee to make the same selections by default when
   you run "terraform init" in the future.

   Terraform has been successfully initialized!

   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.

   If you ever set or change modules or backend configuration for Terraform,
   rerun this command to reinitialize your working directory. If you forget, other
   commands will detect it and remind you to do so if necessary.
   /home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin plan -input=false
   /home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin plan -input=false

   Terraform used the selected providers to generate the following execution
   plan. Resource actions are indicated with the following symbols:
   + create

   Terraform will perform the following actions:

   # azurerm_resource_group.rg will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "eastus"
         + name     = "aa-prod-eus-mgmt-rg"
         + tags     = {
            + "App_Contact" = "gerry@automationadmin.com"
            + "CostCenter"  = "100"
            + "Description" = "Automation Admin Terraform POC"
            + "Environment" = "prod"
            + "Owner"       = "Automation Admin"
         }
      }

   Plan: 1 to add, 0 to change, 0 to destroy.

   ─────────────────────────────────────────────────────────────────────────────

   Note: You didn't use the -out option to save this plan, so Terraform can't
   guarantee to take exactly these actions if you run "terraform apply" now.

   Terraform used the selected providers to generate the following execution
   plan. Resource actions are indicated with the following symbols:
   + create

   Terraform will perform the following actions:

   # azurerm_resource_group.rg will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "eastus"
         + name     = "aa-prod-eus-mgmt-rg"
         + tags     = {
            + "App_Contact" = "gerry@automationadmin.com"
            + "CostCenter"  = "100"
            + "Description" = "Automation Admin Terraform POC"
            + "Environment" = "prod"
            + "Owner"       = "Automation Admin"
         }
      }

   Plan: 1 to add, 0 to change, 0 to destroy.

   ─────────────────────────────────────────────────────────────────────────────

   Note: You didn't use the -out option to save this plan, so Terraform can't
   guarantee to take exactly these actions if you run "terraform apply" now.

   Terraform used the selected providers to generate the following execution
   plan. Resource actions are indicated with the following symbols:
   + create

   Terraform will perform the following actions:

   # azurerm_resource_group.rg will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-prod-scus-mgmt-rg"
         + tags     = {
            + "App_Contact" = "gerry@automationadmin.com"
            + "CostCenter"  = "100"
            + "Description" = "Automation Admin Terraform POC"
            + "Environment" = "prod"
            + "Owner"       = "Automation Admin"
         }
      }

   Plan: 1 to add, 0 to change, 0 to destroy.

   ─────────────────────────────────────────────────────────────────────────────

   Note: You didn't use the -out option to save this plan, so Terraform can't
   guarantee to take exactly these actions if you run "terraform apply" now.

   Terraform used the selected providers to generate the following execution
   plan. Resource actions are indicated with the following symbols:
   + create

   Terraform will perform the following actions:

   # azurerm_resource_group.rg will be created
   + resource "azurerm_resource_group" "rg" {
         + id       = (known after apply)
         + location = "southcentralus"
         + name     = "aa-prod-scus-mgmt-rg"
         + tags     = {
            + "App_Contact" = "gerry@automationadmin.com"
            + "CostCenter"  = "100"
            + "Description" = "Automation Admin Terraform POC"
            + "Environment" = "prod"
            + "Owner"       = "Automation Admin"
         }
      }

   Plan: 1 to add, 0 to change, 0 to destroy.

   ─────────────────────────────────────────────────────────────────────────────

   Note: You didn't use the -out option to save this plan, so Terraform can't
   guarantee to take exactly these actions if you run "terraform apply" now.
   -01-14T00:25:54Z level=info msg=[command]/home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin init

   Initializing the backend...

   Successfully configured the backend "azurerm"! Terraform will automatically
   use this backend unless the backend configuration changes.

   Initializing provider plugins...
   - Finding hashicorp/azurerm versions matching "3.30.0"...
   - Installing hashicorp/azurerm v3.30.0...
   - Installed hashicorp/azurerm v3.30.0 (signed by HashiCorp)

   Terraform has created a lock file .terraform.lock.hcl to record the provider
   selections it made above. Include this file in your version control repository
   so that Terraform can guarantee to make the same selections by default when
   you run "terraform init" in the future.

   Terraform has been successfully initialized!

   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.

   If you ever set or change modules or backend configuration for Terraform,
   rerun this command to reinitialize your working directory. If you forget, other
   commands will detect it and remind you to do so if necessary.

   -01-14T00:25:54Z level=info msg=[command]/home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin init

   Initializing the backend...

   Successfully configured the backend "azurerm"! Terraform will automatically
   use this backend unless the backend configuration changes.

   Initializing provider plugins...
   - Finding hashicorp/azurerm versions matching "3.30.0"...
   - Installing hashicorp/azurerm v3.30.0...
   - Installed hashicorp/azurerm v3.30.0 (signed by HashiCorp)

   Terraform has created a lock file .terraform.lock.hcl to record the provider
   selections it made above. Include this file in your version control repository
   so that Terraform can guarantee to make the same selections by default when
   you run "terraform init" in the future.

   Terraform has been successfully initialized!

   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.

   If you ever set or change modules or backend configuration for Terraform,
   rerun this command to reinitialize your working directory. If you forget, other
   commands will detect it and remind you to do so if necessary.

   -01-14T00:25:54Z level=info msg=[command]/home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin init

   Initializing the backend...

   Successfully configured the backend "azurerm"! Terraform will automatically
   use this backend unless the backend configuration changes.

   Initializing provider plugins...
   - Finding hashicorp/azurerm versions matching "3.30.0"...
   - Installing hashicorp/azurerm v3.30.0...
   - Installed hashicorp/azurerm v3.30.0 (signed by HashiCorp)

   Terraform has created a lock file .terraform.lock.hcl to record the provider
   selections it made above. Include this file in your version control repository
   so that Terraform can guarantee to make the same selections by default when
   you run "terraform init" in the future.

   Terraform has been successfully initialized!

   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.

   If you ever set or change modules or backend configuration for Terraform,
   rerun this command to reinitialize your working directory. If you forget, other
   commands will detect it and remind you to do so if necessary.

   -01-14T00:25:54Z level=info msg=[command]/home/runner/work/_temp/c3c0f6cb-7901-4fd2-b79b-282c6a920406/terraform-bin init

   Initializing the backend...

   Successfully configured the backend "azurerm"! Terraform will automatically
   use this backend unless the backend configuration changes.

   Initializing provider plugins...
   - Finding hashicorp/azurerm versions matching "3.30.0"...
   - Installing hashicorp/azurerm v3.30.0...
   - Installed hashicorp/azurerm v3.30.0 (signed by HashiCorp)

   Terraform has created a lock file .terraform.lock.hcl to record the provider
   selections it made above. Include this file in your version control repository
   so that Terraform can guarantee to make the same selections by default when
   you run "terraform init" in the future.

   Terraform has been successfully initialized!

   You may now begin working with Terraform. Try running "terraform plan" to see
   any changes that are required for your infrastructure. All Terraform commands
   should now work.

   If you ever set or change modules or backend configuration for Terraform,
   rerun this command to reinitialize your working directory. If you forget, other
   commands will detect it and remind you to do so if necessary.
   ```

   - This would of course fail because each of the two sets of Resource Groups have the same name because I wasn't specific enough with my naming so they would get an error.

   - What's happening, I think, is Terragrunt is going to that directory and recursively searching downwards and finding all four `terragrunt.hcl` files:

   - hub\east\deployment\terragrunt.hcl
   - hub\southcentral\deployment\terragrunt.hcl
   - spoke\east\deployment\terragrunt.hcl
   - spoke\southcentral\deployment\terragrunt.hcl

   - Then for each one, it is passing their customized `locals` as `inputs` to the terraform code that is up at the `infra` folder [way way above it](https://github.com/gerryw1389/terraform-examples/tree/main/2023-01-04-terragrunt-repo-structure-v1/infra). This is because if you read their `source` for terraform, it says `source = "${find_in_parent_folders("infra")}"`

1. But what if you wanted to have code in nonprod that is different than prod? Or east that is different from southcentralus?

   - You have two fixes, one is you set a bunch of [flags](https://automationadmin.com/2022/10/tf-using-flags-for-settings) as your input variables like `includes_resource_group` and if that is true, conditionally deploy that resource.
   - Second is you create separate folder under `./infra` and point to that instead, like `./infa/nonprod` and `./infa/prod` then update your source like `source = "${find_in_parent_folders("infra")}//nonprod"` in your terragrunt.hcl. I cover this in [Terragrunt Repo Structure V2](https://automationadmin.com/2023/01/terragrunt-repo-structure-v2).


1. What if you don't feel like copying that same `terragrunt.hcl` 8 times? Well I found the fix for this shortly after posting this, you just use `includes` and point higher up. I cover this in [Terragrunt Repo Structure V2](https://automationadmin.com/2023/01/terragrunt-repo-structure-v2)

1. As a last example (for now), I wanted to show that you can mix your terragrunt and terraform code in the same structure and just reference terraform from terragrunt by using `source = ./"` in your terragrunt file and keeping them in the same folder structure. I cover this in [Terragrunt Repo Structure V3](https://automationadmin.com/2023/01/terragrunt-repo-structure-v3). Keep in mind this is not recommended since you end up repeating alot which defeats the purpose of terragrunt.

1. That's it for now, will continue to post about Terragrunt in the future. Main reference I used was [this repo](https://github.com/rubiconba/devops-lecture-terragrunt) to get started. Thanks to those contributors!