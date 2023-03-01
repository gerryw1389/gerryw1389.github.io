---
permalink: /lab/
title: "Lab"
layout: single
classes: wide
---

In an effort to better understand Terraform, I have signed up for 4 pay-as-you-go subscriptions in Azure:

- automationadmin-hub-nonprod
- automationadmin-hub-prod
- automationadmin-spoke-nonprod
- automationadmin-spoke-prod

This is a common model people use for managing cloud providers as you can search `hub and spoke model` and get hundreds of results. One of the first links is to Microsoft's [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/hub-spoke-network-topology) which I reference often. In it, they basically say:

   - In your hub subscriptions, you can have DNS zones, Express Route connections, ect. setup.
   - In your spoke subscriptions, you can reference your hub subscription resources as needed.

This is a common theme you will see in my [Terraform Examples Repo](https://github.com/gerryw1389/terraform-examples) where I will be passing two subscription ID's as environmental variables ( [for example](https://github.com/gerryw1389/terraform-examples/blob/main/2023-02-27-terraform-template/yaml/spoke/release/prod-eus-linux.yaml#L79)). The key here is that those will always be used to build two providers:

   - A [`spoke-subscription` provider](https://github.com/gerryw1389/terraform-examples/blob/6fb0ddc2388bef96712397c97eb92e11f6acc457/2023-02-27-terraform-template/infra/nonprod/spoke/scus/backend.tf#L37)
   - A [`hub-subscription` provider](https://github.com/gerryw1389/terraform-examples/blob/6fb0ddc2388bef96712397c97eb92e11f6acc457/2023-02-27-terraform-template/infra/nonprod/spoke/scus/backend.tf#L56).

Then, in your deployment's main.tf for example, you can reference resources in your hub subscription if needed by [passing the providers](https://developer.hashicorp.com/terraform/language/modules/develop/providers#passing-providers-explicitly).

   - You can see this in the [common data lookup module call](https://github.com/gerryw1389/terraform-examples/blob/6fb0ddc2388bef96712397c97eb92e11f6acc457/2023-02-27-terraform-template/infra/nonprod/spoke/scus/common_data_lookup.tf#L47).
   - This is because that module references resources both hub nonprod and hub prod subscriptions.
   - This example uses a different method to build providers on the fly and call a module. I don't have an example on my blog where you pass a hub and spoke provider but it happens all the time at my job where modules will need to reference resources in the spoke subscription and the hub subscription so just be aware.

The following posts go into more details about my "test lab":
   - [Setup Azure Devops For Terraform](https://automationadmin.com/2022/05/setup-azdo-terraform)
   - [Terraform: Setup New Subscription](https://automationadmin.com/2022/10/tf-new-subscription)
   - [Terraform: Template](https://automationadmin.com/2022/10/terraform-template)

Lastly, I have written [tons of posts](https://automationadmin.com/tags/#infrastructureprovisioning) about terraform and how to use it with CI/CD pipelines so be sure to give those a read. Thanks!