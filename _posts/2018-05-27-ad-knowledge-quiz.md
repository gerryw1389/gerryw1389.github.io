---
title: AD Knowledge Quiz
date: 2018-05-27T04:09:11+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/05/ad-knowledge-quiz/
tags:
  - SysAdmin
---
<!--more-->

  
This is part of a three part series:  
[General Knowledge Quiz](https://automationadmin.com/2018/05/general-knowledge-quiz/)  
[Network Knowledge Quiz](https://automationadmin.com/2018/05/network-knowledge-quiz/)  
AD Knowledge Quiz

Active Directory and Domain

**What is Item Level Targeting?  
** Create a GPO, in the common tab, choose item level targeting and create a group of users.

**What is loopback processing?  
** Loopback processing => This policy directs the system to apply the set of GPOs for the computer to any user who logs on to a computer affected by this policy.
   - [Loopback processing of Group Policy](https://support.microsoft.com/en-us/help/231287/loopback-processing-of-group-policy)   
   - [User Group Policy loopback processing mode](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc978513(v=technet.10))  

1. Link the required user policy to computer OU  
2. Decide the computer policy object to use  
3. Configure GPO loopback processing  
The setting is located on Computer Configuration > Policies > Administrative Templates > System > Group Policy > Configure user Group Policy loopback processing mode.  
Double click the setting. Set it as Enabled then select the mode from the dropdown menu.

As mentioned in the opening, there are two modes for loopback processing:  
Replace: When selected, user policies linked to computer OU will override the other user policies that linked to the user OU.  
Merge: When selected, user policies linked to computer OU will be applied along with the other user policies that linked to the user OU. If any conflicting setting between policies, GPO will process them normally based on the link order.  
Based on the requirement in this scenario, the best suitable mode is Replace because "Dev User Policy" must be applied instead of the other policies that applied normally via the user OU.  
When loopback processing has been enabled, those user policies should be replaced by the "Dev User Policy" that is linked to the computer OU. Like a normal GPO, loopback processing should be applied once the policy refreshed, or we can force it by using command `gpupdate /force`

**What is the difference between Enterprise Admins and Domain Admins?**

Enterprise Admins (only appears in the forest root domain)

Description:  
Members of this group have full control of all domains in the forest. By default, this group is a member of the Administrators group on all domain controllers in the forest. By default, the Administrator account is a member of this group. Because this group has full control of the forest, add users with caution.

Default user rights:

Access this computer from the network; Adjust memory quotas for a process; Back up files and directories; Bypass traverse checking; Change the system time; Create a pagefile; Debug programs; Enable computer and user accounts to be trusted for delegation; Force shutdown from a remote system; Increase scheduling priority; Load and unload device drivers; Allow log on locally; Manage auditing and security log; Modify firmware environment values; Profile single process; Profile system performance; Remove computer from docking station; Restore files and directories; Shut down the system; Take ownership of files or other objects.

Enterprise Administration:

Administering the AD Schema (Schema Admins is technically the only thing required&#8230;)  
Creating Certificate Authority (Root and Issuing)  
Managing Certificate Templates (Default or otherwise)  
DHCP Authorization  
Forest trust relationships  
Forest Preparation and Functional Level management  
Global Sites and Services Management and administration (for all domains)  
Creation of Sites & Site-Links  
Creation of IP Subnets  
Terminal Services Licensing  
Creation and Destruction of Domains  
FSMO Role Seizure (Domain Naming, Schema)  
[Schema only needs schema admins&#8230;]  
Global Domain Controller Replication Management  
Global Domain Management  
Global Group Policy Management  
Global Administrative Control for All Domain users and computers  
Take ownership of all forest and domain resources

Domain Admins

Description:  
Members of this group have full control of the domain. By default, this group is a member of the Administrators group on all domain controllers, all domain workstations, and all domain member servers at the time they are joined to the domain. By default, the Administrator account is a member of this group. Because the group has full control in the domain, add users with caution.

Default user rights:  
Access this computer from the network; Adjust memory quotas for a process; Back up files and directories; Bypass traverse checking; Change the system time; Create a pagefile; Debug programs; Enable computer and user accounts to be trusted for delegation; Force a shutdown from a remote system; Increase scheduling priority; Load and unload device drivers; Allow log on locally; Manage auditing and security log; Modify firmware environment values; Profile single process; Profile system performance; Remove computer from docking station; Restore files and directories; Shut down the system; Take ownership of files or other objects.

Domain Administration

\*\*CAUTION\*\* => By default, Domain Admins in the Root Domain can make themselves Enterprise Admins  
Domain / DC Group Policy Management  
Domain user and computer administration  
Delegation of rights within Domain  
FSMO Role Seizure (RID, PDC, Infrastructure)  
Domain Controller Installation (DCPROMO)  
Domain Controller Recovery (DRM)  
Domain Controller Replication Management  
Sites and Services Management for Domain level Controllers (Replication & Global Catalog)  
Enterprise Domain Services (SCOM, SCCM) (System Container Modification)  
Creation of Organizational Units and other AD objects in Domain  
Domain Preparation and Function Level Management  
Creation of domain level DFS Namespaces

**What is LDAP? Why it is used.**  
LDAP is the Lightweight Directory Access Protocol. Its an active directory protocal ,Basically, it's a protocol used to access data from a database. LDAP is an internet standard protocol that runs over TCP/IP.

**What is Active Directory? Why it used.**  
Active Directory is a Directory Service created by Microsoft. It is included with most Windows Server operating systems. Active Directory is primarily used to store directory objects like users and groups and computers printers. Using Active Directory brings a number of advantages to your network:  
Centralized user account management  
Centralized policy management (group policy)  
Better security management

**What is an Active Directory?**  
It is a database (Active Directory is a special-purpose database)

**What is an object**  
An object is an instance of storage of a class, user is an object, computer account is also an object etc.

**What is an attribute?**  
Property of an Object called an attribute, think of user object, and think of all available attributes associating with user object, name, last name, logon name etc.

**What is the name of Active Directory Database, when you install Domain Controller, by default directory database gets created?**  
Active Directory database is. DIT database, it is NTDS.dit

**NTDS.DIT Database is partitioned database, what are the partitions on it?**  
1. Domain  
2. Configuration  
3. Schema  
4. Application (if created)

**In Which partition Exchange Server information is kept (tricky question)**  
All of the partitions.  
1. Domain  
2. Configuration  
3. Schema

**Considering single Forest with 12 domains, how many FSMO role in total exist?**  
Total FSMO roles in this scenario = 38  
12 X 3 = 36 (PDC, RID, Infrastructure) Master  
2 For each Forest (Domain Naming Master and Schema Master per Forest)  
Total = 38

**What is FSMO?**  
Flexible Single Master Operations

**What is the least important FSMO role, considering day to day operations which one of FSMO role absence would be least significant impact and Why?**  
Perhaps Schema Master if you assume you don't extend your schema every day or RID master

**What is the most important FSMO role, considering day to day operations which one of FSMO role absence would be most significant impact and why?**  
PDC Emulator (explain why)

**What is the difference in between seizing and moving FSMO roles?**  
Peaceful operation versus forcing it. Seizing is the operation when FSMO role owner is no longer accessible and after seizing FSMO roles, you cannot bring the previous FSMO role owner back to network.

**What is KCC and what does it do?**  
Knowledge Consistence Checker, it builds replication connections in between domain controllers

**What is LSAS**  
Lsass.exe (Local Security Authority Subsystem Service) is the process which, on an Active Directory domain controller, is responsible for providing Active Directory database lookups, authentication,  
and replication

**What kind of replication Active Directory uses? is it pull or push?**  
Active Directory uses pull replication. In pull replication, a destination replica requests information from a source replica. The request specifies the information that the destination needs, based on its knowledge of changes already received from the source and from all other domain controllers in the domain. When the destination receives information from the source, it applies that information, bringing itself more up-to-date. The destination's next request to the source excludes the information that has already been received and applied.

The alternative is push replication. In push replication, a source sends information to a destination unsolicited, in an attempt to bring the destination more up-to-date. Push replication is problematical because it is difficult for the source to know what information the destination needs. Perhaps the destination has received the same information from another source. If a source sends information to a destination, there is no guarantee that the destination is going to apply it; if the source assumes otherwise, the system is unreliable.

**Define DSRM Mode?**  
Directory Services Restore Mode (DSRM) is a special boot mode for repairing or recovering Active Directory. It is used to log on to the computer when Active Directory has failed or needs to be restored.  
To manually boot in Directory Services Restore Mode, press the `F8` key repeatedly. Do this immediately after BIOS POST screen, before the Windows logo appears. (Timing can be tricky; if the Windows logo appears you waited too long.) A text menu menu will appear. Use the up/down arrow keys to select Directory Services Restore Mode or DS Restore Mode. Then press the Enter key.

**Where is the AD database held? What other folders are related to AD?**  
The AD data base is stored in c:\windows\ntds\NTDS.DIT.

**Have you ever Installed AD?**  
To Install Microsoft Active Directory:  
Ensure that you log on to the computer with an administrator account to perform installation.  
Click electing Start > Administration Tools > Server manager > Configure your Server.  
In the Welcome page, click Next.  
In the Operating system compatibility panel, click Next.  
On the Domain Controller Type panel, select Domain controller for a new domain and click Next.  
On the Create New Domain panel, select Domain in a new forest and click Next.  
On the New Domain Name panel, enter the DNS suffix for your new Active Directory. This name will be used during Tivoli Provisioning Manager installation, so make a note of it. Click Next.  
On the NetBIOS Domain Name panel, enter the NetBIOS name of the domain. The first part of the DNS name is usually sufficient. Click Next.  
On the Database and Logs panel, select the desired folders for the Database and Logs. C:\Windows\NTDS is the default. Click Next.  
On the Shared System Volume panel, enter a valid directory for the system volume. C:\Windows\Sysvol is the default. Click Next to continue.  
If you configured DNS successfully, the Permissions setting panel is displayed. Select Permissions compatible only with Windows 2000 or Windows Server 2003. Click Next.  
On the Directory Services Restore Mode Administrator Password panel, enter a valid password to be used when running the Directory Services in Restore Mode. Click Next  
Verify the settings and Click Next to begin the Active Directory configuration. The server will be rebooted as part of the process.

**What is the use of SYSVOL folder**  
All active directory data base security related information store in SYSVOL folder and it's only created on NTFS partition. SYSVOL is a folder that exists on all domain controllers. It is the repository for all of the active directory files. It stores all the important elements of the Active Directory group policy. The File Replication Service or FRS allows the replication of the SYSVOL folder among domain controllers. Logon scripts and policies are delivered to each domain user via SYSVOL. SYSVOL stores all of the security related information of the AD.

**What is global catalog**  
The Global Catalog is a database that contains all of the information pertaining to objects within all domains in the Active Directory environment

**What is Active Directory Schema?**  
Schema is an active directory component describes all the attributes and objects that the directory service uses to store data.

**What is PDC emulator and how would one know whether PDC emulator is working or not?**  
PDC Emulators: There is one PDC emulator per domain, and when there is a failed authentication attempt, it is forwarded to PDC emulator. It acts as a "tie-breaker" and it controls the time sync across the domain. These are the parameters through which we can know whether PDC emulator is working or not.  
• Time is not syncing  
• User's accounts are not locked out  
• Windows NT BDCs are not getting updates  
• If pre-windows 2000 computers are unable to change their passwords.

**What is RID Master?**  
RID master stands for Relative Identifier for assigning unique IDs to the object created in AD.

**What is Infrastructure Master?**  
Infrastructure Master is accountable for updating information about the user and group and global catalogue.

**What are the five Flexable Single Master Operation Roles (FSMO)**  
The 5 FSMO server roles:  
Schema Master Forest Level One per forest  
Domain Naming Master Forest Level One per forest  
PDC Emulator Domain Level One per domain  
RID Master Domain Level One per domain  
Infrastructure Master Domain Level One per domain  
Schema Master and Domain Naming Master are forest wide role and only available one on each Forest, Other roles are Domain wide and one for each Domain AD replication is multi master replication and change can be done in any Domain Controller and will get replicated to others Domain Controllers, except above file roles, this will be flexible single master operations (FSMO), these changes only be done on dedicated Domain Controller so it's single master replication.

**Which FSMO role is the most important? And why?**  
Interesting question which role is most important out of 5 FSMO roles or if one role fails that will impact the end-user immediately Most amateur administrators pick the Schema master role, not sure why maybe they though Schema is very critical to run the Active Directory . Correct answer is PDC, now the next question why? Will explain role by role what happens when a FSMO role holder fails to find the answer.

> Schema Master – Schema Master needed to update the Schema, we don't update the schema daily right, when will update the Schema? While the time of operating system migration, installing new Exchange version and any other application which requires extending the schema So if are Schema Master Server is not available, we can't able to update the schema and no way this will going to affect the Active Directory operation and the end-user  
> Schema Master needs to be online and ready to make a schema change, we can plan and have more time to bring back the Schema Master Server
> 
> Domain Naming Master – Domain Naming Master required to creating a new Domain and creating an application partition, Like Schema Master we don't create Domain and application partition frequently. So if are Domain Naming Master Server is not available, we can't able to create a new Domain and application partition, it may not affect the user, user event didn't aware Domain Naming Master Server is down
> 
> Infrastructure Master – Infrastructure Master updates the cross domain updates, what really updates between Domains? Whenever user login to Domain the TGT has been created with the list of access user got through group membership (user group membership details) it also contain the user membership details from trusted domain, Infrastructure Master keep this information up-to-date, it update reference information every 2 days by comparing its data with the Global Catalog (that's why we don't keep Infrastructure Master and GC in same server) In a single Domain and single Forest environment there is no impact if the Infrastructure Master server is down. In a Multi Domain and Forest environment, there will be impact and we have enough time to fix the issue before it affect the end-user.
> 
> RID Master– Every DC is initially issued 500 RID's from RID Master Server. RID's are used to create a new object on Active Directory, all new objects are created with Security ID (SID) and RID is the last part of a SID. The RID uniquely identifies a security principal relative to the local or domain security authority that issued the SID When it gets down to 250 (50%) it requests a second pool of RID's from the RID master. If RID Master Server is not available the RID pools unable to be issued to DC's and DC's are only able to create a new object depends on the available RID's, every DC has anywhere between 250 and 750 RIDs available, so no immediate impact
> 
> PDC – PDC required for Time sync, user login, password changes and Trust, now you know why the PDC is important FSMO role holder to get back online, PDC role will impact the end-user immediately and we need to recover ASAP The PDC emulator Primary Domain Controller for backwards compatibility and it's responsible for time synchronizing within a domain, also the password master. Any password change is replicated to the PDC emulator ASAP. If a logon request fails due to a bad password the logon request is passed to the PDC emulator to check the password before rejecting the login request.

**Where is the AD database held and how would you create a backup of the database?**  
The database is stored within the windows NTDS directory. You could create a backup of the database by creating a backup of the System State data using the default NTBACKUP tool provided by windows or by Symantec's Netbackup. The System State Backup will create a backup of the local registry, the Boot files, the COM+, the NTDS.DIT file as well as the SYSVOL folder.

**What are the components of AD?**  
• Logical Structure: Trees, Forest, Domains and OU  
• Physical Structures: Domain controller and Sites

**Briefly explain how Active Directory authentication works**  
When a user logs into the network, the user provides a username and password. The computer sends this username and password to the KDC which contains the master list of unique long term keys for each user. The KDC creates a session key and a ticket granting ticket. This data is sent to the user's computer. The user's computer runs the data through a one-way hashing function that converts the data into the user's master key, which in turn enables the computer to communicate with the KDC, to access the resources of the domain.  
or:  
When a user enters a user name and password, the computer sends the user name to the Key Distribution Centre (KDC). The KDC contains a master database of unique long term keys for every principal in its realm. The KDC looks up the user's master key (KA), which is based on the user's password. The KDC then creates two items: a session key (SA) to share with the user and a Ticket-Granting Ticket (TGT). The TGT includes a second copy of the SA, the user name, and an expiration time. The KDC encrypts this ticket by using its own master key (KKDC), which only the KDC knows. The client computer receives the information from the KDC and runs the user's password through a one-way hashing function, which converts the password into the user's KA. The client computer now has a session key and a TGT so that it can securely communicate with the KDC. The client is now authenticated to the domain and is ready to access other resources in the domain by using the Kerberos protocol.

**Mention what is the difference between domain admin groups and enterprise admins group in AD?**  
Enterprise Admin Group  
• Members of this group have complete control of all domains in the forest.  
• By default, this group belongs to the administrators group on all domain controllers in the forest.  
• As such this group has full control of the forest, add users with caution.  
Domain Admin Group  
• Members of this group have complete control of the domain  
• By default, this group is a member of the administrators group on all domain controllers, workstations and member servers at the time they are linked to the domain.  
• As such the group has full control in the domain, add users with caution.

**What is Kerberos?**  
Kerberos is an authentication protocol for network. It is built to offer strong authentication for server/client applications by using secret-key cryptography.

**What is FSMO?**  
Flexible single master operation is a specialized domain controller (DC) set of tasks, used where standard data transfer and update methods are inadequate. AD normally relies on multiple peer DCs, each with a copy of the AD database, being synchronized by multi-master replication.

**What is Active Directory Partitions?**  
Active Directory partition is how and where the AD information logically stored.

**What are all the Active Directory Partitions?**  
• Schema  
• Configuration  
• Domain  
• Application partition

**What is KCC?**  
KCC (knowledge consistency checker) is used to generate replication topology for inter site replication and for intra-site replication. Within a site replication traffic is done via remote procedure calls over ip, while between sites it is done through either RPC or SMTP.

**Explain what intrasite and intersite replication is and how KCC facilitates replication**  
The replication of DC's inside a single site is called intrasite replication whilst the replication of DC's on different sites is called Intersite replication. Intrasite replication occurs frequently while Intersite replication occurs mainly to ensure network bandwidth.  
KCC is an acronym for the Knowledge Consistency Checker. The KCC is a process that runs on all of the Domain Controllers. The KCC allows for the replication topology of site replication within sites and between sites. Between sites, replication is done through SMTP or RPC whilst Intersite replication is done using procedure calls over IP.

**Why do we need Netlogon?**  
Maintains a secure channel between this computer and the domain controller for authenticating users and services. If this service is stopped, the computer may not authenticate users and services, and the domain controller cannot register DNS records.

**Explain about Trust in AD ?**  
To allow users in one domain to access resources in another, Active Directory uses trusts. Trusts inside a forest are automatically created when domains are created. The forest sets the default boundaries of trust, not the domain, and implicit, transitive trust is automatic for all domains within a forest. As well as two-way transitive trust, AD trusts can be a shortcut (joins two domains in different trees, transitive, one- or two-way), forest (transitive, one- or two-way), realm (transitive or nontransitive, one- or two-way), or external (nontransitive, one- or two-way) in order to connect to other forests or non-AD domains.

**Different modes of AD restore ?**  
A nonauthoritative restore is the default method for restoring Active Directory. To perform a nonauthoritative restore, you must be able to start the domain controller in Directory Services Restore Mode. After you restore the domain controller from backup, replication partners use the standard replication protocols to update Active Directory and associated information on the restored domain controller.  
An authoritative restore brings a domain or a container back to the state it was in at the time of backup and overwrites all changes made since the backup. If you do not want to replicate the changes that have been made subsequent to the last backup operation, you must perform an authoritative restore. In this one needs to stop the inbound replication first before performing the An authoritative restore.

**What is Global Catalog and its function?**  
The global catalog is a distributed data repository that contains a searchable, partial representation of every object in every domain in a multidomain Active Directory Domain Services (AD DS) forest. The global catalog is stored on domain controllers that have been designated as global catalog servers and is distributed through multimaster replication. Searches that are directed to the global catalog are faster because they do not involve referrals to different domain controllers.  
The global catalog provides the ability to locate objects from any domain without having to know the domain name. A global catalog server is a domain controller that, in addition to its full, writable domain directory partition replica, also stores a partial, read-only replica of all other domain directory partitions in the forest.  
Forest-wide searches. The global catalog provides a resource for searching an AD DS forest. Forest-wide searches are identified by the LDAP port that they use. If the search query uses port 3268, the query is sent to a global catalog server.User logon. In a forest that has more than one domain, two conditions require the global catalog during user authentication: Universal Group Membership Caching: In a forest that has more than one domain, in sites that have domain users but no global catalog server, Universal Group Membership Caching can be used to enable caching of logon credentials so that the global catalog does not have to be contacted for subsequent user logons. This feature eliminates the need to retrieve universal group memberships across a WAN link from a global catalog server in a different site.  
• In a domain that operates at the Windows 2000 native domain functional level or higher, domain controllers must request universal group membership enumeration from a global catalog server.  
• When a user principal name (UPN) is used at logon and the forest has more than one domain, a global catalog server is required to resolve the name.  
Exchange Address Book lookups. Servers running Microsoft Exchange Server rely on access to the global catalog for address information. Users use global catalog servers to access the global address list (GAL).

**What is RODC? Why do we configure RODC?**  
Read only domain controller (RODC) is a feature of Windows Server 2008 Operating System. RODC is a read only copy of Active Directory database and it can be deployed in a remote branch office where physical security cannot be guaranteed. RODC provides more improved security and faster log on time for the branch office.  
46. What is role seizure? Who do we perform role seizure?  
Role seizure is the action of assigning an operations master role to a new domain controller without the support of the existing role holder (generally because it is offline due to a hardware failure). During role seizure, a new domain controller assumes the operations master role without communicating with the existing role holder. Role seizure can be done using repadmin.exe and Ntdsutil.exe commands.

**What do you understand by Garbage Collection? Explain.**  
Garbage collection is a process of Active Directory. This process starts by removing the remains of previously deleted objects from the database. These objects are known as tombstones. Then, the garbage collection process deletes unnecessary log files. And the process starts a defragmentation thread to claim additional free space. The garbage collection process is running on all the domain controllers in an interval of 12 hours.

### GPO / OU

**What is the difference between local, global and universal groups**  
Domain local groups assign access permissions to global domain groups for local domain resources. Global groups provide access to resources in other trusted domains. Universal groups grant access to resoures in all trusted domains.  
Domain Local Group: Use this scope to grant permissions to domain resources that are located in the same domain in which you created the domain local group. Domain local groups can exist in all mixed, native and interim functional level of domains and forests. Domain local group memberships are not limited as you can add members as user accounts, universal and global groups from any domain. Just to remember, nesting cannot be done in domain local group. A domain local group will not be a member of another Domain Local or any other groups in the same domain.  
Global Group: Users with similar function can be grouped under global scope and can be given permission to access a resource (like a printer or shared folder and files) available in local or another domain in same forest. To say in simple words, Global groups can be use to grant permissions to gain access to resources which are located in any domain but in a single forest as their memberships are limited. User accounts and global groups can be added only from the domain in which global group is created. Nesting is possible in Global groups within other groups as you can add a global group into another global group from any domain. Finally to provide permission to domain specific resources (like printers and published folder), they can be members of a Domain Local group. Global groups exist in all mixed, native and interim functional level of domains and forests.  
Universal Group Scope: These groups are precisely used for email distribution and can be granted access to resources in all trusted domain as these groups can only be used as a security principal (security group type) in a windows 2000 native or windows server 2003 domain functional level domain. Universal group memberships are not limited like global groups. All domain user accounts and groups can be a member of universal group. Universal groups can be nested under a global or Domain Local group in any domain.

**What is group nesting.**  
Adding one group as a member of another group is called 'group nesting'. This will help for easy administration and reduced replication traffic

**What is Domain controller?**  
A domain controller (DC) is a server that handles all the security requests from other computers and servers within the Windows Server domain

**What is domain?**  
A domain is a set of network resources (applications, printers, and so forth) for a group of users. The user needs only to log in to the domain to gain access to the resources, which may be located on a number of different servers in the network.

**What is Forest?**  
A collection of one or more Active Directory domains that share a common schema, configuration, and global catalog.

**What is global catalog.**  
The Active Directory Global Catalog is the central storage of information about objects in an Active Directory forest. A Global Catalog is created automatically on the first domain controller in the first domain in the forest. The Domain Controller which is hosting the Global Catalog is known as a Global catalog server.

**What is tree.**  
An Active Directory tree is a collection of Active Directory domains that begins at a single root and branches out into peripheral, child domains. Domains in an Active Directory tree share the same namespace. An Active Directory forest is a collection of Active Directory trees, similar to a real world forest. Catalog Server.

**What is site.**  
A Site object in Active Directory represents a geographic location that hosts networks.

**What Is Group Policy.**  
Group Policy is a feature of the Microsoft Windows NT family of operating systems that control the working environment of user accounts and computer accounts. Group Policy provides the centralized management and configuration of operating systems, applications, and users' settings in an Active Directory environment.

**What is the order in which GPOs are applied? LSDOU**  
Local Group Policy object  
Site  
Domain and  
Organizational Units.

**What is the difference between software publishing and assigning.**  
Assign Users : The software application is advertised when the user logs on. It is installed when the user clicks on the software application icon via the start menu, or accesses a file that has been associated with the software application.  
Assign Computers :The software application is advertised and installed when it is safe to do so, such as when the computer is next restarted.  
Publish to users : The software application does not appear on the start menu or desktop. This means the user may not know that the software is available. The software application is made available via the Add/Remove Programs option in control panel, or by clicking on a file that has been associated with the application. Published applications do not reinstall themselves in the event of accidental deletion, and it is not possible to publish to computers.

**Can I deploy non-MSI software with GPO.**  
Yes, create the fiile in .zap extension.

**Name a few benefits of using GPMC.**  
Easy administration of all GPOs across the entire Active Directory Forest  
View of all GPOs in one single list  
Backup and restore of GPOs Migration of GPOs across different domains and forest.

**How frequently is the client policy refreshed ?**  
90 minutes give or take.

**Where are group policies stored ?**  
C:\Windows\System32\GroupPolicy.

**Group policy backup**  
To backup a single GPO, right-click the GPO, and then click Back Up.  
To backup all GPOs in the domain, right-click Group Policy Objects and click Back Up All.

**What are three primary functions of Organizational Units?**  
Organize Data, Deploy GPO, Delegate permissions (We use AD Groups to assign permissions to not get confused and be precise with your answer)

**If you have one OU and you have mixed server in it (Windows 2008 and Windows 2012 servers) How do, I apply GPO to only Windows 2012 Servers. Assuming I cannot create any new OU.**  
Use WMI filtering and only target specific Windows Server version

**What are lingering objects?**  
Lingering objects can exists if a domain controller does not replicate for an interval of time that is longer than the tombstone lifetime (TSL).

**What is TOMBSTONE lifetime?**  
Tombstone lifetime in an Active Directory determines how long a deleted object is retained in Active Directory. The deleted objects in Active Directory is stored in a special object referred as TOMBSTONE. Usually, windows will use a 60- day tombstone lifetime if time is not set in the forest configuration.

**What is OU ?**  
Organization Unit is a container object in which you can keep objects such as user accounts, groups, computer, printer . applications and other (OU). In organization unit you can assign specific permission to the user's. organization unit can also be used to create departmental limitation.

### AD Tools

**What tool would you use to edit AD?**  
`Adsiedit.msc` is a low level editing tool for Active Directory. `Adsiedit.msc` is a Microsoft Management Console snap-in with a graphical user interface that allows administrators to accomplish simple tasks like adding, editing and deleting objects with a directory service. The `Adsiedit.msc` uses Application Programming Interfaces to access the Active Directory. Since `Adsiedit.msc` is a Microsoft Management Console snap-in, it requires access MMC and a connection to an Active Directory environment to function correctly.

**If you have lost one of the domain controllers how do you clean up Active Directory database for the lost DC?**  
Meta Data Cleanup with Ntdsutil.exe is a command-line tool

**What is REPLMON?**  
This GUI tool enables administrators to view the low-level status of Active Directory replication, force synchronization between domain controllers, view the topology in a graphical format, and monitor the status and performance of domain controller replication.

**What is NETDOM ?**  
NETDOM is a command-line tool that allows management of Windows domains and trust relationships. It is used for batch management of trusts, joining computers to domains, verifying trusts, and secure channels.

**What tool can interact with (. DIT) database (the most common)**  
`adsiedit.msc`

**Tell me few uses of NTDSUTIL commands?**  
We can use ntdsutil commands to perform database maintenance of AD DS, manage and control single master operations, Active Directory Backup restoration and remove metadata left behind by domain controllers that were removed from the network without being properly uninstalled.

**How would you manage trust relationships from the command prompt?**  
Netdom.exe is another program within Active Directory that allows administrators to manage the Active Directory. Netdom.exe is a command line application that allows administrators to manage trust relationship within Active Directory from the command prompt. Netdom.exe allows for batch management of trusts. It allows administrators to join computers to domains. The application also allows administrators to verify trusts and secure Active Directory channels.