from django.urls import path
from . import views

app_name = 'references'

urlpatterns = [
    path('',views.index, name='home'),

    # Страницы для оружия
    path('weapons/', views.weapons_list, name='weapons_list'),  # Список оружия
]
