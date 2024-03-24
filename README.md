# Braydon's Horror House PROJECT README

### Author Manjula Lal,

## Contents

- Brief
- External user’s goal:
- Site owner's goal
- Project Initial ERD and data base design
- Develop strategy and Wireframe
- Miro Board
- Balsamiq
- Lucid Chart
- Github project and Milestones
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

![iamresponsive](/static/images/iamresponsiveppp.png)

### External user’s goal:

The user requires engaging content that is entertaining to which they would like to visit the site again. Also they want to be a part of a community with people with the same interests,which will also give them the opportunity to share there own content and have there details available, so other users know who put the post up, which will give the user a very personal touch to the website.

### Site owner's goal:

My goal was aimed to entertain users to engage within a community within similar interests. When it comes to spooky stories, there is a very big market for people who find this of interest and my aim was to include some features that are very different to what you see in modern websites and want to continue to develop this site as there is alot of potential for growth. What I wanted to do was to have a wesbite that was not to overpowering so it appeals to the masses, and didnt want people to be left too overwhelmed and stresesd in the enviroment they are reading stories, so I focused purely on the mental aspect alongside creativity.

### Project Initial ERD and data base design

I had created this ERD prior to creating the models so I knew exactly how to design my database which is the vore of this website.
![Project ERD](/static/images/erd3.png)

## Develop strategy and Wireframe

## Miro Board

The Miro Board was the initial tool we used for iteration. The board allowed us to quicky communicate how the over project will be worked on, start until finished, placed all articles and pictures we will be using and the technology that will be used.

## Balsamiq

Balsamiq was used to design the initial idea of the Braydon's Jorrow House website which entailed all user features, navigation and placeholders for pictures that would be incorporated within the website. We had made minor alterations in the finished project to support user friendliness and responsivness

![Balsamiq Wireframe](/static/images/wireframe.png)

## Lucid Chart

I decided to create a visual map of the website so we could clearly conceptualise the project as a whole. As you can see there alot of work left to do for this website and alot of potential of scope.

![Lucid Chart](/static/images/lucidPP.png)

## Github project

For our User Stories, I had decided to use Github project whereby I had designed, based on user requirements, what should be entailed within this project and what I could save for the next iteration. To support this I had also created milestones and issues, which are avilable on Github for you to view.

## Features

- When the user comes to this website, they will see a list of stories which they can click into to read the story. These stories were created via users and which will be in rows of three. The pictures on the car are automated, so whatever the story, the card will contain the same picture as this will create a good consistancy throughout the website.

![stories](/static/images/stories.png)

- The submit story option and drop down form are below the stories section. The user must be logged in to write there story. If they are not, after they have wrote the story and submitted, they will be redirected to the login page.

![submit story and dropdown](/static/images/story-dropdown.png)

- The register page, consist of a disclaimer and functionality to allow the user to create there account sucessfully.

![register Page](/static/images/sign-up-page.png)

- The navbar has the option of a homepage, login and register. When logged in to the website, the navbar has the option to view profile. If the user uploads a pictures, it will be shown in the navbar until the user signs out.

![navbar](/static/images/navbar.png)

- The profile allows the user a more personalised connection to the website and also attract other users to connect with them via there social links, a bio and upload a picture. All these are optional as uploading stories and giving comments only requires the user to be logged in. Also at the bottom of the profile page, the user can see which stories they have added to the website.
  ![profile](/static/images/profile.png)

- When the user uploads a story, when the user clicks on the story title, it brings the user to this page where the full story is available for the viewer. Under the story title will be the details of the user and there picture.

![inside card](/static/images/inside-card.png)

- The comments section, allows the user to write comments under the stories, where they can also edit and delete there comments. This section also calculates how many comments this story has had.

![comments](/static/images/comments.png)

## Styling frontend development

I had decided to use a gradient for the Nav bar, footer and background. I wanted to have an eerie look, but also wanted it to be warm and welcoming so for the navbar and footer, I used the 'moons spot' gradient and then I chose a purple gradient for the rest of the website. I had also used pictures created by AI to give my website a more original and personalised look that would differ it from other sites who attempt to attempt to foster the same entertainment. My attempt to have a both eerie and welcoming website has been successful.

## Fixed Bugs

- The problem I was having was that even though my CSRF_TRUSTED_ORIGINS were correct, the screen my dev screen would keep throwing, error. It was notived then that the numbers at the end of the URL kept iterating by one, so after changing my number at the end of my URL, I was able to see my webpage.

![Iteration issues](/static/images/iteration-issue.png)

- I was having integrity errors, and inroder to fix them, I had to create a new function to rectify the issue.

![Integrity error](/static/images/integrity-error.png)

- The problem was that the URL /stories/set_avatar/ was being matched by the stories_detail pattern instead of the set_avatar pattern. This happened because the set_avatar pattern was defined after the stories_detail pattern in the urlpatterns list.

Django processes URL patterns in the order they are defined, and it stops as soon as it finds a match. Since the stories_detail pattern was defined before the set_avatar pattern, Django matched /stories/set_avatar/ to the stories_detail pattern, causing the post_detail view to be called instead of the set_avatar view.

To resolve this issue, rearranged the urlpatterns list so that the set_avatar pattern is defined before the stories_detail pattern. This ensures that requests to /stories/set_avatar/ are correctly routed to the set_avatar view.

![Issue with URL](/static/images/url.png)

- Before adding the slug field, there were duplicated field declarations within the Story model. This duplication caused confusion and could lead to errors. The corrected version removed the duplicated fields, ensuring clarity and consistency in the model definition-from django.utils.text import slugify

![Slugify](/static/images/slugify.png)

## Unfixed Bug

Though the profile page can be updated as many times as the user wants, the edit button will not work. It is something that will be improved for the next iteration.

## Testing

- All top level links works as expected.

- User Account Creation works as expected.

- User login and logout works as expected.

- User comments and reviews have full CRUD functionality.

## Future features and modifications

Eventually this website will allow users the option to pick an avatar instead of uploading a picture. The decoration of the website is still in working progress whereby the wesite wants to provide the user the ability to listen to the content aswell as reading it. Alongside this, an online shop where users can buy and sell there horror merchandise alongise Braydons merchandise which will consists of books. They will Braydon will act as an intermediary for payments where Braydon will get a share of the price the users items are sold at.

## Tools and Technology used

- HTML used for the main site content.

- CSS used for design website.

- JavaScript used for user interaction.

- Python used for back-end programming.

- Git for version control.

- Bootstrap used alongside CSS to help build faster and help enhance user experience and responsiveness.

- Django used for Python framework.

- ElephantSQL for Postgres database.

- Heroku was used to deploy the back-end.

- Cloudinary used for online static file storage.

## Credits

We would like to give a huge thanks to our facilitator David Calikes and our coding coaches Kevin and Martin at the Code institute for there exceptional guidance and support. I would also like to give a special thanks to my mentor Daisy who has supported me throughout my project

Leonardo.ai was used to create our images for the website.
chat gpt was used to enhance my knowledge, help with identifying bugs and assist with indenting issues
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
