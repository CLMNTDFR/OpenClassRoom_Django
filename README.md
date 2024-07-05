# Django exercices

Welcome to this repository dedicated to learning the Django Framework.
In this project, you will see that I have developed the following skills:
- Installing Django via a virtual environment
- Initialized a basic project with the appropriate dependencies
- Started a server and created a database
- Created a sub-application that I installed in the project
- Created views with HTTP responses
- Separated the application logic with a Django template
- Added style with CSS
- Performed CRUD operations via the Django administrator
- Linked data to views
- Use of DjangoForms and ModelForm

I turned the project to create a web application similar to a social network.
The aim of this network is to share groups from the Lille underground scene.
A user will be able to authenticate in order to share various information about a music group, such as its contact details, its derivative products and its events using typical "CRUD" operations.<br><br>
For now, I've named this interface N.U.B for "North Underground Bands".
Feel free to browse the site and navigate through structured data.<br><br>
I am open to any avenues for improvement!

# Memo for a quick start

1. <strong>Create env:</strong><br>
- `python -m venv env`

2. <strong>Activate env:</strong><br>
- `source env/bin/activate`

3. <strong>Install Django into env:</strong><br>
- `pip install django`

4. <strong>Keep track of packages in a file requirements.txt:</strong><br>
- `pip freeze > requirements.txt`

5. <strong>Magic operation with:</strong><br>
- `django-admin startproject merchex`
<br>to initialize an empty project.

6. <strong>Run a server:</strong><br>
- `cd merchex`<br>
- `python3 manage.py runserver`<br>
(`manage.py` is the new `django-admin`)<br>
💡 You can view a graphical interface of your website at http://127.0.0.1:8000/

7. <strong>Create project's database:</strong><br>
- Press `Ctrl+C` to exit the running server.
- `python3 manage.py migrate`<br>
💡 You will see a new file named `db.sqlite3` in your `merchex` folder. Add `db.sqlite3` to your .gitignore.

8. <strong>Create a first sub-application:</strong><br>
Each application or sub-application will have a specific role.<br>
Our first app is called "listings":<br>
- `python3 manage.py startapp listings`<br>
💡 You will see a new folder named `listings`

9. <strong>Install app in project:</strong><br>
Go the your file `merchex/merchex/settings.py` and add your new app 'listings' in 'INSTALLED_APPS':
```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'listings',
]
```