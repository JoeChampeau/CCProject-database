from django.urls import path
from . import views

urlpatterns = [
    path('', views.collection, name='index-collection'),
    path('dir_example', views.directory, name='index-directory')
]