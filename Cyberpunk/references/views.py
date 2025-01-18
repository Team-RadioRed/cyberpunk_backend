from django.shortcuts import render
from bson.objectid import ObjectId
from django.http import Http404
from django.conf import settings

weapons_collection = settings.MONGO_DB["weapons"]

def index(request):
    """Главная страница"""
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)

def implants(request):
    """Страница имплантов"""
    return render(request, 'main/implants.html')

def weapons_list(request):
    """Отображение списка оружия"""
    collection = settings.MONGO_DB["weapons"]
    weapons = list(collection.find({}, {"_id": 1, "name": 1}))
    for weapon in weapons:
        weapon["id"] = str(weapon.pop("_id"))  # Заменяем _id на id
    return render(request, "references/weapons_list.html", {"weapons": weapons})

def weapon_detail(request, weapon_id):
    """Отображение деталей оружия"""
    collection = settings.MONGO_DB["weapons"]
    try:
        weapon = collection.find_one({"_id": ObjectId(weapon_id)})
        if weapon is None:
            raise Http404("Weapon not found")
        weapon["_id"] = str(weapon["_id"])
        return render(request, "references/weapon_detail.html", {"weapon": weapon})
    except Exception:
        raise Http404("Invalid ID")