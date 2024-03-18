# Braydon's Horror House PROJECT README
### Author Manjula Lal,

## Contents

- Brief
- External user’s goal:

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

Welcome to the Braydon's Horror House platform. Our platform aims to promote an entertaining experience for horror enthusiasts who wish to share there stories and experiences. 

![iamresponsive](/assets/images/readme/iamresponsive.png)

### External user’s goal:

#### 

#### 

#### 


### Site owner's goal:

Create and entertainment platform


### Project Initial ERD and data base design 

![Project ERD](/assets/images/readme/alls_well_erd.png)

## Develop strategy and Wireframe

## Miro Board

The Miro Board was the initial tool we used for iteration. The board allowed us to quicky communicate how the over project will be worked on, start until finished, placed all articles and pictures we will be using and the technology that will be used.  


## Balsamiq
Balsamiq was used to design the initial idea of the All Well’s website which entailed all user features, navigation and placeholders for pictures that would be incorporated within the website. We had made minor alterations in the finished project to support user friendliness and responsivness

![Balsamiq homepage]
![Balsamiq Booking]
![Project Login]
## Lucid Chart

We decided to create a visual map of the website so we could clearly conceptualise the project as a whole.  

![Lucid Chart]

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

Styling font pairing -

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


Leonardo.ai was used to create our images for the website.

chat gpt was used to enhance our knowledge within this project.

Miro was used for ideation for the front end and backend.