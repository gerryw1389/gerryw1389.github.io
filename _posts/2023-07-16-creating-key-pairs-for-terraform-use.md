---
title: Creating Key Pairs For Terraform Use
date: 2023-07-16T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/07/creating-key-pairs-for-terraform-use
tags:
  - Azure
  - Terraform
  - PKI
---
<!--more-->

### Description

Sometimes, you will need to create a key pair, deploy a VM, and then add that key to the Authorized Hosts. Here is how:

### To Resolve:

1. Create keypair for a new user: 

```shell
cd c:\scripts
mkdir keys
cd ./keys/
ssh-keygen -t rsa -m PEM -b 2048
```

1. Take public portion and add it to your variables:

```terraform
variable "ssh_authorized_keys" {
  type        = string
  description = "ssh authorized key"
  default     = "ssh-rsa AAAAB3Nza..D0RiVG6Wz7oisRN81Xu4iraxN"
}
```

1. Run the `terraform apply` to provision the VM.

1. Next, you should be able to ssh to the machine and add other keys as needed.

   ```shell
   gerry@home:C:\scripts\keys
   > ssh  -i key cloud-user@10.97.4.205
   The authenticity of host '10.97.4.205 (10.97.4.205)' can't be established.
   ECDSA key fingerprint is SHA256:E5vsJ6oDFIZxG+AvQaxxEqZ9Ck8b8IBKBBSASBrxfpA.
   Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
   Warning: Permanently added '10.97.4.205' (ECDSA) to the list of known hosts.
   Activate the web console with: systemctl enable --now cockpit.socket

   Register this system with Red Hat Insights: insights-client --register
   Create an account or view all your systems at https://red.ht/insights-dashboard
   [cloud-user@my-vm ~]$
   [cloud-user@my-vm ~]$ sudo su
   [root@my-vm cloud-user]#
   [root@my-vm cloud-user]# whoami
   root
   [root@my-vm cloud-user]#
   [root@my-vm cloud-user]# cat /etc/redhat-release
   Red Hat Enterprise Linux release 8.7 (Ootpa)
   [root@my-vm cloud-user]#
   ```

1. Here we create a new local user and add some public portion of a key pair to authorized_keys file:

   ```shell
   useradd myuser
   mkdir /home/myuser/.ssh
   echo ssh-rsa some-key >> /home/myuser/.ssh/authorized_keys
   visudo # add : %myuser ALL=(ALL) NOPASSWD: ALL
   chown -R myuser:myuser /home/myuser/.ssh
   ```

1. In Windows, to connect to a newly deployed VM you will need to use the SSH Keys you just created. Here is how you do it, for example, connecting to the `my-vm` in previous steps:

1. First, get the private key and paste it in a file called `priv.txt` at `c:\scripts`.
   - Now right click on the file and "disable inheritence" and "convert all permissions to explicit".
   - Then remove everyone except your user and give your user full rights to the file.

1. Now ensure you have the Windows SSH Client feature installed, `Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0`

1. Next, open Powershell and cd to that directory and use the key file to connect to a VM:

   ```shell
   cd c:\scripts
   ssh -i priv.txt cloud-user@10.10.10.10
   ```
