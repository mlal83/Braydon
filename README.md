# ALL'S WELL PROJECT README
## By The CODING QUAD
### Author Manjula Lal,

## Contents

- Brief
- External user’s goal:
- Students
- Therapists/Instructors
- Food Vendors
- Site owner's goal
- Potential features to include
- Project Initial ERD and data base design
- Develop strategy and Wireframe
- Miro Board
- Balsamiq
- Lucid Chart
- Github project
- Features
- Styling frontend development
- Fixed Bugs
- Unfixed Bugs
- Testing
- Future features and modifications
- Tools and Technology used 
- Credits


## Brief -- Project  3: Learner Wellness

Welcome to the All’s WELL platform. Our platform aims to promote mental health and physical well by providing easy access to resources, services, and healthy dining options on campus.

![iamresponsive](/assets/images/readme/iamresponsive.png)

### External user’s goal:

#### Students: 

Access resources and services that promote mental and physical well-being. Book sessions or join classes easily.

#### Therapists/Instructors: 

Create profiles, offer services, and manage bookings. Engage with the student community and get feedback.

#### Food Vendors: 

List healthy food options and attract health-conscious students.

### Site owner's goal:

Foster a healthy campus environment by centralising wellness resources.

### Potential features to include:

User registration.
Therapist/Instructor profiles: For students to read about and book sessions.
Event/Session booking: For therapy, yoga, meditation, or fitness classes.
Food section: ~~Highlighting healthy dining options on campus with ratings, reviews, and menu options.~~
Give healthy eating and diet advice
Resources: Articles, videos, and podcasts related to mental and physical wellness

### Project Initial ERD and data base design 

![Project ERD](/assets/images/readme/alls_well_erd.png)

## Develop strategy and Wireframe

## Miro Board

The Miro Board was the initial tool we used for iteration. The board allowed us to quicky communicate how the over project will be worked on, start until finished, placed all articles and pictures we will be using and the technology that will be used.  


## Balsamiq
Balsamiq was used to design the initial idea of the All Well’s website which entailed all user features, navigation and placeholders for pictures that would be incorporated within the website. We had made minor alterations in the finished project to support user friendliness and responsivness

![Balsamiq homepage](/assets/images/readme/Balsamiq-Home.png)

![Balsamiq Booking](/assets/images/readme/Balsamiq-S&T.png)

![Project Login](/assets/images/readme/Balsamiq-login.png)

## Lucid Chart

We decided to create a visual map of the website so we could clearly conceptualise the project as a whole.  

![Lucid Chart](/assets/images/readme/Lucid1.png)

## Github project

For our User Stories, we had decided to use Github project whereby 12 out of the 14 user stories were completed leaving the food section to the next iteration. 

![Git Hub Project](/assets/images/readme/projectboard.png)

## Features

- Articles, Account creation and Reader Comments

![articles](/assets/images/readme/articles.png)

- Events 

![events page](/assets/images/readme/eventspage.png)

- User Reviews

![user reviews](/assets/images/readme/userreviews.png)

- Provider Profiles and Booking Link

![profiles and booking](/assets/images/readme/bookingspage.png)

- Provider session booking via Calendly

![calendly](/assets/images/readme/calandely.png)

## Styling frontend development

Styling font pairing - Raleway & Merriweather. A pastel colour palette of 3 shades of blue/green and beige was used.  The intention for the MVP styling was to convey an identity that was  Lighthearted, "fun" and warm theme to appeal to people of all ages.

We had used, CSS, Bootstrap and HTML for this.

## Fixed Bugs

Summernote stops the display of Event/Article type in Article Admin Screen.

![Old Code](/assets/images/readme/old_code.png)

The code higlighted in the article model above displayed the Event/Article content type on the admin page. This was broken by Summernote.
This functionality is being left in place in case it works somewhere other than the admin panel!

![New Code](/assets/images/readme/new_code.png)

Adding the highlighted code to the Summernote admin class replaced the lost funtionality resulting in the image below.

![Fixed display](/assets/images/readme/fixed_type_display.png)

the missing single quote from this line in logout.html
<p>{% trans 'Are you sure you want to sign out? %}</p>
was causing a "TemplateSyntaxError" at /accounts/logout/ which we had fixed

## Unfixed Bug

In the forms for Comments and Reviews, The text  "Body** appears, we have been unable to find it and remove it.

![unfixed comments bug](/assets/images/readme/userreviews.png)

## Testing

- All top level links works as expected.

- User Account Creation works as expected.
 
- User login and logout works as expected.

- User comments and reviews have full CRUD functionality.

- External links to calendar provider (Calendly) work as expected.

## Future features and modifications

Give users the option to make payments using stripe so they can pay for deposit online before appointment date.

A shop feature to buy health equipment and books.

## Tools and Technology used

HTML used for the main site content.

CSS used for design website.

JavaScript used for user interaction.

Python used for back-end programming.

Git for version control.

Bootstrap used alongside CSS to help build faster and help enhance user experience and responsiveness.

Django used for Python framework.

ElephantSQL for Postgres database.

Heroku was used to deploy the back-end.

Cloudinary used for online static file storage.

## Credits

We would like to give a huge thanks to our facilitator David Calikes and our coding coaches Kevin and Martin at the Code institute for there exceptional guidance and support.

The blog project designed by code institute was used to help design the Django framework.

Leonardo.ai was used to create our images for the website.

chat gpt was used to enhance our knowledge within this project.

Miro was used for ideation for the front end and backend of AllsWell.