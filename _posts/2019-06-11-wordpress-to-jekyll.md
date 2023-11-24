---
title: Wordpress To Jekyll
date: 2019-06-11T23:51:43-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/06/wordpress-to-jekyll/
tags:
  - Linux
  - WebSoftware
tags:
  - PersonalConfig
  - WebServer
---
<!--more-->

### Description:

To migrate my blog from a self hosted website to Github Pages using Jeykll, I did the following steps following this [Quick-Start Guide - Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)

This guide used the following infrastructure:
- My host computer is a Windows 10 physical machine
- I have WSL installed and I access Github on my windows machine by changing directories to `cd /mnt/c/_gwill/google/scripts/powershell/site/gerryw1389.github.io`
- My Wordpress instance is a Centos 7 machine running in Virtual Box on my host computer

### To Resolve:

1. Fork [Minimal Mistakes Starter](https://github.com/mmistakes/mm-github-pages-starter)

2. Rename to `gerryw1389.github.io` on github

3. Sync to my computer in the directory `C:\_gwill\google\scripts\powershell\site\gerryw1389.github.io` which I access from WSL as `/mnt/c/_gwill/google/scripts/powershell/site/gerryw1389.github.io`

4. In WSL, run the following:

   ```shell
   cd /mnt/c/_gwill/google/scripts/powershell/site/gerryw1389.github.io
   sudo apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev nodejs
   gem install bundler jekyll
   ```

   - Got error similar to:

   ```escape
   Building native extensions.  This could take a while...
   ERROR:  Error installing mysql:
       ERROR: Failed to build gem native extension.

   /usr/bin/ruby extconf.rb
   mkmf.rb can't find header files for ruby at /usr/lib/ruby/ruby.h

   Gem files will remain installed in /usr/lib/ruby/gems/1.8/gems/mysql-2.8.1 for inspection.
   Results logged to /usr/lib/ruby/gems/1.8/gems/mysql-2.8.1/ext/mysql_api/gem_make.out
   ```

   - fix:

   ```shell
   sudo apt-get install ruby-all-dev
   ```

   - Then I ran:

   ```shell
   bundle exec jekyll serve
   ```

   - Got error:

   ```escape
   Could not find gem 'github-pages' in any of the gem sources listed in your Gemfile.
   Run `bundle install` to install missing gems.
   ```

5. Instead, I just ran `bundle` instead of `bundle install`

   - Then run `bundle exec jekyll serve` to browse the site locally. 
   - Then browse to http://localhost:4000 - Site is working now!

6. Now I just export my wordpress site and copy my jekyll export to `_posts` directory. To do this I did:

   - In your Wordpress Admin web GUI, install [Jekyll Exporter](https://wordpress.org/plugins/jekyll-exporter/)

   - If it works, do an export from there. It wouldn't work for me - just got a white page. So I did the following steps manually:
   - On the server, install wp-cli - https://wp-cli.org/

   ```shell
   curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
   php wp-cli.phar --info
   chmod +x wp-cli.phar
   sudo mv wp-cli.phar /usr/local/bin/wp
   ```

   - The plugin should already be in your wordpress directory, but if not - go ahead and download it from the link above.

   ```shell
   cd /var/www/html/wp-content/plugins/jekyll-exporter
   php jekyll-export-cli.php > jekyll-export.zip
   # or
   # /usr/local/bin/wp jekyll-export > /root/export.zip
   ```

   - If you get:

   ```escape
   [root] jekyll-exporter# php jekyll-export-cli.php > jekyll-export.zip
   PHP Fatal error:  Uncaught Error: Class 'ZipArchive' not found in /var/www/html/wp-content/plugins/jekyll-exporter/jekyll-exporter.php:430
   Stack trace:
   #0 /var/www/html/wp-content/plugins/jekyll-exporter/jekyll-exporter.php(457): Jekyll_Export->zip_folder('/tmp/wp-jekyll-...', '/tmp/wp-jekyll....')
   #1 /var/www/html/wp-content/plugins/jekyll-exporter/jekyll-exporter.php(340): Jekyll_Export->zip()
   #2 /var/www/html/wp-content/plugins/jekyll-exporter/jekyll-export-cli.php(28): Jekyll_Export->export()
   #3 {main}
     thrown in /var/www/html/wp-content/plugins/jekyll-exporter/jekyll-exporter.php on line 430
   ```

   - Fix:

   ```shell
   yum install php-pecl-zip # https://www.linuxquestions.org/questions/linux-server-73/install-zip-extension-for-php-on-centos-922408/
   ```

7. Copy the zip file to your Windows Computer in the git location that WSL can access

   - Then `git add --all` and `push` your files to your repo.

8. After the site is working, the next step is to ensure that images get replaced

   - To a find/replace:
   - ![sccm](https://automationadmin.com/assets/images/uploads/2019/04/sccm.jpg){:class="img-responsive"}
   - In vscode, do a recursive replace `https://www.gerrywilliams.net/wp-content` to `https://gerryw1389.github.io/assets/images`

9. Then update DNS => A records and subdomain forward 

   - Sign into Google Domains
   - Delete current A record
   - Create a new 'A' Record with the values of `185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153`

   - For subdomain forward:
   - `www.gerrywilliams.net => http://gerrywilliams.net` with options `Temporary redirect (302), Forward path, Enable SSL`

   - Update it under Github.com - Repo - Settings - Custom Address - Paste it in


10. Now do a find/replace again for `https://gerryw1389.github.io/assets/images` to `https://automationadmin.com/assets/images`

11. Install link checker

   ```shell
   cd /mnt/z/google/scripts/powershell/site/gerryw1389.github.io
   # Add to gemfile:
   # gem 'rake'
   # gem 'html-proofer'
   bundle install
   ```

   - And now that it's installed, build your site and have htmlproofer check for the broken links:

   ```shell
   bundle exec jekyll build
   bundle exec htmlproofer ./_site
   ```

12. Lastly, see my [Changes](https://automationadmin.com/2019/08/wordpress-to-jekyll-changes/) for the different tweaks done.