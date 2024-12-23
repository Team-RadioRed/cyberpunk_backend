from django.core.management.base import BaseCommand
from references.models import Weapons_DB  # Импортируйте вашу модель

class Command(BaseCommand):
    help = 'Delete all records from MyModel in the database'

    def handle(self, *args, **kwargs):
        # Удаляем все записи из указанной модели
        count = Weapons_DB.objects.all().delete()  # Удаляем все записи
        self.stdout.write(f'Deleted {count} records from {Weapons_DB.__name__}.') # Выводим кол-во удаленных записей