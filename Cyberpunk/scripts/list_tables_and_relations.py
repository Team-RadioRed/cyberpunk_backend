print("Starting table and relation listing...")
from django.db import connection
import os
import sys
import django

# Добавляем путь к корневой директории проекта в PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Устанавливаем DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cyberpunk.settings")
django.setup()

def list_tables_and_relations():
    print("Fetching tables...")
    try:
        with connection.cursor() as cursor:
            # Список всех таблиц
            cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tables = cursor.fetchall()
            print("Tables in the database:")
            for table in tables:
                print(f" - {table[0]}")

            # Вывод связей (foreign keys)
            cursor.execute("""
                SELECT
                    tc.table_name AS source_table,
                    kcu.column_name AS source_column,
                    ccu.table_name AS target_table,
                    ccu.column_name AS target_column
                FROM
                    information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                    AND tc.table_schema = kcu.table_schema
                JOIN information_schema.constraint_column_usage AS ccu
                    ON ccu.constraint_name = tc.constraint_name
                    AND ccu.table_schema = tc.table_schema
                WHERE tc.constraint_type = 'FOREIGN KEY'
                ORDER BY tc.table_name, kcu.column_name;
            """)
            relations = cursor.fetchall()
            print("\nTable relations (Foreign Keys):")
            for relation in relations:
                print(f" - {relation[0]} ({relation[1]}) -> {relation[2]} ({relation[3]})")
    except Exception as e:
        print(f"Error listing tables and relations: {e}")

if __name__ == "__main__":
    list_tables_and_relations()
