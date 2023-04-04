from django.urls import path

from .api.urls import urlpatterns_api
from . import views


app_name = 'films'

urlpatterns = [
    path('films/', views.MainPageListView.as_view(), name="home"),
    path('films/<int:film_id>/', views.film_detail, name='film_detail'),
    path('films/film_category/<int:cat_id>/', views.filter_films_by_category,
         name='by_category'),
    path('films/create/', views.CreateFilm.as_view(), name='create') 

] 

urlpatterns += urlpatterns_api

