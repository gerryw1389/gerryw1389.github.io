---
title: Customizing A Chrome Theme
date: 2018-03-18T15:06:01+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/customizing-a-chrome-theme/
categories:
  - LocalSoftware
tags:
  - Tweaks
---
<!--more-->

### Description:

Follow this post to take a Chrome theme and tweak it to your needs.

### To Resolve:

1. Follow [How to edit Chrome Themes](https://github.com/mike-u/EditChromeThemes)

2. Download and install the "just black" theme from the Theme store.

3. Open `%localappdata%\Google\Chrome\User Data\Default\Extensions` and sort by date modified. Select the first one and find the `manifest.json` file.

4. Copy the files to another folder, I chose `c:\scripts\t`

5. Change something. I changed `tab_text` to `138, 210, 147`

6. Open Chrome and go to `chrome://extension`. Enable developer mode (checkbox at the top) and browse to your directory to load your unpacked file

7. This should load your custom Chrome theme. Continue to tweak as you please.

8. When you are ready, click the same option to pack your file. This will convert it to a `.crx` which is the theme file that is portable.