this is the app inside the weather_backend project


packages:
    pip install djangorestframework requests


Step 1: Install Django
pip install django

Step 2: Set Up Django in Your Virtual Environment
Create a virtual environment: Navigate to the directory where you want to create your project and run:
python -m venv env
Activate the virtual environment: Depending on your operating system:

.\env\Scripts\activate
Install Django in the virtual environment: After activating the virtual environment, install Django:

pip install django djangorestframework python-decouple requests django-cors-headers
Check that django-admin is available: Now try running:

django-admin --version

Step 3: Start the Django Project
Once Django is installed and django-admin is recognized, you can create the Django project:

django-admin startproject weather_backend
This should create the weather_backend directory with all the necessary files.

run:
    python manage.py runserver

