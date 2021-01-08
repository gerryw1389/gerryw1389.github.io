---
title: 'Python: Intermediate Snippets'
date: 2020-06-07T16:00:43-05:00
author: gerryw1389
layout: single
classes: wide
permalink: 2020/06/python-intermediate-snippets
categories:
  - Linux
tags:
  - Scripting-Python
---
<!--more-->

### Description:

Here are some snippets I have been using lately:

### To Resolve:

1. To send a REST API call (Event Grid in this Example):

   ```python
   from datetime import datetime, timezone
   import requests
   import json
   import collections

   def send_req(subject, payload, key):

      date1 = datetime.now(timezone.utc)
      date2 = (str(date1).replace(" ", "T").replace("+00:00", "0")) + 'Z'

      # generate body
      body = collections.OrderedDict()
      body["body"] = payload

      # insert into main body
      data = collections.OrderedDict()
      data["id"] = "MyApp"
      data["subject"] = subject
      data["topic"] = "somePub"
      data["eventType"] = "MyAppApproval"
      data["eventTime"] = date2
      data["data"] = body
      data["dataVersion"] = "1.0"
      data["metadataVersion"] = None
      #print("data: ", data)

      headers = collections.OrderedDict()
      headers['Content-Type'] = 'application/json'
      headers['aeg-sas-key'] = key
      #print("headers: ", headers)

      data2 = "[" + json.dumps(data) + "]"
      #print("data string: ", data2)

      url = "https://mycompany.southcentralus-1.eventgrid.azure.net/api/events"
      r = requests.post(url, headers=headers, data=data2)
      # print(r.status_code)
      return r


   s = '85d89569-5c9e-4fc6-a394-7bb9d724b614'
   p = '{"AppName": "SomeApp", "PermName": "SomePermission", "ChangeRequestType": "ADD"}'
   k = 'SbBjasdfasdf'
   req = send_req(s, p, k)
   print(req.status_code)

   if req.status_code == 200:
      print("good")
   else:
         pass

   ```

2. To send an email using Office 365 user:

   ```python
   import smtplib
   from email.mime.text import MIMEText
   import os

   def send_email(strPassword):
      
      html = """\
      <html>
      <head>
      </head>
      <body>
      This is a sample body
      </body>
      </html>
      """
      msg = MIMEText(html, 'html')
      msg['Subject'] = 'Test message'

      mailserver = smtplib.SMTP('smtp.office365.com',587)
      mailserver.ehlo()
      mailserver.starttls()
      mailserver.login('fromAccount@domain.com', strPassword)
      mailserver.sendmail('fromAccount@domain.com','toAccount@domain.com',msg.as_string())
      mailserver.quit()


   try:
      email = os.environ["EMAIL"]
   except Exception as e:
      exit(1)

   send_email(email)
   ```

3. Read from a CSV file:

   ```python
   import csv

   def read_csv(filename):
      add_remove = []
      app_name = []
      perm_name = []

      with open(filename) as csvDataFile:
         csvReader = csv.reader(csvDataFile)
         for row in csvReader:
               add_remove.append(row[1])
               app_name.append(row[5])
               perm_name.append(row[7])
      return add_remove, app_name, perm_name

   file = '/csv/dataset_500.csv'
   add_remove, app_name, perm_name = read_csv(file)
   print(add_remove[1])
   print(app_name[1])
   print(perm_name[1])
   ```

4. Loop through files in a directory and move them if needed:

   ```python

   import os
   import shutil

   directory = '/myapp'

   try:
      items = os.scandir(directory)
   except Exception as e:
      print("No files in the directory")
      exit(0)

   match = 0

   for item in items:
      # print('processing :', item.name)
      if item.path.endswith(".csv") and item.is_file() and item.name.find('dataset') == 0:
         match = match + 1
         print('Found file to process: ', item.path)
         dest = '/myapp/processed/' + item.name
         # do something with the file
         # move file to destination
         try:
               shutil.move(item.path, dest)
         except Exception as e:
               print("Unable to move folder to destination: ", item.name)
      else:
         pass
      
      if match == 0:
         print("No files in the directory that match expected format")
         exit(0)
      else:
         pass

   ```

5. Run native commands:

   ```python
   import subprocess

   stat = 'systemctl status firewalld'
   print('Running: ', stat)
   st = subprocess.run(stat, shell=True, stdout=subprocess.PIPE)
   print(st)
   ```

6. Using environmental vars:

   - Step 1: Create your venv folder and add the `python-dotenv` package:

   ```shell
   cd /myuser/scripts
   mkdir csv
   cd csv
   scl enable rh-python36 bash
   python -m venv /myuser/scripts/csv/venv
   source /myuser/scripts/csv/venv/bin/activate
   pip install --upgrade pip
   python3 -m pip install python-dotenv
   ```

   - Step 2: Create an `.env` file at the root of your `csv` folder and enter

   ```python
   EMAIL="somePass"
   KEY="someKey"
   ```

   - Step 3: Enter the following in your `.py` file that should also be at root of `csv` folder

   ```python
   from dotenv import load_dotenv

   load_dotenv()

   try:
      key = os.environ["KEY"]
   except Exception as e:
      print("Unable to get environmental variable: key")
      exit(1)
   # same for EMAIL
   ```

7. Implement a base logging:

   ```python
   import logging
   import logging.handlers
   import sys

   logger = logging.getLogger("")
   logger.setLevel(logging.DEBUG)
   handler = logging.handlers.RotatingFileHandler(
      '/mnt/z/google/scripts/python/example3.log', maxBytes=(1048576*5), backupCount=7
   )
   formatter = logging.Formatter("%(asctime)s => %(levelname)s : %(message)s", datefmt='%Y-%m-%d %I:%M:%S %p')
   handler.setFormatter(formatter)
   logger.addHandler(handler)

   logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

   logging.info('hello world')

   logging.error('error - hello world')

   logging.warning('warning - hello world')
   name = 'Gerry'

   logging.error('%s raised an error', name)

   a = 5
   b = 0

   try:
      c = a / b
   except Exception as e:
      logging.error("Exception occurred", exc_info=True)

      logging.warning('warning - hello world')
   ```

   - Output:
  
  ```log
  [user@server logs]# cat eventgrid_2020-06-22-17-19-37.log
   2020-06-22 05:19:37 PM => INFO : ==========================
   2020-06-22 05:19:37 PM => INFO : Starting function...
   2020-06-22 05:19:37 PM => INFO : Logfile fullname: /myuser/scripts/logs/send-eventgrid_2020-06-22-17-19-37.log
   2020-06-22 05:19:37 PM => INFO : Found file to process: /csv/dataset_556.csv
   2020-06-22 05:19:37 PM => INFO : Payload to send: {"key": "someData", "key2": "someData2", "key3": "someData3"}
   2020-06-22 05:19:37 PM => INFO : Sending: SomeData
   2020-06-22 05:19:37 PM => DEBUG : Starting new HTTPS connection (1): mycompany.southcentralus-1.eventgrid.azure.net:443
   2020-06-22 05:19:37 PM => DEBUG : https://mycompany.southcentralus-1.eventgrid.azure.net:443 "POST /api/events HTTP/1.1" 200 0
   2020-06-22 05:19:39 PM => INFO : Request completed successfully
  ```

