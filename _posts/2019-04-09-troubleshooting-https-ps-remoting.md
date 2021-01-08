---
title: Troubleshooting HTTPS PS Remoting
date: 2019-04-09T21:34:08+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2019/04/troubleshooting-https-ps-remoting/
categories:
  - Windows
tags:
  - Scripting-Powershell
---
<!--more-->

### Description:

PS Remoting over HTTPS is pretty straightforward to setup. You setup a GPO then you run a script to bind a computer's SSL cert to the listener. These are steps you can do for troubleshooting:

Example: I want to allow `server.domain.com` on `10.10.10.10` to be able to Remote PS to `server2.domain.com` on `10.10.10.20`.

### To Resolve:

1. Verify that the cert imported on server2.domain.com.

   - Run `certlm.msc` - Look under the personal store and see if the certificate is there. You could also run:

   ```powershell
   $Cert = Get-Childitem Cert:\LocalMachine\My | Where-Object { $_.Issuer.StartsWith("CN=InCommon") -and $_.notafter -gt (get-date) }
   ```

   NOTE: The $cert variable should have an active certificate issued from InCommon. Make sure to change this depending on what CA you use.
   {: .notice--success}

2. Verify that the cert is bound to the https listener

   ```powershell
   Cd wsman:\localhost\listener
   Ls
   # look at listeners listed
   ```

   - Sometimes you will see that the computer has a HTTP listener setup. We need to remove that!

   ```powershell
   Rm -r .\listener_blah # you can tab to autocomplete this
   Ls
   #verify it is blank
   ```

   - Now let's bind it to our cert from step 1, but first let's check what's in it:

   ```powershell
   PS WSMan:\localhost\Listener> $cert
      Directory: Microsoft.PowerShell.Security\Certificate::LocalMachine\My
   Thumbprint                                Subject
   ----------                                -------
   B1DA3CE7  CN=server2-test.domain.com, OU=Blah ..
   AB9BFA77  CN=server2-b.domain.com, OU=Blah..
   486DF147  CN=server2.domain.com, OU=Blah..
   ```

   - Well there's the problem, more than one cert is valid! We want the last one because it looks best (matches the hostname). So we will use `$cert[-1]` to reference it and bind it to the listener! The `[-1]` thing is a general powershell way to reference the last element in an array, look it up later.

   ```powershell
   New-Item -Path WSMan:\LocalHost\Listener -Transport HTTPS -Address * -CertificateThumbPrint $Cert[-1].Thumbprint -Force
   ```

   - Much better! Now if we `ls` the wsman:\localhost\listener directory, we see that it has a https listener that is bound to the correct cert. How do we know this? We verify of course. Just `ls`  the listener using autocomplete (tab key on your keyboard) and you will see its thumbprint. Just make sure it matches the thumbprint from the cert from the previous command.

3. Now we test. From server.domain.com, we run:

   ```powershell
   $servers = @('server2.domain.com')
   invoke-command -ComputerName $servers -scriptblock { write-output $env:computername } -usessl
   ```

   NOTE: I made `$servers` an array because the logic is that you will use a comma separated list of servers or do something like `$servers = get-content c:\scripts\servers.txt` to get a list of a bunch of servers.
   {: .notice--success}

4. Verify that the firewall has that port opened **at the host level** on the target machine. Open firewall.cpl => Advanced settings => Sort by port => Look to see that it is enabled. From PS:

   ```powershell
   # look for Enabled to be 'yes'
   netsh advfirewall monitor show firewall rule name="Name of your GPO"
   ```

5. If it's still not working, use Test-Netconnection from server.domain.com to server2.domain.com to verify **at the network level** if there is issues:

   ```powershell
   Test-NetConnection -Computername server2.domain.com -Port 5986
   # Look for 'TCPSucceeded' to be 'True'
   ```

   NOTE: A lot of times ICMP will work, but TCP won't if you are in an environment with segregation rules between different VLANs. If this test fails, you will need to correct it yourself or get with the appropriate team to ensure that server.domain.com can contact server2.domain.com on TCP 5986.
   {: .notice--success}