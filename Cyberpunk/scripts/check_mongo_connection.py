import os
import django
from pymongo import MongoClient
from decouple import config

'''
# Устанавливаем Django окружение(убрать большой комментарий если не работает)
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cyberpunk.settings")
django.setup()
'''

def check_remote_mongo_connection():
    """Проверяет соединение с удалённой MongoDB."""
    try:
        # Используем URI из .env
        mongo_client = MongoClient(config('DATABASE_URI'))

        # Проверяем доступность базы данных
        db = mongo_client[config('DATABASE_NAME')]
        collections = db.list_collection_names()  # Получаем список коллекций

        print(f"✅ Успешное подключение к MongoDB: {config('DATABASE_NAME')}")
        print(f"Доступные коллекции: {collections}")

        # Закрываем клиент после проверки
        mongo_client.close()

    except Exception as e:
        print(f"❌ Ошибка подключения к MongoDB: {e}")

# Запуск проверки (код запускается только если вызвать его напрямую)
if __name__ == "__main__":
    check_remote_mongo_connection()