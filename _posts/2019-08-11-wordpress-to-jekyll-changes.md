---
title: Wordpress To Jekyll Changes
date: 2019-08-11T08:00:44-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/08/wordpress-to-jekyll-changes/
tags:
  - WebSoftware
tags:
  - VersionControl
  - WebServer
---
<!--more-->

### Description:

I did the following steps once I moved my site from Wordpress to Jekyll. Mainly used find and replace in regex/normal mode to remove unwanted stuff from previous blogs.

### To Resolve: 


#### Changes To MD Files: 

1. Remove 'blogger' entries at top of file

   - Find: `^blogger:.*$\n`
   - Replace: blank

   NOTE: This uses the formula `^CONTENT.*$\n` or `^.*CONTENT.*$\n` in the find string to remove not just the text, but the entire line.
   {: .notice--success}

2. Remove 'id' entries at top of file
   - Find: `^id:.*$\n`
   - Replace: blank

3. Remove span elements  
   - Find: `<span style="background-color: white;">`
   - Replace: blank
   - Find: `<span`
   - Replace: blank

4. Replace special character ascii codes with what they are.
   - Find: `&#8216;`
   - Replace: single quote open
   - Find: `&#8217;`
   - Replace: single quote close
   - Find: `&#8220;`
   - Replace: open double quotes
   - Find: `&#8221;`
   - Replace: open double quotes
   - Find: ``&#8211;`
   - Replace: hypen; I'm thinking of making this => but I'm sure it will break everything
   - Find: `&nbsp;`
   - Replace: blank

5. This is by far the most time consuming, but the idea is that with Markdown, you want anything numbered to be on the far left and anything that needs to be added between numbers needs to be indented by at least 2 space characters, I use 3.

   - So what I would have on a post used to look like:

   ```escape
   1. Some task
   2. Some other task
   Some image
   Some Code
   3. Some other task
   ```

   - All of these would be at the same level. When the document rendered with Jekyll, it would re-number anything between numbers so you would see:

   ```escape
   1. Some task
   2. Some other task
   Some image
   Some Code
   1. Some other task
   ```

   - Notice how step 3 turned to 1? What the hell? Well it's because I need to indent like so:

   ```escape
   1. Some task
   2. Some other task
      Some image
      Some Code
   3. Some other task
   ```

   - Then it renders properly!
  
6. Next, I had to go through substeps and make them `-` instead of `1a.`. For example:

   - You would see something like:
   
   ```escape
   1. Some task
   1a. Some subtask
   ```

   - Correct them to look like:
   
   ```escape
   1. Some task
     - Some subtask
   ```

7. Next, convert list of HTML to tables if possible:

   ```escape
   | table | example | one|
   |:---:|:---:|:---:|
   | item | in | table|
   ```

8. Find all the `NOTE:` fields and add `{: .notice--success}` at the end so that they present [cleanly](https://mmistakes.github.io/mm-github-pages-starter/blog/post-notice/)

9. Changed the code fences per [this post](https://automationadmin.com/2020/01/regex-code-fence-search/)

