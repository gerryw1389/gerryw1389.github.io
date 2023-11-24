---
title: VSCode Config
date: 2019-06-15T00:40:27-05:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/06/vscode-config
tags:
  - LocalSoftware
tags:
  - PersonalConfig
  - NoteTaking
---
<!--more-->

### Description:

So I have been using [Cherrytree](https://www.giuspen.com/cherrytree/) for a long time, but recently wanted to try out VSCode for everyday note taking. Here is where I will keep my VSCode Settings over time. I exported all notes to a directory. Then used powershell to bulk rename all `.txt` to `.md` - [see here](https://github.com/gerryw1389/powershell/blob/main/gwFilesystem/Public/Rename-Items.ps1). After moving to VScode, I only needed to [fix the themes for Markdown](https://automationadmin.com/2019/12/modify-vscode-markdown-theme/) and I was good to go!

### To Resolve:

1. Keyboard shortcuts

   - `Ctrl+Shift+p` - Brings up search menu

   - Basic
   - `shift+alt+f` - format code (best feature in vscode!!)
   - `shift+alt+up/down` - Copy line
   - `ctrl+end` - go to end of file/  `ctrl+home` - go to beginning of file
   - `alt+z` - toggle line wrap
   - `ctrl+x` - No selection / cut line - same for copy and `ctrl+c`
   - `Ctrl+Shift+v` - In the editor, this allows you see your markdown in another tab

   - Cursors
   - `Ctrl+Alt+up/down` - Insert cursor above/below
   - `shift+alt+i` - Insert cursor at end of each line selected
   - `Alt+Click` - Add new cursor

   - Find / Replace
   - `Ctrl+Shift+f` - This searches all files. Just remember to put `./_notes` in the includes if you want to search by folder
   - `Ctrl+Shift+h` - Same but replace

2. Extensions (as of 2019-06):

   - For an up-to-date reference, check out my [Settings.json here](https://github.com/gerryw1389/misc/blob/main/vscode/settings-sync.json)

   - Linux Themes for VS Code
     - Preferred theme - 'Monokai Dimmed'
   - Markdown All in one
     - So that you can use shortcuts to like `Ctrl+B` to bold something
   - Markdown PDF
     - Print PDFs from .md files
   - Paste Image
     - Allows you to paste from clipboard using `Ctrl+Alt+V`
   - Scripting-Powershell
     - Auto format code using `Ctrl+Alt+F`
     - Auto linting
   - Puppet
     - Auto linting
   - vscode-fileheader
     - Press `Ctrl+Alt+i` to insert a header to a file
   - vscode-icons
     - Preferred icon theme
   - Insert DateString
     - Adds date by `Ctrl+Shift+i` and full date by `Ctrl+Shift+Alt+i`

3. Extensions - Config

   - Configure vscode-fileheader

   ```escape
   "fileheader.tpl": "---\r\n@Author: {author}\r\n@Date: {createTime}\r\n@Last Modified by: {lastModifiedBy}\r\n@Last Modified time: {updateTime}\r\n---\r\n\r\n",
   "fileheader.LastModifiedBy": "Gerry Williams",
   "fileheader.Author": "Gerry Williams",
   ```

   - Now, when you press `Ctrl+Alt+i` you get the following at the top of your file:

   ```escape
   ---
   @Author: Gerry Williams
   @Date: 2019-06-03 13:26:12
   @Last Modified by: Gerry Williams
   @Last Modified time: 2019-06-03 13:26:12
   ---
   ```

4. settings.json (User/Workspace) - VS Code provides two different scopes for settings:
   - User Settings - Settings that apply globally to any instance of VS Code you open. This is the `settings.xml` file.
   - Workspace Settings - Settings stored inside your workspace and only apply when the workspace is opened. This is a `*.code-workspace` file.
   - ***Note: Workspace settings override user settings.***
   - For an up-to-date reference, check out my [Settings.json](https://github.com/gerryw1389/misc/blob/main/vscode/settings-sync.json)

5. [keybindings.json](https://github.com/gerryw1389/misc/blob/main/vscode/keybindings.json) - Preferences: Open Keyboard Shortcuts File (json)

6. Don't forget - Create VSCode PS profile: `Microsoft.VSCode_profile.ps1` in `C:\users\username\Documents\WindowsPowershell`
