from django.http import JsonResponse
from Cyberpunk.db import get_mongo_db

def index(request):
    """Главная страница API"""
    return JsonResponse({'message': 'Добро пожаловать в API Cyberpunk RED'})

def implants(request):
    """Заглушка для страницы имплантов в API"""
    return JsonResponse({'message': 'Раздел имплантов API в разработке'})

def weapons_list(request):
    """API: Список оружия с фильтрацией"""

    db = get_mongo_db()  # Подключаемся к базе
    weapons_collection = db["weapon"]

    # Получение фильтров из строки запроса
    query = {}
    if (rarity := request.GET.get('rarity', '').strip()) and rarity != "Все":
        query['rarity'] = rarity
    if (weapon_type := request.GET.get('weapon_type', '').strip()) and weapon_type != "Все":
        query['weapon_type'] = weapon_type
    if (skill := request.GET.get('skill', '').strip()):
        query['skill'] = skill
    if (price_category := request.GET.get('price_category', '').strip()):
        query['price_category'] = price_category
    if (sources := request.GET.getlist('source')):  
        query['source'] = {'$in': sources}
    if (official := request.GET.get('official', '').strip()) in ['Да', 'Нет']:
        query['official'] = official == 'Да'

    # Получение данных из MongoDB
    weapons = list(weapons_collection.find(query))
    weapons = [{**weapon, '_id': str(weapon['_id'])} for weapon in weapons]

    if not weapons:
        return JsonResponse({'message': 'Оружие не найдено', 'weapons': []})

    return JsonResponse({'weapons': weapons})