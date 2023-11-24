
### AutomationAdmin.com

Migration from self-hosted Wordpress to Jeykll on Github Pages => [https://automationadmin.com](https://automationadmin.com).

Minimal Mistakes => The blog's [parent theme](https://github.com/mmistakes/minimal-mistakes)

#### Changes To Parent Theme:

1. Setup my markdown template for new posts as follows:

   ```escape
   ---
   title: New Note
   date: Ctrl + Shift + Alt + i
   author: gerryw1389
   layout: single
   classes: wide
   permalink: /copy file name WITHOUT Extension - ex: /2019/08/opendns/
   tags:
     - Azure
     - Terraform
   ---
   <!--more-->

   ### Description:

   Text

   ### To Resolve:

   1. Text2
   ```

1. To get it to show line numbers for code blocks, inside `_config.yml` I set:

   ```yaml
   markdown: kramdown
   kramdown:
   syntax_highlighter: rouge
   syntax_highlighter_opts:
      css_class: "highlight"
      span:
         line_numbers: false
      block:
         line_numbers: true
   ```

1. Recently, I wanted to change the font to be smaller, I did this by editing `/assets/css/main.scss` and putting in:

   ```escape
   --- 
   # Only the main Sass file needs front matter (the dashes are enough) 
   --- 

   @charset "utf-8";

   @import "minimal-mistakes/skins/{{ site.minimal_mistakes_skin | default: 'default' }}"; // skin
   @import "minimal-mistakes"; // main partials

   // https://github.com/mmistakes/minimal-mistakes/issues/1219#issuecomment-326809412
   html {
      font-size: 12px; // originally 16px
      @include breakpoint($medium) {
         font-size: 16px; // originally 18px
      }

      @include breakpoint($large) {
         font-size: 18px; // originally 20px
      }

      @include breakpoint($x-large) {
         font-size: 20px; // originally 22px
      }
   }
   ```

   - So font size went from `18 => 16`, `20 => 18`, and `22 => 20` for each type

5. For left sidebar options for single posts, I use the following at `_data/naviagation.yml`:

   ```escape
   categories:
   - title: Home
      children:
         - title: "<= Back To Home"
         url: https://automationadmin.com/
         - title: "Popular Posts"
         url: https://automationadmin.com/2016/02/popular-posts/
   - title: Donate
      children:
         - title: "Buy me a coffee ❤"
         url: https://www.paypal.com/paypalme2/gerryw1389
   ```

1. For Google Adsense I pasted code into `includes/head/custom.html`
   - More [info on my blog](https://automationadmin.com/2019/10/google-adsense-and-disqus) if needed
   - I recently moved from disqus to [utterances](https://mmistakes.github.io/minimal-mistakes/docs/configuration/#utterances-comments) per the Parent Theme's docs.

1. Change dates from `%B %d, %Y` to `%Y-%m-%d` by adding under `defaults:` the sub values `show_date: true` and `date_format` per [docs](https://mmistakes.github.io/minimal-mistakes/docs/configuration/#post-dates)

1. Anything I might have missed should be [here](https://automationadmin.com/2019/08/wordpress-to-jekyll-changes).

1. NOTE: I'm currently stuck on version 4.16.5 due to [an issue I discussed here](https://automationadmin.com/2023/01/unable-to-update-theme). It's probably an easy fix but I haven't figured it out yet :/

### DISCLAIMER

See [Parent Theme](https://github.com/mmistakes/minimal-mistakes) for any licenses with anything outside of `_posts`. Please see the MIT [license](./LICENSE) for licensing for my content inside `_posts`.
