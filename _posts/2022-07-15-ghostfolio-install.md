---
title: Ghostfolio Install
date: 2022-07-15T09:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2022/07/ghostfolio-install/
categories:
  - Linux
  - LocalSoftware
tags:
  - Setup
  - LinuxServer
  - Scripting-Bash
  - VirtualizationSoftware
  - Scripting-Powershell
  - Scripting-RestAPI
---
<!--more-->

### Description:

So I needed an excuse to follow the `Rocky verus Alma` debate that has been going on since the [Centos issue](https://www.reddit.com/r/Fedora/comments/rg62vp/centos_linux_8_is_about_to_die_what_do_you_do/) (basically instead of being a downstream disto for RHEL they are moving it upstream which will make it less stable, at least in theory) so I decided to create a server using Hyper-V and install [Ghostfolio](https://github.com/ghostfolio/ghostfolio) on Rocky 8 as a test. Here are my notes.

### To Resolve:

1. Create VM and run the command to allow virtualization: `Set-Vmprocessor -Vmname ghostfolio -ExposeVirtualizationExtensions $True`

1. Update: `sudo dnf update --refresh`

1. Install EPEL: 

   ```shell
   sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
   sudo dnf update --refresh
   ```

1. Install docker/git:

   ```shell
   sudo dnf install -y dnf-utils git
   sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
   sudo dnf install -y docker-ce
   ```

   - So I had an issue where when I copied the URL it pasted with a `1~` on the end so when I went to install docker it said `docker not found` or something.
   - I then ran a `sudo dnf repolist` and found `download.docker.com_linux_centos_docker-ce.repo1_.repo` in the list of repos.
   - So I googled `dnf remove repo` and found a bunch of links on how to disable the repo but the idea is to do something like:

   ```shell
   rpm -qa |grep -i repo-name
   rpm -e some-repository-rpm-package

   # If RPM-package not found then simply remove repo file with following command:
   # rm /etc/yum.repos.d/repo-file.repo

   # so this removed the repo from the repolist
   rm /etc/yum.repos.d/download.docker.com_linux_centos_docker-ce.repo1_.repo

   ```

   - So I ran the docker install again and this time it worked since it found the correct package from the repo.

1. So now that it is installed, let's start it `sudo systemctl start docker` and enable it `sudo systemctl enable docker`

   - verify: `sudo systemctl list-unit-files | grep docker` shows `docker.service` is `enabled`


1. Add firewall rules for docker:

   ```shell
   sudo firewall-cmd --zone=public --add-masquerade --permanent
   sudo firewall-cmd --reload
   ```

1. Download/install docker-compose:

   ```shell
   sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

1. Next, we add our user account to the `docker` group so we don't have to keep using `sudo`:

   ```shell
   sudo usermod -aG docker gerry
   id gerry # see docker in list
   ```

1. Now we can run a test container:

   ```shell
   mkdir ~/my-app
   cd ~/my-app
   mkdir src
   cd src
   vi ./simple_server.py
   #paste in:
      #!/usr/bin/env python
      from http.server import HTTPServer, SimpleHTTPRequestHandler
      def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
            """Entrypoint for python server"""
            server_address = ("0.0.0.0", 8000)
            httpd = server_class(server_address, handler_class)
            print("launching server...")
            httpd.serve_forever()

      if __name__ == "__main__":
         run()
   #exit
   # So this should start the webserver, but first let's give it a page to feed us:
   echo "hello from container port 8000" > a.html
   # now go back up a level to dockerfile directory
   cd ..
   vi dockerfile
   #paste in:
      FROM python:3.8
      ENV SRC_DIR /usr/bin/src/webapp/src
      COPY src/* ${SRC_DIR}/
      WORKDIR ${SRC_DIR}
      ENV PYTHONUNBUFFERED=1
      CMD ["python", "simple_server.py"]
   # exit; See https://automationadmin.com/2020/12/docker-with-python-image for explanation of the dockerfile
   # this will build the docker app:
   docker build -t myapp .
   # This will spin up a container based off the build in detached mode:
   docker run -d -p 8000:8000 --name myapp-running myapp
   ```

1. Now we can run a second container so we can see how Docker keeps static copies of data in each container:

   ```shell
   cd ./src
   vi a.html
   # change the port to 8005
   # exit
   vi simple_server.py
   # change the port to 8005
   # exit
   cd ..
   docker build -t myapp2 .
   # This will spin up a container based off the build in detached mode:
   docker run -d -p 8005:8005 --name myapp2-running myapp2
   ```

1. Now from another machine on the network, open up a browser and go to the URLs and you should see the two containers running on different ports: `http://192.168.10.10:8000/a.html` and `http://192.168.10.10:8005/a.html`

1. So after this what I did was practice different docker commands by spinning up containers and deleting them, viewing them, stopping them, ect.

   - First, to view containers that are running, run: `docker ps`
   - To see all containers regardless of status: `docker ps -a`. This is important because you CANNOT reuse a container name or image name so you have to delete container or image if you want to use them again.
   - The longer way to view containers: `docker container ls`
   - To delete a container: `docker rm 4743b12994cb --force`. Note: In this case `4743b12994cb` was the container id and I used `--force` because the container was running. If you stop it first you should be able to delete cleanly. You can also pass in the container name.
   - To stop a container: `docker stop myapp2-running`. You can use `start` and `restart` as well.
   - Apparently, the previous commands are shorter ways of writing out `docker container rm` or `docker container stop` or `docker container $subcommand`

1. So containers are one thing, but another thing is `images` or builds.

   - First, to view images, run `docker image ls`
   - To delete an image: `docker image rm myapp --force`

1. Also, if you expose a container but the outside can't reach it, it could be your host's firewalls so you need to make sure to do the usual:

   ```shell
   firewall-cmd --add-port=8005/tcp --permanent
   firewall-cmd --reload
   ```

1. As you can imagine, we have only scratched the surface of docker. See [the full](https://docs.docker.com/engine/reference/commandline/docker/) list of commands you can run to manage containers and play around to learn more. I will in future posts.

1. Okay, so I have a VM and I have docker, let's [get started](https://github.com/ghostfolio/ghostfolio/blob/main/README.md) ...

1. First, let's make a directory for our project: `mkdir ~/ghost && cd ~/ghost`

1. Pull the repo: 

   ```shell
   ssh-keygen -t rsa -b 4096 -C "gerry@automationadmin.com"

   # Add the key to your SSH Agent for Auth:
   ssh-add ~/.ssh/id_rsa
   # Could not open a connection to your authentication agent.
   eval `ssh-agent -s`
   ssh-add -l
   #The agent has no identities.
   ssh-add ~/.ssh/id_rsa
   # Identity added: /home/gerry/.ssh/id_rsa (gerry@automationadmin.com)

   cat ~/.ssh/id_rsa.pub
   # Add the ssh key to your github account.
   # Clone the repo by the following:
   git clone git@github.com:ghostfolio/ghostfolio.git
   ```

1. Edit the `./env` secrets: 
   - Type: `vi ./env` , enter your secrets where it says to, save and exit.

1. Pull the image: `docker-compose --env-file ./.env -f docker/docker-compose.yml up -d`

   - Running `docker container ls` shows 3 containers running: redis, postgres, and ghostfolio.

1. Setup the DB `docker-compose --env-file ./.env -f docker/docker-compose.yml exec ghostfolio yarn database:setup`

1. Open `http://192.168.10.10:3333` in your browser and accomplish these steps:

   - Create a new user via Get Started (this first user will get the role ADMIN)
   - Go to the Admin Control Panel and click Gather All Data to fetch historical data
   - Click Sign out and check out the Live Demo


1. I then wrote some Powershell files to test adding transactions via REST API:

   ```powershell
   Function Get-GhostToken
   {
      [CmdletBinding()]
      Param
      (
         [string]$AccountID
      )

      $URL = "http://192.168.10.10:3333/api/v1/auth/anonymous/" + $AccountID
      $headers = @{ } 
      $body = @{}
      $params = @{
         "Headers" = $headers
         "Body"    = $body
         "Method"  = "GET"
         "URI"     = $URL
      }
      [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
      $req = Invoke-RestMethod @params
      return $($req.authToken)
   }

   Function Add-Record
   {
      [CmdletBinding()]
      Param
      (
         [string]$AuthToken
      )

      $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
      $headers.Add("Content-Type", "application/json")
      $headers.Add("Accept", "application/json")
      $headers.Add("Authorization", "Bearer $AuthToken")
      
      $bodyArray = @()   
      $body = [ordered]@{
         "currency"   = "USD"
         "date"       = "2018-05-06T00:00:00.000Z"
         "dataSource" = "MANUAL"
         "fee"        = 0
         "quantity"   = 1
         "symbol"     = "VTSAX"
         "type"       = "BUY"
         "unitPrice"  = 50
      }
      $bodyArray += $body
      $bodyJson = $bodyArray | ConvertTo-Json
      #Write-Verbose $bodyJson
      $params = @{
         "Headers"     = $headers
         "Body"        = $bodyJson
         "Method"      = "Post"
         "URI"         = "http://192.168.10.10:3333/api/v1/order"
         "ContentType" = "application/json"
      }
      [Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"
      $req = Invoke-RestMethod @params -Verbose
      return $req
   }

   $AccountID = "my-account-number"

   $Token = Get-GhostToken -AccountID $AccountID

   $Record = Add-Record -AuthToken $Token -Verbose

   Write-Output $Record
   ```

   - From here, you just need to export CSV files from your financial institutions, create a powershell script to read them in using [`import-csv`](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-csv?view=powershell-7.2) and then do an `Add-Record` function call with the values. I didn't want to go this far as I just wanted a simple setup for now. Maybe will update in the future.