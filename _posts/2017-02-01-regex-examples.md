---
title: Regex Examples
date: 2017-02-01T08:33:11+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/02/regex-examples/
tags:
  - LocalSoftware
tags:
  - Regex
---
<!--more-->

### Description:

This post is a companion post for [Notepad++](https://automationadmin.com/2017/02/notepadplusplus-settings/) but extracted out becuase you can use regex in most scripting languages. 

### To Resolve:

1. Examples:

#### To insert text at the beginning of each line:  
1. Press Ctrl+A to select all text  
2. Press Ctrl+H to bring up find/replace  
3. Select the third radio button on the bottom left (search mode) for `regular expression`  
4. In the `find what` type: `^`  
5. In the `replace with` type: `(whatever text you want at the beginning of each line)`

#### To insert text at the end of each line:  
1. Press Ctrl+A to select all text  
2. Press Ctrl+H to bring up find/replace  
3. Select the third radio button on the bottom left (search mode) for `regular expression`  
4. In the `find what` type: `$`  
5. In the `replace with` type: `(whatever text you want at the end of each line)`

#### To Clear the text after a certain character on each line (for example a double quotation mark):  
1. Search for the regular expression: `".*`  
2. Replace with `(blank)`
3. Another example: to remove everything after `/` on each line the search would be: `/.*`*

#### Remove duplicates:
Find: `^(.\*?)$\s+?^(?=.\*^\1$)`  
Replace with: `(blank)`  
Check the box `. matches new line`

#### Remove Empty lines:
Find: `\r\n\W*\r\n`  
Replace with: `\r\n`

#### Remove just numbers (good for copying code):
Find: `[0-9]`  
Replace: `(blank)`

#### Clear everything after a character, in this case, the double quotation mark
Find: `".*`  
Replace: `(blank)`

#### Clear entire line a phrase is found in.
Find: `^CONTENT.*$\n`  
Replace: `(blank)`

or:

Find: `^.*CONTENT.*$\n`  
Replace: `(blank)`

#### To remove trailing spaces:
Find: `[ \t]+$`  
Replace: `(blank)`

#### To remove leading line spaces:
Find: `^[ \t]+`  
Replace: `(blank)`

#### To remove leading and trailing line spaces:
Find: `^[ \t]+|[ \t]+$`  
Replace: `(blank)`

#### Remove spaces in middle of a string:
Find: `\s+(?=\s)`  
Replace: `(blank)`

#### Remove trailing spaces:
Find: `([^ \t])[ \t]+$`  
Replace: `\1`

#### To Capitalize Every Word:
Find: `w+`  
Replace: `u$0`

#### To remove double lines:
Find: `^\n\n`  
Replace: `(blank)`

#### To Search A Phrase And Replace with (Phrase + Text):
Find: `^mail: ([a-z0-9]{6,})$` 
   - example, will match `mail: {any 6 characters}` like `mail: abcdef` or `mail: 12ctl9`

Replace: `mail: \1@subdomain.domain.com` 
   - will replace `mail: abcdef` with `mail: abcdef@subdomain.domain.com` for example

#### To fix levels in Markdown:
Find all lists that start with 8 spaces and make them 7

Find: `^-` With 8 spaces before for the `-`  
Replace: `-` With 7 spaces before for the `-`  

   - Do this so that all first level lists is 3 spaces, 5 spaces for level 2 lists, and 7 spaces for level 3 lists.

#### To add a Sentences In Middle Of Text Blocks

Find: `DirXML`
Replace: `changeType: modify\nreplace: extensionAttribute10\nDirXML`

   - For the following example:

   - Before:

   ```escape
   dn: cn=mxt8167,ou=Student,o=company
   DirXML-ADContext: CN=mxt8167,OU=Student,DC=company,DC=com
   extensionAttribute10: Fall_2011
   ```

   - After:

   ```escape
   dn: cn=mxt8167,ou=Student,o=company
   changetype: modify
   replace: extensionAttribute10
   DirXML-ADContext: CN=mxt8167,OU=Student,DC=company,DC=com
   extensionAttribute10: Fall_2011
   ```

#### To find all instances of something not followed by something else:

   - See [answer](https://stackoverflow.com/questions/31201690/find-word-not-followed-by-a-certain-character)

Find: `Github(?!.com)`
   - Example: The previous line finds all instances of `Github` not followed by `.com` so no `github.com` should return.

Find: `Github(?!.com|.io)`
   - Example: The previous line finds all instances of `Github` not followed by `.com` or `.io` so no `github.com` or `github.io` should return.

