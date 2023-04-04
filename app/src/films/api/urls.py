from django.urls import path
from . import views


urlpatterns_api = [
    path('api/v1/films/', views.main_page)
]
