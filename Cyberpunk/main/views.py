from django.http import JsonResponse
from Cyberpunk.db import get_mongo_db
from pymongo import ASCENDING
from fuzzysearch import find_near_matches

# Заглушка для главной страницы
def main_page(request):
    try:
        db = get_mongo_db()
        collections = db.list_collection_names()
    except Exception as e:
        return JsonResponse({"message": "Ошибка подключения к базе", "details": str(e)}, status=500)
    
    news_collection = db['news']
    news = news_collection.find().sort('date', -1).limit(5)  # Сортируем по дате, ограничиваем 5 последними новостями
    
    return JsonResponse({
        'directories': [{'name': collection} for collection in collections],
        'news': list(news)
    })

def search_in_collections(db, collections, search_filter, query):
    """Функция для поиска в коллекциях по фильтру и обработке совпадений."""
    results = []

    # Проходим по каждой коллекции и ищем совпадения
    for collection_name in collections:
        collection = db[collection_name]
        cursor = collection.find(search_filter, {"_id": 0}).sort("name.ru", ASCENDING).limit(10)
        results.extend(cursor)

    # Если нет результатов, ищем совпадения по близким названиям
    if not results:
        matched_ids = []  # Список для хранения ID совпавших объектов
        for collection_name in collections:
            collection = db[collection_name]
            cursor = collection.find({}, {"name.ru": 1, "name.en": 1, "_id": 1})  # Получаем поля названий и айди

            for item in cursor:
                name_ru = item.get("name", {}).get("ru", "")
                name_en = item.get("name", {}).get("en", "")  # Извлекаем ру и англ названия для поиска по ним

                # Проверяем, насколько похоже введенное слово на названия в базе
                if find_near_matches(query, name_ru, max_l_dist=1) or find_near_matches(query, name_en, max_l_dist=1):
                    matched_ids.append(item["_id"])  # Сохраняем _id совпавшего объекта

        if matched_ids:
            for collection_name in collections:
                collection = db[collection_name]
                cursor = collection.find({"_id": {"$in": matched_ids}}, {"_id": 0})  # Получаем все поля для объектов с совпавшими _id
                results.extend(cursor)

    return results[:10]  # Ограничиваем выдачу до 10 элементов

def global_search(request):
    """Глобальный поиск по всем коллекциям"""

    query = request.GET.get("q", "").strip()
    lookfor_collection = request.GET.get("collection", "global")
    if not query or len(query) < 2:
        return JsonResponse({"message": "Некорректный запрос", "results": []}, status=400)

    db = get_mongo_db()
    collections = db.list_collection_names()  # коллекции, по которым будет вестись поиск

    if lookfor_collection not in collections and lookfor_collection != "global":
        return JsonResponse({"message": "Некорректное название коллекции", "results": []}, status=404)

    search_filter = {
        "$or": [
            {"name.ru": {"$regex": query, "$options": "i"}},  # Поиск в русском названии
            {"name.en": {"$regex": query, "$options": "i"}}   # Поиск в английском названии
        ]
    }

    results = []

    if lookfor_collection == "global":
        results = search_in_collections(db, collections, search_filter, query)
    else:
        collections.remove(lookfor_collection)  # Убираем текущую коллекцию из списка

        # Поиск только в указанной коллекции
        collection = db[lookfor_collection]
        cursor = collection.find(search_filter, {"_id": 0}).sort("name.ru", ASCENDING).limit(10)
        results.extend(cursor)

        if len(results) < 7:
            # Если результатов меньше 7, ищем и в других коллекциях
            results.extend(search_in_collections(db, collections, search_filter, query))

    return JsonResponse({"results": results})