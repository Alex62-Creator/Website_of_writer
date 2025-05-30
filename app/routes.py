from flask import  render_template, request, redirect, url_for, flash
from app import app, mail
from flask_mail import Message
from app.forms import EmailForm

# Создаем маршрут для первой страницы
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')


@app.route("/shop", methods=["GET", "POST"])
def shop():
    return render_template('shop.html')


@app.route("/about", methods=["GET", "POST"])
def about():
    form = EmailForm()
    if form.validate_on_submit():
        try:
            # Создание письма
            msg = Message(
                subject=f"Message of site from {form.username.data}",
                sender=app.config['MAIL_USERNAME'],
                recipients=["grimwoodworldcastingshadows@gmail.com"],
                reply_to=form.email.data  # Для ответа напрямую отправителю
            )

            # Форматирование текста
            msg.body = f"""
            📧 New message from Contact page:

            👤 Name: {form.username.data}
            📩 Email: {form.email.data}
            📝 Message:
            {form.text.data}

            ---
            This is an automated message, please do not reply directly.
            """

            # Отправка
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')

        except Exception as e:
            app.logger.error(f"Mail error: {str(e)}")
            flash('There was an error sending your message', 'danger')

        return redirect(url_for('about'))

    return render_template('about.html', form=form)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = EmailForm()
    if form.validate_on_submit():
        try:
            # Создание письма
            msg = Message(
                subject=f"Message of site from {form.username.data}",
                sender=app.config['MAIL_USERNAME'],
                recipients=["grimwoodworldcastingshadows@gmail.com"],
                reply_to=form.email.data  # Для ответа напрямую отправителю
            )

            # Форматирование текста
            msg.body = f"""
                📧 New message from Contact page:

                👤 Name: {form.username.data}
                📩 Email: {form.email.data}
                📝 Message:
                {form.text.data}

                ---
                This is an automated message, please do not reply directly.
                """

            # Отправка
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')

        except Exception as e:
            app.logger.error(f"Mail error: {str(e)}")
            flash('There was an error sending your message', 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)

@app.route("/book1")
def book1():
    return render_template('book1.html')

@app.route("/book2")
def book2():
    return render_template('book2.html')

@app.route("/book3")
def book3():
    return render_template('book3.html')
