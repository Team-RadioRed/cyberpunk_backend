from django.urls import path
from . import views

app_name = 'references'

urlpatterns = [
    path('',views.index, name='home'),

    # Страницы для оружия
    path('weapons/', views.weapons_list, name='weapons_list'),  # Список оружия
    path('weapons/<str:weapon_id>/', views.weapon_detail, name='weapon_detail'),  # Детали оружия
]
