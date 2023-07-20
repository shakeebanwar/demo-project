## Setup Instructions

Follow these steps to set up the Django project:

1.Clone the repository to your local machine:

git clone https://github.com/shakeebanwar/demo-project.git

2.Install the project dependencies:

pip install -r requirements.txt


## Database Setup

By default, this project uses SQLite as the database. However, you can change the database settings in settings.py to use other databases like PostgreSQL or MySQL.

Run the following commands to apply the initial migrations:

python manage.py migrate


## Running the Development Server

To run the development server, use the following command:

python manage.py runserver

## Test Cases

This project includes test cases to ensure the proper functionality of the registration API. To run the test cases, use the following command:

python manage.py test


## The test cases include the following scenarios:
1.Successful registration with all required fields.
2.Registration with missing required fields.
3.Registration with an invalid email address.



