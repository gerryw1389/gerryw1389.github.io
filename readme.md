
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
   categories:
   - WebSoftware
   tags:
   - Cloud
   - Azure-LogicApps
   ---
   <!--more-->

   ### Description:

   Text

   ### To Resolve:

   1. Text2
   ```

2. To get it to show line numbers for code blocks, inside `_config.yml` I set:

   ```escape
   # per https://github.com/jekyll/jekyll/issues/4619
   markdown: kramdown
   kramdown:
   syntax_highlighter: rouge
   syntax_highlighter_opts:
      default_lang: csharp
      css_class: 'highlight'
      span:
      line_numbers: false
      block:
      line_numbers: true
   ```

3. Add the 'Suggest An Edit' at the end of every article (thanks [https://www.brianbunke.com/](https://www.brianbunke.com/)!:

   - [Edit this file](https://github.com/gerryw1389/gerryw1389.github.io/blob/master/_layouts/single.html) (see around line 79)  
   - Also edit `config.yml` and add in `github_repository: https://github.com/gerryw1389/gerryw1389.github.io` under the 'Site Settings' section

4. Recently, I wanted to change the font to be smaller, I did this by editing `/assets/css/main.scss` and putting in:

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
         font-size: 14px; // originally 18px
      }

      @include breakpoint($large) {
         font-size: 16px; // originally 20px
      }

      @include breakpoint($x-large) {
         font-size: 18px; // originally 22px
      }
   }
   ```

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

6. For Google Adsense I pasted code into `includes/footer/custom.html` and `includes/head/custom.html` and then on `_layouts/default.html` I made sure that:
   - The line `{% include head/custom.html %}` was between the `<head>` tags
   - The line `{% include footer/custom.html %}` was between the `<footer>` tags
   - More [info on my blog](https://automationadmin.com/2019/10/google-adsense-and-disqus) if needed

7. Anything I might have missed should be [here](https://automationadmin.com/2019/08/wordpress-to-jekyll-changes/)

8. Change dates from `%B %d, %Y` to `%Y-%m-%d` by doing a find and replace. I originally added `show_date` and `date_format` per [docs](https://mmistakes.github.io/minimal-mistakes/docs/configuration/#post-dates) but I think since I'm overwriting `_layouts/single.html` that it ignores the general config.yml.

### DISCLAIMER

See [Parent Theme](https://github.com/mmistakes/minimal-mistakes) for any licenses with anything outside of `_posts`. Please see the MIT [license](./LICENSE) for licensing for my content inside `_posts`.
