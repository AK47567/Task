# Task Management API

## Overview  
This is a Django REST Framework (DRF)-based API for managing tasks. It allows users to create, update and retrieve tasks with various statuses.

## Features  
- Create a new task  
- Retrieve task details  
- Update task status  

## Tech Stack  
- **Backend:** Django, Django REST Framework (DRF)  
- **Database:** PostgreSQL  
- **Authentication:** Django Authentication  

## Setup & Installation  

```sh
#Clone the repository

git clone <repo-url>
cd Task


#Create and activate a virtual environment (For windows)

python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate


#Install required dependencies

pip install -r requirements.txt


#Connect the Database in settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


#Run the migrations 

python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser  # Optional for admin access


#Run/Start the Django Development Server

python manage.py runserver
```


| Method   |         Endpoint           | Description      |
|----------|----------------------------|------------------|
| `POST`   | `/api/task/`               | Create a task    |
| `GET`    | `/api/task/`               | Get all tasks    |
| `GET`    | `/api/task/<id>/`          | Get a task by ID |
| `PUT`    | `/api/task/<id>/`          | Update a task    |
| `POST`   | `/api/user/registration/`  | Register a User  |
| `POST`   | `/api/user/login/`         | Login a User     |


## Key Points to Remember

- User must be logged in to assign, create, update task.
- User must first register before assigning or fetching any Task.
- Unauthenticated Users will get an error of 404.

## Sample API Request

### **POST** `/api/task/`


{ \
    "name": "Test Task", \
    "description": "This is a test.", \
    "type": "Urgent", \
    "status": "Pending" \
}
