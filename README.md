# django-learning

- This repo was created using the django quickstart guide found [here](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
- This repo is for learning django and will be used to create a simple poll app

## django commands

1. creating the project `django-admin startproject <project_name>`
1. running the server `python manage.py runserver` this defaults to port 8000 but you can run it on a different port by adding the port number at the end of the command
1. creating the app `python manage.py startapp <app_name>` apps can be thought of as modules, they can be created at differnet levels of the project that will affect how they are used, for this repo we will be creating them at the same level as the manage.py file, which is located in the same directory as the project_name folder
1. To create a simple view, we head over to the views.py and implement this code:

   ```python
    from django.http import HttpResponse


    def index(request):
      return HttpResponse("Hello, world. You're at the polls index.") 
    ```

1. We then need to create a urls.py with this code:

   ```python
    from django.urls import path

    from . import views

    urlpatterns = [
      path('', views.index, name='index'),
    ]
    ```

1. Next is to point the URLconf at the polls.url module, head over to django_learning/urls.py and import django.urls.include and insert the urlpatterns list.

    ```python
      from django.contrib import admin
      from django.urls import include, path
  
      urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
      ]
      ```

1. Now we can run the server and go to the url `http://localhost:8000/polls/` and we should see the text we put in the views.py file. At http://8000/polls/ you should see "Hello hacker, you're at the polls index." if you followed my text input.

