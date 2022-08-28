# VOYAGEVERT TESTING

## By Mark Todman
---
## OVERVIEW
1. [Performance and Accessibility](#performance-and-accessibility)
1. [Validation](#validation)
1. [Automated Testing](#automated-testing)
1. [Manual Testing](#manual-testing)

---
## PERFORMANCE AND ACCESSIBILITY

## Lighthouse Reports

All pages accessible from the Navbar to authenticated users and superusers were tested for Performance, Accessibility, Best Pracitices and SEO using Lighthouse in Chrome Developer Tools.

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

The HTML of each page on the site was manually accessed through Chrome View Page Source. The HTML was copied and pasted into the Nu HTML Checker. All pages pass with no errors or warnings.

During testing a number of issues were identified and corrected:

- Aria-controls description needed to match the data-bs-target for the navbar toggle
- Update form action to pass validation
- Adjust location of endif statement to ensure closing div tags rendered correctly

## CSS Validation

The custom CSS file locate in the static folder was tested using the [W3 CSS Validator](https://jigsaw.w3.org/css-validator/validator) via direct code input and no errors were found:

![W3C CSS Validation](/static/images/testing/w3c-css-validation.png)

## Python Validation (PEP8)

All Python code was manually checked using [PEP8 Online](http://pep8online.com/). 

Models:

![Models PEP8 Validation](/static/images/testing/pep8-models-validation.png)

URLS:

![URLS PEP8 Validation](/static/images/testing/pep8-urls-validation.png)

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
- All lines adjusted to <80 characters. Except one in the URLS which remains at 82 characters. The hashtag noqa was applied to pass the PEP8 validation as code readability was not an issue.

---
## AUTOMATED TESTING

Automated tests were created and run using unittest. Manual testing was undertaken to cover full functionality and cover aspects not covered by automated testing. Thirteen automated tests were created and run to check returned results were as expected.

![Automated Tests](/static/images/testing/automated-testing.png)

A coverage report was produced to identify areas covered by automated testing and to ensure gaps in automated testing were covered by manual testing.

![Coverage Report](/static/images/testing/testing-coverage.png)

---
## MANUAL TESTING

Thorough manual testing was undertaken throughout production. In final manual testing 56 different test cases were analysed to ensure all testing criteria were satisfied.

The full results of manual testing are documented in here: [Manual Testing Documentation](https://drive.google.com/drive/folders/1QCuFZbqjsvEpSDiCDNzbrCREvbGR0NGn?usp=sharing)
