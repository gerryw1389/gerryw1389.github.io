---
title: 'Unable To Update Theme'
date: 2023-01-05T07:10:21-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/01/unable-to-update-theme
tags:
  - Linux
tags:
  - WebServer
---
<!--more-->

### Description:

So I practice the use of [version pinning](https://automationadmin.com/2022/08/git-tagging) which is pretty common in my line of work and one of the things you need to do periodically is update your git tags to the next to latest version of your upstream source. Well the issue I've been having lately that I haven't looked in to yet is my [upstream theme source](https://github.com/mmistakes/minimal-mistakes/tree/master) for this blog.

When I update to any version past `4.15.5` which is [what I'm currently pinned to](https://github.com/gerryw1389/gerryw1389.github.io/blob/main/_config.yml#L4) I get the following text at the top of my home page:

`"", "avatar"=>"/assets/images/gerryw.png", "bio"=>"", "links"=>[{"label"=>"GitHub", "icon"=>"fab fa-fw fa-github", "url"=>"https://github.com/gerryw1389"}, {"label"=>"Reddit", "icon"=>"fab fa-reddit-alien", "url"=>"https://www.reddit.com/user/gerryw1389/"}, {"label"=>"Popular Posts", "icon"=>"fas fa-fw fa-link", "url"=>"https://automationadmin.com/2016/02/popular-posts"}, {"label"=>"Bookmarks", "icon"=>"fas fa-bookmark", "url"=>"https://automationadmin.com/2016/02/bookmarks"}]}">`

All other pages like 'About', 'Categories', and even individual posts don't have this issue.

### To Resolve:

1. One of the first steps to troubleshooting blog issues is to see what happens when you try locally, so I ran these commands:

   ```shell
   cd blog/dir
   gem update
   #delete Gemfile.lock
   bundle install
   bundle update --bundler
   bundle exec jekyll serve
   ```

1. I don't remember if it was here or not but I got this output at some point:

   ```escape
   ekyll Feed: Generating feed for posts
   ^C  Liquid Exception: Could not locate the included file 'author-profile.html' in any of ["/mnt/c/_gwill/repo-home/h1website/_includes", "/tmp/jekyll-remote-theme-20230217-4507-1202n68/_includes"]. Ensure it exists in one of those directories and is not a symlink as those are not 
   allowed in safe mode. in /_layouts/single.html
               Error: Could not locate the included file 'author-profile.html' in any of ["/mnt/c/_gwill/repo-home/h1website/_includes", "/tmp/jekyll-remote-theme-20230217-4507-1202n68/_includes"]. Ensure it exists in one of those directories and is not a symlink as those are not allowed in safe mode.
               Error: Run jekyll build --trace for more information.
   ```

1. All I know is I searched the upstream repo for:

   - The [next release up](https://github.com/mmistakes/minimal-mistakes/commits/4.16.6)
	- So the problem is between commit `5ab086cb4c8cbcfaaa74fe42295d93ed579ea448` which was the `v4.16.6` and commit `6311da0b1623a19fa81d92f428f017bb0c1a386b` which was the `v4.16.5` release.
	- Looking at the [change log](https://mmistakes.github.io/minimal-mistakes/docs/history/#4166), he mentions:
	- *"Fix site.url in Organization/Person JSON-LD schema."* - but when I look at that issue, I'm unable to discern how that relates to my blog.
   - But I'm not sure which of these changed what. Need to look into this at some point. I'm fine pinned to this version for now though.
	- It very well may be one of the other issues that was fixed. All I know is upgrading to any version past this one causes the issue even if I go to the latest release today which is [`v4.24.0`](https://github.com/mmistakes/minimal-mistakes/commits/4.24.0)
