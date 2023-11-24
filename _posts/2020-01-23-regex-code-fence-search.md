---
title: 'Regex Code Fence Search'
date: 2020-01-23T10:38:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/01/regex-code-fence-search/
tags:
  - LocalSoftware
tags:
  - Regex
  - WebServer
---
<!--more-->

### Description:

This post covers how I resolved an issue with my Jekyll setup with Github Pages where I need to use regex to: `I want to match "```\n" but not "```\n\n"` ignore the sets of double quotes. This may need to be added to [this post](https://automationadmin.com/2019/08/wordpress-to-jekyll-changes/) but I will keep it here for now.

### To Resolve

1. In vscode, do a recursive search for ` ```\n(?!\n) ` per [Stack Overflow response](https://stackoverflow.com/questions/31201690/find-word-not-followed-by-a-certain-character)

2. Next, I wanted to fill in all code fences on my site with some kind of language. Since my theme uses the Rouge lexer, I followed [this guide](https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers) and put the following:

   - `escape` - This is the default code block that doesn't highlight anything (as far as I know)
   - `powershell` - Powershell
   - `shell` - Anything with bash or linux
   - ... and others as appropriate


