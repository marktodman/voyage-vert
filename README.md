# VoyageVert

## By Mark Todman

![Launch page screenshot.](/static/images/readme/voyagevert-amiresponsive.png)

The deployed [VoyageVert](https://voyagevert.herokuapp.com/) app.

The [GitHub repository.](https://github.com/marktodman/voyage-vert)

---
## OVERVIEW
1. [VoyageVert Concept](#voyagevert-concept)
1. [Strategy](#strategy)
1. [Scope](#scope)
1. [Structure](#structure)
1. [Skeleton](#skeleton)
1. [Surface](#surface)
1. [Planning](#planning)
1. [Features](#features)
1. [Resources](#resources)
1. [Testing](#testing)
1. [Deployment](#deployment)
1. [Future Development Ideas](#future-development-ideas)
1. [Credits](#credits)

## VOYAGEVERT CONCEPT

The concept for the VoyageVert web application comes from a need to validate an existing business idea, which has been worked on with the business owner's permission. The existing website for the [VoyageVert](https://www.voyagevert.org/) business set outs the vision for a future of sustainable ocean travel using high-speed yachts. One key aspect to moving the business forward is to demonstrate the demand for the service to investors.

This VoyageVert web application concept is to present a showcase of potential routes and trips to interested potential users of the business and gather user information to validate the business concept. The web app can be used as a landing page as part of a marketing campaign to engage users, gather user information and to test consumer interest in certain routes of travel and potential dates of travel using zero-carbon sea travel instead of air travel. The focus for this VoyageVert application is to focus in on user interest in particular routes and trips, generating expressions of interest can then be actioned by the business owners.

---
## STRATEGY

To create a web application that engages users in providing feedback on routes and trips that would be of interest for a zero-carbon, high-speed yacht service. 

### Target Audience:

- Environmentally conscious travellers looking for an alternative to flight
- Adventurous travellers looking to explore different ways to travel
- Investors considering investment in zero carbon travel solutions
- Regulators researching zero carbon travel options

---
## SCOPE

1. Visually appealing and intuitive user experience
2. Scalable design that allows for the application to grow as more information is added
3. Extensive frontend functionality for Users to support an engaging user experience
4. Extensive frontend functionality for Admins to support rapid testing and deployment
5. Responsive site design that delivers excellent user experience across platforms

---
## STRUCTURE

### Functional Structure

1. LANDING PAGE: the home page contains a clear mission statement and instructions to get started with on the application. At this point the user can link straight to the content or registration. Returning users can login from the landing page. Register and Login are also available from the Navbar.
2. ROUTES PAGE: a responsive list of cards that details the routes (departure and destination) available. Each Route card has information about the duration and the distance of the route, together with a description. The Routes page can be accessed directly through the Navbar. This page is responsive and scalable and will grow as more Routes are added.
3. TRIPS PAGES: Trips pages are dynamically linked to the Routes, displaying trip dates available on each Route as Trip cards. Trips are available through a dropdown on the main Navbar and are listed by Route. Only available (published) Trips for each Route will be displayed on the Trips page. There will be a message on the page if no Trips are available, together with a link to return to the Routes page. This page is responsive and scalable and will grow as more trips are added.
4. BOOKING PAGE: Bookings are dynamically linked to each Trip, displaying the booking information for a specific Trip date on a specific Route. A Booking page is only available to Authenticated Users. A login redirect is in place to ensure users register and login before a booking can be made. The Trip date, Route name and Username information is locked in each Booking to enhance UX and reduce user errors. The number of passengers is the only required field and all other fields are optional. The user can input specific information about each Booking, including special assistance needs and additional comments. Users can record cabin preferences and whether they would want to be an active member of the crew.
5. REGISTERATION PAGE: Users are required to register prior to making a booking. The required fields are username and password. There are optional fields for email, first name and last name. The optional information can also be added on the Account page.
6. ACCOUNT PAGE: profiles are created automatically at user registration. An Account link becomes active in the Navbar once a user is authenticated. The Account page provides editable information on the User including: Name, Email, Bio, Sailing Experience. The User can delete their Account, which will delete all information from the database. The Account page also provides a record of all Bookings. Bookings can be edited and deleted by authenticated users.
7. ADMIN PANEL PAGE: the admin panel page on the frontend is only accessible by a Superuser account. The Admin Panel page become visible in the Navbar once a Superuser is authenticated. The Admin Panel provides a summary of all User Bookings by Trip Date and Route Name. All Routes and Trips are visible in the Admin Panel whether published or draft. All Routes and Trips can be edited or deleted from the frontend Admin Panel.
8. ADD ROUTE / ADD TRIP PAGES: Superusers also have access to pages to Add Route and Add Trip. These pages becomes visible in the Navbar once a Superuser is authenticated. These pages have full capabilities to add all required information to create a Route or a Trip.
9. LOGIN / LOGOUT PAGES: Username and password is required for returning users to login. Login will be remembered, depending on browser settings. When users seek to logout (via Navbar), they are asked to confirm. This is to prevent accidental logout via the Navbar. Successful login and logout are confirmed by onscreen messaging and users are returned to the home page.


<details>
<summary><strong>Flowchart of Functional Structure</strong></summary>
<br>

![VoyageVert Function Structure](/static/images/readme/voyagevert-flowchart.png)
</details>
<br>

### Database Structure

Four customer models were created to produce the required database structure. 

1. ROUTE MODEL: The Route Model contains all the information for a specific route. This model has the route name (departure and destination), description, duration, distance, status and featured image.
2. TRIP MODEL: The Trip Model creates a trip linked to a Route by the route name. The Trip model also has fields for description, status and interest.
3. BOOKING MODEL: The Booking Model creates a booking linked to a Trip by the date and a Route by the route name. The Booking Model is also linked to the User Model through the passenger field. There is additional information for total number of passengers, cabin type, crew option, sailing experience, special assistance needs and comments.
4. PROFILE MODEL: The Profile Model has a OneToOne relationship with the User Model and associated Bio and Sailing Experience information with the User.

<details>
<summary><strong>Entity Relationship Diagram (ERD)</strong></summary>
<br>

![VoyageVert ERD](/static/images/readme/voyagevert-erd.png)
</details>
<br>

---
## SKELETON

The skeleton of the site was designed in accordance with the scope, focusing on consistent and intuitive UX that could easily scale as the site data expanded with additional routes and trips. Wireframes for the main user and admin pages were designed using Balsamiq. 

The wireframes provided a basic outline for the site, which was modified according to development requirements during production and user feedback.

<details>
<summary><strong>Wireframes</strong></summary>
<br>
Landing Page Wireframe:

![Landing Page Wireframe](/static/images/readme/home-wireframe.png)
<br>
<br>
Routes Page Wireframe:

![Routes Page Wireframe](/static/images/readme/routes-wireframe.png)
<br>
<br>
Trips Page Wireframe:

![Trips Page Wireframe](/static/images/readme/trips-wireframe.png)
<br>
<br>
Booking Page Wireframe:

![Booking Page Wireframe](/static/images/readme/booking-wireframe.png)
<br>
<br>
Account Page Wireframe:

![Account Page Wireframe](/static/images/readme/account-wireframe.png)
<br>
<br>
Admin Panel Page Wireframe:

![Admin Panel Page Wireframe](/static/images/readme/admin-wireframe.png)
<br>
<br>
Delete Confirmation Page Wireframe:

![Delete Confirmation Page Wireframe](/static/images/readme/delete-wireframe.png)
<br>
<br>
</details>
<br>

---
## SURFACE

The surface was designed to be clean and allow focus on the routes, trips and booking information. The routes and trips styling was based on cards which included destination images, together with descriptive information and clear actions. 

Color palletes were chosen to reflect the theme of the sea. Two color palletes were chosen using [Coolors](https://coolors.co/). A dark blue background with white text and white cards was utilised to reflect the sea theme and to help key information stand out for the user.

<details>
<summary><strong>Color Palettes</strong></summary>
<br>

![Color palette 1](/static/images/readme/voyagevert-palette-1.png)
<br>
<br>

![Color palette 2](/static/images/readme/voyagevert-palette-2.png)
</details>
<br>

Route and trip cards were chosen to be white to allow the important information to standout. This design was taken through the site with color text on a white background for all forms and tables. 

Buttons were styled to standout with hover actions to provide user feedback. All delete or cancel buttons were styled in red as a widely accepted color to direct user caution.

Two fonts were chosen for the site using [Google Fonts](https://fonts.google.com/). Oleo Script Swash Caps was used for the VoyageVert logo present on every page. Catamaran was used for the text for the Navbar and main site content throughout the site to satisfy the UX objectives.

---
## PLANNING

## Agile Development Practices

Agile development practices were used to manage delivery throughout this project. The processes and tools are detailed below.

### Epics and User Stories

Initially, Epics were determined, which led to the creation of a number of User Stories under each Epic. The User Stories were then prioritised through the Product Backlog.

#### Epics:

1. As a Business Owner I would like to see which Routes and Trips generate the most interest.

2. As a Site Admin I would like to be able to manage my site from the frontend so that I can easily make changes and test the impact on UX.

3. As a Site User I would like to be able to express interest in trips to demonstrate my interest in this service.

4. As a Site User I would like to be able to manage my account information so that I can make changes if my details or requirements change.


These Epics were then broken down into 21 more detailed User Stories. The User Stories were produced using the [GitHub Issues](https://github.com/marktodman/voyage-vert/issues) functionality in the repo where all User Stories can be reviewed.

Each User Story consisted of a number of tasks to ensure completion. These tasks were identified for each User Story and worked through to completion of the User Story.

### Agile Development Tools

The [GitHub Issues](https://github.com/marktodman/voyage-vert/issues) were then prioritised using the [Project Kanban Board](https://github.com/users/marktodman/projects/3) within the repo. User Stories were moved through the process from To do >> In Progress >> Done on the Kanban Board.

To provide a more detailed Agile process, MoSCoW prioritisation was undertaken using [Google Sheets](https://drive.google.com/drive/folders/1qUzzt05p5ZK3oxgmrcyhPj-C4_KSk1UD?usp=sharing) workbooks. 

Detailed descriptions of the Agile Development Process and Agile Development Experience are provided below:


<details>
<summary><strong>Agile Development Process</strong></summary>
<br>
At the start of the project, all User Stories were prioritised in the Product Backlog. All User Stories were assigned a User Story Point estimation to allow Time Boxing. The project was then split into four Iterations, with each Iteration lasting one week. It was estimated that each week a total of 10 story points could be completed. Initially, a total of 46 story points were identified, which meant that it was possible some functionality may not be completed. 
<br>
<br>
At the start of each week, User Stories were prioritised into the corresponding Iteration sheet on the basis of 60% Must Have allocation for the Iteration. 20% were allocated Could Have, leaving 20% Should Have based on the prioritised Product Backlog. Tasks were identified for each User Story and steadily worked through during the Iteration. At the end of each Iteration, progress was reviewed to ensure Story Point estimation was appropriate. Prioritisation was also reviewed to ensure that all aspects of the project were completed in time to ship the project to meet the deadline. The results of these Iteration reviews are documented in the Google Sheets workbooks accessible via the link below: 
<br>
<br>

[Agile Development Documents.](https://drive.google.com/drive/folders/1qUzzt05p5ZK3oxgmrcyhPj-C4_KSk1UD?usp=sharing)
<br>
</details>
<br>
<details>
<summary><strong>Agile Development Review</strong></summary>
<br>
Generally, Story Point estimation was found to be reasonable on a weekly basis. All Must Have User Stories were completed in each Iteration. All Should Have User Stories were also completed in each Iteration. In most Iterations, all Could Haves were also completed. This was due to the creation of capacity to complete the User Stories in the Iteration, rather than poor estimation of the Story Points.
<br>
<br>
Through the process of the mid-point review, additional User Stories regarding Admin CRUD functionality were identified, which put additional time pressure on successful User Story completion. However, the use of Agile tools allowed these additional User Stories to be included and the impact identified. 
<br>
<br>
At the conclusion of this stage of the project, there is one outstanding User Story relating to a Newsletter sign up. As the Iterations progressed and the project neared the shipping deadline, the Newsletter User Story was down-prioritised relative to the other User Stories and, ultimately, ended up as a Won't Have User Story for this release.
</details>
<br>

---
## FEATURES

## Navbar

The navbar is a responsive element, which collapses to a hamburger icon on smaller screens. The navbar is persistent on all pages. The contents of the navbar change depending on whether the user is 1) a guest 2) an authenticated user 3) a superuser.

Guest Navbar. Register and Login navigation is available:

![Guest Navbar](/static/images/readme/guest-navbar.png)

Authenticated User Navbar. Account and Logout navigation is available:

![User Navbar](/static/images/readme/user-navbar.png)

Superuser Navbar. Admin dropdown is available:

![Superuser Navbar](/static/images/readme/superuser-navbar.png)

The Routes page containing a summary of all available routes is on all navbar versions. The Trips dropdown menu provides a summary of all available trips by Route. The user clicks on a route and will be taken to all available trips on that route. This bypasses the routes page and enhances UX: 

![Trips dropdown menu](/static/images/readme/trips-navbar.png)

Superusers have direct access to the frontend Admin Panel page from the navbar. The Superuser can edit and delete all routes and trips (whether published or draft) from the Admin Panel. Superusers also have quick access to Add Route and Add Trip functionality from the navbar:

![Admin dropdown menu](/static/images/readme/admin-navbar.png)

## Routes Page

The Routes pages provides all available routes by departure and destination. The page is responsive and scalable. On larger screens there are four route cards across the page. On medium size screens this reduces to two and on smaller screens, like mobiles, this reduces to one. As new routes are added and published these will be added as Route Cards to the existing screen. Currently there is no limit to the number that would be displayed and there is no pagination. Pagination would have to be considered if the UX becomes impacted by the inclusion of too many routes.

Each Route is presented on a Route Card which includes the departure and destination locations, a description of the route, the duration, the distance and the option to click through to view available trips on that route.

![Routes page](/static/images/readme/routes-page.png)

## Trips Page

The Trips pages provide information on all available trips on a given route. The page is responsive and scalable. On larger screens there are four trip cards across the page. On medium size screens this reduces to two and on smaller screens, like mobiles, this reduces to one. As new trips are added and published these will be added as Trip Cards to the existing screen. Currently there is no limit to the number that would be displayed and there is no pagination. Pagination would have to be considered if the UX becomes impacted by the inclusion of too many trips on a given route.

Each Trip is presented on a Trip Card which includes the trip date, a description of the trip and the option to click through to express interest in booking. Users must have an account and be logged in to be directed to the Booking page. If users are not authenticated they will be redirected to the login page on clicking the button. If users are not yet registered, there is a link in the login to register first.

![Trips page](/static/images/readme/trips-page.png)

## Booking Page

Users must be authenticated to access the Booking page. The Booking page can only be accessed via the specific trip being booked. The Booking page provides a booking form for user completion. 

The date, route name and username fields are auto-completed for the specific trip chosen by the user. These fields cannot be changed.

The user must enter the total number of passengers for the booking. There are criteria choices for type of cabin (private or shared) and sailing experience (none/some/lots). There are text fields for Special Assistance Needs and Additional Comments - both of these fields can be left blank and both can be edited by the user later.

![Booking page 1](/static/images/readme/booking-page-1.png)
![Booking page 2](/static/images/readme/booking-page-2.png)

The submit button has a hover affect to provide user feedback:

![Booking button](/static/images/readme/booking-page-3.png)

## Account Page

Authenticated users have access to an Account page, through which they can manage their account. Users are able to edit and delete their account details. Users can edit their first name, last name and email. These details are all requested at registration, but are not required. If these were not input at registration the fields will be blank. Users cannot change their username to prevent database errors. 

![Account information](/static/images/readme/account-page-1.png)

The bio and sailing experience information is not requested at registration. This profile information is created at the same time as the user account is created. The bio field will be blank, whilst the sailing experience field will default to None. These can both be edited.

Deletion will delete all records for the user.

![Account deletion information](/static/images/readme/account-page-2.png)

There is also a My Trips section on the account page. If the user has not booked any trips this section will be blank and there is a message to tell the user that trips will appear once they have made a booking.

![My Trips information](/static/images/readme/account-page-3.png)

Each Booking can be edited or deleted. The same Booking fields are editable as at the time of making the booking. Deletion will wipe the Booking from the database and cannot be undone, but a new booking could be made.

![Booking deletion information](/static/images/readme/account-page-4.png)

## Admin Panel, Add Route and Add Trip Pages

Authenticated superusers have access to an Admin Panel which provides feedback on User Bookings as well as full CRUD functionality through the frontend. 

The User Bookings Summary table shows the site admin how many users have made bookings for each trip on each route. This information is linked to the database records and updates automatically as a user adds a booking. This is the number of users that have booked a trip, not the total number of passengers.

![Total User Bookings](/static/images/readme/admin-page-1.png)

All Routes are summarised in the Admin Panel page by Route Name, Description, Duration, Distance and Status. All Routes are shown whether draft (not displayed on the routes page) or published (displayed on the routes page). 

![Admin Route Information](/static/images/readme/admin-page-2.png)

All Trips are summarised in the Admin Panel page by Trip Date, Route Name, Description and Status. All Routes are shown whether draft (not displayed on the routes page) or published (displayed on the routes page). 

![Admin Trip Information](/static/images/readme/admin-page-3.png)

All Route and Trip information can be edited. This is an example from the Edit Route page:

![Edit Route Information](/static/images/readme/admin-page-4.png)

All Routes and Trips can be deleted. There is a confirmation step for Route and/or Trip deletion. This is an example for a Route deletion:

![Delete Route Information](/static/images/readme/admin-page-5.png)

New Routes and Trips can be added to the database from the frontend. The Add Route and Add Trip pages can be accessed from the Admin dropdown in the navbar. Once added, the Routes and Trips will be included in the Admin Panel Page. Here is an example from the Add Route page:

![Add Route Information](/static/images/readme/admin-page-6.png)

---
## RESOURCES

## Languages

- Python
- HTML5
- CSS3
- JavaScript

## Frameworks & Libraries

- Django: The web app is built using the Django framework
- Bootstrap5: Frontend framework used to provide structure, style and responsive behaviour

## Programs

- Heroku: Container-based cloud Platform used to deploy the VoyageVert app and host the Postgres database
- Cloudinary: Cloud hosting platform used to host static CSS files and image urls
- GitPod: Developer platform for managing code, files and version control
- GitHub: Repository for all code. Also used to manage agile development approach
- Google Sheets: Managing agile development approach and manual testing documentation
- Balsamiq: Creating wireframes
- Lucidchart: Producing Functional Structure Flowchart and Entity Relationship Diagram


---
## TESTING

Automated and Manual Testing was undertaken across the application. The results are presented in the [Testing markdown document located in the GitHub repo.](testing.md)

---
## DEPLOYMENT

The VoyageVert web app is deployed via [GitHub](https://github.com/) and [Heroku](https://www.heroku.com/).

The deployed VoyageVert web app: [VoyageVert](https://voyagevert.herokuapp.com/)

### GitHub Repository

The code is located in a [GitHub repository](https://github.com/marktodman/voyage-vert).

### Forking the GitHub Repository

To use this code and make changes without affecting the original code, it is possible to 'fork' the code on the GitHub repository through the following steps:

1. Create an account at [GitHub](https://github.com/).
1. Log into your GitHub account.
1. Go to the GitHub repository for [VoyageVert](https://github.com/marktodman/voyage-vert).
1. Click the 'Fork' button in the upper right-hand corner of the page.
1. A copy of the repository will be available in your own repository.

### Heroku Deployment 

The site is deployed to [Heroku](https://www.heroku.com) through the following steps:

1. Log in to Heroku or create an account if required.
1. On the Welcome page click the button labelled 'New' in the top right corner, just below the header.
1. From the drop-down menu select 'Create new app'.
1. Enter a unique app name. 
1. Select the relevant geographical region.
1. Click to 'Create App'.
1. Navigate to 'Settings' and scroll down to the 'Config Vars' section. 
1. Click 'Reveal Config Vars' and enter 'PORT' for the key and '8000' for the value. Then click 'Add'.
1. Add CLOUDINARY_URL, DATABSE_URL and SECRET_KEY.
1. Click on the 'Deploy' tab.
1. Next to 'Deployment method' select 'GitHub'.
1. Connect the relevant GitHub repository.
1. Under 'Manual deploy' choose the correct branch and click 'Deploy Branch'. 
1. Under 'Automatic deploys' you can select 'Automatic Deploys' so that the site updates when updates are pushed to GitHub.

---
## FUTURE DEVELOPMENT IDEAS

There are a number of future development ideas to be deployed under future versions of the app:

1. Add a Newsletter sign up to develop a community. 
1. Custom 404 and other Error pages to improve UX. 
1. Extend the profile information to include more user information and avatar.
1. Automatically populate Booking forms with profile information to improve UX.
1. Add a Bookings count to provide user feedback on popularity of certain Routes and Trips.
1. Add more Routes and Trips.
1. Add a Blog to generate site engagement and grow site traffic.

---
## CREDITS

The useful [Django documentation](https://docs.djangoproject.com/en/4.1/) was invaluable in the creation of this project.

There was a lot of useful Django information on [Codemy's YouTube Channel](https://www.youtube.com/c/Codemycom/playlists), which really helped in the development of this project.

The World Map Favicon was sourced from [Favicon.io](https://favicon.io/).

Images were all open source and free to use from [Pexels](https://www.pexels.com) and [Unsplash](https://unsplash.com/). A special thanks to [Rachel Claire](https://www.pexels.com/@rachel-claire/) who took the picture used on the home page and as a placeholder image for routes and trips cards.

[Stack Overflow](https://stackoverflow.com/) was helpful in the resolution of a number of specific issues, including:
- Early errors in database schema associated with relationships between models - resolved by [zeroing and making new migrations](https://stackoverflow.com/questions/58000680/django-safely-remove-old-migrations) 
- Issue with non-string type datetime.date - resolved by [applying str()](https://stackoverflow.com/questions/64976269/str-returned-non-string-type-datetime-date)

- Getting [card images to be the same size](https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width)
- [How to populate a form](https://stackoverflow.com/questions/53075940/how-to-pre-populate-django-modelform-fields)

Some other key challenges were overcome using information from other sources:
- Accessing variables across templates resolved by [creating a context_processor.py file](https://www.skillsugar.com/how-to-create-context-processor-in-django)
- [How to create a custom allauth form](https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/)
- [How to add a profile model](https://www.youtube.com/watch?v=Alua227cOmY&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=27)
- [Automatically applying the profile model when adding a new user](https://blog.khophi.co/extending-django-user-model-userprofile-like-a-pro/)

Chris Quinn and Martina Terlevic as Mentors at the [Code Institute](https://codeinstitute.net/) provided excellent direction and helped with resources to steer this project to completion. 