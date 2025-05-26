from flask import  render_template, request, redirect, url_for
from app import app

# Создаем маршрут для первой страницы
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')

#@app.route("/books", methods=["GET", "POST"])
#def books():
    #return render_template('book1.html')

@app.route("/shop", methods=["GET", "POST"])
def shop():
    return render_template('shop.html')

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template('about.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template('contact.html')

@app.route("/book1")
def book1():
    return render_template('book1.html')

@app.route("/book2")
def book2():
    return render_template('book2.html')

@app.route("/book3")
def book3():
    return render_template('book3.html')
