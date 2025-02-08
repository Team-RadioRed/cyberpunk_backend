import random
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views import View
from Cyberpunk.db import get_mongo_db

class NetworkGenerator(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @method_decorator(require_POST)
    def post(self, request):
        try:
            data = json.loads(request.body)
            difficulty = int(data.get('difficulty', 10))
            branching = data.get('branching', False)

            if not (6 <= difficulty <= 18):
                return JsonResponse({'error': 'Сложность сети должна быть от 6 до 18.'}, status=400)

            def generate_floor(level, max_branch_chance):
                content_type = random.choice(['enemy', 'password', 'data'])
                if content_type == 'enemy':
                    num_enemies = max(1, difficulty // 3 + random.choice([-1, 0, 1]))
                    
                    # Получаем противников из базы данных, у которых есть значения в полях perception или speed
                    db = get_mongo_db()
                    programs_collection = db["program"]
                    enemies_cursor = programs_collection.find({
                        "$or": [
                            {"perception": {"$exists": True, "$ne": None}},
                            {"speed": {"$exists": True, "$ne": None}}
                        ]
                    })
                    enemies_list = list(enemies_cursor)
                    
                    if not enemies_list:
                        content = f'{num_enemies} ЛЁД'
                    else:
                        selected_enemy = random.choice(enemies_list)
                        content = f'{num_enemies} ЛЁД: {selected_enemy.get("name", "Неизвестный противник")}'
                elif content_type == 'password':
                    hack_difficulty = max(5, difficulty + random.choice([-2, -1, 0, 1, 2]))
                    content = f'Пароль СЛ {hack_difficulty}'
                else:
                    hack_difficulty = max(5, difficulty + random.choice([-2, -1, 0, 1, 2]))
                    content_type_choice = random.choice(['control_node', 'file'])
                    if content_type_choice == 'control_node':
                        content = f'Узел управления СЛ {hack_difficulty}'
                    else:
                        content = f'Файл СЛ {hack_difficulty}'

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
            network = generate_floor(num_floors - 1, 0.3)
            return JsonResponse(network, safe=False)
        except ValueError:
            return JsonResponse({'error': 'Некорректное значение сложности.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)