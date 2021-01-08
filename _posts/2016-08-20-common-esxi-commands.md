---
title: Common ESXI Commands
date: 2016-08-20T04:03:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/08/common-esxi-commands/
categories:
  - SysAdmin
tags:
  - VirtualizationSoftware
  - OneLiners-Bash
---
<!--more-->

### Description:

I don't use VMWare in my environment, but I have used it in home labs and it appears in most job listings so it's definitely something worth taking your time to learn. ESXI is a linux based distro modified by VMWare as a hypervisor to host virtual machines on. Here is a small list of commands you can run:

### To Resolve:

1. First a few Linux commands available in all distro's:

   |Command| Description|
   |:---|:---|
   |`find/cat/grep`| These three commands are crucial when trying to find specific files or text within a  file. The find command will locate a specific file, based on either a filename or a pattern. Cat is used to simply display the contents of a file, while grep can be used to search for specific text within a single or group of files.|
   |`find /path/to/vm/folder –iname *delta*`| list all delta disks of a VM.|
   |`cat hostd.log | grep error`| search occurrences of &#8220;error&#8221; within the hostd.log|
   |`head/tail`| These two commands can be very useful when viewing the contents of a file. While the `cat` command is great for displaying the complete contents of a file, head and tail can be used to show either just the beginning or end part of the file, skipping the contents in the middle. tail can be extremely useful in times of troubleshooting, especially when specifying the `-f` flag to monitor log files in real time.|
   |`tail -f /var/log/vmkernel.log`| watch the vmkernel log in real time.|
   |`less`| The less command becomes extremely useful when you are displaying the contents of large files. By piping `|` your cat output to less, you are able to have the system page the output, allowing us to scroll through the output, both up and down through the file. See next example.|
   |`cat /var/log/vpxa.log | less`| output vpxa.log to the screen with a paging fashion.|
   |`df/vdf`| These two commands deal with presenting information about free space within file systems. The df command, now showing VMFS data stores, will show the size, used and available space within both our file system and our data stores. To view the usage of the different ramdisks within an ESXi host, you must use the vdf command. Both commands are great for discovering any issues that may be caused due to low free space.|
   |`ps/kill`| These commands deal with discovering and forcibly terminating services that are running inside of the ESXi host. The ps command contains many command line switches, but is most commonly used to retrieve the running world ID of a process in order to send to the kill command. The kill command then respectively terminates that process.|
   |`vi`| Those who are unfamiliar with vi will most definitely have trouble learning it. The vi command is a text editor that is used to modify the contents of a file – a must-have skill for any vSphere administrator performing troubleshooting from the command shell.|

2. Esxi Commands:

   |Command| Description|
   |:---|:---|
   |`services.sh`| While Linux services are normally handled using the services command, ESXi services are handled much the same way utilizing the services.sh command. Services.sh can be passed with a stop, start, or restart flag to perform the respected operation on all ESXi services.|
   |`services.sh restart`| restart all ESXi services.|
   |`/etc/init.d`| The scripts located in /etc/init.d can be used to start/stop their respective services one at a time. If you just wanted to restart the vCenter Server Agent (also known as the vpxa service), you could run /etc/init.d/vpxa restart to restart it. On the other hand, services.sh restart would restart all services.|
   |`/etc/init.d/vpxa restart`| restart vCenter Agent on host|
   |`cat /etc/chkconfig.db`| view current running status of all ESXi services.|
   |`vmkping`| We are all familiar with the functionality of the age old `ping.exe` command. But, vmkping takes this one step further and allows you to use the IP stack of the VMkernel to send Internet Control Message Protocol (ICMP) packets through specified interfaces. Meaning, you could send a ping packet out through the vMotion network, rather than over the management network.|
   |`vmkping –I vmk1 10.10.10.1`| send ICMP request to 10.10.10.1 through vmk1 interface|
   |`nc`| Coupled with vmkping, the nc command (netcat) can be useful when confirming network connectivity to a certain IP from an ESXi host. While vmkping confirms communication through ICMP, there are times when we want to confirm connection on a specific TCP port (think iSCSI connections on port 3260).|
   |`nc –z 10.10.10.10 3260`| test connectivity to 10.10.10.10 on port 3260.|
   |`vmkfstools`| If you ever need to manage VMFS volumes and virtual disks via the command line, then vmkfstools is the command for you. The vmkfstools command allows you to create, clone, extend, rename and delete VMDK files. In addition to the virtual disk options, you can also create, extend, grow and reclaim blocks from our file systems with vmkfstools.|
   |`vmkfstools –i test.vmdk testclone.vmdk`| clones test.vmdk to testclone.vmdk|
   |`esxtop`| When it comes to performance monitoring and troubleshooting on an ESXi host, few tools can give you as much information as esxtop. With similar functionality to the Linux top command, esxtop goes one step further by gathering VMware-specific metrics as they compare to CPU, interrupt, memory, network, disk adapter, disk device, disk VM and power management.|
   |`vscsiStats`| When you need to go one step further with your performance monitoring of storage I/O, vscsiStats can be a great help. The vscsiStats command will help you gather a collection of data and metrics that pertain to a VM's disk I/O workload. In the end, you are basically left with a sample to help you gather the most common I/O size and latency averages. Using vscsiStats can prove to be invaluable when capacity planning or migrating your back end storage as well.|
   |`vim-cmd`| Vim-cmd is a command space that is built over top of the hostd process, allowing the end user to script and command almost every vSphere API. Vim-cmd has a number of sub ESXi commands dealing with different portions of the virtual infrastructure and is very easy to use compared to its counterpart, vimsh.|
   |`dcui`| The VMware Direct User Console Interface (DCUI) is the menu-based option listing that you see when you initially log into an ESXi host. There are many different options available to you from the DCUI, such as root password maintenance, network and maintenance. Sometimes you may only have SSH access to the host, but thankfully, you can still get to the DCUI menu-based system by simply executing dcui from the command line.|
   |`vm-support`| Ever feel like grabbing a complete bundle of all the support and log information that you have inside of your ESXi host? That is exactly what vm-support does. This tool is invaluable, and if you have ever been on a support call with VMware, you have probably already ran this.|

3. EsxiCli:

   - The esxcli command is so vast that we cannot simply classify it as a single command. esxcli contains many different namespaces allowing you to control virtually everything that ESXi offers. Listed below are some (but certainly not all) of the commonly used namespaces:

   |Command| Description|
   |:---|:---|
   |`esxcli hardware`| The hardware namespace of esxcli can prove extremely useful when you are looking to get information about the current hardware and setup of your ESXi host|
   |`esxcli hardware cpu list`| retrieve CPU information (family, model and cache).|
   |`esxcli hardware memory get`| retrieve information about memory (available and non-uniform memory access).|
   |`esxcli iscsi`| The iscsi namespace can be used to monitor and manage both hardware and software iSCSI setups.|
   |`esxcli iscsi software`| can be used to enabled/disable the software iSCSI initiator.|
   |`esxcli iscsi adapter`| can be used to setup discovery, CHAP and other settings for both your hardware and software iSCSI adapters.|
   |`esxcli iscsi sessions`| can be used to list established iSCSI sessions on the host.|
   |`esxcli network`| The network namespace of esxcli is extremely valuable when looking to monitor and make changes to anything and everything dealing with vSphere networking, including virtual switches, VMKernel network interfaces, firewalls and physical network interface cards (NICs).|
   |`esxcli network nic`| list and modify NIC information, such as name, wake on LAN, and speeds.|
   |`esxcli network vm list`| list networking information about your VMs that have an active network port.|
   |`esxcli network vswitch`| Commands to retrieve and manipulate options on VMware's standard and distributed virtual switches.
   |`esxcli network ip`| Commands to manage VMkernel ports, including management, vMotion and Fault Tolerance networks. Also contains the ability to modify any of the IP stack in regard to the host, including DNS, IPsec and routing information.|
   |`esxcli software`| The software namespace can be used to retrieve and install different pieces of software and drivers on your ESXi host.|
   |`esxcli software vib list`| list the software and drivers currently installed on the ESXi host|
   |`esxcli storage`| This is perhaps one of the most used esxcli command namespaces and contains everything and anything you need in order to manage the core storage attached to vSphere.|
   |`esxcli storage core device list`| list the current storage devices|
   |`esxcli storage core device vaai status get`| get the current status of VAAI support on your storage devices.|
   |`esxcli system`| This command gives you the ability to control ESXi advanced options, such as setting up syslog and managing host status.|
   |`esxcli system maintenanceMode set –enabled yes/no`| set the host into maintenance mode.|
   |`esxcli system settings advanced`| View and change ESXi advanced settings (Hint: Use esxcli system settings advanced list –d to view the settings that deviate from the default).|
   |`esxcli system syslog`| Syslog information and configuration|
   |`esxcli vm`| The VM namespace of ESXi can be used to list out various tidbits of information about the VMs running on the host and shut them down forcibly if needed.|
   |`esxcli vm process list`| List out process information for powered on VMs|
   |`esxcli vm process kill`| Terminate running VM process, essentially shutting down or forcibly powering off a VM.|
   |`esxcli vsan`| The VSAN namespace of ESXi contains a ton of commands dealing with VSAN setup and maintenance, including data store, network, fault domain, and policy configuration.|
   |`esxcli vsan storage`| commands for configuring local storage for use with VSAN, including adding and removing physical disks and modifying auto claim.|
   |`esxcli vsan cluster`| commands to leave/join VSAN clusters on the local host.|
   |`esxcli esxcli`| That's right! The esxcli command has a namespace called esxcli. By using the esxcli namespace, you are able to get further information on any or all the commands that lie within the esxcli utility.|
   |`esxcli esxcli command list`| list out every esxcli command on the system along with the functions it provides.|

### References:

["Top 25 VMware ESXi commands"](http://searchservervirtualization.techtarget.com/tip/The-top-25-ESX-commands-and-ESXi-commands)