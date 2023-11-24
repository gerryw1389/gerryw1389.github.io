---
title: Guide To Certificates
date: 2017-10-09T17:14:15+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/10/guide-to-certificates/
tags:
  - SysAdmin
  - Security
---
<!--more-->

### Description:

From [https://www.reddit.com/r/sysadmin/comments/6zq3us/sysadmin\_guide\_to_certificates/](https://www.reddit.com/r/sysadmin/comments/6zq3us/sysadmin_guide_to_certificates/):

After seeing /u/I\_will\_have\_you\_CCNA post today What networking or IT concept did you struggle with and just couldn't seem to learn?, it seems like many sysadmins are struggling with the concepts of certificates. I figured I would take my shot at creating an explanation of certificates, and (hopefully be able to) answer any questions you might have. The more administrators that understand the concepts the safer the internet becomes.

So&#8230;

Version 1 (Symmetric Key Encryption):  
This is encryption where 2 parts agree on a key and they can use it to encrypt and decrypt the same message.

Encryption:  
plaintext => encryption(key) => ciphertext  
Decryption:  
ciphertext => decryption(key) => plaintext

This is still used when the person encrypting and decrypting is the same person. e.g. encrypting a hard drive. The flaw of this style lies in having to communicate the key to all parties securely.  
Which brings up&#8230;

Version 2 (Asymmetric Encryption):  
Now, as the name suggests, encrypting and decrypting require a different key. This is called a key pair. This means that you can encrypt using either key, and decrypt using the other. So&#8230;

Encryption using Key 1:  
plaintext => encryption(key1) => ciphertext(1)  
Decryption using Key 1's pair:  
ciphertext(1) => decryption(key2) => plaintext

Encryption using Key 2:  
plaintext => encryption(key2) => ciphertext(2)  
Decryption using Key 2's pair:  
ciphertext(2) => decryption(key1) => plaintext

This allows us to give out one key and keep the other a secret. So say I keep key 1 and give out key 2. Great, you have just assigned key 1 to be your PRIVATE KEY and key 2 to be your PUBLIC KEY  
So lets revise:

Encryption using PRIVATE KEY:  
plaintext => encryption(PRIVATE) => ciphertext(1)  
Decryption using PUBLIC KEY:  
ciphertext(1) => decryption(PUBLIC) => plaintext

Encryption using PUBLIC KEY:  
plaintext => encryption(PUBLIC) => ciphertext(2)  
Decryption using PRIVATE:  
ciphertext(2) => decryption(PRIVATE) => plaintext

So now that the two situations are different only by which key was used we can look at the differences.

1) Encrypting using your private key means that anyone with your public key can decrypt it. Usually this is the opposite of what people want when they encrypt something, but this does mean one thing&#8230; That the recipient of the message can guarantee that the message came from you. Congratulations, you just digitally signed a message.  
2) Someone encrypting a message using your public key means that only you can decrypt it. This means that now, once it is encrypted, that message is secret. Someone has just encrypted a message to you.

Alright, now we are starting to get somewhere, but we still want to be able to encrypt a message to someone else, not just receive an encrypted message. Luckily all the parts are in place. To encrypt a message to someone else we just have to reverse the previous diagram and have the person we are communicating with send us their public key. So..

Encryption using other users PRIVATE KEY:  
plaintext => encryption( PRIVATE[user2] ) => ciphertext(1)  
This isn't going to be possible for us to do as their private key should never leave their system.  
Decryption using other users PUBLIC KEY:  
ciphertext(1) => decryption( PUBLIC[user2] ) => plaintext

Encryption using other users PUBLIC KEY:  
plaintext => encryption( PUBLIC[user2] ) => ciphertext(2)  
Decryption using other users PRIVATE KEY:  
ciphertext(2) => decryption( PRIVATE[user2] ) => plaintext  
Once again, this isn't possible for us to do, as we don't have their private key.

Ok so this enabled two more scenarios for us.

1) Decrypting a message user2 sent us using their public key. In this case anyone with the public key can read it so its no secret, but we can confirm that the message came from them. We just verified a signature.  
2) Last but not least, we encrypted a message using the other users public key, anyone with that public key can encrypt a message, but only user 2 can read it. Finally we can sent a secret message to user 2. We have encrypted a message.

This is what we have been looking for, but one problem still remains. There is a lot of keys, and the more users there are the faster that number increases, and if we haven't talked to this computer before how can we for sure know that they are who they say they are when they give us their public key?  
Enter&#8230;

Version 2.1 (Public Key Infrastructure):  
Ok, so we have identified that we want to use asymmetric encryption, but we still can't confirm user 2 is who they say they are. So now, naturally, we want to ask someone else. Enter the Certificate Authority. This is the third party that we have agreed we will both trust. (or in most cases, whoever made your browser/OS/etc has vetted as a reputable third party as thats all they have to go by, their reputation).  
So now, once again we have to be fancy and use encryption so the Certificate Authority generates their public and private key. But this time, we only care about one direction. The Certificate Authority encrypting to us. This means that they have signed a message to us and we can confirm that it came from them.  
Ok, what do we care about them saying? The other users public key. So the other user sends their public key to the nice and trusted Certificate Authority, and they verify they are who they say they are, and hand them back a handy dandy certificate (you know I had to get to it eventually).  
So what does this MEAN: Now when user 2 give us their certificate, I can check with someone I trust to confirm it came from user 2!  
Thats all it is folks, a certificate is just a public key that, whoever we give it to, can verify came from us.

I know that has all been really long winded, and was a bit rushed, so I'll come back and edit as I can to make it more clear, and as people have questions. Please feel free to ask as many questions as you have, tell me where I am wrong, etc. The more admins that understand this and the deeper we understand this the safer our communications and data become.

TL;DR: A certificate is a public key that can be proven to come from who they claim they are.  
EDIT: When you request a certificate for your server, mark your damn calendar for when it expires. Maybe even create a script or monitoring service that will tell you it expires in a week, month, or however much lead time you need to replace it.

