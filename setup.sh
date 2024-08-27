#!/bin/bash

# Create project directory
mkdir -p hire_ai/app/routes
mkdir -p hire_ai/app/static/css
mkdir -p hire_ai/app/templates/dashboard

# Create initial files
touch hire_ai/__init__.py
touch hire_ai/config.py
touch hire_ai/requirements.txt
touch hire_ai/run.py

# Create files in app directory
touch hire_ai/app/__init__.py
touch hire_ai/app/models.py
touch hire_ai/app/routes/__init__.py
touch hire_ai/app/routes/auth.py
touch hire_ai/app/routes/main.py
touch hire_ai/app/static/css/styles.css
touch hire_ai/app/templates/base.html
touch hire_ai/app/templates/login.html
touch hire_ai/app/templates/signup_applicant.html
touch hire_ai/app/templates/signup_recruiter.html
touch hire_ai/app/templates/dashboard/applicant_dashboard.html
touch hire_ai/app/templates/dashboard/recruiter_dashboard.html
