---
title: Developing Python On Windows
date: 2020-10-04T08:30:45-06:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/10/developing-python-on-windows
tags:
  - Windows
  - LocalSoftware
tags:
  - NoteTaking
  - Scripting-Python
  - VsCode
---
<!--more-->

### Description:

As an alternative to [developing with WSL](https://automationadmin.com/2020/06/developing-python-on-windows-wsl) I found it much easier to just install Python on Windows and use vscode. Maybe when I up my skills I will go back to using it with WSL, but here is all I had to do to start developing with Python on Windows.

### To Resolve:

1. Install Python 3.9 windows installer for python.org. During installation, choose to add to path.

2. In vscode, install `python` extension.

3. Upgrade pip:

   ```powershell
   cd "C:\Program Files\Python39\"
   ./python.exe -m pip install --upgrade pip
   ```

4. Then, if you have a file you want to format, it will prompt you to install `pep8`. Just select "yes" and it will install no hassles (unlike WSL where I had to fight it for some reason).

5. If you want to install packages on your system, just use `pip`. For example, for `azure-functions` I did:

   - Install by `./python.exe -m pip install azure-functions`
   - then type: `./python.exe`
   - now that you are in python, just type `import azure.functions` and start using their [module](https://docs.microsoft.com/en-us/python/api/azure-functions/azure.functions?view=azure-python)
