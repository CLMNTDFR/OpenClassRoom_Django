## Init: Django Project:

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
## Create page/views:

1. <strong>Open `listings/views.py` and add:</strong><br>
```
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')
```



