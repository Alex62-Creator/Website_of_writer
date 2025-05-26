from flask import Flask

# Создаём экземпляр класса Flask (переменную app)
app = Flask(__name__)

# Создаем секретный ключ для защиты данных
app.config['SECRET_KEY'] = 'your_secret_key'

# Импортируем маршруты
from app import routes