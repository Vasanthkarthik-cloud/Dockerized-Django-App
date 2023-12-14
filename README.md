# Dockerized-Django-App

# Description
This repository is focussed on delpoying a django application in a container(Docker). The website consists of two basic static webpages as it focussed more on dockerizing the application rather than building the website and giving it a purpose.

#Setup
The steps involved in the setup are:
1. Install python3(latest version)
2. Install Docker(latest version)
3. Install Django
   
#Procedure
1.Build a web app using django. A simple one can be created using the documentation https://docs.djangoproject.com/en/5.0/
2.Deploy and test the app in your local server.
3.Create a Dockerfile in your project directory and place the contents as mentioned in mysite/Dockerfile. The commands are well explained in the documentation https://docs.docker.com/
4.Create a file called requirements.txt which lists the version requirements of various tools used mainly python and a python WSGI HTTP Server for UNIX called gunicorn. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.
5.Create a file called docker-compose.yml.
