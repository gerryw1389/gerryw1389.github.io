---
title: Notepad++ Settings
date: 2017-02-01T04:33:11+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/02/notepadplusplus-settings/
tags:
  - LocalSoftware
tags:
  - PersonalConfig
---
<!--more-->

### Description:

This post is just for my notes on my Notepad++ install.

### To Resolve:

1. Go to Style Configurator => Obsidian

   ```escape
   Consolas 12
   Check box = Enable Global font
   Check box = Enable Global font size
   ```

2. Enable the Explorer plugin and set to my scripts path.

### Tips and Tricks

1. Sort by line and remove the duplicate lines at the same time

   - Get the TextFX plugin. This used to be included in older versions of Notepad++, but if you have a newer version, you can add it from the menu by going to Plugins => Plugin Manager => Show Plugin Manager => Available tab => TextFX => Install. In some cases it may also be called TextFX Characters, but this is the same thing.
   - Then check boxes and buttons required will now appear in the menu under: TextFX => TextFX Tools.
   - Make sure `sort outputs only unique` is checked.
   - Next, select a block of text (Ctrl+A to select the entire document). Finally, click `sort lines case sensitive` or `sort lines case insensitive`

2. To Replace Spaces on Each Line (this happens when you copy multiple columns from Excel to Npp):

   - Copy the amount of spaces in between each word to your clipboard  
   - Press Ctrl+A to select all text  
   - Press Ctrl+H to bring up find/replace  
   - Paste in the blank spaces in the `find what` dialog  
   - In the replace with, make sure it is completely blank  
   - Select the option to replace all

3. To remove trailing spaces for each line:  

   - Edit => Blank Operations => Trim trailing space

4. To remove leading space for each line:  

   - Edit => Blank Operations => Trim leading space

5. To remove empty lines:  

   - Edit => Line Operations => Remove Empty Lines  
   - or in Extended mode:  
   - Search: `\n\r`  
   - Replace: `(blank)`

6. To sort lines alphabetically:  

   - Edit => Line Operations => Sort Lines Lexicographically Ascending

7. Remove all lines that start with specific word

   - Go to the search menu Ctrl+F and open the "Mark" tab.
   - Check "Bookmark line" (if there is no "Mark" tab update to the current version).
   - Enter your search term (Select Regex and `^YourWordHere`) and click "Mark All" - All lines containing the search term are bookmarked.
   - Now go to the Menu "Search => Bookmark => Remove Bookmarked lines"
