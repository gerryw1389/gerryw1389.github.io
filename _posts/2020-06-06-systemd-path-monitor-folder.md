---
title: Systemd Path Monitor Folder
date: 2020-06-06T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/06/systemd-path-monitor-folder
categories:
  - Linux
tags:
  - LinuxServer
---
<!--more-->

### Description:

So I needed an event based way to monitor `/csv` for specific csv file patterns. For this example, the pattern the application writes is `dataset_1.csv` where the number increments on the end. Here is how I set RHEL 7 to run a script every time a file was written matching `/csv/dataset_*.csv`:

### To Resolve:

1. Run:

   - `vi /usr/local/bin/csv.ps1`

   - Paste/save:

   ```powershell
   #!/usr/bin/env pwsh
   $date = Get-Date -Format "yyyy-MM-dd-HH:mm:ss"
   write-output "$date : new file" > /home/myuser/new-file.txt
   ```

   - Now test run

   ```shell
   chmod +x /usr/local/bin/csv.ps1
   ./csv.ps1
   cat /home/myuser/new-file.txt
   # 2020-06-05-12:00:49 : new file
   ```

2. Configure a new service and have it run that script when a pattern is found:

   ```shell
   cd /etc/systemd/system
   touch monitorcsv.service
   vi monitorcsv.service

      [Unit]
      Description="Monitor csv directory"

      [Service]
      ExecStart=/usr/local/bin/csv.ps1

   touch monitorcsv.path
   vi monitorcsv.path

      [Unit]
      Description="Monitor the /csv for changes"

      [Path]
      PathExistsGlob=/csv/dataset*.csv
      Unit=monitorcsv.service

      [Install]
      WantedBy=multi-user.target

   systemd-analyze verify /etc/systemd/system/monitorcsv.*
   # gave errors for other services but not the one I created? Moving on...

   sudo systemctl start monitorcsv.path
   
   # Now, we see if it is working...
   rm /home/myuser/new-file.txt
   ll /csv/
   # no dataset*.csv files
   touch /csv/dataset_12.csv
   cat /home/myuser/new-file.txt
   # 2020-06-05-12:12:20 : new file
   # Sweet! Lets see if it fires if we move the csv - it doesn't write


   cat /home/myuser/new-file.txt
   2020-06-05-12:17:25 : new file
   mv /csv/dataset_12.csv /csv/processed/dataset_12.csv
   cat /home/myuser/new-file.txt
   2020-06-05-12:17:25 : new file
   # exactly what we wanted, it doesn't fire because we moved a file from that directory to another
   ```

3. Post config

   ```shell
   # run on startup
   systemctl enable monitorcsv.path

   # troubleshooting (if needed)
   systemctl status monitorcsv.path
   journalctl -u monitorcsv.path
   ```


### References:

["Systemd Path Units"](https://www.putorius.net/systemd-path-units.html)











