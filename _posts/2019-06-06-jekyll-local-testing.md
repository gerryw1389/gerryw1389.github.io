---
title: Jekyll Local Testing
date: 2019-06-06T02:36:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/jekyll-local-testing/
categories:
  - Linux
tags:
  - WebServer
---
<!--more-->

### Description:

This post assumes you have [WSL](https://automationadmin.com/2017/09/windows-subsystem-for-linux-wsl/) installed. What we are doing is building our Github Pages site locally, and if you like the changes, then push them to github using a commit in VSCode.

### To Resolve:

1. Open up Windows Bash and type:

   ```shell
   sudo -- sh -c 'apt-get update; apt-get upgrade -y; apt-get dist-upgrade -y; apt-get autoremove -y; apt-get autoclean -y'
   sudo apt-get install ruby-full build-essential zlib1g-dev
   echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
   echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
   echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   gem install jekyll bundler
   cd /mnt/c/_gwill/google/scripts/markdown/gerryw1389.github.io
   bundle install
   # if you get an error `Errno::EPERM: Operation not permitted @ utime_internal`, see below
   bundle exec jekyll serve
   ```

   - Got the following error: 

   ```escape
   ERROR:
   [gerry@OIT-JXQ9RQ2][2020-01-13][/mnt/c/_gwill/google/scripts/markdown/gerryw1389.github.io]
   > bundle exec jekyll serve
   Configuration file: /mnt/c/_gwill/google/scripts/markdown/gerryw1389.github.io/_config.yml
               Source: /mnt/c/_gwill/google/scripts/markdown/gerryw1389.github.io
         Destination: /mnt/c/_gwill/google/scripts/markdown/gerryw1389.github.io/_site
   Incremental build: disabled. Enable with --incremental
         Generating...
   Invalid theme folder: _sass
         Remote Theme: Using theme mmistakes/minimal-mistakes
         Jekyll Feed: Generating feed for posts
      GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.
      GitHub Metadata: Error processing value 'repo_pages_info':
   Liquid Exception: uninitialized constant Faraday::Error::ConnectionFailed Did you mean? Faraday::ConnectionFailed in /_layouts/default.html
   jekyll 3.8.5 | Error:  uninitialized constant Faraday::Error::ConnectionFailed
   Did you mean?  Faraday::ConnectionFailed
   ```

   - For the sub-error `GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data.` I [skipped for now](https://github.com/github/pages-gem/issues/399)


   - For the sub-error `GitHub Metadata: Error processing value 'repo_pages_info':` I skipped for now.

   - For the sub-error

   ```escape
   Liquid Exception: uninitialized constant Faraday::Error::ConnectionFailed Did you mean? Faraday::ConnectionFailed in /_layouts/default.html
   jekyll 3.8.5 | Error:  uninitialized constant Faraday::Error::ConnectionFailed
   Did you mean?  Faraday::ConnectionFailed
   ```

   - The fix was to add the line `gem 'faraday', '~> 0.17.3'` to `gemfile` and then run `bundle update faraday` while in my site's directory.

2. Now browse http://localhost:4000

   - Test by changing `minimal_mistakes_skin: air # "air", "aqua", "contrast", "dark", "dirt", "neon", "mint", "plum", "sunrise"` to `neon` and then running `bundle exec jekyll serve` and navigating to `http://localhost:4000` - works as intended!

3. Update => 2020-01-24: So the above commands worked on my work computer, but my home computer failed after `bundle update` with the error:

   ```escape
   There was an error accessing `/home/gerry/.bundle/cache/compact_index/rubygems.org.443.29b0360b937aa4d161703e6160654e47/versions`.
   The underlying system error is Errno::EPERM: Operation not permitted @ utime_internal -
   /home/gerry/.bundle/cache/compact_index/rubygems.org.443.29b0360b937aa4d161703e6160654e47/versions
   ```

   - So I tried `sudo chmod -R 766 /home/gerry/.bundle/` and `sudo chmod -R 766 /tmp` and it still failed
   - So then I ran `sudo rm -rf /home/gerry/.bundle/cache/` and tried again. It then said my ruby version was too low - it wants `2.4`
   - I then ran:

   ```shell
   sudo apt-get install ruby-full
   Reading package lists... Done
   Building dependency tree
   Reading state information... Done
   ruby-full is already the newest version (1:2.3.0+1).
   0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
   gerry@gw-vmh:/mnt/c/_gwill/google/scripts/markdown/gerryw1389.github.io$ ruby --version
   ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu]
   ```

   - So even after running updates, it didn't matter because my version was too low. So I then follow [this](https://vitux.com/how-to-install-latest-ruby-on-rails-on-ubuntu/) post:

   ```shell
   gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
   curl -sSL https://get.rvm.io | bash -s stable --ruby
   source ~/.rvm/scripts/rvm
   echo "source ~/.rvm/scripts/rvm" >> ~/.bashrc
   source ~/.bashrc
   rvm --version
   rvm get stable --autolibs=enable
   rvm list known
   rvm install ruby-2.6
   rvm --default use ruby-2.6
   bundle install
   ```

   - Gave this info:

   ```escape
   /home/gerry/.rvm/rubies/ruby-2.6.3/lib/ruby/2.6.0/rubygems.rb:283:in `find_spec_for_exe': Could not find 'bundler' (2.1.4) required by your /mnt/z/google/scripts/markdown/gerryw1389.github.io/Gemfile.lock. (Gem::GemNotFoundException)
   To update to the latest version installed on your system, run `bundle update --bundler`.
   To install the missing version, run `gem install bundler:2.1.4`
   ```

   - So I did what it said and it worked!

   ```shell
   gem install bundler:2.1.4
   bundle update --bundler
   bundle install
   bundle exec jekyll serve
   ```

