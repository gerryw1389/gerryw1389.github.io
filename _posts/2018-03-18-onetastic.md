---
title: Onetastic
date: 2018-03-18T14:44:21+00:00
author: gerryw1389
layout: single
classes: wide
permalink: /2018/03/onetastic/
categories:
  - LocalSoftware
tags:
  - Tweaks
  - NoteTaking
---
<!--more-->

### Description:

[Onetastic](https://getonetastic.com/) is an extension system for OneNote that I use quite often. Follow this guide for a couple things to do with it:

### To Resolve:

1. Download my zip folder [here](https://github.com/gerryw1389/powershell/blob/main/Other/misc/onetastic.zip).

2. Install the latest version of Onetastic

3. Open OneNote and click on Home tab => Macros => New Macro => Paste in the text documents into the Edit XML button on the bottom. It will name it automatically. Do this for each one.

   - If you wish to edit the Macros, the main things to change are:
   - If it starts with `color` => Go to line 10 and change the Hex code to whatever color you want the sections to be. Go to line 46 and do the same thing. Keep in mind this one changes all open sections (haven't tried with multiple notebooks), and changes the actual Notebook icon color.
   - If it starts with `theme` => Go to line 3 and change the Hex code to whatever color you want the backgrounds to be. Go to line 29 to change the text color. This one only changes all the notes in the current section.
   - I found this [ColorPicker](https://imagecolorpicker.com/) site to be super helpful. What you do is take a screenshot and upload it to the site. It will then give you the Hex Code for the color you can use. Keep in mind that most themes have a dark and a light version of the theme for contrast. Example, if you use &#8220;dark grey&#8221; office it uses `#444444` for dark and `#B2B2B2` for light.
   - For dark themes I use [Obsidian](http://www.eclipsecolorthemes.org/?view=theme&id=21) text font `#E0E2E4` and for light themes I just use `black`.

4. Click on whichever Macro to run it.

   - For example, to set the Obsidian Theme I would:
   - Click Color => AllSectionsObsidian. This will set the section colors to Obsidian as well as your Notebook icon.
   - Click Background => CurrentSectionObsidian. This will set all the pages in the current section to Obsidian.
   - I would then create a new blank page and clear everything out. Then go to the Insert tab => Page Templates => Create a new one with your new Theme.

5. Preview:

   <img class="alignnone size-full wp-image-5249" src="https://automationadmin.com/assets/images/uploads/2018/03/onetastic.jpg" alt="" width="1555" height="739" srcset="https://automationadmin.com/assets/images/uploads/2018/03/onetastic.jpg 1555w, https://automationadmin.com/assets/images/uploads/2018/03/onetastic-300x143.jpg 300w, https://automationadmin.com/assets/images/uploads/2018/03/onetastic-768x365.jpg 768w, https://automationadmin.com/assets/images/uploads/2018/03/onetastic-1024x487.jpg 1024w" sizes="(max-width: 1555px) 100vw, 1555px" /> 

   - Enjoy! I also have a Gray theme to go along with the &#8220;Dark Gray&#8221; theme in MS OneNote.