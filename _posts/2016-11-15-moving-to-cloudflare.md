---
title: Moving To CloudFlare
date: 2016-11-15T05:08:09+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/11/moving-to-cloudflare/
categories:
  - Networking
tags:
  - Cloud
  - Setup
---
<!--more-->

### Description:

So currently, my site is gerrywilliams.ddns.net and it's working fine. Just to learn new things, I decided to try some new things. Ultimately, I went from:  
http site hosted free using noip.com => https site hosted on CloudFlare for a dollar a month for my domain name. Here are the steps I did:

### To Resolve:

1. First, I found the domain name `gerrywilliams.net` on Google Domains for $12/yr. Purchased.

2. I then signed up for Cloudflare and had change my DNS records in Google Domains to point to theirs. NOTE: By doing this, you will lose basically all the services that Google gives you like free emails, ex: admin@yourdomain.com or tech@yourdomain.com. That's okay, we will get those back another way (see step 5).

   - DNS servers at the time of this writing:  
     - `ali.ns.cloudflare.com`
     - `dale.ns.cloudflare.com`

3. The first thing I did was add an `A` record pointing my home IP address. So at this point you have one A record and the two NS records.

   - Record type = `A`
   - Name = `www`
   - Value = `MyPublicIPinV4Format`
   - TTL = `Automatic`

4. Next, I setup the [naked domain redirect](https://automationadmin.com/2016/11/naked-domain-redirect-cloudflare/).

5. Next, I setup [Mailgun](https://automationadmin.com/2016/11/setting-up-mailgun-with-cloudflare/) for the email.

6. Next, I setup [SSL](https://automationadmin.com/2016/11/setup-ssl-using-apache-on-centos-7/) for my site.

7. I then had to go back to step 4 and add the `s` from http => https.

8. Lastly, I wanted an automated way to update my home IP automatically so I modified [this](https://gist.github.com/benkulbertis/fff10759c2391b6618dd/) script and set it as a scheduled task (next step). All credit goes to creator of the script (see link)!

   - Create a folder in your documents and copy this script

   ```shell
   cd ~  
   mkdir update-ip  
   cd /update-ip  
   touch updateip.sh  
   ```

   - Copy and paste the following after modifying for your setup:

   ```shell
   #!/bin/bash

   # CHANGE THESE
   auth_email="user@example.com"
   auth_key="c2547eb745079dac9320b638fadsf5e225cf473cc5cfdda41" # found in cloudflare account settings
   zone_name="example.com"
   record_name="www.example.com"

   # MAYBE CHANGE THESE
   ip=$(curl -s http://ipv4.icanhazip.com)
   ip_file="ip.txt"
   id_file="cloudflare.ids"
   log_file="cloudflare.log"

   # LOGGER
   log() {
       if [ "$1" ]; then
           echo -e "[$(date)] - $1" >> $log_file
       fi
   }

   # SCRIPT START
   log "Check Initiated"

   if [ -f $ip_file ]; then
       old_ip=$(cat $ip_file)
       if [ $ip == $old_ip ]; then
           echo "IP has not changed."
           exit 0
       fi
   fi

   if [ -f $id_file ] && [ $(wc -l $id_file | cut -d " " -f 1) == 2 ]; then
       zone_identifier=$(head -1 $id_file)
       record_identifier=$(tail -1 $id_file)
   else
       zone_identifier=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=$zone_name" -H "X-Auth-Email: $auth_email" -H "X-Auth-Key: $auth_key" -H "Content-Type: application/json" | grep -Po '(?<="id":")[^"]*' | head -1 )
       record_identifier=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$zone_identifier/dns_records?name=$record_name" -H "X-Auth-Email: $auth_email" -H "X-Auth-Key: $auth_key" -H "Content-Type: application/json"  | grep -Po '(?<="id":")[^"]*')
       echo "$zone_identifier" > $id_file
       echo "$record_identifier" >> $id_file
   fi

   update=$(curl -s -X PUT "https://api.cloudflare.com/client/v4/zones/$zone_identifier/dns_records/$record_identifier" -H "X-Auth-Email: $auth_email" -H "X-Auth-Key: $auth_key" -H "Content-Type: application/json" --data "{\"id\":\"$zone_identifier\",\"type\":\"A\",\"name\":\"$record_name\",\"content\":\"$ip\"}")

   if [[ $update == *"\"success\":false"* ]]; then
       message="API UPDATE FAILED. DUMPING RESULTS:\n$update"
       log "$message"
       echo -e "$message"
       exit 1 
   else
       message="IP changed to: $ip"
       echo "$ip" > $ip_file
       log "$message"
       echo "$message"
   fi
   ```

   - Then

   ```shell
   chmod +x updateip.sh  
   ./updateip.sh  
   # make sure it works
   ```

9. To set as a Scheduled Task (crontab):  

   ```shell
   crontab -e  
   #paste in:  
   0,14,29,44 \* \* \* \* /home/gerry/update-ip/updateip.sh > /home/gerry/update-ip/crontab.log
   ```

10. This will update my CloudFlare IP every 15 minutes and log it to crontab.log in the same directory.
