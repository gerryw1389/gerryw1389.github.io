---
title: Update To Building Jekyll Locally
date: 2023-11-24T05:24:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2023/11/update-build-local
tags:
  - WSL
  - Jekyll
---
<!--more-->


### Description

It's been a while since I have updated my website, so I went through these steps as of 2023-11 to build/test locally:

### Steps

1. First, new computer so I had to install `wsl`:

   ```shell
   wsl --install -d Ubuntu-22.04
   sudo -- sh -c 'apt-get update; apt-get upgrade -y; apt-get dist-upgrade -y; apt-get autoremove -y; apt-get autoclean -y'
   sudo apt-get install ruby-full build-essential zlib1g-dev
   echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
   echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
   echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   gem install jekyll bundler
   bundle install
   bundle exec jekyll serve
   ```

1. This produced:

   ```escape
   Configuration file: /mnt/c/_gwill/repo-home/h1website/_config.yml
               Source: /mnt/c/_gwill/repo-home/h1website
         Destination: /mnt/c/_gwill/repo-home/h1website/_site
   Incremental build: disabled. Enable with --incremental
         Generating...
         Remote Theme: Using theme mmistakes/minimal-mistakes
         Jekyll Feed: Generating feed for posts
      GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
                     done in 104.025 seconds.
   Auto-regeneration: disabled. Use --watch to enable.
   /home/gerry/gems/gems/jekyll-3.9.3/lib/jekyll/commands/serve/servlet.rb:3:in `require': cannot load such file -- webrick (LoadError)
         from /home/gerry/gems/gems/jekyll-3.9.3/lib/jekyll/commands/serve/servlet.rb:3:in `<top (required)>'
         from /home/gerry/gems/gems/jekyll-3.9.3/lib/jekyll/commands/serve.rb:184:in `require_relative'
         from /home/gerry/gems/gems/jekyll-3.9.3/lib/jekyll/commands/serve.rb:184:in `setup'
         from /home/gerry/gems/gems/jekyll-3.9.3/lib/jekyll/commands/serve.rb:102:in `process'
         from /home/gerry/gems/gems/jekyll-3.9.3/lib/jekyll/commands/serve.rb:93:in `block in start'
         from /home/gerry/gems/gems/jekyll-3.9.3/lib/jekyll/commands/serve.rb:93:in `each'
         from /home/gerry/gems/gems/jekyll-3.9.3/lib/jekyll/commands/serve.rb:93:in `start'
         from /home/gerry/gems/gems/jekyll-3.9.3/lib/jekyll/commands/serve.rb:75:in `block (2 levels) in init_with_program'
         from /home/gerry/gems/gems/mercenary-0.3.6/lib/mercenary/command.rb:220:in `block in execute'
         from /home/gerry/gems/gems/mercenary-0.3.6/lib/mercenary/command.rb:220:in `each'
         from /home/gerry/gems/gems/mercenary-0.3.6/lib/mercenary/command.rb:220:in `execute'
         from /home/gerry/gems/gems/mercenary-0.3.6/lib/mercenary/program.rb:42:in `go'
         from /home/gerry/gems/gems/mercenary-0.3.6/lib/mercenary.rb:19:in `program'
         from /home/gerry/gems/gems/jekyll-3.9.3/exe/jekyll:15:in `<top (required)>'
         from /home/gerry/gems/bin/jekyll:25:in `load'
         from /home/gerry/gems/bin/jekyll:25:in `<main>'
   ```

1. So then I googled and found this [Stack Overflow](https://stackoverflow.com/questions/69890412/bundler-failed-to-load-command-jekyll) post with the answer:

   ```shell
   gerry@gw-host:/mnt/c/_gwill/repo-home/h1website$ bundle add webrick
   Fetching gem metadata from https://rubygems.org/.........
   Resolving dependencies...
   Fetching gem metadata from https://rubygems.org/.........
   Resolving dependencies...
   Fetching webrick 1.8.1
   Installing webrick 1.8.1
   gerry@gw-host:/mnt/c/_gwill/repo-home/h1website$ bundle exec jekyll serve
   Configuration file: /mnt/c/_gwill/repo-home/h1website/_config.yml
               Source: /mnt/c/_gwill/repo-home/h1website
         Destination: /mnt/c/_gwill/repo-home/h1website/_site
   Incremental build: disabled. Enable with --incremental
         Generating...
         Remote Theme: Using theme mmistakes/minimal-mistakes
         Jekyll Feed: Generating feed for posts
      GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
                     done in 98.374 seconds.
                     Auto-regeneration may not work on some Windows versions.
                     Please see: https://github.com/Microsoft/BashOnWindows/issues/216
                     If it does not work, please upgrade Bash on Windows or run Jekyll with --no-watch.
   Auto-regeneration: enabled for '/mnt/c/_gwill/repo-home/h1website'
      Server address: http://127.0.0.1:4000
   Server running... press ctrl-c to stop.
   ^Cgerry@gw-host:/mnt/c/_gwill/repo-home/h1website$ 
   ```

1. That's it! Surprisingly not to much to test locally.