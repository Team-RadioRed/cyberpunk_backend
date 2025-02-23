from django.urls import path
from main.views import global_search
from . import views

app_name = 'main'  # Регистрация пространства имен

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path("search/", global_search, name="global_search"),
]
