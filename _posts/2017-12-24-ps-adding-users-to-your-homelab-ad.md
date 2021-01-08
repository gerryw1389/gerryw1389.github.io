---
title: 'PS: Adding Users To Your Homelab AD'
date: 2017-12-24T02:58:32+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/12/ps-adding-users-to-your-homelab-ad/
categories:
  - Windows
tags:
  - Scripting-Powershell
  - TestLab
  - ActiveDirectory
---
<!--more-->

### Description:

This is how you would go about adding AD Users to a test environment.

### To Resolve:

1. Copy and paste the following to your domain controller and run it.

```powershell
For ($I = 0; $I -Lt $Numberofusers; $I++)
        {
            $Data = Invoke-Webrequest -Uri "https://randomuser.me/api/"
            $User = $Data.Content | Convertfrom-Json
            $Email = $User.Results.Email
            $FirstName = $User.Results.Name.First
            $LastName = $User.Results.Name.Last
            $Together = ($FirstName + "." + $LastName)  
            $Upn = $Together + "@" + $Fqdn
            New-Aduser -Name $Together `
                -Accountpassword $Pass `
                -Changepasswordatlogon $False `
                -Postalcode $User.Results.Location.PostCode `
                -Country "US" `
                -State $User.Results.Location.State `
                -City $User.Results.Location.City `
                -Streetaddress $User.Results.Location.Street `
                -Givenname $FirstName `
                -Surname $LastName `
                -Displayname "$FirstName $LastName" `
                -Emailaddress $Email `
                -Enabled $True `
                -Userprincipalname $Upn `
                -Path $Ou
            Write-Output "User account created: $Together in $Ou " 
        }
    }
```

2. You would have to fill in the required variables and of course have to be able to populate using the internet (randomuser.me's website API's), so this method may not be so clean. In that case, I have another script that creates 50 users statically.

```powershell
$1 = @{ First = "Todd"; Last = "Parker" }
        $2 = @{ First = "Shawn"; Last = "Allen" }
        $3 = @{ First = "Harold"; Last = "Thomas" }
        $4 = @{ First = "Patrick"; Last = "Evans" }
        $5 = @{ First = "Tammy"; Last = "Torres" }
        $6 = @{ First = "Kevin"; Last = "Richardson" }
        $7 = @{ First = "Ruth"; Last = "Henderson" }
        $8 = @{ First = "Michelle"; Last = "Gonzales" }
        $9 = @{ First = "Bonnie"; Last = "Martin" }
        $10 = @{ First = "Harry"; Last = "Hernandez" }
        $11 = @{ First = "James"; Last = "Price" }
        $12 = @{ First = "Philip"; Last = "Stewart" }
        $13 = @{ First = "Louis"; Last = "Morris" }
        $14 = @{ First = "Eric"; Last = "Bell" }
        $15 = @{ First = "Jesse"; Last = "Jones" }
        $16 = @{ First = "Matthew"; Last = "Alexander" }
        $17 = @{ First = "Andrew"; Last = "Ward" }
        $18 = @{ First = "Donna"; Last = "Reed" }
        $19 = @{ First = "Brandon"; Last = "Martinez" }
        $20 = @{ First = "Russell"; Last = "Green" }
        $21 = @{ First = "Patricia"; Last = "Wood" }
        $22 = @{ First = "Richard"; Last = "Cook" }
        $23 = @{ First = "Henry"; Last = "Howard" }
        $24 = @{ First = "Janice"; Last = "Wilson" }
        $25 = @{ First = "Cynthia"; Last = "Williams" }
        $26 = @{ First = "Denise"; Last = "Clark" }
        $27 = @{ First = "John"; Last = "Phillips" }
        $28 = @{ First = "Willie"; Last = "Lopez" }
        $29 = @{ First = "Janet"; Last = "Edwards" }
        $30 = @{ First = "Ernest"; Last = "Barnes" }
        $31 = @{ First = "Dennis"; Last = "Young" }
        $32 = @{ First = "Sandra"; Last = "Patterson" }
        $33 = @{ First = "Carolyn"; Last = "Gray" }
        $34 = @{ First = "Elizabeth"; Last = "Cox" }
        $35 = @{ First = "Paul"; Last = "Johnson" }
        $36 = @{ First = "Randy"; Last = "Flores" }
        $37 = @{ First = "Julia"; Last = "Lee" }
        $38 = @{ First = "Lawrence"; Last = "Campbell" }
        $39 = @{ First = "Timothy"; Last = "Lewis" }
        $40 = @{ First = "Teresa"; Last = "Cooper" }
        $41 = @{ First = "Alice"; Last = "Taylor" }
        $42 = @{ First = "Douglas"; Last = "Jenkins" }
        $43 = @{ First = "Mildred"; Last = "Powell" }
        $44 = @{ First = "Mark"; Last = "Kelly" }
        $45 = @{ First = "Louise"; Last = "Watson" }
        $46 = @{ First = "Stephen"; Last = "Nelson" }
        $47 = @{ First = "Evelyn"; Last = "James" }
        $48 = @{ First = "Edward"; Last = "Rogers" }
        $49 = @{ First = "Shirley"; Last = "Bailey" }
        $50 = @{ First = "Maria"; Last = "Baker" }

        $Array = @($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25, `
                $26, $27, $28, $29, $30, $31, $32, $33, $34, $35, $36, $37, $38, $39, $40, $41, $42, $43, $44, $45, $46, $47, $48, $49, $50)

        Foreach ($Number In $Array)
        {
            $FirstName = $Number.First.Tostring()
            $LastName = $Number.Last.Tostring()
            $Together = ($FirstName + "." + $LastName)  
            $Upn = $Together + "@" + $Fqdn
            New-Aduser -Name $Together `
                -Accountpassword $Pass `
                -Changepasswordatlogon $False `
                -Givenname $FirstName `
                -Surname $LastName `
                -Displayname "$FirstName $LastName" `
                -Emailaddress $Upn `
                -Enabled $True `
                -Userprincipalname $Upn `
                -Path $Ou
            Write-Output "AD User Created: $Together"  
        }
```

3. Source is maintained under [gwActiveDirectory](https://github.com/gerryw1389/powershell/tree/main/gwActiveDirectory/Public)