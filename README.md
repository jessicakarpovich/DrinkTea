Project Tea
========

Project Tea is a website that uses a Django backend to hold information about specific teas.

Components
----------
    - Home Page with information about why I made it
    - A Teas Page that lists all of the Teas from my datatbase with an image of each
    - A Tea Detail Page for each Tea that includes two images, a description of the tea, and a list of ways it can be prepared.
    
Installaton
-----------
To get started, install Python 3 and Django

    https://docs.djangoproject.com/en/1.11/topics/install/

Note: You probably also want to install pip3.

Currently I am using Python 3.6.2 and Django 1.11.4 for this project.

Getting Started
-----------------
To run the website on your computer, (assuming you are using a Mac, if not, it may be a bit different)

    - open up a Terminal
    - cd into the teawebsite folder which holds the manage.py file
    - run the command: python3 manage.py runserver
    - open up a browser and enter the following URL 127.0.0.1:8000/
    
There you go, now you should be on the Home Page.
To access the admin page and make changes go to 127.0.0.1:8000/admin/
The current superuser has username: demo, email: demo@example.com, password: demopassword

Note About Images in Tea List
---------------------------------
If adding or changing the images in the tea/static/imgs folder, be sure that they are all of the same height.
If not, you can get some odd results such as some rows might start on the right side instead of the left.
