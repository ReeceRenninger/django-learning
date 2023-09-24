from django.urls import path

from . import views # from here import views

urlpatterns = [
  path("", views.index, name="index")
]