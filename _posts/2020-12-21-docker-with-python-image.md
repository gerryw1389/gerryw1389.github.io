---
title: Docker With Python Image
date: 2020-12-21T11:37:56-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/12/docker-with-python-image
tags:
  - Linux
tags:
  - VirtualizationSoftware
  - Scripting-Bash
  - Scripting-Python
---
<!--more-->

### Description:

In this post, I will get started with Docker by downloading the `python` image and playing around with it.

### To Resolve:

1. To start fresh, I wanted to install an [Ubuntu VM](https://automationadmin.com/2020/12/latest-ubuntu-install) on Hyper-V. One that I will use often. I have always been a fan of the MATE desktop so I started with that:

   - Download Ubuntu Mate 20.04
     - Install as a Generation 2 VM. Before starting, go to Settings and uncheck "Secure Boot" settings.
     - Start installer, set everything as normal and ensure you don't enable auto-login.

   - Run:

   ```shell
   sudo apt-get update -y && sudo apt-get upgrade -y

   # setup Hyper-V stuff
   wget https://raw.githubusercontent.com/Microsoft/linux-vm-tools/master/ubuntu/18.04/install.sh
   sudo chmod +x install.sh
   sudo ./install.sh

   #if error:
   sudo vi /etc/xrdp/xrdp.ini

   #change port= to 
   port=vsock://-1:3389
   use_vsock=false
      
   sudo ufw enable
   sudo ufw allow 3389
   sudo ufw list

   # older instructions, feel free to ignore but they get the larger screen
   sudo vi /etc/default/grub
   GRUB_CMDLINE_LINUX_DEFAULT="quiet splash video=hyperv_fb:1720*1440"
   sudo update-grub
   ```

   - This wasn't working until I went and modified `/etc/xrdp/xrdp.ini` once again:

   ```shell
   port=tcp://:3389
   use_vsock=true
   ```

   - This got me a RDP session, but there were a few problems:
    - This didn't enable `enhanced mode` with shared clipboards, drives, ect like I wanted
    - If you were logged into the VM, it would give an error `xrdp could not acquire name on session bus`. So you had to `logoff` the user.

   - After reading, I found that it would probably be best to just install regular Ubuntu 18.04 from the [quick create](https://www.tenforums.com/tutorials/118110-hyper-v-quick-create-setup-ubuntu-linux-virtual-machine.html) screen in Hyper-V, so I went with that instead.

2. Next, install [Docker](https://docs.docker.com/engine/install/ubuntu/):

   - Run:

   ```shell
   # first update and install vim
   sudo apt-get update -y && sudo apt-get upgrade -y
   sudo apt install vim

   # Now copy the following to gedit:
   sudo apt-get install \
   apt-transport-https \
   ca-certificates \
   curl \
   gnupg-agent \
   software-properties-common

   #paste that in the terminal and let it install those packages

   #Add Docker’s official GPG key:
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

   #Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
   sudo apt-key fingerprint 0EBFCD88

   sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

   #install
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```

3. Now let's get started

   - Run:

   ```shell
   mkdir ~/my-app
   cd ~/my-app
   vim ./app.py

   #paste in:
   #!/usr/bin/env python
   for x in range(0,11):
      if x % 2 == 0:
            print(x)

   vim ./requirements.txt
   #paste in:
   requests==2.22.0

   vim dockerfile
   #paste in:
   FROM python:3
   WORKDIR /usr/src/app
   COPY requirements.txt ./
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   CMD [ "python", "./app.py" ]
   ```

   - Next, we build the container and run it:

   ```shell
   sudo docker build -t myapp .
   sudo docker run -it --rm --name my-running-app myapp

   # should see
   # 0
   # 2
   # 4
   # 6
   # 8
   # 10
   ```

4. Now we will make a change and run it again:

   - Run:

   ```shell
   # Modify app.py to now be:
   #!/usr/bin/env python
   import time

   for x in range(0,11):
      print(f"processing...{x}")
      if x % 2 == 0:
            time.sleep(7)
            print(x)

   # rebuild it
   sudo docker build -t myapp .
   # run it again
   sudo docker run -it --rm --name my-running-app myapp
   # now we see:
   # processing...0
   # number is divisible by 2: 0
   # processing...1
   # processing...2
   # number is divisible by 2: 2
   # processing...3
   # processing...4
   # number is divisible by 2: 4
   # processing...5
   # processing...6
   # number is divisible by 2: 6
   # processing...7
   # processing...8
   # number is divisible by 2: 8
   # processing...9
   # processing...10
   # number is divisible by 2: 10
   ```

5. This is cool and all, but what if we run `sudo docker ps` or even with a `-a` switch, it doesn't list anything. That is because these containers are spun up, ran, and torn down. Let's see if we can modify this to run a web server or something instead:

   - run:

   ```shell
   cd ~
   mkdir myapp2
   cd ~/myapp2
   echo "hello world" > a.html
   python3 -m http.server
   # in a web browser, go to localhost:8000 and you will see a.html. Clicking on that will get you the hello world page.

   # now lets put it in a file and try again:
   vim server.py
   ```

   ```python
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
   ```

   ```shell
   # validate
   python3 ./server.py
   # Should say launching server and stay running until you control-c

   # create a src folder and move the server.py there for docker to use
   mkdir src
   mv ./server.py ./src/

   # now lets create a dockerfile and run it
   vim dockerfile
   # paste in per https://jonathanmeier.io/containerize-a-python-web-server-with-docker/
   FROM python:3.8
   ENV SRC_DIR /usr/bin/src/webapp/src
   COPY src/* ${SRC_DIR}/
   WORKDIR ${SRC_DIR}
   ENV PYTHONUNBUFFERED=1
   CMD ["python", "simple_server.py"]
   # this says:
   # Use python 3.8
   # Copy the files in our project directory’s src folder into the container at /usr/bin/src/webapp/src.
   # Then set the image’s working directory to the src directory.
   # Set PYTHONUNBUFFERED=1 as an environment variable so that python sends print and log statements directly to stdout. 
   # If we did not set this, we would not see logs from our container because they would be sent to a buffer.

   # first let's modify our html page before build
   vim a.html
   # move it to src folder as well
   mv ./a.html ./src/
   # change hello world to "hello world from container"

   # now build and run
   sudo docker build -t myapp2 .
   sudo docker run -p 8000:8000 --name my-running-web-server myapp2

   # if you open a browser you can now go to localhost:8000/a.html and see "hello world from container"!
   ```

6. Now that we got this far, I'm not really digging the "control-c" thing. If I run `sudo docker ps` I can now get some containers to show up but many times not cleanly. 

   - I think running it detached would be better. This is done with `-d` switch.
   - So now I run `sudo docker run -d -p 8000:8000 --name my-r2 myapp2` and I get a long string.
   - Now if I run `sudo docker ps` I get a clean looking output with the correct string showing the container is running steadily.
     - If I want to see its logs I can run `sudo docker logs -ft my-r2`. 
     - I prefer doing `sudo docker container logs my-r2` instead though so I don't have to Control-C out of it.
   - If I want to stop/start/restart the container, I run `sudo docker container stop my-r2` replacing stop appropriately
   - If I want similar output to `sudo docker ps`, I can run `sudo docker container ls`



