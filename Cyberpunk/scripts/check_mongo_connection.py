import os
import django
from pymongo import MongoClient
from django.conf import settings

# Устанавливаем Django окружение
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cyberpunk.settings")
django.setup()

def check_remote_mongo_connection():
    """Проверяет соединение с удалённой MongoDB."""
    try:
        # Используем URI из settings.py
        mongo_client = MongoClient(settings.MONGO_URI)

        # Проверяем доступность базы данных
        db = mongo_client[settings.MONGO_DB_NAME]
        collections = db.list_collection_names()  # Получаем список коллекций

        print(f"✅ Успешное подключение к MongoDB: {settings.MONGO_DB_NAME}")
        print(f"Доступные коллекции: {collections}")

        # Закрываем клиент после проверки
        mongo_client.close()

    except Exception as e:
        print(f"❌ Ошибка подключения к MongoDB: {e}")

# Запуск проверки
if __name__ == "__main__":
    check_remote_mongo_connection()