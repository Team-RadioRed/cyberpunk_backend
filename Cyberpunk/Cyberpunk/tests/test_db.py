import pytest
from pymongo import MongoClient

def check_remote_mongo_connection():
    """Проверяет соединение с удалённой MongoDB."""
    try:
        # Используем URI из .env
        mongo_client = MongoClient({{secrets.DATABASE_URI}})

        # Проверяем доступность базы данных
        db = mongo_client[{{secrets.DATABASE_NAME}}]

        mongo_client.close()

        return 1

    except Exception as e:
        return e

def test_connection():
    result = check_remote_mongo_connection()

    if isinstance(result, Exception):  # Если получили ошибку, тест падает
        pytest.fail(f"MongoDB connection failed: {result}")

    assert result == 1