---
title: Deploy vRO v8.0.1 Instance
date: 2020-04-08T07:18:46-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/04/deploy-vro-v8-0-1-instance
tags:
  - LocalSoftware
tags:
  - Orchestration
---
<!--more-->

### Description:

In this post, I will go over how I deployed a vRO appliance v8.0.1 in on-prem vCenter.

### To Resolve:

1. Login to VMWare's support site and download the `.iso` image.

2. Deploy it in vCenter with the appropriate hostname, IP Address info, ect.

3. Follow [this guide](https://docs.vmware.com/en/vRealize-Orchestrator/8.0/com.vmware.vrealize.orchestrator-install-config.doc/GUID-61267B72-2963-4E22-9630-DA90AF40EC05.html) to setup vCenter SSO

   - Essentially, login to `https://your_orchestrator_FQDN/vco-controlcenter` with root/ password you setup in vCenter when you deployed appliance
   - Join to vCenter using admin account
   - Add the AD group you want to have access

4. In my case, I couldn't get to vco-controlcenter even on first boot because vco-app failed to even start. So I followed [this KB](https://kb.vmware.com/s/article/78235) which has you run these 3 commands:

   ```shell
   vracli cluster exec -- bash -c 'echo -e "FROM vco_private:latest\nRUN sed -i s/root:.*/root:x:18135:0:99999:7:::/g /etc/shadow\nRUN sed -i s/vco:.*/vco:x:18135:0:99999:7:::/g /etc/shadow" | docker build - -t vco_private:latest'

   vracli cluster exec -- bash -c 'echo -e "FROM db-image_private:latest\nRUN sed -i s/root:.*/root:x:18135:0:99999:7:::/g /etc/shadow\nRUN sed -i s/postgres:.*/postgres:x:18135:0:99999:7:::/g /etc/shadow" | docker build - -t db-image_private:latest'

   #Persist the new changes through reboots:

   /opt/scripts/backup_docker_images.sh
   ```

5. Once that was setup, SSH'd into the box and created a script called `/root/rs.sh` for restart-service:

   ```shell
   /opt/scripts/svc-stop.sh
   sleep 120
   /opt/scripts/deploy.sh --onlyClean
   sleep 60
   /opt/scripts/deploy.sh
   ```

   - I also ran `passwd -x 99999 root` because it has something like under the [release notes](https://docs.vmware.com/en/vRealize-Orchestrator/8.0.1/rn/VMware-vRealize-Orchestrator-801-Release-Notes.html#knownissues)

   - This whole issue started because I would issue `reboot` commands and apparently that stopped Kubernetes from working properly. I would run `kubectl describe nodes` and they would all be set to `starting`. Running `kubectl --namespace kube-system describe pod tiller-deploy-5c996fbc66-zxhmt` would give me `0/1 nodes are available: 1 node(s) had taints that the pod didn't tolerate.`  

6. Troubleshooting VRO:

   - Run `watch "kubectl -n prelude get all"` to see all containers matching prelude and their status
   - Run `kubectl describe nodes` to get a general idea of containers
   - Run `kubectl --namespace kube-system describe pod tiller-deploy-5c996fbc66-zxhmt` to see details on a specific pod, just replace tiller-deploy with whatever from previous command
   - See [here](https://www.tutorialspoint.com/kubernetes/kubernetes_kubectl_commands.htm) for generic commands
   - See [here](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) for more like:

   ```shell
   kubectl get pods --all-namespaces # List all pods in all namespaces
   kubectl get pods # List all pods in the namespace
   kubectl logs my-pod # dump pod logs (stdout)
   ```
