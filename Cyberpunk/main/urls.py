from django.urls import path
from . import views

app_name = 'main'  # Регистрация пространства имен

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path("search/", views.global_search, name="global_search"),
]
