from flask import Flask
from flask_mail import Mail

# Создаём экземпляр класса Flask (переменную app)
app = Flask(__name__)

# Создаем секретный ключ для защиты данных
app.config['SECRET_KEY'] = 'your_secret_key'

# Конфигурация почты
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Для Gmail
app.config['MAIL_PORT'] = 587  # Порт для TLS
app.config['MAIL_USE_TLS'] = True  # Обязательно использовать TLS
app.config['MAIL_USE_SSL'] = False  # SSL должен быть выключен
app.config['MAIL_USERNAME'] = 'your_mail'  # Ваша почта
app.config['MAIL_PASSWORD'] = 'your_password'  # Пароль приложения

mail = Mail(app)

# Импортируем маршруты
from app import routes
