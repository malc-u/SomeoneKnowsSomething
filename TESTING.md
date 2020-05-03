# Someone Know Something TESTING

- [Someone Know Something TESTING](#someone-know-something-testing)
  - [Manual testing](#manual-testing)
  - [User stories testing](#user-stories-testing)
  - [Automated testing](#automated-testing)
    - [HTML validation](#html-validation)
      - [base.html](#basehtml)

## Manual testing

## User stories testing

## Automated testing

### HTML validation

This was carried out using [W3C Markup Validation ](https://validator.w3.org/).

#### base.html 

Validation brings up 1 error:
Bad value {{url_for('static', filename='css/style.css')}} for attribute href on element link: Illegal character in path segment: { is not allowed.

This was left unfixed as advised on [Flask - The Base Layout](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/) as correct.

