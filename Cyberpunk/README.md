# Cyberpunk_RED Backend
Бэкэнд сайта для настольной ролевой игры **Cyberpunk RED**.

## Требования
- Python 3.8 или новее
- PostgreSQL установленный и настроенный

## Установка и запуск
1. **Клонируйте репозиторий** (только если он ещё не скачан), и перейдите в директорию проекта:
    ```bash
    git clone https://github.com/AngelSamOf/cyberpunk_db_back.git
    cd Cyberpunk
    ```

2. **Создайте и активируйте виртуальное окружение**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```

3. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Настройте подключение к базе данных**:
    - Откройте файл `Cyberpunk\Cyberpunk\settings.py`.
    - В разделе `DATABASES` укажите имя пользователя, пароль и IP-адрес вашей базы данных.
    - Убедитесь, что PostgreSQL настроен правильно.

5. **Примените миграции**:
    ```bash
    python manage.py migrate
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
