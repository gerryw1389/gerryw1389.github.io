---
title: Installing Equinox GTK Engine In Fedora
date: 2016-12-24T08:17:51+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2016/12/installing-equinox-gtk-engine-in-fedora/
categories:
  - Linux
tags:
  - LinuxClient
  - Tweaks
---
<!--more-->

### Description:

This post is going to be pretty short, but this is the steps to install the GTK engine Equinox. There are plenty of others to choose from (search engine: "gtk engines github"), but I like this combination on my Fedora MATE desktop.

### To Resolve:

1. First install dev packages:

```shell
sudo yum install gtk-devel
```

2. Go to the Equinox download page [here](https://www.gnome-look.org/content/show.php/Equinox+GTK+Engine?content=121881) and download all 4 of the files.

3. In your downloads, extract the equinox installer and open a terminal:

```shell
configure --prefix=/usr --libdir=/usr/lib64 --enable-animation

# This compiles and installs the engine.
make install
```

4. Then load themes from the same link. They should show up in Customize => Appearance under the Themes.

5. Lastly, load the Faenza icons from the same link. Note that for these, once you extract the folder you have to open a terminal and type:

```shell
./install
```