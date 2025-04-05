from django.http import JsonResponse
from Cyberpunk.db import get_mongo_db

def index(request):
    """Главная страница API"""
    return JsonResponse({'message': 'Добро пожаловать в API Cyberpunk RED'})

def get_collection_data(collection_name, empty_message):
    """Функция для получения данных из MongoDB коллекции"""
    db = get_mongo_db()  
    collection = db[collection_name]  
    cursor = collection.find({}, {"_id": 0})  # Исключаем _id в запросе

    # Если данных нет, возвращаем сообщение
    data = list(cursor)
    if not data:
        return JsonResponse({'message': empty_message, collection_name: []}, status=400)

    return JsonResponse({collection_name: data})

def weapons_list(request):
    """API: Список оружия"""
    return get_collection_data("weapon", "Оружие не найдено")

def programs_list(request):
    """API: Список программ"""
    return get_collection_data("program", "Программы не найдены")

def cyberware_list(request):
    """API: Список имплантов"""
    return get_collection_data("cyberware", "Импланты не найдены")

def transport_list(request):
    """API: Список имплантов"""
    return get_collection_data("transport", "Транспорт не найден")

def roles_list(request):
    """API: Список имплантов"""
    return get_collection_data("role", "Роли не найдены")