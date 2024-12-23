from django.shortcuts import render
from rest_framework import generics
from .models import Weapon, Implant, Program, Demon
# from .serializers import WeaponListSerializer, WeaponDetailSerializer, ImplantListSerializer, ImplantDetailSerializer, ProgramListSerializer, ProgramDetailSerializer, DemonListSerializer, DemonDetailSerializer

def index(request):
    data = {
        'title': 'Главная страница',

    }
    return render(request, 'main/index.html', data)


def implants(request):
    return render(request, 'main/implants.html')

'''
def weapons(request):
    return render(request, 'references/weapons.html')'''

def weapons_list(request):
    weapons = Weapon.objects.all()
    return render(request, 'references/weapons_list.html', {'weapons': weapons})

def weapon_detail(request, id):
    weapon = Weapon.objects.get(id=id)
    return render(request, 'references/weapon_detail.html', {'weapon': weapon})

def implants_list(request):
    implants = Implant.objects.all()
    return render(request, 'references/implants_list.html', {'implants': implants})

# Страница импланта (подробности одного импланта)
def implant_detail(request, id):
    implant = Implant.objects.get(id=id)
    return render(request, 'references/implant_detail.html', {'implant': implant})

# Страница программ (список всех программ)
def programs_list(request):
    programs = Program.objects.all()
    return render(request, 'references/programs_list.html', {'programs': programs})

# Страница программы (подробности одной программы)
def program_detail(request, id):
    program = Program.objects.get(id=id)
    return render(request, 'references/program_detail.html', {'program': program})

# Страница демонов (список всех демонов)
def demons_list(request):
    demons = Demon.objects.all()
    return render(request, 'references/demons_list.html', {'demons': demons})

# Страница демона (подробности одного демона)
def demon_detail(request, id):
    demon = Demon.objects.get(id=id)
    return render(request, 'references/demon_detail.html', {'demon': demon})