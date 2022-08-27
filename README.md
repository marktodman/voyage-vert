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
1. [Testing](#testing)
1. [Deployment](#deployment)
1. [Future Development Ideas](#future-development-ideas)
1. [Credits](#credits)

## VOYAGEVERT CONCEPT

The concept for the VoyageVert web application comes from a need to validate an existing business idea, which has been worked on with the business owner's permission. The existing website for the [VoyageVert](https://www.voyagevert.org/) business set outs the vision for a future of sustainable ocean travel using high-speed yachts. One key aspect to moving the business forward is to demonstrate the demand for the service to investors.

This VoyageVert web application concept is to present a showcase of potential routes and trips to interested potential users of the business and gather user information to validate the business concept. The web app can be used as a landing page as part of a marketing campaign to engage users, gather user information and to test consumer interest in certain routes of travel and potential dates of travel using zero-carbon sea travel instead of air travel. The focus for this VoyageVert application is to focus in on user interest in particular routes and trips, generating expressions of interest can then be actioned by the business owners.

---
## STRATEGY

To create a web application that engages users in providing feedback on particular routes and trips that would be of interest for a zero-carbon, high-speed yacht service. 

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
5. Responsive site desgin that delivers excellent user experience across platforms

---
## STRUCTURE

1. LANDING PAGE: the home page contains a clear mission statement and instructions to get started with on the application. At this point the user can link straight to the content or registration. Returning users can login from the landing page. Register and Login are also available from the Navbar.
2. ROUTES PAGE: a responsive list of cards that details the routes (departure and destination) available. Each Route card has information about the duration and the distance of the route, together with a description. The Routes page can be accessed directly through the Navbar. This page is responsive and scalable and will grow as more Routes are added.
3. TRIPS PAGES: Trips pages are dynamically linked to the Routes, dsiplaying trip dates available on each Route as Trip cards. Trips are available through a dropdown on the main Navbar and are listed by Route. Only available (published) Trips for each Route will be displayed on the Trips page. There will be a message on the page if no Trips are available, together with a link to return to the Routes page. This page is responsive and scalable and will grow as more trips are added.
4. BOOKING PAGE: Bookings are dynamically linked to each Trip, displaying the booking information for a specific Trip date on a specific Route. A Booking page is only available to Authenticated Users. A login redirect is in place to ensure users register and login before a booking can be made. The Trip date, Route name and Username information is locked in each Booking to enhance UX and reduce user errors. The number of passengers is the only required field and all other fields are optional. The user can input specific information about each Booking, including special assistance needs and additional comments. Users can record cabin preferences and whether they would want to be an active member of the crew.
5. REGISTERATION PAGE: Users are required to register prior to making a booking. The required fields are username and password. There are optional fields for email, first name and last name. The optional information can also be added on the Account page.
6. ACCOUNT PAGE: profiles are created automatically at user registration. An Account link becomes acitve in the Navbar once a user is authenticated. The Account page provides editable information on the User including: Name, Email, Bio, Sailing Experience. The User can delete their Account, which will delete all information from the database. The Account page also provides a record of all Bookings. Bookings can be edited and deleted by authenticated users.
7. ADMIN PANEL PAGE: the admin panel page on the fronted is only accessible by a Superuser account. The Admin Panel page becomes visible in the Navbar once a Superuser is authenticated. The Admin Panel provides a summary of all User Bookings by Trip Date and Route Name. All Routes and Trips are visible in the Admin Panel whether published or draft. All Routes and Trips can be edited or deleted from the frontend Admin Panel.
8. ADD ROUTE / ADD TRIP PAGES: Superusers also have access to pages to Add Route and Add Trip. These pages becomes visible in the Navbar once a Superuser is authenticated. These pages have full capabilities to add all required information to create a Route or a Trip.
9. LOGIN / LOGOUT PAGES: Username and password is required for returning users to login. Login will be remembered, depending on browser settings. When users seek to logout (via Navbar), they are asked to confirm. This is to prevent accidental logout via the Navbar. Successful login and logout is confirmed by onscreen messaging and users are returned to the home page.


<details>
<summary><strong>Flowchart of Functional Structure</strong></summary>
<br>

![VoyageVert Function Structure](/static/images/readme/voyagevert-flowchart.png)
</details>
<br>

---
## PLANNING

## Agile Development Practices

Agile development practices were used to manage delivery throughout this project. The processes and tools are detailed below.

### Epics and User Stories

Initially, a number of Epics were determined, which led to the creation of a number of User Stories under each of the Epics. The User Stories were then prioritised through the Product Backlog.

#### Epics:

1. As a Business Owner I would like to see which Routes and Trips generate the most interest.

2. As a Site Admin I would like to be able to manage my site from the frontend so that I can easily make changes and test the impact on UX.

3. As a Site User I would like to be able to express interest in trips to demonstrate my interest in this service.

4. As a Site User I would like to be able to manage my account information so that I can make changes if my details or requirements change.


These Epics were then broken down into 21 more detailed User Stories. The User Stories were produced using the [GitHub Issuses](https://github.com/marktodman/voyage-vert/issues) functionality in the repo where all User Stories can be reviewed.

### Agile Development Tools

The [GitHub Issuses](https://github.com/marktodman/voyage-vert/issues) were then prioritised using the [Project Kanban Board](https://github.com/users/marktodman/projects/3) within the repo. User Stories were moved through the process from To do >> In Progress >> Done on the Kanban Board.

To provide a more detailed Agile process, MoSCoW prioritisation was undertaken using [Google Sheets](https://drive.google.com/drive/folders/1qUzzt05p5ZK3oxgmrcyhPj-C4_KSk1UD?usp=sharing) workbooks. 

Detailed descriptions of the Agile Development Process and Agile Development Experience are provided below:


<details>
<summary><strong>Agile Development Process</strong></summary>
<br>
At the start of the project all User Stories were prioritised in the Product Backlog. All User Stories were assigned a User Story Point estimation to allow Time Boxing. The project was then split into four Iterations, with each Iteration lasting one week. It was estimated that each week a total of 10 story points could be completed. Initially, a total of 46 story points were identified, which meant that it was possible some functionality may not be completed. 
<br>
<br>
At the start of each week, User Stories were prioritised into the corresponding Iteration sheet on the basis of 60% Must Have allocation for the Iteration. 20% were allocated Could Have, leaving 20% Should Have based on the prioritsed Product Backlog. At the end of each Iteration, progress was reviewed to ensure Story Point estimation was appropriate. Prioritisation was also reviewed to ensure that all aspects of the project were completed in time to ship the project to meet the deadline.
<br>
</details>
<br>
<details>
<summary><strong>Agile Development Experience</strong></summary>
<br>
Generally, Story Point estimation was found to be reasonable on a week by week basis. All Must Have User Stories were completed in each Iteration. All Should Have User Stories were also completed in each Iteration. In most Iterations, all Could Haves were also completed. This was due to the creation of capacity to complete the User Stories in the Iteration, rather than poor estimation of the Story Points.
<br>
<br>
Through the process of the mid-point review, additional User Stories regarding Admin CRUD functionality were identified, which put additional time pressure on successful User Story completion. However, the use of Agile tools allowed these additional User Stories to be included and the impact identified. 
<br>
<br>
At the conclusion of this stage of the project, there is one outstanding User Story relating to a Newsletter sign up. As the Iterations progressed and the project neared the shipping deadline, the Newsletter User Story was down-prioritised relative to the other User Stories and, ultimately, ended up as a Won't Have User Story for this release.
</details>
<br>

