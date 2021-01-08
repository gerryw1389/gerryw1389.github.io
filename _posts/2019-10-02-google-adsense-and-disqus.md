---
title: Google Adsense and Disqus
date: 2019-10-02T12:32:15-06:00
author: gerryw1389
layout: single
classes: wide
permalink: 2019/10/google-adsense-and-disqus
categories:
  - WebSoftware
---
<!--more-->

### Description:

This post describes how I added Google Adsense and Disqus to the Github Pages hosted website. Not sure if this is 100% legal yet, but [I think so](https://webapps.stackexchange.com/questions/56898/am-i-allowed-to-host-a-commerical-website-on-github-pages)

### To Resolve:

1. Google Adsense

   - In order to add Google Adsense from my blog I need to create a custom script to insert between `<head>` elements

   - Since I'm currently using the remote theme [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes), this means adding the following file in my local instance:

   ```shell
   cd /mnt/c/_gwill/google/scripts/powershell/site/gerryw1389.github.io
   mkdir ./includes/
   mkdir ./includes/head
   touch ./includes/head/custom.html
   ```

   - Copy and paste the following, then save and exit:

   ```javascript
   <!-- start custom head snippets -->

   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
   <script>
   (adsbygoogle = window.adsbygoogle || []).push({
      google_ad_client: "ca-pub-551489asdfasdf9109",
      enable_page_level_ads: true
   });
   </script>

   <!-- insert favicons. use https://realfavicongenerator.net/ -->

   <!-- end custom head snippets -->
   ```

   - Then do a `git commit` and `git push` to Github as usual and wait for the build to complete.

   - Now go back to Google Adsense and look and see what it says:

    ![adsense](https://automationadmin.com/assets/images/uploads/2019/06/adsense.png){:class="img-responsive"}


2. Adding disqus as your commenting system is fairly straightforward, sign up for disqus, register your website, get your shortname in admin panel => site settings.

   - Then in your `_config.yml`

   ```yaml
   site settings:
   comments:
   provider: "disqus"
   disqus:
      shortname: "gerrywilliams-net"

   # Down below, in post settings, add
   comments: true
   ```

