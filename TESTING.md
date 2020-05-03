# Someone Know Something TESTING

- [Someone Know Something TESTING](#someone-know-something-testing)
  - [Manual testing](#manual-testing)
  - [User stories testing](#user-stories-testing)
  - [Automated testing](#automated-testing)
    - [HTML validation](#html-validation)
      - [base.html](#basehtml)
      - [footer.html](#footerhtml)
      - [navbar.html](#navbarhtml)

## Manual testing

## User stories testing

## Automated testing

### HTML validation

This was carried out using [W3C Markup Validation ](https://validator.w3.org/).

#### base.html 

Validation brings up 1 error:

- Bad value `{{url_for('static', filename='css/style.css')}}` for attribute `href` on element `link`: Illegal character in path segment: { is not allowed.

This was left unfixed as advised on [Flask - The Base Layout](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/) as correct.

#### footer.html

Validation brings up 1 warning:

- Consider adding a `lang` attribute to the html start tag to declare the language of this document.

Validation also brings up 2 errors:

- Non-space characters found without seeing a doctype first. Expected `<!DOCTYPE html>`
- Element `head` is missing a required instance of child element `title`

These were left unfixed as this file contains html for one block/component of an application layout that is clearly indicated in the file by syntax used `{% block footer %} {% endblock %}`.

#### navbar.html

Validation brings up 1 warning that is exactly the same as in footer.html It also brings up 18 erros:

- First 2 are exactly the same as in footer.html - left unfixed as this file containes html for one block/component of an applicaton that is clearly indicated in the file by sytnax used `{% block navbar %}``{% endblock %}`
- 12 errors related to use of `{{ url_for }}` in all links on the page - in top navbar, sidebar and logo. All left unfixed as linked correctly as advised in [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/#)
- 2 errors informing about repeated occurence of `id="navbarDropdown"`. Left unchanged as there are 2 separate drop down multilink navigation bars used and mentioned `id` is Bootstrap class for multi-link droping down navbar items.
- 2 errors informing about not allowed text in element `ul` - these were `{% else %}` and `{% endif %}`. Left unchanged as the statments are valid [Jinja control structures](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-control-structures)

This is Bootstrap class for multi-link droping down navbar items.


