---
title: What Happens When You Google
date: 2016-08-21T16:57:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/what-happens-when-you-google/
tags:
  - Networking
---
<!--more-->

### Description:

The age old interview question, &#8220;what happens when you go to google.com&#8221; can finally be answered in depth.

### To Resolve:

1. The overall view is: Keyboard signal sent => Packet sent as a request => DNS resolves location => Packet as sent back from DNS server => Your client browser renders according to the received packet back.

2. Keyboard signal sent => an electrical circuit specific to the enter key is closed (either directly or capacitively). This allows a small amount of current to flow into the logic circuitry of the keyboard, which scans the state of each key switch, debounces the electrical noise of the rapid intermittent closure of the switch, and converts it to a keycode integer, in this case 13. The keyboard controller then encodes the keycode for transport to the computer. This is now almost universally over a Universal Serial Bus (USB) or Bluetooth connection, but historically has been over PS/2 or ADB connections. In Windows, the &#8220;WM_KEYDOWN&#8221; message is sent to the app using the key pressed as one of the parameters.

3. The URL is broken down to determine the protocol requested (HTTP) and the location of the page requested, in this case &#8220;google.com&#8221;. The browser first checks if the site is in the HSTS List which is a list of sites that can only be contacted via HTTPS. The browser then checks if the site name is using any non-ASCII characters, and if so => encodes useing Punycode to Unicode format.

4. DNS lookup => The browser checks if the domain is in its cache. If it is not, it then checks the OS host file using the &#8220;gethostbyname&#8221; library function. If it is not there, the OS will send the packet to its DNS server using the ARP protocol. If the local DNS server does not have the host name that matches the query, it sends it to DNS root servers starting with &#8220;.com&#8221; and then &#8220;google.&#8221;. If you requested &#8220;docs.google.com&#8221; the DNS server would then have to query for &#8220;docs&#8221;. DNS servers respond to queries if they have a SOA (start of authority) for the requested host name. For more details, check out [this](https://www.verisign.com/en_US/website-presence/online/how-dns-works/index.xhtml?).

5. Once the IP is returned from the DNS query, it sends the UDP request back via port 53 to your machine (or using TCP if the request is too large). Note that your machine doesn't need to have port 53 open for outgoing, the sending DNS server uses this port to send requests back. This is because most OS's randomize the source port for DNS requests.

6. Packet sent back => If TLS was used (as in this case), the browser sends a &#8220;clientHello&#8221; packet and waits for the server to send a &#8220;serverHello&#8221; packet back that includes the cipher, compression methods, and the servers signed certificate issued by a CA (certificate authority). The cert contains a public key that will be used to encrypt the rest of the handshake until a symmetric key can be agreed upon. The server decrypts random bytes using its private key and uses those to create the symmetric key. The client sends a &#8220;finish&#8221; message using its private key to hash it. The server generates its own hash and decrypts the clients &#8220;finish&#8221; message to see if it matches. If it does, it sends its own &#8220;finish&#8221; message with the symmetric key. From then on, the HTTP protocol will be used with the symmetric key as the hash.

7. HTTPD (HTTP daemon) which is the HTTP server protocol used on the server (usually nginx/apache for linux, IIS for Windows) converts the &#8220;Get/ Http/1.1&#8221; request for resources from the client to determine which pages are being requested. It then sends them to the client. Now the last two steps are handled by the client => parsing and rendering.

8. Client rendering => The browser will render the HTTP request based of the contents of the HTML resource and CSS settings in page. Sometimes after a page is rendered, a browser language such as Javascript may be ran to make changes. Flash or Java may execute as well.

### References:

["What happens when..."](https://github.com/alex/what-happens-when)