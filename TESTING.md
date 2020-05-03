# Someone Know Something TESTING

- [Someone Know Something TESTING](#someone-know-something-testing)
  - [Manual testing](#manual-testing)
  - [User stories testing](#user-stories-testing)
  - [Automated testing](#automated-testing)
    - [HTML validation](#html-validation)
      - [base.html](#basehtml)
      - [footer.html](#footerhtml)

## Manual testing

## User stories testing

## Automated testing

### HTML validation

This was carried out using [W3C Markup Validation ](https://validator.w3.org/).

#### base.html 

Validation brings up 1 error:

- Bad value {{url_for('static', filename='css/style.css')}} for attribute href on element link: Illegal character in path segment: { is not allowed.

This was left unfixed as advised on [Flask - The Base Layout](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/) as correct.

#### footer.html

Validation brings up 1 warning:

- Consider adding a lang attribute to the html start tag to declare the language of this document.

Validation also brings up 2 errors:

- Non-space characters found without seeing a doctype first. Expected <!DOCTYPE html>
- Element head is missing a required instance of child element title

These were left unfixed as this file contains html for one block/component of an application layout that is clearly indicated int he file by syntax used `{% block footer %} {% endblock %}`.


