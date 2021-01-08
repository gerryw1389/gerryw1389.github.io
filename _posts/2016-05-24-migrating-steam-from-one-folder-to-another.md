---
title: Migrating Steam From One Folder To Another
date: 2016-05-24T12:22:00+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/05/migrating-steam-from-one-folder-to-another/
categories:
  - Windows
tags:
  - Migration
---
<!--more-->

### Description:

Steam is an application used by PC Gamers to play games. It hosts all the application data associated with games and is usually close to 100 GB in size or larger depending on the number of games the user has installed. When migrating steam from one pc to another or one drive to another, there is a way to move them without having to re-download all the files.

### To Resolve:

1. Create a folder in the new location where you'll store your games. If you're on Steam, you'll need to do it through Steam. Head to Settings > Downloads > Steam Library Folders and click "Add Library Folder".

2. Navigate to your new Steam library folder and create a new folder within it called &#8220;steamapps&#8221;. Then, create a folder in steamapps called &#8220;common&#8221;. So the setup is: drive:\pathtosteam\steamapps\common.

3. Head to your current Steam folder and find the folder for the game you want to move. You'll likely find it in steamapps/common. Copy the game's folder, e.g. "Borderlands 2", to the new steamapps/common folder you created in step 2.

4. Open Steam, right-click on the game you're moving, and select "Delete Local Content". This will uninstall the game from its original location.

5. When that's done, click the Install button to re-install the game. In the "Choose location" dropdown, choose the Steam folder on your new hard drive.

6. Instead of re-downloading the game (which could take hours), Steam will detect the existing files there and make any necessary minor changes. When it's done, you should be able to play the game as usual.

NOTE: Follow the article for reference on how to do this for Origin as well.

### References:

["How to Move a PC Game to Another Hard Drive (Without Re-Downloading It)"](http://lifehacker.com/how-to-move-a-pc-game-to-another-hard-drive-without-re-1714706774)