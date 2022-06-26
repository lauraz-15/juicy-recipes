![logo](README_images/logo.png)

# Juicy Recipes

Link to the live project: [here](https://juicy-recipes.herokuapp.com/)


## Table of Contents 

- [Introduction](#introduction)
- [Features](#features)
- [Wireframes](#wireframes)
- [Design](#design)
- [Database Desing](#database-design)
- [Technologies](#technologies)
- [Testing](#testing)
- [Issues and bugs](#issues-and-bugs)
- [Deployment](#deployment)
- [Credits](#credits)



## Introduction

Juicy Recipes is a platform for users to create and share recipes and interact with other users.
Platform is built using Django Python-based framework, additionally Javascript is used to import and dispplay results from [Edamam API](https://www.edamam.comgclid=EAIaIQobChMIzLWV0qXL-AIVy-vtCh10Hw_ZEAAYASAAEgIS3vD_BwE) search results.


## Features

### Home Page

#### Navigation bar
    - Navigation bar is displayed on all pages providing access to all menu items to users on all pages
    - The list of menu items will change dependign on if the user is logged in, for example, if the user is logged in, then "logout" option will be presented. Also additional menu items will be presented to the logged in users such as "My Favorites", "Add Recipe" and "My Recipes"
    - The nav items are interactive which means that once the user hovers over the items, yellow underline appears to indicate that the item is clickable
    - The navigation menu is responsive, which means it will change to hamburger menu when viewed on smaller screens

![Navigation Menu](README_images/logo.png)


#### Hero Image
    - Hero image is presented on home landing page, which is intended to inform the user what kind of website this is and what it is about.

![Hero image](README_images/logo.png)


#### Footer
    - Footer is visible at the bottom of all pages, it matched the color and design feel of the rest of the site
    - It includes additional information about thw site and useful socal links that when clicked will be opened in a new browser

![footer](README_images/logo.png)

### Inspiration Page
    - Page consists of a list of reciipes organised in 8 different categories from Edamam API request, this lets the user to get some inspiration and see what recipes are available elsewhere. Content is orgnised in a easy to read format, familiar to the user recipes that are available on the other pages.
    - When user clicks on on of the recipes, new page opens where recipe is publihsed, user can read more about it and make their own version of it and then post the recipe on Juicy recipes site whilst referncing the source page.

![Inspiration](README_images/logo.png)

### Search Page
    - Search page has an input field presented as a main item on the page, this helps the user to easily understand that they can search for any recipes
    - Results are presented in a familiar design cards, with the source infomation rigth at the bottom, which helps the user to choose which recipes to pick. 
    -The Search option on Juicy Recipes site lets the user to see the photo of the recipe result straight away, which helpS the user to quickly find what they like without browsing through many sites and spending time.

![Search](README_images/logo.png)

### Recipes
    - The recipes page lists all user recipes that have been posted on Juicy Recipes site by all users, it is easy to browse through the paginated pages without getting lost on the page
    - User can see the likes and comments for each recipe on the all recipes view, this helps the user which recipe is most liked by other users 

![Recipes](README_images/logo.png)

### My favorites
    - My favorites page consist of recipes that logged in user have liked/favorited, this lets the user to easily find the recipes they have liked
    - Users can unlike the recipe, which will remove the recipe from the "My Favorites" page

![My Recipes](README_images/logo.png)

### My Recipes
    - My Recipes page consist of recipes logged in user has created, this lets the user to overview the list of their recipes and easily and quickly access recipes detail page to make edits or delete the recipe
    - By vieiwng this page users can easily overview how many likes and comments each of their created recipe has.

![My Recipes](README_images/logo.png)

### Add Recipe
    - This page presents a form to a user, each field has a description at the top of it, so that users can easily understand what they need to do for each field.
    - Placeholder photo is added to the recipe if the user fails to add a recipe at the time, this encourages user to post the recipes in case the image is not available straight away. They can uplaod the actual photo later on when clicking on "Edit" option on recipe detail page.
    - When "Submit" button is clicked user is directed to "My Recipes" page and user feedback message appears at the top of the page indicating that recipe has been posted, which assures the user that recipe has been published and enables user to immidiately view it on the page where they are directed to.

![Add Recipe](README_images/logo.png)

### Recipe Detail Page
    - Each user recipe page has it's own detail page, whcih lets the user to view each individual recipe details on a seperate page where full content is visible. Information is organsised in sections that lets the user to easily navigate to the information they want to find.
    - The page has the like and comment options that lets the user to interact with the content
    - If logged in user is vieiwng their own recipe there will be "Edit" and "Delete" options presented to the user which gived the user control over the content they have published
    - At the bottom of the recipe details page a comment section is available to users to view user converstaions.
    - If the user is logged in there is an option to leave a comments which lets the user to interact with other users

![Add Recipe](README_images/logo.png)

### Accounts

#### Register Page
    - The register page is available to all users and the link is presented each time a unlogges user is trying to access content that is available only for registered users
    - Sign-up is easy withouth email verification which enables the user to quickly access full functionallity of the site

![Register page](README_images/logo.png)

#### Login Page
    - The login is userd for registered users to access the site
    - If incorrect login details will be entered user will be notified, which lets the user to understand why they have not been logged in.
    - If the log in details ahve been eneterd successfully, then user will be notified with a message appearing at the top of the page which will then time out after 3 seconds.

![Logged-in](README_images/logo.png)

#### Log out Page
    - When user will click on this item on the menu bar, another page will optn up asking the user if they want to log out, this lets the user to controld their action, in case if they have pressed the button by accident.
    - If the user has logged out, a message will appear at the top of the page advising that, which ensures the user that thir account is safe.

![Logged-out](README_images/logo.png)


### Features to add
    - Add category option for user recipes, so that users can filter the categories and quickly find what they are looking for
    - Add photo upload option to comment section, so that users can share their own version of the recipe
    - Contact Us section, so that users can get in contact with site admins

[Back to top ⇧](#juicy-recipes)
