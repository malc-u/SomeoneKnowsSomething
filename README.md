<p align="center">
<img src="https://i.ibb.co/N27FgpP/logoand.png">
</p>

[This website](https://someone-knows-something.herokuapp.com/) was created for English speaking enthusiasts of true crime drama as well as people that like drama in general. Podcast is a form that can be introduced to  people that like books and/or films but find too little time to focus on any of these.

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
- [Information Architecture](#information-architecture)
  - [Database](#database)
  - [Data Storage Types](#data-storage-types)
  - [Collections Data Structure](#collections-data-structure)
    - [Users collection](#users-collection)
    - [Podcasts collection](#podcasts-collection)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [Testing](#testing)
- [Deployment](#deployment)
  - [How to run this project locally](#how-to-run-this-project-locally)
  - [Deployment to Heroku](#deployment-to-heroku)
- [Credits](#credits)
  
# UX

## Project purpose

**As a passionate book reader** as well as a fan of all types of psychological and crime films/series I realized that due to family/work commitments **I hadn't got much  time to concentrate on reading and watching TV but at the same time I used to spend roughly 2 - 2.5 hrs daily in the car - commuting**. Although there is such a thing as audiobooks **I found that podcast**(better structured and in relatively short episodes) **is a better choice**. Podcasts **gave me great opportunity of mixing business with pleasure**.

Despite this I quickly realised that **finding a good podcast was a challenge** in itself. It meant scrolling through a podcast app, trying to listen to something only to realize after 1 episode that this wasn't the right thing. Another option was to **search internet** for top charts created by journalists for newspapers or web portals.

While the first option was very easy to navigate, after couple of uses suggested content was pretty much similar to what I have just finished. Second option was giving me the chance to broaden the content however it meant searching internet for mentioned titles.

**This page recommends limited number of content to unregistered users** however it **gives** opportunity for **a registered user** to check another user's favourite podcasts and to see **all content added by them split into 3 categories** - depending on the podcast origin. It also gives registered user opportunity to access podcast website - via a button - and explore ways of listing to it directly from there.

### Site visitor goals

These goals are:

- Have somewhere to search for podcasts that they are interested in.
- Possibility of reading the plot details before listening to the podcast.
- Knowing that the page is dedicated to this genre and there will not be need of wasting time to find something interesting.

Another/possible goals might be:

- Direct access to podcast website.
- Possibility of listening to the podcast via links.
- Reaching podcasts that are not too popular in users part of the world but that user might find interesting.
- Possibility of finding out who the producer is in order to search for similar content beyond this page.

Someone knows something - True Crime Podcast website is an ideal way to met all these goals as it:

- presents users with true crime podcasts,
- presents users with podcasts from USA, UK and Australia,
- allows users to read more about each podcast,
- allows users to access podcasts pages directly,
- allows users to listen to podcasts via links,
- allows users to easily access producer's page to explore.

### User stories

1. As a user I want the page to be easy to navigate.
2. As a user that is accessing the page from the mobile phone only I want to be able to use it without any problems with content displayed properly.
3. As a true crime podcast listener I want to be able to see content I am interested in.
4. As a busy person I want to have possibility of easily navigating to the content that I can listen to on the go.
5. As a user I want to be able to see more details about the content.
6. As a user that is interested in this genre I want to have link directly to the podcast website.
7. As a user that is aware I might have missed some interesting content from the past I want to have content release year displayed.
8. As a British user I want to have possibility of exploring stories from other parts of the world.
9. As a money savvy user I want to have possibility of accessing content via all means provided by the producer.
10. As a user that relies on recommendations I want to have possibility of finding our what other users like.
11. As a user that likes to stay up to date  I want to see release year to keep on top of new content.
12. As a user that doesn't like long stories and in general prefers films to TV series I want to be able to see how many episodes each podcast have.
13. As a user that likes to share my ideas I want to be able to add/update and delete content to the page for others to enjoy.
14. As a user that values security I want to be able to change my password as and when I want.

## Design choices

<p align="center">
<img src="https://i.ibb.co/dp0bJ2v/multidevice.png">
</p>

### Color scheme

<img src="https://i.ibb.co/pddrtdn/palette.png">

Colors that were picked had be subtle enough not to overwhelm colorful cards of the podcasts covers.

Yellow ![#fad201](https://place-hold.it/15x15/fad201/fad201)#fad201 and black ![#000000](https://place-hold.it/15x15/000000/000000)#000000 were picked to be reminiscent of a tape "POLICE LINE DO NOT CROSS".

Charcoal ![#36454f](https://place-hold.it/15x15/36454f/36454f)#36454f was picked as first thing that comes to mind when we think about crime is "gray" This color it is subtle and corresponds well with yellow and white as well as does not cause distraction for colorful podcasts covers.

Off yellow ![#ffffbf](https://place-hold.it/15x15/ffffbf/ffffbf)#ffffbf was picked to make forms stick out more but to be subtle enough to not overwhelm them.

Finally blue ![#5bc0de](https://place-hold.it/15x15/5bc0de/5bc0de)#5bc0de is a standard Bootstrap "info" class color that was used to differentiate between buttons when more than 1 is present or where there is a need for another color than yellow. It corresponds and compliments remaining colors well.

### Fonts

Font Roboto was picked as it is subtle and well known to many due to being default font for Android phones as well as Google services. It is clean and modern.

Oswald on the other hand, was picked as it displays good (in bold) on the yellow background. It stands out however it does not overwhelms.

### Logo - headline

"Someone Knows Something" - this sentence is the key one. I can risk to say that it appears in 95% of all crime books/films/series or podcasts. It is almost guaranteed that at some point, some character  related to the story will say it.

It was also noted by Canadian film-maker and writer David Ridgen who crated 5 seasons of podcasts with the same name.

### Icons

<img src="https://i.ibb.co/xfXfwNf/myaccount.png">

This website - my account section - uses Font Awesome Icons to direct logged in user to add, listen to, edit or delete podcasts. It also displays an icon to allow user to access password change section.
There is also fingerprint icon in the top left corner of navbar. This used to toggle sidebar. This icon is not displayed on mobile devices.

## Wireframes

Initial wireframes for this project can be seen in the [Wireframes folder](https://github.com/malc-u/SomeoneKnowsSomething/tree/master/wireframes).

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
2. Picture of a phone with earphones attached referring to listening on the go.
3. Question "Already registered?" and button linking to Login page directly next to it.

### Register page

1. Head-word with "Register to Listen Now" - reusing styling of police tape.
2. Form that allows to register to the website. It consists of 3 fields to be filled in and submit button. These 3 fields are:
   - "Username" - displaying information that username is case-sensitive and must be between 5-20 characters
   - "Password" - displaying information that password is case-sensitive and must be between 5-20 characters
   - "Confirm Password" - displaying information to retype the password
3. Question "Already registered?" and button linking to login page directly underneath.

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

1. Head word - Account Dashboard - reusing styling of police tape and  cog icon leading to the change password page on the right.
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

- "Title" - displaying information "Podcast title"
- "Podcast Image Link" - displaying information "Link to podcast cover image
- "Origin" - displaying 3 radio button to chose from - Australia, UK and USA
- "Release Year" - displaying information "YYYY"
- "Description" - displaying information "Plot description"
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
3. Right side (tablets and desktops) and bottom of the page (mobiles) displays form that allows for podcast to be deleted from database therefore from displaying on the page. Form is with 1 field to be filled in and a submit button. This field is called "Enter password to delete".

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

# Information Architecture

## Database

This website is a student project that required for MongoDB to be used.

## Data Storage Types

The types of data stored in the data base for this project are:

- ObjectId
- String
- Boolean
- Integer

## Collections Data Structure

This website relies on two database collections:

### Users collection

| Title      | Key in DB | Validation type                                    | Data type |
|------------|-----------|----------------------------------------------------|-----------|
| Account ID | _id       | None                                               | ObjectId  |
| Name       | username  | text, data required, minlength="5", maxlength="40" | String    |
| Password   | password  | text, data required, minlength="5", maxlength="40" | String    |

[Example JSON - users collection](https://github.com/malc-u/SomeoneKnowsSomething/blob/master/schemas/users.json)

### Podcasts collection

| Title                         | Key in DB      | Validation type                                            | Data type |
|-------------------------------|----------------|------------------------------------------------------------|-----------|
| Podcast ID                    | _id            | None                                                       | ObjectId  |
| Name                          | username       | text, data required, minlength="5", maxlength="40"         | String    |
| Title                         | podcast_title  | text, data required                                        | String    |
| Link to podcast cover picture | podcast_imgurl | url, data required                                         | String    |
| Podcast's country of origin   | origin         | radio field, data required, 1-"UK", 2-"Australia", 3-"USA" | Integer   |
| Year of podcast release       | release_year   | text, data required, minlength="4", maxlength="4"          | String    |
| Description                   | description    | textarea, data required, maxlength="500"                   | String    |
| Number of episodes            | no_episodes    | text, data required, minlength="1", maxlength="3"          | String    |
| Link to the podcast           | podcast_link   | text, data required                                        | String    |
| Is this podcast favourite?    | is_favourite   | checkbox, data required                                    | Boolean   |
| Is this podcast recommended?  | is_recommended | None, default="False"                                      | Boolean   |

- The users username is added to each podcast database entry automatically to match the user who added it to the site. This links the two database collections together.
- The recommended in the database is automatically populated as False. This allows admin to manually amend podcasts to be displayed as recommended on the page visible to all - registered and unregistered users.

[Example JSON - podcasts collection](https://github.com/malc-u/SomeoneKnowsSomething/blob/master/schemas/podcasts.json)

# Technologies

## Languages

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [Python](https://www.w3schools.com/python/)
- [JavaScript](https://www.w3schools.com/js/)

## Libraries

- [JQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/)
- [FontAwesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- [Flask](https://palletsprojects.com/p/flask/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)

## Tools

- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
- [Autoprefixer](https://autoprefixer.github.io/)
- [Balsamiq](https://balsamiq.com/)
- [Imgbb](https://imgbb.com/)
- [Canva](https://www.canva.com/)
- [MongoDB](https://www.mongodb.com/cloud/atlas)
- [JSON Formatter](https://www.freeformatter.com/json-formatter.html)
- [Markdown Table](https://www.tablesgenerator.com/markdown_tables)

# Testing

Testing details can be found in separate [TESTING.md file](https://github.com/malc-u/SomeoneKnowsSomething/blob/master/TESTING.md)

# Deployment

## How to run this project locally

You must have following installed on your machine:

1. IDE such as VS Code or Sublime
2. Python3
3. PIP
4. Git
5. MongoDB running locally on your machine and connected onto your MongoDB Atlas

**Once this is installed you can follow below steps:**

1. **Save** a zip **copy of [this](https://github.com/malc-u/SomeoneKnowsSomething)** Github **repository** using "Clone of download" green button or clone repository dircetly to your IDE using command

```console
git clone https://github.com/malc-u/SomeoneKnowsSomething
```

2. In the terminal of your IDE **open folder with the repository**
3. **Create virtual environment** using command

```console
Windows: python -m venv <name of your virtual environment>
Linux: py3 -m venv <name of your virtual environment>
```

4. **Activate** your **virtual environment** with command

```console
Windows: <name of your virtual environment>\Scripts\activate
Linux: source <name of your virtual environment>\Scripts\activate
```

5. If needed upgrade pip locally using command

```console
Windows: python -m pip install --upgrade pip
Linux: sudo -H pip3 install --upgrade pip
```

6. **Install** all Python **modules** this project depends on using command:

```console
Windows: pip install -r requirements.txt
Linux: pi3 install -r requirements.txt
```

7. **Create** file **`.flaskenv`** in repository and **include MONGO_URI and SECRET_KEY** to your own data base. Please call your **database `sks`** and include **2 collections** in it. First called **`users` and** second called **`podcasts`**. Examples of JSON structure of these collections can be seen in [schemas folder](https://github.com/malc-u/SomeoneKnowsSomething/tree/master/schemas)

8. **Run** this **application** using command:

```console
Windows: python app.py
Linux: python3 app.py
````

9. **Visit website** using following in your browser's address bar

```console
http://127.0.0.1:5000
```

## Deployment to Heroku

To deploy this project to Heroku follow the steps below:

1. **Create file** called `requirements.txt` **using** the **terminal command** `pip freeze > requirements.txt`
2. **Create file** called `Procfile` **with** the **terminal command** `echo web: python app.py > Procfile`
3. `git add` and `git commit` the new requirements and Procfile and then `git push` to **push the project to GitHub**
4. On the Heroku website and by using "New" button **in Heroku dashboard create a new app**, give it a name and set the region to Europe
5. In the **Heroku dashboard** of your newly created application, **click on "Deploy" > "Deployment method"** and **select GitHub**
6. **Confirm the link of** the **Heroku** app **to** the correct **GitHub** repository
7. **Click** on **"Settings" > "Reveal Config Vars" in Heroku** dashboard
8. **Set** the **following** config **vars**:

   - key: **DEBUG** as a value: **False**
   - key: **IP** as a value: **0.0.0.0**
   - key: **PORT** as a value: **5000**
   - key: **MONGO_URI** as a value: **mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority**
   - key: **SECRET_KEY** as a value: **<your_secret_key>**
  
9. **Click "Deploy" in Heroku** dashboard
10. Make sure the **master branch** is **selected in** the **"Manual Deployment"** section of this page and then **click "Deploy Branch"**
11. The site is now successfully deployed

# Credits

This project has been created by me, however some content has been imported such as podcast details, cover pictures, descriptions etc.:

- [Unravell: Showball](https://www.abc.net.au/radio/programs/truecrime/)
- [Who the hell in Hamish?](https://www.theaustralian.com.au/podcasts/podcast-who-the-hell-is-hamish/news-story/c95b519a9ececa6076df80bd130ba158)
- [Missing Cryptoqueen](https://www.bbc.co.uk/programmes/p07nkd84/episodes/downloads)
- [Dr. Death](https://wondery.com/shows/dr-death/)
- [Manhunt: Finding Kevin Parle](https://www.bbc.co.uk/sounds/series/p054dybk)
- [Unheard: The Fred and Rose West Tapes](https://www.somethinelse.com/projects/unheard-the-fred-rose-west-tapes/)
- [What happened to Zac?](https://www.novafm.com.au/podcast/what-happened-to-zac/?amp)
- [The Lady Vanishes](https://7news.com.au/news/the-lady-vanishes)
- [Fake heiress](https://www.bbc.co.uk/programmes/p07y1w0h)
- [The Lighthouse](https://www.theaustralian.com.au/podcasts/the-lighthouse-what-happened-to-theo-hayez/news-story/8a68d51efd1bd28c509c02dc36881fb5)
- [Girl taken](https://www.bbc.co.uk/programmes/m000ghxl)
- [The Clearing](https://gimletmedia.com/shows/the-clearing)
- [Over my dead body - Tally](https://wondery.com/shows/over-my-dead-body/)
- [The Teachers Pet](https://www.theaustralian.com.au/podcasts/the-teachers-pet-the-unsolved-murder-of-lyn-dawson/news-story/da4bb90abff76bbe0f2bd932aa987e2a)
- [Joe Exotic : Tiger King](https://wondery.com/shows/joe-exotic/)
- [Dirty John](https://wondery.com/shows/dirty-john/)
- [Perfect Storm - True stroy of the Chamberlains](https://7news.com.au/entertainment/podcasts/a-perfect-storm-a-seven-west-media-podcast--c-547246)
- [Small Town , Big Crime](https://podcasts.google.com/?feed=aHR0cHM6Ly9mZWVkcy5idXp6c3Byb3V0LmNvbS83MjM5MTUucnNz&ved=0CAAQ4aUDahcKEwiQ_-OP1PToAhUAAAAAHQAAAAAQAQ&hl=en)
- [Beenham Valley Road](https://www.six10mediagroup.com/beenhamvalleyroad)

Following people and their work influenced me and this project:

- [Corey Schafer](https://coreyms.com/) Flask Youtube [tutorial](https://www.youtube.com/watch?v=UIJKdCIEXUQ&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3) - mechanics of using WTForms
- [Romain Dorgueil](https://romain.dorgueil.net/about/) - advice on using request.method in WTForms
- [Simen Daehlin](https://github.com/Eventyret) - Code Institute mentor

I have used following for researching ideas and ways of creating content needed for my page:

- Sidebar - created using ideas from following pages: [Page 1](https://bootstrapious.com/p/bootstrap-sidebar), [Page 2](https://blackrockdigital.github.io/startbootstrap-simple-sidebar/) and [Page 3](https://stackoverflow.com/questions/32244890/my-sidebar-scrollbar-is-not-working)
- Radio fields in forms - [Page 1](https://gist.github.com/doobeh/4667330) and [Page 2](https://wtforms.readthedocs.io/en/2.3.x/fields/)
- Check password hashed - based on [example 9](https://www.programcreek.com/python/example/58659/werkzeug.security.check_password_hash)
- request.method == 'GET' in forms - used following advice from [Page 1](https://romain.dorgueil.net/wiki/python/wtforms) and [Page 2](https://stackoverflow.com/a/23714791)
- Index page picture - comes from [here](https://unsplash.com/photos/TMOeGZw9NY4)
- 404 error picture - comes from [here](https://pixabay.com/vectors/error-404-panel-attention-work-3060993/)
- Logo created using [Canva](https://www.canva.com/)
- Color placeholders created using [Place-Hold](https://place-hold.it/)
- [TextArea and other fields in forms](https://wtforms.readthedocs.io/en/stable/fields.html)
- [Multi Device Website Mockup Generator](https://techsini.com/)
- [Code Pen](https://codepen.io/)
- [Stack overflow](https://stackoverflow.com/)
