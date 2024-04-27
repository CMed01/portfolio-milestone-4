# __Portfolio Project 4 - Full Stack__
## __The Ox Box__
 __*“Strong body, strong mind, strong life”*__

![The Ox Box](documentation/doc_images/the-ox-box-grey.jpg)
### __Demo__

The live site can be viewed here - ["INSERT TITLE HERE"]()

Github repository can be viewed here - [CMed01/portfolio-milestone-4](https://github.com/CMed01/portfolio-milestone-4/)

![Am I Responsive](./readme-assets/am-i-responsive.png)


## Table of Contents
* [User Experience](#user-experience)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## __User Experience__

The Ox Box Project is designed to create a vibrant online community focused on holistic health and wellness. Users can review insightful blog content and register an account opening further opportunities to read, view and comment on both exercise routines and blog posts, fostering interaction and knowledge-sharing. Additionally, all users can directly reach out via a contact form, enabling individuals to seek personalised health advice from the owner. With dedicated sections for daily exercise workouts and a health and lifestyle blog, our website aims to empower users to embark on their journey towards a healthier and more fulfilling lifestyle.

### __User Stories__
- US01: Navigate the site
    - As a Site User I can view the landing page so that I can determine the purpose of the application
        - Acceptance criteria
            - I can access the home page and easily view the purpose of the site
            - I can use the menu bar to navigate through the sites content

- US02: Read about the site
    - As a user, I can click on the About link so that I can read about the site.
        - Acceptance criteria
            - I can navigate to the about section of the website.

- US03: View blog articles
    - As a user, I can read health and lifestyle blog articles so that I can learn about improving my well-being
        - Acceptance criteria
            - I can navigate to the blog section of the website.
            - I see a list of blog articles with titles and previews

- US04: Reach out for personlaised services (contact form)
    -  As a user, I can use the contact form to reach out for personalised health and lifestyle advice.
        - Acceptance criteria
            - I can navigate to the contact form section of the website.
            - I see a form with fields to input my name, email, subject, and message.
            - Upon submission, I receive a message successfully confirming form submission 

- US05: Account registration
    - As a new user, I can register for an account so that I can access the features of The Ox Box website.
        - Acceptance criteria
            - I can see a registration form with fields for my name, email, and password.
            - Upon successful registration, I receive a message confirming my registration.

- US06: Account login
    - As a registered user, I login into the website and access member content
        - Acceptance criteria
            - I can see a login form with fields for my email and password.
            - Upon successful login, I am redirected to the homepage of The Ox Box website.

- US07: Access registered user content
    - As a registered user, after logging in, I can view exercise workouts of the day
        - Acceptance criteria
            - I can navigate to the workouts section of the website.
            - I see a list of available workouts with details such as date, time, and description

- US08: Create, update and delete comments on workouts
    - As a registered user, I can read, review and delete comments on workouts so that I can share feedback or ask questions
        - Acceptance criteria
            - I can view the comment section below each workout.
            - I can write a comment and submit it
            - I can record my score for the workout.
            - I can delete or update my own comment

- US09: Create, update and delete comments on blog article
    - As a registered user, I can read, review and delete comments on blog articles so that I can engage with the content
        - Acceptance criteria
            - I can view a comment section below each blog article.
            - I can write a comment and submit it.
            - I can delete or update my own comment

- US10: Restrict access to register users 
    - As a non-registered user, I have limited access to certain features.
        - Acceptance criteria
            - I can view blog articles only
            - I cannot view or comment on blog articles
            - I cannot access, view or comment on workouts

- US11: Manage blog content
    - As an admin, I can create, review and delete blog content and approve submitted comments.
        - Acceptance criteria
            - I have access to a backend dashboard where I can add new blog content.
            - I can view pending comments and approve or reject them.

- US12: Manage workout content
    - As an admin, I have access to create, review and delete workout content and approve submitted comments.
        - Acceptance criteria
            - I can view and modify workout content.
            - I can comment on blog articles and workouts.

- US13: Review contact form submissions
    - As a super admin, I can access and review form submissions full control and access.
        - Acceptance criteria
            - I can access all features of the website.
            - I have exclusive access to review contact form submissions.

- US14: Control access for all users
    - As a super admin, I have full control and access to all content.
        - Acceptance criteria
            - I have superuser access for all features of the website.

### __Features__

#### __Current__
- F01: Navbar
- F02: Landing page/About page
- F03: Contact Form
    * Admin portal
- F04: User authentication
    * Registration
    * Login
    * Sign out
    * Access control
- F06: Blog/Workout articles
    * Create
- F07: Commenting
    * Create
    * Admin review
    * Amend
    * Delete
- F08: UX messaging
    * Successful POST requests

#### __Future__
- New gym facility for personal use
- Online booking system for access to gym
- Personal record of workout and tracking of performance.
- Personalised dashboard for tracking activity
- Registered user communication
 
## __Technologies__
- [Neon](https://neon.tech/)

### __Languages__

* HTML
* CSS
* Javascript
* Python

### __Frameworks, programs and libraries__

* [Django]() - Framework used to create full stack
    * [AllAuth](https://docs.allauth.org/en/latest/) - use to provide authetication framework for project
* [Am I Responsive?](https://ui.dev/amiresponsive) - Used to create an image of the website on various screen sizes.
* [Heroku](https://www.heroku.com/) - Used to deploy the website
* [LucidChat]() - Entity relationship diagrams
* [Figma]() - wireframes
* [Neon]() - Database
* [Favicon](https://favicon.io/) - Used to create favicon
* [Font Awesome]()
* [Bootstrap 5](https://getbootstrap.com/)
    * [Pagination](https://getbootstrap.com/docs/4.0/components/pagination/)
* [Pexels](https://www.pexels.com/) - Used for stock copyright free images
* [Google Fonts](https://fonts.google.com/)
    - Bebas Neue
    - Inter
* [ChatGPT](https://chat.openai.com/) - used to create the test blogs.
* [WodWell](https://wodwell.com/) - used to create the library of workouts

## __Testing__
### __Validator testing__

* __[W3C Markup Validation Service](https://validator.w3.org/)__
    - Describe Test and Results

<br>

* __[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)__
    - Describe Test and Results
    
<br>

* __[JavaScript Testing (JSHint)](https://jshint.com/)__
    - Describe Test and Results

<br>

* __Lighthouse testing using [PageSpeed Insights](https://pagespeed.web.dev/)__
    - Describe Test and Results

<br>

* __[CI Python Linter](https://pep8ci.herokuapp.com/)__
    - Describe Test and Results
    - ![CI Python Linter](./readme-assets/python-validation-test.png)


### __Browser Compatability__

### __Test Cases and Results__

<details open>
<summary>The below table details the test cases that were used. </summary>
<br>

- Insert table of tests here

</details>

### __Debugging__
- Merging Django with Neon
    - [Connect a Django application to Neon](https://neon.tech/docs/guides/django)
    - [Neon + Django Integration Example](https://community.neon.tech/t/neon-django-integration-example/411)
- Creating url link for admin page for authorised users
    - [Django](https://forum.djangoproject.com/t/cant-create-link-to-admin-page-in-my-template/12533) - "Can’t create link to admin page in my template"
- Using signal.py to automatically create a profile when a new user registers
    - [Django signals](https://docs.djangoproject.com/en/5.0/topics/signals/)
- Adding access control using mixins
    - [Django Mixins](https://docs.djangoproject.com/en/5.0/topics/auth/default/)

## __Deployment__

### __How this site was deployed__

1. Open an account with Heroku.

2. On the home dashboard of your account, select "New" then "Create new app".

3. Create an unique app name, select the region and click create.

3. Click on the _Settings_ tab and add the following build packs:
    * `heroku/python`
    * `heroku/nodejs`

4. Create the following _Config Var_ called `PORT`. Set this to `8000`

5. Click on the _Deploy_ tab and connect with GitHub.

6. Select the correct repository.

7. Chose between automatic deploy or manual deploy.

8. Once successfully deployed you can visit the working website.

### __How to clone the repository__

1. Go to the 
 repository on GitHub.

2. Click the "Code" button to the right of the screen, click HTTPs and copy the link there.

3. Open a GitBash terminal. 

4. Change the working directory to the location where you want the clone directory.

5. On the command line, type "git clone" then paste in the copied url (https://github.com/CMed01/portfolio-milestone-3) and press the Enter key to begin the clone process

## __Credits__

### __Content__

* All content was written by the developer

### __Code__

* Insert any links to where code was adapted

### __Acknowledegements__
