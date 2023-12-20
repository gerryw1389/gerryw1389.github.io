---
title: Setup Portable Python Scripts On Windows
date: 2020-02-06T08:31:52-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/02/setup-portable-python-scripts-on-windows
tags:
  - Windows
tags:
  - Python
---
<!--more-->

### Description:

Sometimes, you may need to run python scripts on Windows. In many cases, it is best to create virtual directories for each script that you run so that if you upgrade python on the system, dependencies will remain stable. Here is how I would go about setting up a new utility server (this assumes you have a `dependencies.txt` inside each python folder with the name of modules you need python to import):

### To Resolve:

1. Copy the self contained folders over and delete the `venv` folder for each one, we will recreate them to make sure it works.

2. Install python 3.8.2 (windows amd64 installer) to `e:\python` globally on the windows server.

3. Open PS as administrator and type:

   ```powershell
   cd c:\scripts
   e:\python\python.exe -m venv c:\scripts\venv
   cd .\venv\scripts
   . .\activate.ps1
   # should now see : (venv) PS C:\scripts\venv\Scripts>
   pip install -r E:\Python1\dependencies.txt
   # it then says that pip needs upgraded, so run:
   python -m pip install --upgrade pip
   exit
   ```

4. Now copy 'c:\scripts\venv' to 'e:\Python1'

5. Before continuing, it said something about pip being too old so lets upgrade it: `e:\python\python.exe -m pip install pip --upgrade`

6. Now test that it works, close all PS windows and open a brand new PS Admin window and type

   ```powershell
   cd e:\Python1
   cd .\venv\scripts
   . .\activate.ps1
   # should now see : (venv) PS e:\Python1\venv\Scripts>
   cd ..\..
   # should now see : (venv) PS e:\Python1>
   python main.py
   # look for any errors.
   ```

   - This assumes that you have a `main.py` in a directory above `venv` that runs some kind of python code.

7. Now just fix any errors until it runs:

   ```powershell
   (venv) PS E:\Python1\venv\Scripts> cd ..\..
   (venv) PS E:\Python1> python main.py
   Running...
   Traceback (most recent call last):
   File "main.py", line 111, in <module>
      main()
   File "main.py", line 20, in main
      conn.bind()
   File "E:\Python1\venv\lib\site-packages\ldap3\core\connection.py", line 530, in bind
      self.open(read_server_info=False)
   File "E:\Python1\venv\lib\site-packages\ldap3\strategy\sync.py", line 56, in open
      BaseStrategy.open(self, reset_usage, read_server_info)
   File "E:\Python1\venv\lib\site-packages\ldap3\strategy\base.py", line 147, in open
      raise LDAPSocketOpenError('unable to open socket', exception_history)
   ldap3.core.exceptions.LDAPSocketOpenError: ('unable to open socket', [(LDAPSocketOpenError('socket connection error while opening: [WinError 10061] No connection could be made because the target machine actively refused it'), ('10.10.10.100', 636))])
   (venv) PS E:\Python1>
   ```

   - We can see here that it is trying to make an LDAP BIND to port 636 on `10.10.10.100` but getting rejected. Looks like we need to verify that this new server has access to that server at the network layer (switch rules or Network Security Group) and the host layer (make sure destination server will allow inbound from this server)

