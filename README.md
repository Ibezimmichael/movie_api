Overview
This is a simple Django Rest Framework project that provides an API for movies. It allows users to create, read, update and delete movies in a database.

Prerequisites
Python 3.10
pip
Django 3.2
Django Rest Framework
Installation
Clone the repository

Install the required packages with pip:

Copy code
pip install -r requirements.txt
Run the migrations to set up the database:

python manage.py migrate
Start the development server:


python manage.py runserver
Open a web browser and navigate to http://localhost:8000 to see the API documentation.

Usage
The API has the following endpoints:

GET /movies/: Retrieve a list of all movies.
POST /movies/: Create a new movie.
etc