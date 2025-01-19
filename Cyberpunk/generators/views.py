import random
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views import View


class NetworkGenerator(View):
    # Разрешаем обработку всех методов через dispatch, добавляя CSRF-исключение
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # Обработка GET-запроса (отображение формы)
    def get(self, request):
        # Отображение HTML-страницы для генератора
        return render(request, 'network_generator.html')

    # Обработка POST-запроса (генерация сети)
    @method_decorator(require_POST)  # Гарантируем, что метод доступен только для POST
    def post(self, request):
        try:
            data = json.loads(request.body)
            difficulty = int(data.get('difficulty', 10))
            branching = data.get('branching', False)

            # Проверка сложности
            if not (6 <= difficulty <= 18):
                return JsonResponse({'error': 'Сложность сети должна быть от 6 до 18.'}, status=400)

            # Генерация сети
            network = self.generate_network(difficulty, branching)
            return JsonResponse(network, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # Генерация структуры сети
    def generate_network(self, difficulty, branching):
        def generate_floor(level, max_branch_chance):
            content_type = random.choice(['enemy', 'password', 'data'])
            if content_type == 'enemy':
                num_enemies = max(1, difficulty // 3 + random.choice([-1, 0, 1]))
                content = f'{num_enemies} ЛЁД'
            elif content_type == 'password':
                hack_difficulty = max(5, difficulty + random.choice([-2, -1, 0, 1, 2]))
                content = f'Пароль СЛ {hack_difficulty}'
            else:
                hack_difficulty = max(5, difficulty + random.choice([-2, -1, 0, 1, 2]))
                content = f'Узел управления СЛ {hack_difficulty}'

            next_rooms = []
            if branching and level > 0 and random.random() < max_branch_chance:
                num_branches = random.randint(2, 3)
                for _ in range(num_branches):
                    next_rooms.append(generate_floor(level - 1, max_branch_chance - 0.1))
            elif level > 0:
                next_rooms.append(generate_floor(level - 1, max_branch_chance))

            return {
                'type': content_type,
                'content': content,
                'next': next_rooms if next_rooms else None
            }

        num_floors = random.randint(6, 10)
        return generate_floor(num_floors - 1, 0.3)