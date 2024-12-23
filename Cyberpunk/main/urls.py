from django.urls import path
from . import views

app_name = 'main'  # Регистрация пространства имен

urlpatterns = [
    path('',views.index, name='index'),
    path('implants', views.implants, name='implants'),
]
