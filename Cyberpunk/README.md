# Cyberpunk_RED Backend
Этот проект представляет собой бэкэнд сайта по НРИ Cyberpunk RED
## Установка и запуск

1. Перейдите в директорию проекта:
   ```bash
   cd Cyberpunk
2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    venv\Scripts\activate
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
4. Проведите миграции базы данных:
    ВНИМАНИЕ! перед тем как проводить миграции, убедитесь в 
том, что имя пользователя, пароль пользователя и айпи БД 
в Cyberpunk\Cyberpunk\settings.py совпадают с вашими. Найти их
вы можете в DATABASES = {... обращайте внимание на комментарии
    ```bash
    python manage.py migrate
5. Запустите сервер:
    ```bash
    python manage.py runserver