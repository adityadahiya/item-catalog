# Udacity Item Catalog

A simple web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users have the ability to post, edit, and delete their own items.

## Usage

#Launch the Vagrant VM from inside the *vagrant* folder with:

vagrant up

#Then access the shell with:

vagrant ssh

#Then move inside the catalog folder:

cd /vagrant/catalog

#Setup the database using:
python database_setup.py

#Populate the database using:
python items.py

#Then run the application:
python project.py`

#After the last command you are able to browse the application at this URL:
http://localhost:5000/

