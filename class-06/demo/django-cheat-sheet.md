# Django Cheat Sheet

## Create project folder and cd into it
  
- $ mkdir django-things && cd $_
- $ poetry init -n
- $ poetry add django
- $ poetry install
- $ poetry shell
- $ django-admin startproject django_things .
  - Note the . at end

- run it
    ```
    $ python manage.py runserver
    ```
    - Should see "The installer worked successfully!" at http://localhost:8000
    - You can safely ignore the "unapplied migrations" warning for now.

---

## MV*
### Model, View, Template, Url (with settings.py to stitch it together)

- Create an app
  - `$ python manage.py startapp things`
- Add `things.apps.ThingsConfig` to end of `INSTALLED_APPS` section in `settings.py`

---

## Create a View

- edit **things/views.py**
    
	```
	from django.views.generic import TemplateView
	
	
	class HomeView(TemplateView):
	
	    template_name = 'home.html'
	    
    ```
---

## Add the Url

- $ touch **things/urls.py**


	 ```
	from django.urls import path
	from .views import HomeView, AboutView
	
	urlpatterns = [
	    path('', HomeView.as_view(), name='home'),
	    path('about', AboutView.as_view(), name='about'),
	]
	 ```
    
- add the urlpatterns to **things_project/urls.py**

    ```
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('things.urls')),
    ]
    ```
    
- add a template
	- create a 'templates' folder at top level of project, e.g. next to manage.py
	- create `home.html` in templates folder	    
- tell settings where to find the templates
 -     
    ---
    - Run it!
    `$ python manage.py runserver`
