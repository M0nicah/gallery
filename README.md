# gallery
Gallery App.
Django gallery app that allows you to save your images and stores them in a CDN.

The goal of this project is to provide minimalistic django configurations that stores your image files on a CDN and that anyone can use.

### BDD
An admin uploads an image and when the website is reloaded:
#### Outcomes
  - Then a user should be able to view the image(s) on the home page.\
  - Each Image has an edit and delete button.\
  - When an image is clicked, a pop up modal appears with the image's details.\
  - When the user tries to query the data(from an Image's details e.g category) only relevant images that much the specific query should be displayed.

* [x] A user can view images.
* [x] Only the admin can add new images.
* [x] Each image has its own pop up modal.
* [x] The pop up activates on click.
* [x] The images can be queried.

---

### Technologies Used
- Python
- Django
- PostgresSQL


# Getting Started

First clone the repository from Github and switch to the new directory:
 
    $ git clone https://github.com/M0nicah/gallery.git
  
    $ cd gallery
    
Activate the virtual environment for the project.

     $python3 -m venv virtual
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Then make migrations

    $ python manage.py migrate 
    
Create a super user
    $ python manage.py createsuperuser 

You can now run the development server:

    $ python manage.py runserver


## Author 
Developed by Monica Masae.🚀
