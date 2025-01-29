from django.shortcuts import render
from bson.objectid import ObjectId
from django.http import Http404
from Cyberpunk.db import get_mongo_db

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
    """Список оружия с фильтрацией и сортировкой"""

    db = get_mongo_db()  # Подключаемся к базе
    weapons_collection = db["weapon"]  #  Получаем коллекцию

    # Получение фильтров из строки запроса
    rarity = request.GET.get('rarity', '').strip()
    weapon_type = request.GET.get('weapon_type', '').strip()
    skill = request.GET.get('skill', '').strip()
    price_category = request.GET.get('price_category', '').strip()
    source = request.GET.get('source', '').strip()
    official = request.GET.get('official', '').strip()

    # Формирование запроса к базе
    query = {}
    if rarity and rarity != "Все":
        query['rarity'] = rarity
    if weapon_type and weapon_type != "Все":
        query['weapon_type'] = weapon_type
    if skill:
        query['skill'] = skill
    if price_category:
        query['price_category'] = price_category
    if source:
        query['source'] = source
    if official in ['Да', 'Нет']:
        query['official'] = official == 'Да'

    # Получение данных из MongoDB
    weapons = list(weapons_collection.find(query))

    # Преобразование ObjectId в строку для шаблона
    for weapon in weapons:
        weapon['_id'] = str(weapon['_id'])

    # Передача данных в шаблон
    return render(request, 'references/weapons_list.html', {'weapons': weapons})
