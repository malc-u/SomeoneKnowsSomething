- [Manual testing](#manual-testing)
  - [Responsiveness](#responsiveness)
    - [Bugs - responsiveness](#bugs---responsiveness)
  - [Interaction](#interaction)
    - [Bugs - interaction](#bugs---interaction)
- [User stories testing](#user-stories-testing)
- [Automated testing](#automated-testing)
  - [HTML validation](#html-validation)
    - [base.html](#basehtml)
    - [footer.html](#footerhtml)
    - [navbar.html](#navbarhtml)
    - [sidebar.html](#sidebarhtml)
    - [flash-alerts.html](#flash-alertshtml)
    - [form-add.html](#form-addhtml)
    - [form-delete.html](#form-deletehtml)
    - [form-login.html](#form-loginhtml)
    - [form-password.html](#form-passwordhtml)
    - [form-register.html](#form-registerhtml)
    - [form-update.html](#form-updatehtml)
    - [account.html](#accounthtml)
    - [index.html](#indexhtml)
    - [login.html](#loginhtml)
    - [more.html](#morehtml)
    - [origin.html](#originhtml)
    - [podcast-add.html](#podcast-addhtml)
    - [podcast-delete.html](#podcast-deletehtml)
    - [podcast-update.html](#podcast-updatehtml)
    - [recommended.html](#recommendedhtml)
    - [register.html](#registerhtml)
    - [settings.html](#settingshtml)
  - [CSS Validation](#css-validation)
  - [Java Script Validation](#java-script-validation)
  - [Python Validation](#python-validation)

# Manual testing

## Responsiveness

- **Plan**: this page was planned to be responsive, working on all devices - mobile phones, tablets and desktops. Following this it was planned for Bootstrap library to be used for a page design.
- **Implementation**: page was **tested in Chrome Developer Tools** throughout the process of putting it together to make sure it was responsive to all devices. "Responsive" slider was used to make sure content is shown correctly on desktop, tablet and mobile, that they look as desired by the developer. Bootstrap classes as well as media rules were used to adjust responsiveness. **Tested the pages on all sizes/devices available in Chrome**, these were:
  
  - 360 x 640 Blackberry Z30 & Galaxy Note
  - 375 x 812 iPhone X
  - 375 x 687 iPhone 6/7/8
  - 411 x 731 Pixel 2
  - 411 x 823 Pixel 2 XL
  - 414 x 736 iPhone 6/7/8 Plus
  - 600 x 1024 Blackberry PlayBook
  - 768 x 1024 iPad
  - 1024 x 1366 iPad Pro
  
- **Result**: page is responsive and can be used on all planned devices. There are no elements on this page that are not responding as planned.
- **Conclusion**: all tests that were run on responsivenes were passed therefore page is fully responsive.

### Bugs - responsiveness

Throughout the develompment process I came across these bugs:

- **Hero image**
  - **Bug**: image was not displaying as intended
  - **Fix**: added media in CSS to contain the image within container instead of covering it
  - **Result**: this bug was removed and the picture is displayed as intended on big screens
- 

## Interaction

- **Plan**: there are elements that are planned to be interactive on this page e.g. buttons, navbar, sidebar
- **Implementation**: interaction was carried out on many devices and on several browsers, including Chrome, Firefox and Opera. Following elements were tested by making sure they act in the way they were intended, that they lead to the page or action as planned.
  - Sidebar toggle button
  - Sidebar
  - Navbar toggle button
  - Logo
  - `Navbar-brand`
  - `Login here` button on index page
  - `Read more` button on "Recommended" and "User picks" page
  - `Login to listen` on "Recommended" and "User picks" page
  - `Login to listen` on "Read more" page
  - Navbar links
  - Sidebar links
  - `Listen here` on "Australian", "British", "American", "Recommended" and "User picks" pages
  - `Cog` - password change button in Account dashboard
  - `+` - add podcast button in Account dashboard
  - `Headphones`- listen to podcast button in Account dashboard
  - `Edit` button in Account dashboard
  - `Trash` - delete podcast in Account dashboard
  - `Submit` buttons on all forms
  - Footer icons
- **Result**: all tested elements are interactive as planned . There are no elements on this page that are not responding as planned
- **Conclusion**: all tests that were run on interactivity were passed therefore page is interactive

### Bugs - interaction

Throughout the develompment process I came across two bugs related to page interaction:

- **Sidebar**
  - **Bug**: sidebar was taking too much space on mobile devices
  - **Fix**: added media to remove sidebar display on mobiles, removed sidebar toggle button and created navbar-brand in the top navbar to replace clickable logo that was leading to index page and was nested inside sidebar
  - **Result**: this bug was removed and mobile page display does not include sidebar now
- **Navbar**
  - **Bug**: navbar was not collapsing on click on mobile phones
  - **Fix**: added function in JavaScript to collaps navabr on click 
  - **Result**: this bug is now fixed and navbar works as intended
- 

# User stories testing

1. As a user I want the page to be easy to navigate.
   - this page has got conventional layout with navbar on the top and footer on the bottom
   - there is additional navigation on this page- collapsible sidebar (for tablets and desktops)
2. As a user that is accessing the page from the mobile phone only I want to be able to use it without any problems with content displayed properly.
   - this page is designed to be fully functional on all screen sizes
   - sidebar is removed from the mobile use as this would be taking too much space and would require the user to collapse it on entry
3. As a true crime podcast listener I want to be able to see content I am interested in.
   - this page is dedicated to true crime only
   - the content is related to all types of crimes: missing people, murders, fraud, con-people etc.
   - users are able to add new content that will be displayed in their country of origin tab accordingly
4. As a busy person I want to have possibility of easily navigating to the content that I can listen to on the go.
   - this page allows all users to see the details - read more - about content recommended by admin
   - this page allows all users to see details - read more - about selected content that has been indicated as favourite by the registered users
   - "Listen now" button leads registered users directly to the page when they can listen to the podcast
5. As a user I want to be able to see more details about the content.
   - all users can read more about content recommended by the admin
   - all users can read more about selected content indicated as favourite by the registered users
   - registered users can read about all content added to the page
6. As a user that is interested in this genre I want to have link directly to the podcast website.
   - "Listen now" button leads users directly to the podcast website
7. As a user that is aware I might have missed some interesting content from the past I want to have content release year displayed.
   - release year is required field when adding podcast
   - all podcast already added to the page has got and the one added in the future will be required to have release year added
8. As a British user I want to have possibility of exploring stories from other parts of the world.
   - this page contains podcast from United Kingdom, Australia and United States of America
   - the content is displayed based on the country of origin therefore it is easy for a British user to listen to American or Australian podcast - it requires registering to the page and accessing podcasts in the `Australian` or `American` tabs.
9. As a money savvy user I want to have possibility of accessing content via all means provided by the producer.
    - links to the content provided so far lead to the official podcast sites or sites where the content can be listened to for free
10. As a user that relies on recommendations I want to have possibility of finding our what other users like.
    - this page presents users with `User picks` tab that presents selected content that has been indicated by registered users as their favourite
    - `User picks` are sorted based on their release year so the newest content is displayed first
11. As a user that likes to stay up to date I want to see release year to keep on top of new content.
    - all content already added has got and all content added in the future is required to have release year included
    - release year is clearly displayed for registered users in the origin tabs
    - release year can bee seen on the read more page for unregistered users
    - additionally `Recommended` and `User picks` are displayed in such order to present the newest content first
12. As a user that doesn't like long stories and in general prefers films to TV series I want to be able to see how many episodes each podcast have.
    - all content already added has got and all content added in the future is required to have number of episodes included
    - number of episodes is clearly displayed for registered users in the origin tabs
    - number of episodes can bee seen on the read more page for unregistered users
13. As a user that likes to share my ideas I want to be able to add/update and delete content to the page for others to enjoy.
    - all registered users can add new content to the page
    - all registered users can edit content added by them
    - all registered users can delete content added by them
14. As a user that values security I want to be able to change my password as and when I want.
    - all passwords are hashed and stored in this form
    - all registered users can change password as often as they like

# Automated testing

## HTML validation

This was carried out using [W3C Markup Validation](https://validator.w3.org/).

### base.html

Validation brings up 1 error:

- Bad value `{{url_for('static', filename='css/style.css')}}` for attribute `href` on element `link`: Illegal character in path segment: { is not allowed.

This was left unfixed as advised on [Flask - The Base Layout](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/) as correct.

### footer.html

Validation brings up 1 warning:

- Consider adding a `lang` attribute to the html start tag to declare the language of this document.

Validation also brings up 2 errors:

- Non-space characters found without seeing a doctype first. Expected `<!DOCTYPE html>`
- Element `head` is missing a required instance of child element `title`

These were left unfixed as this file contains html for one block/component of an application layout that is clearly indicated in the file by syntax used `{% block footer %} {% endblock %}`.

### navbar.html

Validation brings up 1 warning that is exactly the same as in footer.html It also brings up 18 erros:

- First 2 are exactly the same as in footer.html - left unfixed as this file containes html for one block/component of an applicaton that is clearly indicated in the file by sytnax used `{% block navbar %}` and `{% endblock %}`
- 12 errors related to use of `{{ url_for }}` in all links in top navbar. All left unfixed as linked correctly as advised in [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/#)
- 2 errors informing about repeated occurence of `id="navbarDropdown"`. Left unchanged as there are 2 separate drop down multilink navigation bars used and mentioned `id` is Bootstrap class for multi-link droping down navbar items.
- 2 errors informing about not allowed text in element `ul` - these were `{% else %}` and `{% endif %}`. Left unchanged as the statments are valid [Jinja control structures](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-control-structures)

### sidebar.html

Validation brings up 1 warning and 14 errors. Warning is identical as in footer.html and navbar.html, errors are:

- First 2 are exactly the same as in footer.html and navbar.html - left unfixed as this file containes html for one block/component of an applicaton that is clearly indicated in the file by sytnax used `{% block sidebar %}` and `{% endblock %}`
- 8 errors related to use of `{{ url_for }}` in all links in the sidebar and logo. All left unfixed as linked correctly as advised in [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/#)
- 1 error related to missing alt in logo - this was fixed, alt addded
- 3 errors informing about not allowed text in element `ul` - these were `{% else %}`, `{% endif %}` and `{% if 'username' in session %}`. Left unchanged as the statments are valid [Jinja control structures](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-control-structures)

### flash-alerts.html

Validation brings 1 warning and 2 errors exactly the same as a warning and first 2 errors in previously validated pages. Action not taken as not required - reasons detailed in the previous occurences.

### form-add.html

Validation brings up 1 warning and 8 errors, first 2 being the same as in all previously validated pages. Remaining 6 errors are about stray tags `tr` & `td` - these were also left unchanged as they were used as advised for [customer rendering of fadio fields in WTForms](https://wtforms.readthedocs.io/en/2.3.x/fields/)

### form-delete.html

Validation of this file brings up 1 warning and 2 errors. They are all equivalent to the ones from footer.html and flash-alerts.html
Action not taken - resons described in previous occurences.

### form-login.html

Validation of this file brings up 1 warning and 2 errors. They are all equivalent to the ones from footer.html, flash-alerts.html and form-delete.html
Action not taken - resons described in previous occurences.

### form-password.html

Validation of this file brings up 1 warning and 2 errors. They are all equivalent to the ones from footer.html, flash-alerts.html, form-delete.html & form-login.html.
Action not taken - resons described in previous occurences.

### form-register.html

Validation of this file brings up 1 warning and 2 errors. They are all equivalent to the ones from footer.html, flash-alerts.html, form-delete.html, form-login.html & form-password.html.
Action not taken - resons described in previous occurences.

### form-update.html

Validation of this file brings up 1 warning and 8 errors. They are all equivalent to the ones from form-add.html.
Action not taken - resons described in previous occurence.

### account.html

Validation of this file brings up 1 warning and 9 errors:

- The warning and first 2 errors are equivalent to the ones from all previously validated pages except base.html.
- 1 errors regarding missing alt in `img` tag - this was fixed
- Remaining 6 errors related to use of `{{ url_for }}` and type of the field used in `href` and `src` (e.g. `{{podcast.podcast_link}}`) in all links on this page. All left unfixed as linked correctly as advised in [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/#)

### index.html

Validation of this file brings up 1 warning and 3 errors.

- The warning and first 2 errors are equivalent to the ones from all previously validated pages except base.html.
- Last error related to use of `{{ url_for }}` - left unfixed as linked correctly as advised in [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/#)

### login.html

Validation of this file brings up 1 warning and 2 errors. They are all equivalent to the ones from previous pages (except base.html)
Action not taken - resons described in previous occurences.

### more.html

Validation of read more page brings up 1 warning and 6 errors.

- Warning and first 3 errors are equivalent to the account.html page.
- Remainign 3 errors related to use of `{{ url_for }}` and type of the field used in `href` and `src` (e.g. `{{podcast.podcast_link}}`) in all links on this page. All left unfixed as linked correctly as advised in [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/#)

### origin.html

Validation of read more page brings up 1 warning and 4 errors.
They are equivalent to the warning, 2 first and 3 last errors from more.html page.
Action not taken - resons described in previous occurences.

### podcast-add.html

Validation of this file brings up 1 warning and 2 errors. They are all equivalent to the ones from previous pages (except base.html)
Action not taken - resons described in previous occurences.

### podcast-delete.html

Validation of this page beings up 1 warning and 5 errors.
They are all equivalent to the ones from origin.html page. Action not taken - described in previous occcurences (origin.html and more.html)

### podcast-update.html

Validation of this file brings up 1 warning and 2 errors. They are all equivalent to the ones from previous pages (except base.html)
Action not taken - resons described in previous occurences.

### recommended.html

Validation of this page beings up 1 warning and 7 errors.
They are all equivalent to the ones from origin.html page. Action not taken - described in previous occcurences (origin.html, more.html and podcast-delete.html)

### register.html

Validation of this page beings up 1 warning and 3 errors.
They are all equivalent to the ones from origin.html page. Action not taken - described in previous occcurences (origin.html, more.html, podcast-delete.html and recommended.html)

### settings.html

Validation of this file brings up 1 warning and 2 errors. They are all equivalent to the ones from previous pages (except base.html)
Action not taken - resons described in previous occurences.

## CSS Validation

[W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS - no errors found.

## Java Script Validation

[JS Hint](https://jshint.com/) was used to validate JavaScript - found 1 warning - missing semicolon - fixed.

## Python Validation

[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension for Visual Studio Code was used to validate Python.
