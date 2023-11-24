---
title: Nano and Vim Shortcuts
date: 2016-12-24T08:24:55+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/nano-and-vim-shortcuts/
tags:
  - Linux
---
<!--more-->

### Description:

There is probably a thousand of these on the intertubes, but here's mine.

### To Resolve:

1. Nano shortcuts

   - `ctrl+g` = help  
   - `ctrl+o` = save file  
   - `ctrl+x` = exit file
 
   - `alt+\` = move to beginning  
   - `alt+/` = move to end  
   - `ctrl+y` = up a page  
   - `ctrl+v` = down a page  
   - `ctrl+a` = beginning of line  
   - `ctrl+e` = end of line  
   - `ctrl+_` = enter a line number, a comma, and a column number
 
   - `ctrl+w` = search for a string, ctrl+c cancels it  
   - `alt+m+a` = select area to copy  
   - `alt+6` = copy => highlight with cursor first  
   - `ctrl+k` = cut => cuts an entire line if you don't highlight anything  
   - `ctrl+m` = inserts a blank line  
   - `ctrl+u` = paste  
   - `alt+r` = replace expr1 with expr2. y for one occurance and a for all
 
   - `alt+x` = remove the help menu at the bottom
 
2. Vim shortcuts

   - Basic Nav:
   - `gg` = Moves to beginning of filename
   - `G` = Moves to the end of file
   - `cntrl+b` = Page up. Think of it as 'b'ack.
   - `cntrl+f` = Page up. Think of it as 'f'orward.
   - Insert text:
   - `a`	= Insert text after the cursor
   - `A`	= Insert text at the end of the line
   - `i`	= Insert text before the cursor
   - `o`	= Begin a new line below the cursor
   - `O`	= Begin a new line above the cursor
   - Delete Text:
   - `dd` = Delete current line
   - `dgg` = Delete to the beginning of the file.
   - `dG` = Delete to end of file
   - Copy/Paste:
   - `yy` = copy current line
   - `p`	= paste storage buffer after current line
   - `P`	= paste storage buffer before current line
   - Searching:
   - `vim filename`
   - press `/`
   - type `word` which you want to search
   - press `Enter`
   - `/pattern` = search forward for pattern
   - `?pattern` = search backward
   - `n` = repeat forward search
   - `N` = repeat backward
   - `/\<word\>` = Full word  
   - Search and replace:
   - `:%s/original/replacement` = Search for the first occurrence of the string "original" and replace it with "replacement"
   - `:%s/original/replacement/g` = Search and replace all occurrences of the string "original" with "replacement"

3. Less shortcuts (added because it's similar)

   - `b` = Moves back one page. Insert a number before to move that many pages back.
   - `f` = Moves forward one page. Insert a number before to move that many pages forward.
   - `/query` = Search something
   - `q` = Quit

