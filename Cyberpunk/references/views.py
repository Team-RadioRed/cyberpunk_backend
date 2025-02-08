from django.http import JsonResponse
from Cyberpunk.db import get_mongo_db

def index(request):
    """Главная страница API"""
    return JsonResponse({'message': 'Добро пожаловать в API Cyberpunk RED'})

def implants(request):
    """Заглушка для страницы имплантов в API"""
    return JsonResponse({'message': 'Раздел имплантов API в разработке'})

def weapons_list(request):
    """API: Список оружия"""

    db = get_mongo_db()  # Подключаемся к базе
    weapons_collection = db["weapon"]

    # Получение данных из MongoDB
    weapons_cursor = weapons_collection.find({})

    # Преобразуем курсор в список и удаляем поле _id
    weapons = []
    for weapon in weapons_cursor:
        weapon.pop('_id', None)  # Удаляем _id, если он есть
        weapons.append(weapon)

    # Проверяем, есть ли данные
    if not weapons:
        return JsonResponse({'message': 'Оружие не найдено', 'weapons': []})

    # Возвращаем данные в формате JSON
    return JsonResponse({'weapons': weapons})


def programs_list(request):
    """API: Список всех программ из коллекции program"""

    # Подключаемся к базе данных
    db = get_mongo_db()
    
    # Выбираем коллекцию program
    programs_collection = db["program"]

    # Получаем все документы из коллекции
    programs_cursor = programs_collection.find({})
    
    # Преобразуем курсор в список
    programs_list = list(programs_cursor)

    # Убираем поле _id из каждого документа
    programs_without_id = []
    for program in programs_list:
        program.pop('_id', None)  # Удаляем _id, если он есть
        programs_without_id.append(program)

    # Проверяем, есть ли данные
    if not programs_without_id:
        return JsonResponse({'message': 'Программы не найдены', 'programs': []})

    # Возвращаем данные в формате JSON
    return JsonResponse({'programs': programs_without_id})