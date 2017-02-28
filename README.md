# Item Catalog
##
### Overview

This is the 5th project in Udacity Full Stack Web Developer Nanodegree. The objective is to develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

This project introduces one of the most popular python web framework, flask, and the Oauth for gmail and facebook authentication and authorization system. 

### Setup
1. Install [Vagrant](http://vagrantup.com/) and [VitrualBox](https://www.virtualbox.org/).
2. Clone the [fullstack-nanodegree-vm repository](http://github.com/udacity/fullstack-nanodegree-vm) to get the Vagrant setup file.
3. Clone [this repository](https://github.com/jtang10/TournamentResults) to your local machine and replace all the files in `vagrant/tournament/`
4. Launch Vagrant VM.
5. To create the psql database, navigate to psql with `psql` and use command `\i itemcatalog.sql` to create the database.
6. To initilize the database and populate it with examples, run the **database_setup.py** followed by **lotsofitems.py**
7. Run **webserver.py** to initialize the website. navigate to `http://localhost:5000` in the browser to access the web application.
