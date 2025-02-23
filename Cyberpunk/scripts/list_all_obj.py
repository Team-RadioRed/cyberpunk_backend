from Cyberpunk.db import get_mongo_db

def list_all():
    """Функция для получения всех объектов из коллекции"""

    db = get_mongo_db()

    collection = input("Введите название коллекции: ").strip()

    # Проверяем, существует ли коллекция
    if collection not in db.list_collection_names():
        print(f"❌ Коллекции '{collection}' не существует.")
        return

    chosen_collection = db[collection]
    objects_cursor = chosen_collection.find({})

    item_list = list(objects_cursor)

    if not item_list:
        print(f"🔍 Коллекция '{collection}' пуста.")
        return

    for item in item_list:
        item['_id'] = str(item['_id'])
        print(item)

if __name__ == "__main__":
    list_all()