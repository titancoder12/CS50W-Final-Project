# My CS50W Capstone Project - Zip.it

## Description
My CS50W Capstone Project, Zip.it, is a Django Application which allows multiple people to chat on different channels. Users that register and log in to the application can add channels, chat on channels, invite people to channels, and accept and decline invites to channels.

## Overview
Ever since the dawn of civilization, communication has become essential for humans. We humans love to talk, and now that technology has advanced greatly, we can talk. A lot. 
    
I built this website because I thought it would be cool if I could make an real time application to let me chat with my friends.

## Installation
All installation requirements are in the requirements.txt file. Python version is 3.9.12.

## Running the Application
First, make sure all the requirements.txt files are installed.
To run the server, `cd` into the directory which you downloaded previously. Then, run
```
python manage.py migrate
```

to migrate the server and
```
python manage.py runserver
```
to actually run the server.

## Distinctiveness and Complexity
My project is 

## Youtube Demo
Click [here](https://www.youtube.com) to watch the demo.

## Application Structure
This application has a front end and a back end. The front end is made with HTML, CSS, Javascript, and Django Templates. The back end is made with Python and Django. The front end calls the back end via an API using JavaScript.

## Files
#### Code
**chat/views.py** - API and views  
**chat/models.py** - Database structure    
**chat/urls.py** - Register paths  
**chat/admin.py** - Register models to admin

#### Django Templates
**chat/templates/chat/channel.html** - Displays chat channel  
**chat/templates/chat/channels.html** - Displays all channels   
**chat/templates/chat/error.html** - Error page  
**chat/templates/chat/index.html** - Displays for landing page  
**chat/templates/chat/invite.html** - Displays form to invite  
**chat/templates/chat/invites.html** - Displays invites  
**chat/templates/chat/login.html** - Displays form to login   
**chat/templates/chat/register.html** - Displays form to register   
**chat/templates/chat/layout.html**  -  Layout for all forms

#### Javascript for Templates
**chat/static/chat/channel.js** - Contacts API to add and read messages in a channel  
**chat/static/chat/channels.js** - Contacts API to list out all the channels  
**chat/static/chat/index.js** - Javascript for index.html  
**chat/static/chat/invite.js** -  Contacts API to invite people to channels  
**chat/static/chat/invites.js** - Contacts API to list out all invites, and also accepts and declines invites   

#### Styling
**chat/static/chat/styles.css** - Styles for all the templates