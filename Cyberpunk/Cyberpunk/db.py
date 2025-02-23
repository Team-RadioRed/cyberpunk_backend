# db.py
from pymongo import MongoClient
from decouple import config

def get_mongo_db():
    client = MongoClient(config('DATABASE_URI'))
    db = client[config('DATABASE_NAME')]  # <- Указываем базу данных здесь

    # Проверка подключения
    try:
        db.list_collection_names()
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise  # Перебрасываем исключение, чтобы уведомить о проблеме

    return db