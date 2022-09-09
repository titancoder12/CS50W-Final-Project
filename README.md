# My CS50W Capstone Project - Zip.it

## Overview
My CS50W Capstone Project, Zip.it, is a Django Application which allows multiple people to chat on different channels. Users that register and log in to the application can add channels, chat on channels, invite people to channels, and accept and decline invites to channels.

## Installation
All installation requirements are in the requirements.txt file. Python version is 3.9.12.

## Running the Application
To run the server, just run the following commands:
```
python manage.py migrate
```
to migrate the server and
```
python manage.py runserver
```
to actually run the server.

## Application Structure
This application has a front end and a back end. The front end is made with HTML, CSS, Javascript, and Django Templates. The back end is made with Python and Django. The front end calls the back end via an API.

## Files
chat/views.py - API and views  
chat/models.py - Database structure    
chat/urls.py - Register paths  
chat/admin.py - Register models to admin
chat/templates/chat/channel.html -  
chat/templates/chat/channels.html -  
chat/templates/chat/error.html -  
chat/templates/chat/index.html -  
chat/templates/chat/invite.html -  
chat/templates/chat/invites.html - 
chat/templates/chat/login.html -  
chat/templates/chat/register.html -  
chat/templates/chat/layout.html  -

