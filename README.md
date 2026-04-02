# Notes app

This is a project for University of Helsinki Data Science course Cyber security base. The aim of the project is to develop a simple web application with at least five OWASP top ten list security flaws along with fixes to the flaws. In this project I have used the 2017 version of the OWASP top ten list. This is done in order to gain understanding of developing a safe web application. The five flaws from the OWASP list I have picked for this project are sql injection, security misconfiguration, cross-site scripting (XSS) and broken access control. CSRF, which is not on the OWASP list, is also added to the project because it was allowed in the course's description.

The app itself is just a simple app which allows users to add, edit and delete notes. All users can see all the notes posted in the app, but only the writer of a specific note can edit and delete note. In order to add, edit and delete notes, user has to create a username and a password.

## Installation
First install Python and Django if you don't have them installed already. Django can be installed with the following command:

```
python -m pip install Django
```

Then clone the git repository to your computer using git clone command. After cloning apply database migrations with the following command:

```
python manage.py migrate
```

After this you can run the development server with command:

```
python manage.py runserver
```

The app can be opened in browser at address:

```
http://127.0.0.1:8000/
```
