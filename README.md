# Cyberpunk_RED Backend
Бэкэнд сайта для настольной ролевой игры **Cyberpunk RED**.

## Требования
- Python 3.8 или новее

## Установка и запуск
1. **Клонируйте репозиторий** (только если он ещё не скачан):
    ```bash
    git clone https://github.com/AngelSamOf/cyberpunk_db_back.git
    ```

2. **Создайте и активируйте виртуальное окружение**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

3. **Установите зависимости**:
    - Перейдите в директорию проекта и установите зависимости
    ```bash
    cd Cyberpunk && pip install -r requirements.txt
    ```

4. **Настройте подключение к базе данных**:
    - Создайте файл `Cyberpunk\.env`.
    - Заполните его по шаблону:
    SECRET_KEY=Ключ Джанго
    DATABASE_URI=URI БД
    DATABASE_NAME=Название используемой БД
    DEBUG=True(Во время разработки)
    - Убедитесь, что MongoDB настроен правильно.

5. **Проверка соединения с MongoDB**:
    - Убедитесь, что сервер MongoDB запущен и доступен.
    - Запустите скрипт проверки соединения:
    ```bash
    python scripts/check_mongo_connection.py
    ```

6. **Создайте суперпользователя (администратор сайта)**:
    ```bash
    python manage.py createsuperuser
    ```
    - Введите имя пользователя, email и пароль.
    - **Заметка:** Поле email не является обязательным, вы можете оставить его пустым.

7. **Запустите сервер разработки**:
    ```bash
    python manage.py runserver
    ```

## Использование
- После запуска сервера откройте [http://127.0.0.1:8000/](http://127.0.0.1:8000/) в браузере.
- Административная панель доступна по адресу [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
