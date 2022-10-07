---
title: Python Use Config Files
date: 2021-07-13T19:25:23-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2021/07/python-use-config
categories:
  - LocalSoftware
tags:
  - Scripting-Python
---
<!--more-->

### Description

One of the easiest ways you can differentiate between environments with python apps is to create yml files in the application's directory and set an environmental variable as the environment. I haven't gotten around to re-writing all my applications (Function Apps), but I plan to do this soon.

### To Resolve:

1. Create your regular `.env` file as follows like:

   ```escape
   STAGE=production
   ```

   - If using a Function App, just set the environmental variable in the Application Settings blade and then do like usual

   ```python
   def import_creds():
      '''
      Gets secrets from Azure Keyvault as an application
      Secret values are stored in the Function App under Configuration
      
      Example of how to call from main():
      keyvault_creds = import_creds()
      logging.info(f"client_id: { keyvault_creds['client_id'] }")
      logging.info(f"client_secret: { keyvault_creds['client_secret'] }")
      logging.info(f"tenant: { keyvault_creds['tenant'] }")
      logging.info(f"vault_name: { keyvault_creds['vault_name'] }")
      '''

      try:
         creds = {}
         creds["client_id"] = os.environ["client_id"]
         creds["client_secret"] = os.environ["client_secret"]
         creds["tenant"] = os.environ["tenant"]
         creds["vault_name"] = os.environ["vault_name"]
      except KeyError:
         logging.error("Unable to get env vars")
      except Exception as e:
         logging.error(f"Generic Catch: {str(e)}")

      return creds
   ```

2. But this time, set a config file in the directory called `.dev.config.yaml` with the contents of:

   ```yaml
   servers:
      - host-a.domain.com
      - host-b.domain.com
      - networks:
         - 10.20.20.0
         - 10.30.30.30

   endpoints:
      - service_now: https://myendpoint-dev.com
      - key: dev-adcd1234567890
   ```

   - Also create a `.prod.config.yaml` in the same directory with the values of:

   ```yaml
   servers:
      - host-c.domain.com
      - host-d.domain.com
      - networks:
         - 10.20.20.0
         - 10.30.30.30

   endpoints:
      - service_now: https://myendpoint-prod.com
      - key: prod-adcd1234567890
   ```

   - Then, either in its own file like `config.py` or inside your `helpers.py`, import them:

   ```python
   import os
   import sys
   from pathlib import Path
   import yaml

   from dotenv import load_dotenv

   load_dotenv()

   try:
      APP_ENV = os.getenv('STAGE', 'development')
   except Exception as e:
      print(f"Unable to get environmental variable: {STAGE}")
      exit(1)

   CONFIG_FILES = {
      'development': '.dev.config.yaml',
      'production': '.prod.config.yaml',
   }

   try:
      conf_file = Path(__file__).parent.joinpath(CONFIG_FILES[APP_ENV])
   except KeyError:
      print(f"Environment config file not found. Provided: '{APP_ENV}'. Accepted: {CONFIG_FILES}")
      sys.exit(1)

   with open(conf_file, 'r') as f:
      CONFIG = yaml.safe_load(f)
   ```

3. Make sure your `requirements.txt` includes the following

   ```escape
   PyYAML==5.3.1
   python-dotenv==0.14.0
   ```

4. Now, in your main code, just call the same config regardless of the environment. For example, in a `main.py`:

   ```python
   from config import CONFIG

   servers = CONFIG['servers']
   print(servers)
   # ['host-c.domain.com', 'host-d.domain.com', {'networks': ['10.20.20.0', '10.30.30.30']}]
   print(servers[0])
   # host-c.domain.com
   print(servers[1])
   # host-d.domain.com
   print(servers[2]['networks'])
   # ['10.20.20.0', '10.30.30.30']
   print(servers[2]['networks'][0])
   # 10.20.20.0

   endpoints = CONFIG['endpoints']
   print(endpoints)
   # [{'service_now': 'https://myendpoint-dev.com'}, {'key': 'dev-adcd1234567890'}]

   sn = CONFIG['endpoints'][0]['service_now']
   print(sn)
   # https://myendpoint-dev.com

   key = CONFIG['endpoints'][1]['key']
   print(key)
   # dev-adcd1234567890
   ```
