---
title: Centos 7 Monitor Directory With Python3
date: 2020-06-09T14:00:43-05:00
author: gerryw1389
layout: single
classes: wide
permalink: 2020/06/centos-7-monitor-dir-with-python-3
categories:
  - Linux
tags:
  - Scripting-Python
---
<!--more-->

### Description:

So the other day, I wrote a [post](https://automationadmin.com/2020/06/systemd-path-monitor-folder) about using the open source version of pwsh to monitor a path, but today I wanted to convert that over to python3. Here is how I did it:

### To Resolve:

1. Following [this guide](https://developers.redhat.com/blog/2018/08/13/install-python3-rhel/#tldr) I installed python 3 on my RHEL 7 box by running:

   ```shell
   subscription-manager repos --enable rhel-7-server-optional-rpms \
   --enable rhel-server-rhscl-7-rpms
   yum -y install @development
   yum -y install rh-python36
   ```

2. Next, I copied over my `monitorcsv.py` that I have been building in vscode:

   ```shell
   cd /myuser/scripts
   mkdir csv
   cd csv
   scl enable rh-python36 bash
   python -m venv /myuser/scripts/csv/venv
   source /myuser/scripts/csv/venv/bin/activate
   pip install --upgrade pip
   python3 -m pip install requests
   python3 -m pip install python-dotenv
   vi monitorcsv.py
   #paste in script
   chmod 700 monitorcsv.py
   exit
   ```

3. Next, I created a caller bash script:

   ```shell
   vi /myuser/scripts/monitorcsv.sh
   # paste in:
   #!/bin/bash
   scl enable rh-python36 bash
   source /myuser/scripts/csv/venv/bin/activate
   python /myuser/scripts/csv/monitorcsv.py
   chmod 700 csv.sh
   ```

4. Create an `.env` file for python to load environmental variables within the env:

   ```python
   EMAIL="somePass"
   KEY="someKey"
   ```

   - Make sure to add at top of your python script:

   ```python
   from dotenv import load_dotenv

   load_dotenv()
   ```

5. Now just update your [service file](https://automationadmin.com/2020/06/systemd-path-monitor-folder) to point to `/myuser/scripts/monitorcsv.sh` instead. Ensure you do a `systemctl daemon-reload` followed by `systemctl restart yourservice.path` and `systemctl restart yourservice` for changes to take effect.
