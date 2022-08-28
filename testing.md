# VOYAGEVERT TESTING

## By Mark Todman
---
## OVERVIEW
1. [Performance and Accessibility](#performance-and-accessibility)
1. [Validation](#validation)
1. [Manual Testing](#manual-testing)
1. [Automated Testing](#automated-testing)
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

The HTML of each page on the site was manually accessed through Chrome View Page Source. The HTML was copied and pasted into the Nu HTML Checker. All pages now pass with no errors or warnings.

During testing a number of issues were identified and corrected:

- Aria-controls description needed to match the data-bs-target for the navbar toggle
- Update form action to pass validation
- Adjust location of endif statement to ensure closing div tags rendered correctly

## CSS Validation

The custom CSS file locate in the static folder was tested using the [W3 CSS Validator](https://jigsaw.w3.org/css-validator/validator) via direct code input and no errors were found:

![W3C CSS Validation](/static/images/testing/w3c-css-validation.png)

## Python Validation (PEP8)

---
## MANUAL TESTING

