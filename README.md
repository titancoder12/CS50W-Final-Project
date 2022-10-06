# My CS50W Capstone Project - Zip.it

## Description
My CS50W Capstone Project, Zip.it, is a Django Application which allows multiple people to chat on different channels. Users that register and log in to the application can add channels, chat on channels, invite people to channels, and accept and decline invites to channels.

## Distinctiveness and Complexity
This project was made from scratch. I came up with this idea because I really wanted to do this and it seemed fun to have an application that allowed people to communicate. All the code in this application is based on the lessons learned in the videos and problem sets of this course. My project is **not** a reimplementation of any of the problem sets. It is not a social network because it is a communication tool for texting other people. When compared to social networks, it does not have posting, commenting, or 'liking', which are the basic features most social networks have. On top of that, a social network usually includes many features that allow for networking. My application is merely an application with one feature in mind, texting. Texting may be part of a social network, but by itself it is not one.

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

## Youtube Demo
Click [here](https://www.youtube.com) to watch the demo.

## Application Structure
This application has a front end and a back end. The front end is made with HTML, CSS, Javascript, and Django Templates. The back end is made with Python and Django. The front end calls the back end via an API using JavaScript. The application uses a SQLite3 database.

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

#### Documentation
**requirements.txt** - Required files for application to run  
**README.md** - This file; all instructions and documentation

## Additional Information
A few things to note, just because I wanted to make some things simpler:
- Databases store raw passwords
- Chat messages are not encrypted