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

## Brief -- Project 3: Braydon's Horror House

Welcome to the Braydon's Horror House platform. Our platform aims to promote an entertaining experience for horror enthusiasts who wish to share there stories and experiences and to build a community where people can engage with each other.

![iamresponsive](/static/images/amIResponsivePP.png)

### External user’s goal:

### Site owner's goal:

My goal was aimed to entertain users to engage within a community with similar interests. When it comes to spooky stories, there is a very big market for people who find this of interest and my aim was to include some features that are very different to what you see in modern website and want to continue to develop this site as there is alot of potential for growth in this website. What I wanted to do was to have a wesbite that was not to overpowering so it appeals to the masses, and didnt want people to be left too overwhelmed and stresesd in the enviroment they are reading stories, so I focused purely on the mental aspect alongside creativity.

### Project Initial ERD and data base design

![Project ERD](/static/images/erd3.png)

## Develop strategy and Wireframe

## Miro Board

The Miro Board was the initial tool we used for iteration. The board allowed us to quicky communicate how the over project will be worked on, start until finished, placed all articles and pictures we will be using and the technology that will be used.

## Balsamiq

Balsamiq was used to design the initial idea of the All Well’s website which entailed all user features, navigation and placeholders for pictures that would be incorporated within the website. We had made minor alterations in the finished project to support user friendliness and responsivness

![Balsamiq Wireframe](/static/images/wireframe.png)

## Lucid Chart

I decided to create a visual map of the website so we could clearly conceptualise the project as a whole. As you can see there alot of work left to do for this website and alot of potential of scope.

![Lucid Chart]

## Github project

For our User Stories, we had decided to use Github project whereby 12 out of the 14 user stories were completed leaving the food section to the next iteration.

![Git Hub Project]

## Features

![stories](/static/images/stories.png)

![submit story and dropdown](/static/images/story-dropdown.png)

![navbar](/static/images/navbar.png)

![profile](/static/images/profile.png)

![inside card](/static/images/inside-card.png)

![comments](/static/images/comments.png)

## Styling frontend development

Styling font pairing -

## Fixed Bugs

![Iteration issues](/static/images/iteration-issue.png)

The problem I was having was that even though my CSRF_TRUSTED_ORIGINS were correct, the screen my dev screen would keep throwing, error. It was notived then that the numbers at the end of the URL kept iterating by one, so after changing my number at the end of my URL, I was able to see my webpage.

![Integrity error](/static/images/integrity-error.png)

I was having integrity errors, and inroder to fix them, I had to create a new function to rectify the issue.

![Issue with URL](/static/images/url.png)
The problem was that the URL /stories/set_avatar/ was being matched by the stories_detail pattern instead of the set_avatar pattern. This happened because the set_avatar pattern was defined after the stories_detail pattern in the urlpatterns list.

Django processes URL patterns in the order they are defined, and it stops as soon as it finds a match. Since the stories_detail pattern was defined before the set_avatar pattern, Django matched /stories/set_avatar/ to the stories_detail pattern, causing the post_detail view to be called instead of the set_avatar view.

To resolve this issue, rearranged the urlpatterns list so that the set_avatar pattern is defined before the stories_detail pattern. This ensures that requests to /stories/set_avatar/ are correctly routed to the set_avatar view.

![Slugify](/static/images/slugify.png)
from django.utils.text import slugify

Before adding the slug field, there were duplicated field declarations within the Story model. This duplication caused confusion and could lead to errors. The corrected version removed the duplicated fields, ensuring clarity and consistency in the model definition

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

We would like to give a huge thanks to our facilitator David Calikes and our coding coaches Kevin and Martin at the Code institute for there exceptional guidance and support. I would also like to give a special thanks to my mentor Daisy who has supported me throughout my project

Leonardo.ai was used to create our images for the website.

chat gpt was used to enhance my knowledge, help with identifying bugs and assist with indenting issues

Miro was used for ideation for the front end and backend developement.
https://www.learningaboutelectronics.com/Articles/
How-to-create-a-drop-down-list-in-a-Django-form.php
Stackoverflow.com
https://gencraft.com/generate
https://docs.djangoproject.com/en/5.0/ref/models/fields/
https://lucid.app/users/login#/login?folder_id=recent
https://app.diagrams.net/
https://www.eggradients.com/gradient/moon-spot
https://blog.logrocket.com/css-header-styles-cross-browser-compatibility/
https://dyatmika.org/students/my-favourite-short-scary-stories/
