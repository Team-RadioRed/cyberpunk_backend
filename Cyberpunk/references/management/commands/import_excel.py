import pandas as pd
from django.core.management.base import BaseCommand
from references.models import Weapons_DB  # Импортируй свою модель


class Command(BaseCommand):
    help = 'Импортирует данные из Excel в таблицу Weapons_DB'

    def handle(self, *args, **kwargs):
        # Укажи путь к файлу Excel
        file_path = r'C:\Users\Administrator\Documents\Копия CyberpunkDB.xlsx'

        # Чтение Excel файла
        df = pd.read_excel(file_path, skiprows=1)  # Пропуск первой строки с заголовками

        # Вывод первых 5 строк для отладки
        print(df.head())

        # Удаляем лишние столбцы
        df.drop(df.columns[[0, 4, 6, 9]], axis=1, inplace=True)

        # Преобразование столбца "да/нет" (предположительно 14 столбец)
        df.iloc[:, 9] = df.iloc[:, 9].apply(lambda x: 1 if x == 'Да' else 0 if x == 'Нет' else None)

        # Ограничение строк до 31
        df = df.iloc[:31]

        # Импорт данных в базу
        for index, row in df.iterrows():
            # Используем iloc для доступа к элементам по индексу
            price_low = row.iloc[10] if row.iloc[14] != 'Нет' else None
            price_mid = row.iloc[11] if row.iloc[15] != 'Нет' else None
            price_high = row.iloc[12] if row.iloc[16] != 'Нет' else None

            # Преобразуем значения цен в числа, если они не равны None
            price_low = price_low if isinstance(price_low, (int, float)) else None
            price_mid = price_mid if isinstance(price_mid, (int, float)) else None
            price_high = price_high if isinstance(price_high, (int, float)) else None

            Weapons_DB.objects.create(
                title_ru=row.iloc[0],
                title_en=row.iloc[1],
                type=row.iloc[2],
                skill_need=row.iloc[3],
                damage=row.iloc[4],
                magazine=row.iloc[5],
                ammo_type=row.iloc[6],
                rate_of_fire=row.iloc[7],
                grab_type=row.iloc[8],
                hidden=row.iloc[9],  # Булевое значение для поля "hidden"
                price_low=price_low,
                price_mid=price_mid,
                price_high=price_high,
                price_category=row.iloc[13],
                features=row.iloc[14],
                description=row.iloc[15],
                source=row.iloc[16]
            )

        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))