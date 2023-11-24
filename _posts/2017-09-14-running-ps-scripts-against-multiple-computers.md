---
title: Running PS Scripts Against Multiple Computers
date: 2017-09-14T23:55:36+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2017/09/running-ps-scripts-against-multiple-computers/
tags:
  - Windows
  - SysAdmin
tags:
  - Scripting-Powershell
  - Powershell-Designing
---
<!--more-->

### Description:

In this post I will show you a way to run a test script against multiple machines. I would have a look at [Setting up PS Remoting](https://automationadmin.com/2016/05/setting-up-ps-remoting/), [PS Remoting GPO](https://automationadmin.com/2016/05/gpo-enable-psremoting/) for setting up the environment to ensure PS Remoting is Enabled.

### To Resolve:

1. On your machine, navigate to `c:\scripts` so we can create four files, three of which you can use against multiple scripts. Make sure that NTFS permissions are strict to this directory as we will be using a password file to store your credentials so that scripts can run if you are away from your computer.

   - Should look like:

   - `C:\scripts\create-file.ps1` => copy the following and save:

   ```powershell
   New-Item -Itemtype Dir -Path C:\Scripts2
   New-Item -Itemtype File -Path C:\Scripts2\Test.Txt
   ```

   - `C:\scripts\computers.txt` => just choose two remote machines on your network and enter them one line a piece:

   - This assumes domain environment where you have admin access to the remote machines. All machines must have also ran the command `Enable-PSRemoting -Force` at sometime prior. All machines must have Network Discovery enabled as well.

   ```powershell
   pc01
   pc02
   ```

   - `C:\scripts\aes.key` => To create, we need to open PS as admin and type:

   ```powershell
   $KeyFile = "C:\Scripts\aes.key"
   $Key = New-Object Byte[] 32
   [Security.Cryptography.RNGCryptoServiceProvider]::Create().GetBytes($Key)
   $Key | Out-File $KeyFile
   ```

   - `C:\scripts\aespassword.txt` => To create, we need to open PS as admin and type:

   ```powershell
   $PasswordFile = "C:\Scripts\aespassword.txt"
   $KeyFile = "C:\Scripts\aes.key"
   $Key = Get-Content $KeyFile
   # NOTE: Replace #Password1 with your admin password
   $Password = "#Password1" | ConvertTo-SecureString -AsPlainText -Force
   $Password | ConvertFrom-SecureString -key $Key | Out-File $PasswordFile
   ```

2. Now that those four files are created, we will create a script that will run the powershell script (`c:\scripts\create-file.ps1`) against the two remote machines (`c:\scripts\computers.txt`). So create a new file called  `c:\scripts\test-remote.ps1`. At the beginning of the script we will place a code block that pulls in our admin credentials (from `aespassword.txt` and `aes.key`) so we can run as a scheduled task if needed. Contents of `c:\scripts\test-remote.ps1`:

   ```powershell
   $User = "domain.com\administrator"
   $PasswordFile = "C:\Scripts\aespassword.txt"
   $KeyFile = "C:\Scripts\aes.key"
   $Key = Get-Content $KeyFile
   $Creds = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, (Get-Content $PasswordFile | ConvertTo-SecureString -Key $Key)
   $Computers = Get-Content C:\scripts\computers.txt
   ForEach ($Computer in $Computers)
   {
   Try
   {
   Invoke-Command -FilePath "c:\scripts\create-file.ps1" -ComputerName $Computer -Credential $Creds
   }
   Catch
   {
   Add-Content c:\scripts\Unavailable-Computers.txt $Computer
   }
   }
   ```

3. Now in Windows file explorer, click File => Open Windows Powershell => Open Windows Powershell as administrator. Now just type: `.\test.remote.ps1`

4. The script has now been ran against our two remote computers. Go ahead and check them out! Open file explorer on the remote computers and see if `c:\scripts2` exists along with its `test.txt` file. This is all it takes to run scripts against multiple machines. You could modify this and set it up on a remote share, but this is just the basics and works just fine.

5. If you want to run Powershell interactively against multiple machines, it's even easier:

   ```powershell
   Invoke-Command -ComputerName $Computers -Scriptblock { hostname }
   ```

   - I usually do this if I just need to figure out one-off's but I prefer to use scripts because each of my scripts log everything to a log file that I can then query to see the results. This works perfect for anything longer than a one liner and has the benefit that you can setup a scheduled task with a script and then run another script like this one to query the remote log file:

   ```powershell
   $User = "domain.com\administrator"
   $PasswordFile = "C:\Scripts\aespassword.txt"
   $KeyFile = "C:\Scripts\aes.key"
   $Key = Get-Content $KeyFile
   $Creds = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, (Get-Content $PasswordFile | ConvertTo-SecureString -Key $Key)
   $Computers = Get-Content C:\scripts\computers.txt
   # Create a file locally to collect the results for each of the remote computers.
   New-Item -Itemtype file -path c:\scripts\results.txt
   # Get the log that is output by each script and pump to results.
   ForEach ($Computer in $Computers)
   {
   $file = "\\$computer\c`$\scripts\create-file.log"
   $a = $computer + "`n" + "##############################";
   Add-Content -Path C:\scripts\results.txt -Value $a
   Add-Content -Path C:\scripts\results.txt -Value (Get-Content $file)
   }
   #Show the results
   $Results = Get-Content C:\scripts\results.txt
   Write-Output $Results
   ```

   - My create-file in the example above doesn't write to a log file, please see my [Template script](https://automationadmin.com/2016/11/ps-template-script/) to see what I mean about logging.

   - What this command will generate is a file on your `C:\scripts` directory called `results.txt`. Inside of it, it will have the contents of a logfile for each computer that you ran a prior script against. It breaks up each computer into it's own line so it's clear to see what log belongs to what computer.

---

So that is what I use in my environment. Scripts on the internet that I have seen usually try to incorporate a complicated Process block or try to include Credentials and stuff in their parameters which seems to work fine as well. For example:

1. Look for built in cmdlets that include the parameter `-ComputerName` (`Get-Command -ParameterName ComputerName`) and try to use those in your script.

2. Or try and use it in your own functions:

   ```powershell
   Param
   (
   [Alias("Cn", "__Server", "Pscomputername")]
   [Parameter(
   Position = 0,
   Valuefrompipeline = $True,
   Valuefrompipelinebypropertyname = $True)]
   [String[]]$Computername = $Env:Computername,

   [ValidateNotNull()]
   [System.Management.Automation.PSCredential]
   [System.Management.Automation.Credential()]
   $Creds = [System.Management.Automation.PSCredential]::Empty
   )
   ```

3. Then somewhere in your script you would try:

   ```powershell
   ForEach ($Computer in $ComputerName)
   {
   # Using Credentials
   If ($PSBoundParameters['Creds'])
   {
   Invoke-Command -ComputerName $Computer -Scriptblock { Get-Content C:\scripts\test.log } -Credential $Creds
   }
   Else
   {
   Invoke-Command -ComputerName $Computer -Scriptblock { Get-Content C:\scripts\test.log }
   }
   }
   ```

   - or something like that, check out [this](http://duffney.io/AddCredentialsToPowerShellFunctions) blog post for more things to try.
   - I used to try this when I first started scripting but I couldn't ever get it to consistently work like my method above, by all means, feel free to go that route as well.

4. Here is one way to capture verbose in remotely running scripts:

   ```powershell
   $VerbosePreference = "continue"
   Start-Transcript -path c:\temp\transcript.txt 
   Write-Verbose "here 1"
   $job = Invoke-Command $RemoteComputer -ScriptBlock {
   $ErrorActionPreference = "Stop";
      $VerbosePreference = "continue";
   Write-Verbose "there 1";
      Write-Verbose "there 2";
      Write-Verbose "there 3";
   } -AsJob 
   Wait-Job $job | Out-Null
   $VerboseMessages = $job.ChildJobs[0].verbose.readall()
   ForEach ($oneMessage In $VerboseMessages) {Write-Verbose $oneMessage}
   Write-Verbose "here 2"
   Stop-Transcript
   ```

   - Per: [Powershell - Problem with Start-transcript using remoting](https://stackoverflow.com/questions/4607417/powershell-problem-with-start-transcript-using-remoting)