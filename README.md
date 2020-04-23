<p align="center">
<img src="https://i.ibb.co/N27FgpP/logoand.png">
</p>

This website was created for English speaking enthusiasts of true crime drama as well as people that like drama in general. Podcast is a form that can be introduced to  people that like books and/or films but find too little time to focus on any of these.

- [UX](#ux)
  - [Project purpose](#project-purpose)
    - [Site visitor goals](#site-visitor-goals)
    - [User stories](#user-stories)
  - [Design choices](#design-choices)
    - [Color scheme](#color-scheme)
    - [Fonts](#fonts)
    - [Logo - headline](#logo---headline)
    - [Icons](#icons)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Existing features](#existing-features)
    - [Every page](#every-page)
    - [Home page](#home-page)
    - [Register page](#register-page)
    - [Login page](#login-page)
    - [Recommended page](#recommended-page)
    - [User picks page](#user-picks-page)
    - [Australian, British and American page](#australian-british-and-american-page)
    - [My account page](#my-account-page)
    - [Add podcast page](#add-podcast-page)
    - [Edit/Update podcast page](#editupdate-podcast-page)
    - [Read more page](#read-more-page)
    - [Delete podcast page](#delete-podcast-page)
    - [Password change page](#password-change-page)
  - [Features left to implement in the future](#features-left-to-implement-in-the-future)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  
# UX

## Project purpose

As a passionate book reader as well as a fan of all types of psychological and crime films/series I realized that due to family/work commitments I hadn't got much  time to concentrate on reading and watching TV but at the same time I used to spend roughly 2 - 2.5 hrs daily in the car - commuting. Although there is such a thing as audiobooks I found that podcast(better structured and in relatively short episodes) is a better choice. Podcasts gave me great opportunity of mixing business with pleasure.

Despite this I quickly realised that finding a good podcast was a challenge in itself. It meant scrolling through a podcast app, trying to listen to something only to realize after 1 episode that this wasn't the right thing. Another option was to search internet for top charts created by journalists for newpapers or web portals.

While the first option was very easy to navigate, after couple of uses suggested content was pretty much similar to what I have just finished. Second option was giving me the chance to broaden the content however it meant searching internet for mentioned titles.

This page recommends limited number of content to unregistered users however it gives opportunity for a register user to check another user's favourite podcasts and to see all content added by them split into 3 categories - depending on the podcast origin. It also gives registered user opportunity to access podcast website - via a button - and explore ways of listing to it directly from there.

### Site visitor goals

These goals are:

- Have somewhere to search for podcasts that they are interested in.
- Possibility of reading the plot details before listening to the podcast.
- Knowing that the page is dedicated to this genre and there will not be need of wasting time to find something interesting.

Another/possible goals might be:

- Direct access to podcast website.
- Possibility of listening to the podcast via links.
- Reaching podcats that are not too popular in users part of the world but that user might find interesting.
- Possibility of finding out who the producer is in order to search for similar content beyond this page.

Someone knows something - True Crime Podcast website is an ideal way to met all these goals as it:

- presents users with true crime podcasts,
- presents users with podcasts from USA, UK and Australia,
- allows users to read more about each podcast,
- allows users to access podcasts pages directly,
- allows users to listen to pdcasts via links,
- allows users to easily access producters page to explore.

### User stories

1. As a user I want easy the page to be easy to navigate.
2. As a user that is accessing the page fromt he mobile phone only I want to be able to use it without any problems with content displayed properly.
3. As a true crime podcast listener I want to be able to see content I am interested in.
4. As a busy person I want to have possibility of easily navigating to the content that I can listen to on the go.
5. As a user I want to be able to see more details about the content.
6. As a user that is interested in this genre I want to have link directly to the producer webiste.
7. As a user that is aware I might have missed some interesting content fromt he pas I want to have content release year displayed.
8. As a British user I want to have possibility of exploring sotries from other parts of the world.
9. As a money savvy user I want to have possibility of accessing content via all means provided by the producer.
10. As a user that relies on recommendations I want to have possibility of finding our what other users like.
11. As a user that likes to stay up to date  I want to see release year to keep on top of new content.
12. As a user that doesn't like long stories and in general prefers fils to Tv series I want to be able to see how many episodes each podcast have.
13. As a user that likes to share my ideas I want to be able to add/update and delete content to the page for oters to enjoy.
14. As a user that values security I want to be able to change my password as and when I want.

## Design choices

<p align="center">
<img src="https://i.ibb.co/dp0bJ2v/multidevice.png">
</p>

### Color scheme

<img src="https://i.ibb.co/pddrtdn/palette.png">

Colors that were picked had be subtle enough not to overwhelm colorful cards of the podcasts covers.

Yellow #fad201 and black #000000 were picked to be reminiscent of a tape "POLICE LINE DO NOT CROSS".

Charcoal #36454f was picked as first thing that comes to mind when we think about crime is "gray" This color it is subtle and corresponds well with yellow and white as well as does not cause distraction for colorful podcasts covers.

Off yellow #ffffbf was picked to make forms stick out more but to be subtle enough to not overwhelm them.

Finally blue #5bc0de is a standard Bootstrap "info" class color that was used to differentiate between buttons when more than 1 is present or where there is a need for another color than yellow. It corresponds and compliments remaining colors well.

### Fonts

Font Roboto was picked as it is subtle and well known to many due to being default font for Android phones as well as Google services. It is clean and modern.

Oswald on the other hand, was picked as it displays good (in bold) on the yellow background. It stands out however it does not overwhelms.

### Logo - headline

"Someone Knows Something" - this sentence is the key one. I can risk to say that it appears in 95% of all crime books/films/series or podcasts. It is almost guaranteed that at some point, some character  related to the story will say it.

It was also noted by Canadian filmmaker and writer David Ridgen who crated 5 seasons of podcasts with the same name.

### Icons

<img src="https://i.ibb.co/S08R8XP/myaccount.png">

This website - my account section - uses Font Awesome Icons to direct logged in user to add, listen to, edit or delete podcasts. It also displays an icon to allow user to acces password change section.
There is also fingerprint icon in the top left corner of navbar. This used to toggle sidebar. This icon is not displayed on mobile devices.

## Wireframes

Initial wireframes for this project can be seen in the [Wireframes folder](https://github.com/malc-u/SomeoneKnowsSomething/tree/master/static/wireframes).

# Features

## Existing features

### Every page

1. Navbar (all sizes of screens, collapsed into burger toggler button on mobiles and smaller tablets e.g. iPads):
   - Brand name "Someone Knows Something"(mobiles only) - on top left hand side - with link to home page.
   - The navigation bar features a fingerprint button that toggles sidebar in the top left corner (tablets and desktops only).
   - For visitors to the site that are not logged in, list items links are available for them to use:
      - Home
      - Podcasts -> collapsing to 2 -> Recommended & -> User Picks
      - Login
      - Register
   - For users that are logged in, the list items are as follows:
      - Home
      - Podcasts collapsing to 5 -> Recommended, -> User Picks, -> Australian, -> British & -> American
      - Hello "Logged in username" collapsing to 3 -> My account, -> Add Podcast & -> Logout
2. Sidebar (tablets and desktops only):
   - The sidebar features "Someone Knows Something" logo on the top with link to the home page.
   - For visitors to the site that are not logged in, list items links are available for them to use:
      - Recommended
      - User Picks
      - Login
      - Register
   - For users that are logged in, the list items are as follows:
     - Recommended
     - User Picks
     - Australian
     - British
     - American
3. Footer includes:
   - links to social media, however not personalized yet as they have not been created yet
   - copyright information
   - link to the author github account

### Home page

1. Head-word with sub-title of the page "True Crime Podcasts" that is reminiscent of a tape "POLICE LINE DO NOT CROSS".
2. Picture of a phone with earphones attached reffering to listening on the go.
3. Question "Already registered?" and button linkin to Login page directly next to it.

### Register page

1. Head-word with "Register to Listen Now" - reusing styling of police tape.
2. Form that allows to register to the website. It consists of 3 fields to be filled in and submit button. These 3 fields are:
   - "Username" - displaying information that username is case-sensitive and must be between 5-20 characters
   - "Password" - displaying information that password is case-sensitive and must be between 5-20 characters
   - "Confirm Password" - displaying information to retype the password
3. Question "Already registered?" and button linking to login page directly undeneath.

### Login page

1. Head-word with "Please Login" - reusing styling of police tape.
2. Form that allows to login to the website. It consists of 2 fields to be filled in and submit button. These 2 fields are:
   - "Username" - displaying information "Please enter your username"
   - "Password" - displaying information "Please enter your password"

### Recommended page

 1. Head-word with "Recommended" - reusing styling of police tape
 2. 8 different podcasts displayed in order form the most recent to the oldest. Each one is displayed as follows:
    - Podcast cover picture displayed using Bootstrap class "card-img-top"
    - Podcast title using Bootstrap "card-title" class within container using Bootstrap "card-body" class
    - Two buttons also within container using Bootstrap "card-body" class:
      - Read More - leading to Read More page
      - Login to listen - for users that are not logged in - leading to Login page
      - Listen here - for users that are logged in - leading to podcast producer website that consists links where podcasts can be listened to.

### User picks page

 1. Head-word with "Users favourites" - reusing styling of police tape
 2. 8 different podcasts displayed in order form the most recent to the oldest. Each one is displayed as follows:

- Podcast cover picture displayed using Bootstrap class "card-img-top"
- Podcast title using Bootstrap "card-title" class within container using Bootstrap "card-body" class
- Two buttons also within container using Bootstrap "card-body" class:
  - Read More - leading to Read More page
  - Login to listen - for users that are not logged in - leading to Login page
  - Listen here - for users that are logged in - leading to podcast producer website that consists links where podcasts can be listened to.

### Australian, British and American page

All these pages are the same except the content they display. They all display content for logged in users from country of origin as in the name of the page.

1. Head-word with "Origin: {{origin as in page title}}" - reusing styling of police tape
2. Podcast cover picture displayed on the left (tablets and desktops) and on the top (mobiles).
3. Podcast title and release date displayed in bold on the right (tablets and desktops) and on directly underneath the picture (mobiles).
4. Podcast description - on the right (tablets and desktops) and on directly underneath the title(mobiles).
5. Number of episodes in the podcast - directly under the description.
6. "Listen here" button that leads to the podcast website - places directly underneath the episode numbers section.

If somehow user that is not logged in lands on this page they will be redirected to login page.

### My account page

1. Head word - my account on the left and cog icon leading to the change password page on the right.
2. Below this is the Podcasts section and in the top right corner of it there is a + icon that leads to add podcast page.
3. Directly below this there is a list of podcasts that were added by the logged in user.
4. Podcast cover picture displayed on the left (tablets and desktops) and on the top (mobiles).
5. Podcast title and release date displayed in bold to the right of the picture (tablets and desktops) and on directly underneath the picture (mobiles).
6. Set of 3 icons displayed in to the right of the title and release date (bigger tablets and desktops) and on directly underneath the picture (smaller tablets and mobiles). These icons are:
   - headphones icon - leading user to podcast website
   - edit icon (pencil and paper icon) - leading user to podcast update page
   - delete icon (trash icon) - leading user to delete podcast page.
7. Podcast description - to the right of the picture (tablets and desktops) and on directly underneath the title and icons (smaller tablets and mobiles).
8. Number of episodes in the podcast - directly under the description.

If somehow user that is not logged in lands on this page they will be redirected to login page.

### Add podcast page

1. Head-word with "Add podcast" - reusing styling of police tape.
2. Form that allows to add podcast to the database and display on the website. It consists of 8 fields to be filled in and submit button. These 8 fields are:

- "Title" - displaying information "Plodcast title"
- "Podcast Image Link" - displaying information "Link to podcast cover image
- "Origin" - displaying 3 radio button to chose from - Australia, UK and USA
- "Release Year" - displaying information "YYYY"
- "Description" - displayng information "Plot description"
- "Favourite" - allowing user to check or leave unchecked this box
- "Number of Episodes" - displaying information "e.g. 8"
- "Link To Podcast Website" - displaying information "Link to podcast's official page"

If somehow user that is not logged in lands on this page they will be redirected to login page.

### Edit/Update podcast page

1. Head-word with "Edit podcast" - reusing styling of police tape.
2. Form that allows to edit podcast and update the database. It consists of 8 pre-populated fields ready to be amended and a submit button. These 8 fields are:

- "Title"
- "Podcast Image Link"
- "Origin""Release Year"
- "Description"
- "Favourite"
- "Number of Episodes"
- "Link To Podcast Website"

If somehow user that is not logged in lands on this page they will be redirected to login page.

### Read more page

1. Head-word with "{{podcast title}}" - reusing styling of police tape.
2. Podcast cover picture.
3. Podcast release date.
4. Podcast description.
5. Number of episodes.
6. Button "Listen here" leading to the podcast page.

### Delete podcast page

1. Head-word with "{{podcast title}}" - reusing styling of police tape.
2. Left side (tablets and desktops) and top of the page (mobiles) - displays contents of Read more page
3. Right side (tablets and desktops) and bottom of the page (mobiles) displays form thah allows for podcast to be deleted from database therefore from displaying on the page. Form is with 1 field to be filled in and a submit button. This field is called "Enter password to delete".

### Password change page

1. Head-word with "Password change" - reusing styling of police tape.
2. Form that allows for password to be changed. It consists of 2 fields to be filled in and submit button. These fields are:

- "Enter New Password" that displays information "Case-sensitive, 5-20 characters"
- "Confirm New Password" that displays information "Repeat Password"

## Features left to implement in the future

I would want to include:

1. Reviews to be left for each podcast.
2. Possibility to be logged in using e-mail not only username
3. Podcasts to be searched using not by origin but e.g. number of episodes or release year.
4. Assign subject to each podcast (such as missing person, murder, fraud etc.) that can be also used to filter down the podcasts by the user.
5. Possibility of adding podcast to own "To listen folder" from origin page etc.

# Technologies

## Languages

- HTML
- CSS
- Python
- JavaScript

## Libraries

## Tools

# Testing

# Deployment

# Credits
