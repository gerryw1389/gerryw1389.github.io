---
title: Learning To Subnet
date: 2017-08-05T05:13:34+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/08/learning-to-subnet/
categories:
  - Networking
---
<!--more-->

### Description:

Subnetting can be tough! When studying for my CCNA, this is the subject I studied the hardest on. You need to do practice problem after practice problem until you feel confident!

   - Use this chart:
   <img class="alignnone size-full wp-image-4565" src="https://automationadmin.com/assets/images/uploads/2017/08/chart.png" alt="" width="460" height="336" srcset="https://automationadmin.com/assets/images/uploads/2017/08/chart.png 460w, https://automationadmin.com/assets/images/uploads/2017/08/chart-300x219.png 300w" sizes="(max-width: 460px) 100vw, 460px" /> 

   - Source: [http://www.quest4.org/ccna/subnet\_cheat\_sheet.htm](http://www.quest4.org/ccna/subnet_cheat_sheet.htm)

### To Resolve:

1. First know your subnet ranges:

   ```escape
   Class A – has to start with a 0

   0 0000001 = 1

   0 1111111 – 128

   Class B – has to start with a 10

   10 00000 = 128

   10 11111=191

   Class C = has to start with a 110

   110 0000 = 192

   110 1111 = 223
   ```

2. RFC 1918/4193 set rules for private addresses

   ```escape
   10.x.x.x /8

   172.16.0.0  – 172.31.255.255 / 12

   192.168.x.x /16
   ```

3. Create a sheet that looks like this when you walk in to the exam:


   ```escape
   Mask:            128  192  224  240  248  252  254  255

   Bits Borrowed:   128  64   32   16   8    4    2    1


   Subnets = 2 to the power of borrowed bits

   Hosts = 2 to the power of unborrowed bits

   First thing to find in any subnet question is how many bits you borrowed from the closest major class (usually /24). Whatever you land on is the increment number. The number above it is the subnet mask.

   ```


3. Question: What network is host 172.16.5.68 255.255.255.240 in?

   - Answer: 172.16.5.64-172.16.5.79. 
   - Explanation: First look at the mask: 256 => `240` = 16, so you have the subnets going up in increments of 16, starting with zero (if subnet zero is permitted in the exam). Each subnet will need to have a subnet and a broadcast number, so this leaves 14 hosts per subnet. The subnets start at 0,16,32,48, 64, 80…224, 240 (the 0 and 240 are valid only if subnet zero is allowed).

   ```escape
   Network       First Host    Last Host     Broadcast
   172.16.5.0    172.16.5.1    172.16.5.14   172.16.5.15
   172.16.5.16  172.16.5.17   172.16.5.30   172.16.5.31
   172.16.5.32  172.16.5.33   172.16.5.62   172.16.5.63
   172.16.5.64  172.16.5.65   172.16.5.78   172.16.5.79       
   * We know it's in this range because 68 is between 65 and 78!
   ```


4. Question: Suppose the following network:

   ```escape
   Admin 44 users
   Faculty network has 60 users
   media has 22 users
   library has 12 users

   Which subnet would accommidate this network?
   A. 255.255.255.128 / 25
   B. 255.255.255.192 / 26
   C. 255.255.255.224 / 27
   D. 255.255.255.240 / 28
   E. 255.255.255.248 / 29
   ```

   - Answer: B. Explanation = Questions you need to ask yourself:
   - How many subnetworks do we need? 
   - At least 4 because there is four different departments.
   - How big does the subnet need to be? 
   - Enough to cover the number of hosts in the largest network. In this case the one with 60 users, so a /26 which gives us 64 hosts in 4 subnets.
   - What are the networks? 
   - 0, 64, 128, 192

5. Which is a usable host address?

   ```escape
   A. 192.168.2.224 /28
   B. 192.168.2.47 /28
   C. 192.168.2.160 /28
   D. 192.168.2.192 /28
   E. None of the above
   ```

   - Answer: B. All the others land on a network address. Explanation = Questions to ask yourself:
   - What is the subnet mask?
   - 255.255.255.240
   - What is the magic number? 16
   - What are the networks?

   ```escape
   16
   32
   48
   64
   80
   96
   112
   128
   144
   160
   176
   192
   208
   224
   240
   256
   ```

6. Given the IP Address space below, create 7 subnets within the range of 192.168.0.0 - 192.168.255.255

   ```escape
   1st - 260 host minimum /23 with 512 hosts
   2nd - 177 host minimum /24 with 256
   3rd - 50 host minimum /26 with 64
   4th - 20 host minimum /27 with 32
   5th - point to point 2 host minimum /30
   6th - point to point 2 host minimum /30
   7th - point to point 2 host minimum /30
   ```


   - Answer: Explanation = Questions to ask
   - How many hosts do we have? 260+177+50+20+2+2+2 = 513. We can't do /23 because that only leaves 512 hosts, so we have to move to a /22 with 1024 hosts.
   - What is the full subnet range? 192.168.0.0 /22
   - What is the subnet mask? For a /22 that is 255.255.252.0
   - What is the bits borrowed (magic number)? 4 because /22 borrows 2 bits and 2^2 = 4. Our network will go up like 192.168.4.0, 192.168.8.0, etc.

   - Step 1: divide up the networks by checking the bits and hosts

   ```escape
   /22 = 1024
   /23 = 512
   /24 = 256
   /25 = 128
   /26 = 64
   /27 = 32
   /28 = 16
   /29 = 8
   /30 = 4 only 2 are usable
   ```

   - Step 2: Assign the networks to the problem, now subnet it out

   ```escape
   Network 1st is 192.168.0.0/23 - 192.168.1.255/23 
   # This network needs 260 hosts so we need a /23. We borrowed one bit to the LEFT OF /24. So we are creating another network. So 2^1 so networks go up by 2: 192.168.2.0, 4.0, 6.0, &#8230;.

   network 2nd is 192.168.2.0/24 - 192.168.2.255/24 
   # standard class c network, covers our 177 host requirement on 1 network.

   network 3rd is 192.168.3.0/26 - 192.168.3.63/26 
   # needs 50 host so a /26 which will cover 64 hosts on 4 sub-networks. I mean that we borrowed 2 bits so 2^2 is 4. But since /26 is SMALLER than /24, we are DIVIDING 256 by the number of borrowed bits, in this case 4 networks with 64 host each.

   network 4th is 192.168.3.64/27 - 192.168.3.95/27
   # needs 20 host so a /27 which will cover 32 hosts with 8 sub-networks (2^3=8).

   network 5th is 192.168.3.96/30 - 192.168.3.99/30
   # needs 2 host so a /30 which will cover 2 hosts. A /30 borrows 6 bits so 2^6=64 so we have 64 sub-networks with two hosts each.

   network 6th is 192.168.3.100/30 - 192.168.3.103/30
   # needs 2 host so a /30 which will cover 2 hosts.

   network 7th is 192.168.3.104/30 - 192.168.3.107/30
   # needs 2 host so a /30 which will cover 2 hosts.
   ```


7. A common subnetting question may ask:

   ```escape
   The admin network has 44 users
   The teacher network has 123 users.
   What should be the best subnet mask?
   ```

   - Answer: 
   - In these situations, you want to answer to the lowest possible fit that you can, don-t make any room for expansion (not realistic).
   - The answer is /25 because that would create two networks, each with up to 126 usable IP-s. 
   - It's tempting to think that you need to add the users and then pick a network that will support them but the question is usually asking what is the smallest subnet you can fit them in.

   ```escape
   The Reasoning:

   So we know a classful Class C network has 24 network bits and 8 host bits that equal 256 hosts (2^8 = 256). This is done by adding the values 128+64+32+16+8+4+2+1=255 plus one because in networking, 0 counts as the first number. So we end with 256, BUT we have to subtract 2 for the network (.0) and the broadcast addresses (.255) so really only 254 usable hosts that can be assigned IP addresses.

   Well a /25 network is half of that. To get that just do the math, 2^7 = 128.  An easy way to picture this is to think of the N to H relationship. /25 will have one of the H bits borrowed for the subnet only giving you 64+32+16+8+4+2+1=127 hosts. But remember the rule with 0 (so you have 128) and how 2 IP-s are always subtracted, this leaves you with 126 usable hosts.

   You can follow this pattern to create a table:

   /24 is 256 host / 254 usable hosts per subnet. This the default class C network. This looks like 255.255.255.0

   /25 is 128 hosts / 126 usable hosts per subnet. This looks like 255.255.255.128

   /26 is 64 hosts / 62 usable hosts per subnet. This looks like 255.255.255.192

   /27 is 32 hosts / 30 usable hosts per subnet. This looks like 255.255.255.224

   /28 is 16 hosts / 14 usable hosts per subnet. This looks like 255.255.255.240

   /29 is 8 hosts / 6 usable hosts per subnet. This looks like 255.255.255.248

   /30 is 4 hosts / 2 usable hosts per subnet. This is the lowest you can go because you need at least two computers to network. This looks like 255.255.255.252

   On the other end of the spectrum is Class B and Class A networks where you borrow Network bits to make more hosts! The following tables describes:

   /16 is 65536 hosts / 65534 usable hosts per subnet. This is the default class B network. This looks like 255.255.0.0

   /17 is 32768 hosts / 32766 usable hosts per subnet. This looks like 255.255.128.0

   /18 is 16384 hosts / 16382 usable hosts per subnet. This looks like 255.255.192.0

   /19 is 8192 hosts / 8190 usable hosts per subnet. This looks like 255.255.224.0

   /20 is 4096 hosts / 4094 usable hosts per subnet. This looks like 255.255.240.0

   /21 is 2048 hosts / 2048 usable hosts per subnet. This looks like 255.255.248.0

   /22 is 1024 hosts / 1022 usable hosts per subnet. This looks like 255.255.252.0

   /23 is 512 hosts / 510 usable hosts per subnet. This looks like 255.255.254.0

   ```

   - Class A networks are uncommon in local network but can be found [here](http://www.tcpipguide.com/free/t_IPSubnettingSummaryTablesForClassAClassBandClassCN-2.htm)

   - A tabled version of this can be found [here](https://www.aelius.com/njh/subnet_sheet.html)

   - Always remember: 128,64,32,16,8,4,2,1 is the values in each octet. When adding they go up like 192,224,240,248,252,254,255

   - Always remember: A subnet is represented as NNNNNNNN.NNNNNNNN.NNNNNNNN.NNHHHHH where N is network addresses and H is hosts. (a /26 network in this example)

   - Always remember: You can get the total number of networks for a subnet by dividing the number of host from 256. For example, a /27 network has 32 hosts so 256/32=8 possible subnets.

8. A common subnetting question may ask:

   ```escape
   192.168.3.55/26
   Is this a usable host address?
   If so, what network is it in?
   ```

   - Answer: 
   - Find the subnet mask. Since this is a /26 we know it is not classful (/24 for Class C, /16 for Class B, and /8 for Class A).
   - We write out 26 1's from left to right
   - 11111111.11111111.11111111.11000000 / the two 1's are borrowed bits/subnet bits
   - We add the two left values to get 192 (128+64)
   - 255.255.255.192
   - Find the magic number. The magic number is the value of the place the last number 1 was in.
   - In this case, it was 64. Values go: 128,64,32,16,8,4,2,1.128,64,32,16,8,4,2,1.128,64,32,16,8,4,2,1.128,64,32,16,8,4,2,1. 64 is where the 1-s ended.
   - Now that you know the magic number, you know the different sub-networks or subnets:
   - 0-63 # where 0 and 63 are unusable because they are the network/broadcast addresses for the subnet respectively.
   - 64-127 # where 64 and 127 are unusable because they are the network/broadcast addresses for the subnet respectively.
   - 128-191 # where 128 and 191 are unusable because they are the network/broadcast addresses for the subnet respectively.
   - 192-255 # where 192 and 255 are unusable because they are the network/broadcast addresses for the subnet respectively.
   - Now that we know the magic number we can also tell you how many hosts are available:
   - There are 4 networks because we borrowed 2 bits. 2^2 = 4.
   - There are 64 hosts because that is the value the last borrowed bit landed on (magic number). 2^6 = 64. BUT 2 of those are not usable, so there is really 62 - usable host per subnet.
   - Now answer the questions, yes it's usable and yes its in the 0-63 network.


9. Example 2:

   ```escape
   192.168.1.153 /27
   Is this a usable host address?
   If so, what network is it in?
   ```

   - Answer:
   - Find the subnet mask. Since this is a /27 we know it is not classful (/24 for Class C, /16 for Class B, and /8 for Class A).
   - We write out 27 11's from left to right
   - 11111111.11111111.11111111.11100000 / the three 1's are borrowed bits/subnet bits
   - We add the three left values to get 224 (128+64+32)
   - 255.255.255.224
   - Find the magic number. The magic number is the value of the place the last number 1 was in.
   - In this case, it was 32. Values go: 128,64,32,16,8,4,2,1.128,64,32,16,8,4,2,1.128,64,32,16,8,4,2,1.128,64,32,16,8,4,2,1. 64 is where the 1-s ended.
   - Now that you know the magic number, you know the different sub-networks or subnets:
   - 32
   - 64
   - 96
   - 128 => its in the .128 network. Broadcast is 159
   - 160.. we can stop here
   - Now that we know the magic number we can also tell you how many hosts are available:
   - There are 8 networks because we borrowed 3 bits. 2^3 = 8.
   - There are 32 hosts because that is the value the last borrowed bit landed on (magic number). 2^5 = 32. BUT 2 of those are not usable, so there is really 30    - usable host per subnet.
   - Now answer the questions, yes it's usable and yes its in the 128-159 network.

10. I highly recommend CCNA in 60 Days as that was my main study guide for the exam.