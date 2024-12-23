from django.urls import path
from . import views

app_name = 'references'

urlpatterns = [
    path('',views.index, name='home'),

    # Страницы для имплантов
    path('implants/', views.implants_list, name='implants-list'),
    path('implants/<int:id>/', views.implant_detail, name='implant-detail'),

    # Страницы для программ
    path('programs/', views.programs_list, name='programs-list'),
    path('programs/<int:id>/', views.program_detail, name='program-detail'),

    # Страницы для демонов
    path('demons/', views.demons_list, name='demons-list'),
    path('demons/<int:id>/', views.demon_detail, name='demon-detail'),

    # Страницы для оружия
    path('weapons/', views.weapons_list, name='weapons-list'),  # Список оружий
    path('weapons/<int:id>/', views.weapon_detail, name='weapon-detail'),  # Детали оружия
    '''
    path('weapons/', WeaponListView.as_view(), name='weapon-list'),
    path('weapons/<int:id>/', WeaponDetailView.as_view(), name='weapon-detail'),
    '''
]
