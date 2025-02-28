from django.urls import path
from . import views

app_name = 'references'

urlpatterns = [
    path('',views.index, name='home'),

    path('weapons/', views.weapons_list, name='weapons_list'),
    path('programs/', views.programs_list, name='programs_list'),
    path('cyberware/', views.cyberware_list, name='cyberware_list'),
    path('transport/', views.transport_list, name='transport_list'),
    path('roles/', views.roles_list, name='roles_list'),
]
