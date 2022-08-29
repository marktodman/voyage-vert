# VOYAGEVERT TESTING

## By Mark Todman
---
## OVERVIEW
1. [Performance and Accessibility](#performance-and-accessibility)
1. [Validation](#validation)
1. [Automated Testing](#automated-testing)
1. [Manual Testing](#manual-testing)
1. [Known Bugs](#known-bugs)

---
## PERFORMANCE AND ACCESSIBILITY

## Lighthouse Reports

All pages accessible from the Navbar to authenticated users and superusers were tested for Performance, Accessibility, Best Practices and SEO using Lighthouse in Chrome Developer Tools.

Home Page:

![Home Page Lighthouse](/static/images/testing/voyagevert-home-lighthouse.png)

Routes Page:

![Routes Page Lighthouse](/static/images/testing/voyagevert-routes-lighthouse.png)

Trips Page (example page for Amsterdam to London Route):

![Trips Page Lighthouse](/static/images/testing/voyagevert-trips-lighthouse.png)

Account Page:

![Account Page Lighthouse](/static/images/testing/voyagevert-account-lighthouse.png)

Admin Panel Page:

![Admin Panel Page Lighthouse](/static/images/testing/voyagevert-admin-lighthouse.png)

During testing a number of issues were identified and addressed to improve performance, accessibility, best practices and SEO:

- Compress images to improve performance. All images were compressed to improve performance without loss in resolution or UX
- Removal of unused webmanifest link in head element
- Add meta description to improve SEO.

---
## VALIDATION

## HTML Validation

The HTML code has been tested for errors with the [W3 HTML Validator](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&showimagereport=yes&doc=https%3A%2F%2Fvoyagevert.herokuapp.com%2F) and passed with no errors.

The HTML of each page of the site was manually accessed through Chrome View Page Source. The HTML was copied and pasted into the Nu HTML Checker. All pages pass with no errors or warnings.

During testing a number of issues were identified and corrected:

- Aria-controls description needed to match the data-bs-target for the navbar toggle
- Change repeat id tags for the two dropdown menus
- Update form action to pass validation
- Adjust location of endif statement to ensure closing div tags rendered correctly in all views

## CSS Validation

The custom CSS file located in the static folder was tested using the [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) via direct code input and no errors were found:

![W3C CSS Validation](/static/images/testing/w3c-css-validation.png)

## Python Validation (PEP8)

All Python code was manually checked using [PEP8 Online](http://pep8online.com/). 

Models:

![Models PEP8 Validation](/static/images/testing/pep8-models-validation.png)

Booking App URLS:

![URLS PEP8 Validation](/static/images/testing/pep8-urls-validation.png)

VoyageVert Project URLS:

![VoyageVert Project Urls PEP8 Validation](/static/images/testing/pep8-vvurls-validation.png)

Views:

![Views PEP8 Validation](/static/images/testing/pep8-views-validation.png)

Forms:

![Forms PEP8 Validation](/static/images/testing/pep8-forms-validation.png)

Apps:

![Apps PEP8 Validation](/static/images/testing/pep8-apps-validation.png)

Admin:

![Admin PEP8 Validation](/static/images/testing/pep8-admin-validation.png)

Context Processors:

![Context Processors PEP8 Validation](/static/images/testing/pep8-contextprocessors-validation.png)

Test Models:

![Test Models PEP8 Validation](/static/images/testing/pep8-testmodels-validation.png)

Test Views:

![Test Views PEP8 Validation](/static/images/testing/pep8-testviews-validation.png)

During testing a few issues were identified and corrected:

- Extra whitespace was deleted
- Indentation was corrected
- Two lines spaces between functions and classes
- All lines adjusted to <80 characters. Except one in the booking app urls.py which remains at 82 characters. The hashtag noqa was applied to pass the PEP8 validation as code readability was not an issue.

---
## AUTOMATED TESTING

Automated tests were created and run using unittest. Manual testing was undertaken to cover full functionality and cover aspects not covered by automated testing. Thirteen automated tests were created and run to check returned results were as expected.

![Automated Tests](/static/images/testing/automated-testing.png)

A coverage report was produced to identify areas covered by automated testing and to ensure gaps in automated testing were covered by manual testing.

![Coverage Report](/static/images/testing/testing-coverage.png)

---
## MANUAL TESTING

Thorough manual testing was undertaken throughout production. During final manual testing, 56 different test cases were analysed to ensure all testing criteria were satisfied.

The full results of manual testing are documented in here: [Manual Testing Documentation](https://docs.google.com/spreadsheets/d/10jtC0ANUu4_oC7cR7QaeMOU8aB2IvYqBj4g4CefscN8/edit#gid=0)

---
## KNOWN BUGS

There are two known bugs, which are scheduled to be fixed in the next version:

- For a Superuser only: when a superuser is on the Admin Panel page, the Trips navbar dropdown will display all Routes, whether these are draft or published. Clicking on a draft Route will display a 404 Error. This only occurs for a superuser and only when viewing the navbar Trips dropdown from the Admin Panel page. The navbar Trips dropdown does not display draft Routes for a superuser on any other page. This bug does not occur for authenticated users. A fix was not identified for this version. Authenticated user UX is not impacted and the site functions as expected.
- Users are able to add more than one booking for a Trip. Multiple bookings does not impact site functionality or create errors, but removing the ability for a user to express their interest in the same trip more than once would improve UX and the data generated from the site.
