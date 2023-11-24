---
title: Install Bind Server On Centos 7
date: 2017-01-14T07:35:40+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/01/install-bind-server-on-centos-7/
tags:
  - Networking
  - Linux
---
<!--more-->

### Description:

Follow these steps to configure a Centos7 box as a DNS server. 

Make sure not to overlook the periods `.` at the end of your host names!
{: .notice--danger}

### To Resolve:

1. Open up a terminal and type: `sudo yum install bind bind-utils`. Bind is now installed and it process is known as `named`

2. First we add our trusted hosts:

   ```shell
   sudo vi /etc/named.conf

   # Edit the options block
   options {
   ...
   allow-transfer { 10.128.20.12; };      # disable zone transfers by default. The IP here is the IP of your server.
   ...
   allow-query { trusted; };  # allows queries from "trusted" clients
   ...
   # Add:
   acl "trusted" {
   10.128.10.11;    # ns1 - can be set to localhost
   10.128.20.12;    # ns2
   10.128.100.101;  # host1
   10.128.200.102;  # host2
   };
   # Add at the end of the file:
   include "/etc/named/named.conf.local";
   # Save and exit
   ```

3. Now we will specify our forward/reverse zones in the following file (should be empty) : sudo vi /etc/named/named.conf.local

   ```shell
   # Add your forward zone
   zone "nyc3.example.com" {
   type master;
   file "/etc/named/zones/db.nyc3.example.com"; # zone file path
   };
   # Add your reverse zone. Note that my IP is 10.128.0.x, you would simply reverse the first two octets as 128.10. If your servers span multiple subnets, create a separate entry for each.
   zone "128.10.in-addr.arpa" {
   type master;
   file "/etc/named/zones/db.10.128";  # 10.128.0.0/16 subnet
   };
   # Save and exit
   ```

4. Now create the directory and files for the zones:

   ```shell
   sudo chmod 755 /etc/named
   sudo mkdir /etc/named/zones
   ```

5. Now we edit the forward zone file:

   ```shell
   sudo vi /etc/named/zones/db.nyc3.example.com

   # First, you will want to add the SOA record. Replace the highlighted ns1 FQDN with your own FQDN, then replace the second "nyc3.example.com" with your own domain. Every time you edit a zone file, you should increment the serial value before you restart the named process--we will increment it to "3". It should look something like this:
   $TTL    604800
   @       IN      SOA     ns1.nyc3.example.com. admin.nyc3.example.com. (
   3         ; Serial
   604800     ; Refresh
   86400     ; Retry
   2419200     ; Expire
   604800 )   ; Negative Cache TTL

   # After that, add your nameserver records with the following lines (replace the names with your own). Note that the second column specifies that these are "NS" records:
   ; name servers - NS records
   IN      NS      ns1.nyc3.example.com.
   IN      NS      ns2.nyc3.example.com.

   # Then add the A records for your hosts that belong in this zone. This includes any server whose name we want to end with ".nyc3.example.com" (substitute the names and private IP addresses). Using our example names and private IP addresses, we will add A records for ns1, ns2, host1, and host2 like so:
   ; name servers - A records
   ns1.nyc3.example.com.          IN      A       10.128.10.11
   ns2.nyc3.example.com.          IN      A       10.128.20.12
   ; 10.128.0.0/16 - A records
   host1.nyc3.example.com.        IN      A      10.128.100.101
   host2.nyc3.example.com.        IN      A      10.128.200.102

   # Save and exit
   ```

6. Now we edit the reverse zone file:

   ```shell
   sudo vi /etc/named/zones/db.10.128

   # Same setup as above
   $TTL    604800
   @       IN      SOA     ns1.nyc3.example.com. admin.nyc3.example.com. (
   3         ; Serial
   604800     ; Refresh
   86400     ; Retry
   2419200     ; Expire
   604800 )   ; Negative Cache TTL

   # Add name servers
   ; name servers - NS records
   IN      NS      ns1.nyc3.example.com.
   IN      NS      ns2.nyc3.example.com.

   # Add PTR records for all of your servers whose IP addresses are on the subnet of the zone file that you are editing
   ; PTR Records
   11.10   IN      PTR     ns1.nyc3.example.com.    ; 10.128.10.11
   12.20   IN      PTR     ns2.nyc3.example.com.    ; 10.128.20.12
   101.100 IN      PTR     host1.nyc3.example.com.  ; 10.128.100.101
   102.200 IN      PTR     host2.nyc3.example.com.  ; 10.128.200.102

   # Save and exit
   ```

7. That's it! Now we check our files using a built-in utility:

   ```shell
   sudo named-checkconf
   ```

   - I failed mine. I had to place `/named` in my `include "/etc/named/named.conf.local";` statement from step 2. My brain saw /named/named and just reduced it haha.

8. Now we check our forward zone config:

   ```shell
   sudo named-checkzone nyc3.example.com /etc/named/zones/db.nyc3.example.com
   ```

9. Now check reverse zone config:

   ```shell
   sudo named-checkzone 128.10.in-addr.arpa /etc/named/zones/db.10.128

   # Again I failed this check. This was the error:
   Jan 02 00:17:52 (truncated) bash[3940]: zone 1.0.0.127.in-addr.arpa/IN: loaded serial 0
   Jan 02 00:17:52 (truncated) bash[3940]: zone 0.in-addr.arpa/IN: loaded serial 0
   Jan 02 00:17:52 (truncated) bash[3940]: zone (truncated)/IN: loading from master file ect/named/zones/db.10.128 failed: file not found
   Jan 02 00:17:52 (truncated) bash[3940]: zone (truncated)/IN: not loaded due to errors.
   Jan 02 00:17:52 (truncated) bash[3940]: _default/(truncated)/IN: file not found
   Jan 02 00:17:52 (truncated) bash[3940]: zone 1628.10.in-addr.arpa/IN: loaded serial 3
   Jan 02 00:17:52 (truncated) systemd[1]: named.service: control process exited, code=exited status=1
   Jan 02 00:17:52 (truncated) systemd[1]: Failed to start Berkeley Internet Name Domain (DNS).
   Jan 02 00:17:52 (truncated) systemd[1]: Unit named.service entered failed state.
   Jan 02 00:17:52 (truncated) systemd[1]: named.service failed.

   # The fix: change "ect" to "/etc", I do this all the time!
   sudo vi /etc/named/named.conf.local
   ```

10. Finally, start/enable the service:

   ```shell
   sudo systemctl start named
   sudo systemctl enable named
   ```

### References:

["How To Configure BIND as a Private Network DNS Server on CentOS 7"](https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-a-private-network-dns-server-on-centos-7)  

["5. A simple domain."](http://www.tldp.org/HOWTO/DNS-HOWTO-5.html)  

