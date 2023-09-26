from django.urls import path
from . import views

urlpatterns = [

    path('start_python_movie_scraping', views.python_movie_scrap)
         ]