from django.http import JsonResponse
from Cyberpunk.db import get_mongo_db

def index(request):
    """Главная страница API"""
    return JsonResponse({'message': 'Добро пожаловать в API Cyberpunk RED'})

def get_collection_data(collection_name, empty_message, response_key):
    """Функция для получения данных из MongoDB коллекции"""
    db = get_mongo_db()  
    collection = db[collection_name]  
    cursor = collection.find({}, {"_id": 0})  # Исключаем _id в запросе

    # Если данных нет, возвращаем сообщение
    data = list(cursor)
    if not data:
        return JsonResponse({'message': empty_message, response_key: []})

    return JsonResponse({response_key: data})

def weapons_list(request):
    """API: Список оружия"""
    return get_collection_data("weapon", "Оружие не найдено", "weapons")

def programs_list(request):
    """API: Список всех программ из коллекции program"""
    return get_collection_data("program", "Программы не найдены", "programs")

def cyberware_list(request):
    """API: Список всех имплантов из коллекции cyberware"""
    return get_collection_data("cyberware", "Импланты не найдены", "cyberware")