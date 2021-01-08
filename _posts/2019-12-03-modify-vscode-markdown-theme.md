---
title: 'Modify VScode Markdown Theme'
date: 2019-12-03T09:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/12/modify-vscode-markdown-theme/
category:
  - LocalSoftware
tags:
  - Tweaks
---
<!--more-->

### Description:

Similar to my onetastic post, this will cover how to change the theme for vscode for markdown files. So many themes in VScode cover programming languages well but leave Markdown in a very odd coloring scheme. The following actions will allow you to color your markdown notes whatever colors you want!

![themes](https://automationadmin.com/assets/images/uploads/2019/12/themes.jpg){:class="img-responsive"}

### To Resolve:

1. Open a markdown document in VScode. Type `Ctrl+Shift+p` and select 'Developer: Inspect TM Scopes'. Copy down the different headings like `meta.paragraph.markdown` and `markup.heading.markdown` in a separate document. 

2. Google 'color picker' and start getting ideas for what colors you want certain things to look like. Another idea is to look at your theme you are using in VSCode and try to match their colors.
   - For example:
   - [Dimmed Monokai 1](https://colorsublime.github.io/themes/Dimmed-Monokai/)
   - [Dimmed Monokai 2](https://github.com/gerane/VSCodeThemes/tree/master/gerane.Theme-dimmed-monokai)
   - Look for `Key name = string / Settings = foreground = #9AA83A`

3. Once you have your settings and colors, just modify your `settings.xml` or your `*.code-workspace` file like so:

   ```json
   "editor.tokenColorCustomizations": {
         "comments": "#9E9E9E",
         "textMateRules": [
               {
               "scope": "meta.paragraph.markdown", // regular text
               "settings": {
                  "foreground": "#9E9E9E"
               }
               },
               {
               "scope": [
                  "markup.heading.markdown", // All headings and their text
                  "markup.fenced_code.block.markdown", // code blocks and everything between them
                  "markup.list", //Just the hypens, not the text
                  "markup.underline",
                  "markup.bold",
                  "markup.italic",
                  "meta.separator.markdown",
               ],
               "settings": {
                  "foreground": "#9AA83A"
               }
               }
         ]
      },
      "workbench.colorCustomizations": {
         "editorCursor.foreground": "#9AA83A"
      },
      "workbench.colorTheme": "Monokai Dimmed"
   ```

4. For an up-to-date reference, check out my [Public Gist - VScode Settings.xml](https://gist.github.com/gerryw1389/ad275818cb8ffc3a7efb8795a85e7080)