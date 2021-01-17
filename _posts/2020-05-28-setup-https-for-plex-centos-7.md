---
title: Setup HTTPS For Plex Centos 7 
date: 2020-05-28T07:27:48-05:00
author: gerryw1389
layout: single
classes: wide
permalink: /2020/05/setup-https-for-plex-centos-7
categories:
  - LocalSoftware
  - Linux
tags:
  - LinuxServer
  - WebServer
---
<!--more-->

### Description:

In this post, I created a Reverse Proxy Server using Nginx for Plex Media Server.

### To Resolve:

1. First, in DNS manager for your domain, create two `A` records called `@` and `plex` that point to your public IP address of the plex server.
2. Allow HTTPS/HTTP at local firewall level and at host level

   ```shell
   sudo firewall-cmd --permanent --zone=public --add-service=http 
   sudo firewall-cmd --permanent --zone=public --add-service=https
   sudo firewall-cmd --reload
   ```

3. Install packages

   ```shell
   yum install nginx python-certbot-nginx certbot
   systemctl start nginx
   systemctl enable nginx
   ```

4. Configure default HTTPS with certbot:

   ```shell
   vi /etc/nginx/conf.d/domain.com
   server {
      server_name domain.com plex.domain.com
   }
   certbot --nginx -d domain.com -d plex.domain.com
   # should say congratulations
   ```

5. Configure nginx for plex

   - create `plex.conf` inside `/etc/nginx/conf.d` :

   ```shell
   [root] conf.d# cat plex.conf
   upstream plex_backend {
      server localhost:32400;
      keepalive 32;
   }

   map $http_upgrade $connection_upgrade {
      default upgrade;
      ''      close;
   }

   server {
      listen 80;
      server_name plex.domain.com;
      return 301 plex.domain.com$request_uri;
   }
   server {
         listen 443 ssl http2; #http2 can provide a substantial improvement for streaming: https://blog.cloudflare.com/introducing-http2/
         server_name plex.domain.com;

         send_timeout 100m; #Some players don't reopen a socket and playback stops totally instead of resuming after an extended pause (e.g. Chrome)

         #Faster resolving, improves stapling time. Timeout and nameservers may need to be adjusted for your location Google's have been used here.
         resolver 8.8.4.4 8.8.8.8 valid=300s;
         resolver_timeout 10s;

         #Use letsencrypt.org to get a free and trusted ssl certificate
         ssl_certificate      /etc/letsencrypt/live/domain.com/fullchain.pem;
         ssl_certificate_key  /etc/letsencrypt/live/domain.com/privkey.pem;

         ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
         ssl_prefer_server_ciphers on;
         #Intentionally not hardened for security for player support and encryption video streams has a lot of overhead with something like AES-256-GCM-SHA384.
         ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:ECDHE-RSA-DES-CBC3-SHA:ECDHE-ECDSA-DES-CBC3-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA';

         #Why this is important: https://blog.cloudflare.com/ocsp-stapling-how-cloudflare-just-made-ssl-30/
         ssl_stapling on;
         ssl_stapling_verify on;
         #For letsencrypt.org you can get your chain like this: https://esham.io/2016/01/ocsp-stapling
         ssl_trusted_certificate /etc/letsencrypt/live/domain.com/chain.pem;

         #Reuse ssl sessions, avoids unnecessary handshakes
         #Turning this on will increase performance, but at the cost of security. Read below before making a choice.
         #https://github.com/mozilla/server-side-tls/issues/135
         #https://wiki.mozilla.org/Security/Server_Side_TLS#TLS_tickets_.28RFC_5077.29
         #ssl_session_tickets on;
         #ssl_session_tickets off;

         #Use: openssl dhparam -out dhparam.pem 2048 - 4096 is better but for overhead reasons 2048 is enough for Plex.
         ssl_dhparam /etc/nginx/dhparam.pem;
         #ssl_ecdh_curve secp384r1;

         #Will ensure https is always used by supported browsers which prevents any server-side http > https redirects, as the browser will internally correct any request to https.
         #Recommended to submit to your domain to https://hstspreload.org as well.
         #!WARNING! Only enable this if you intend to only serve Plex over https, until this rule expires in your browser it WONT BE POSSIBLE to access Plex via http, remove 'includeSubDomains;' if you only want it to effect your Plex (sub-)domain.
         #This is disabled by default as it could cause issues with some playback devices it's advisable to test it with a small max-age and only enable if you don't encounter issues. (Haven't encountered any yet)
         #add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

         #Plex has A LOT of javascript, xml and html. This helps a lot, but if it causes playback issues with devices turn it off. (Haven't encountered any yet)
         gzip on;
         gzip_vary on;
         gzip_min_length 1000;
         gzip_proxied any;
         gzip_types text/plain text/css text/xml application/xml text/javascript application/x-javascript image/svg+xml;
         gzip_disable "MSIE [1-6]\.";

         #Nginx default client_max_body_size is 1MB, which breaks Camera Upload feature from the phones.
         #Increasing the limit fixes the issue. Anyhow, if 4K videos are expected to be uploaded, the size might need to be increased even more
         client_max_body_size 100M;

         #Forward real ip and host to Plex
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;
         # Plex headers
         proxy_set_header X-Plex-Client-Identifier $http_x_plex_client_identifier;
         proxy_set_header X-Plex-Device $http_x_plex_device;
         proxy_set_header X-Plex-Device-Name $http_x_plex_device_name;
         proxy_set_header X-Plex-Platform $http_x_plex_platform;
         proxy_set_header X-Plex-Platform-Version $http_x_plex_platform_version;
         proxy_set_header X-Plex-Product $http_x_plex_product;
         proxy_set_header X-Plex-Token $http_x_plex_token;
         proxy_set_header X-Plex-Version $http_x_plex_version;
         proxy_set_header X-Plex-Nocache $http_x_plex_nocache;
         proxy_set_header X-Plex-Provides $http_x_plex_provides;
         proxy_set_header X-Plex-Device-Vendor $http_x_plex_device_vendor;
         proxy_set_header X-Plex-Model $http_x_plex_model;

               proxy_set_header        Host                      $server_addr;
               proxy_set_header        Referer                   $server_addr;
               proxy_set_header        Origin                    $server_addr;

         #Websockets
         proxy_http_version 1.1;
         proxy_set_header Upgrade $http_upgrade;
         proxy_set_header Connection "upgrade";

         #Disables compression between Plex and Nginx, required if using sub_filter below.
         #May also improve loading time by a very marginal amount, as nginx will compress anyway.
         #proxy_set_header Accept-Encoding "";

         #Buffering off send to the client as soon as the data is received from Plex.
         proxy_redirect off;
         proxy_buffering off;

         location / {
                  #Example of using sub_filter to alter what Plex displays, this disables Plex News.
                  #sub_filter ',news,' ',';
                  #sub_filter_once on;
                  #sub_filter_types text/xml;
                  proxy_pass http://plex_backend;
         }
   }
   ```

   - Edit your `nginx.conf` to match this:

   ```shell
   [root] nginx# cat nginx.conf
   # For more information on configuration, see:
   #   * Official English Documentation: http://nginx.org/en/docs/
   #   * Official Russian Documentation: http://nginx.org/ru/docs/

   user nginx;
   worker_processes auto;
   error_log /var/log/nginx/error.log;
   pid /run/nginx.pid;

   # Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
   include /usr/share/nginx/modules/*.conf;

   events {
      worker_connections 1024;
   }

   http {
      log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for"';

      access_log  /var/log/nginx/access.log  main;

      sendfile            on;
      tcp_nopush          on;
      tcp_nodelay         on;
      keepalive_timeout   65;
      types_hash_max_size 2048;

      include             /etc/nginx/mime.types;
      default_type        application/octet-stream;

      # Load modular configuration files from the /etc/nginx/conf.d directory.
      # See http://nginx.org/en/docs/ngx_core_module.html#include
      # for more information.
      include /etc/nginx/conf.d/*.conf;

      server {
         listen       80 default_server;
         listen       [::]:80 default_server;
         server_name  _;
         root         /usr/share/nginx/html;

         # Load configuration files for the default server block.
         include /etc/nginx/default.d/*.conf;

         location / {
         }

         error_page 404 /404.html;
               location = /40x.html {
         }

         error_page 500 502 503 504 /50x.html;
               location = /50x.html {
         }
      }

   # Settings for a TLS enabled server.
   #
   #    server {
   #        listen       443 ssl http2 default_server;
   #        listen       [::]:443 ssl http2 default_server;
   #        server_name  _;
   #        root         /usr/share/nginx/html;
   #
   #        ssl_certificate "/etc/pki/nginx/server.crt";
   #        ssl_certificate_key "/etc/pki/nginx/private/server.key";
   #        ssl_session_cache shared:SSL:1m;
   #        ssl_session_timeout  10m;
   #        ssl_ciphers HIGH:!aNULL:!MD5;
   #        ssl_prefer_server_ciphers on;
   #
   #        # Load configuration files for the default server block.
   #        include /etc/nginx/default.d/*.conf;
   #
   #        location / {
   #        }
   #
   #        error_page 404 /404.html;
   #            location = /40x.html {
   #        }
   #
   #        error_page 500 502 503 504 /50x.html;
   #            location = /50x.html {
   #        }
   #    }



      server {
      server_name plex.domain.com domain.com; # managed by Certbot
         root         /usr/share/nginx/html;

         # Load configuration files for the default server block.
         include /etc/nginx/default.d/*.conf;

         location / {
         }

         error_page 404 /404.html;
               location = /40x.html {
         }

         error_page 500 502 503 504 /50x.html;
               location = /50x.html {
         }


      listen [::]:443 ssl ipv6only=on; # managed by Certbot
      listen 443 ssl; # managed by Certbot
      ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem; # managed by Certbot
      ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem; # managed by Certbot
      include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
      ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot



   }

      server {
      if ($host = plex.domain.com) {
         return 301 https://$host$request_uri;
      } # managed by Certbot


      if ($host = domain.com) {
         return 301 https://$host$request_uri;
      } # managed by Certbot


         listen       80 ;
         listen       [::]:80 ;

      return 404; # managed by Certbot

   }}
   ```

6. Test your config and restart the service:

   ```shell
   nginx -t
   #output should read okay
   systemctl restart nginx
   ```

7. Create the PCKS #12 file:

   ```shell
   openssl pkcs12 -export -out /root/certificate.pfx \
   -inkey /etc/letsencrypt/live/domain.com/privkey.pem \
   -in /etc/letsencrypt/live/domain.com/cert.pem \
   -certfile /etc/letsencrypt/live/domain.com/chain.pem
      
   # Next you'll be asked to enter a password to encrypt the .pfx file. Enter a password you won't mind saving in the Plex settings in plaintext.
   # Hand it over to plex.
   mv /root/certificate.pfx /var/lib/plexmediaserver
   chown plex:plex /var/lib/plexmediaserver/certificate.pfx
   ```

8. In the Plex Web UI, go to Settings:
   - Custom certificate location: `/var/lib/plexmediaserver/certificate.pfx`
   - Custom certificate encryption key: The password you entered on step 2 of last section
   - Custom certificate domain: <https://plex.domain.com>
   - Save your changes.
   - That's it. You don't even have to restart plex!
   - You can check the Plex\ Media\ Server.log file in `/var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Logs` if you want to verify whether there were any errors.

9. Add Auto renew

   ```shell
   # open crontab
   crontab -e
   # add and save/exit:
   15 0 */10 * * certbot renew >> /var/log/certbot-cron.log 2>&1
   ```
