from orm import the_user, category, product, favorites, orders, order_comp
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mainnn():
    return render_template("menu.html")

#пока футболки

@app.route('/shirts')
def cat_shrt():
    return render_template("katalog.html", items=category.query())

@app.route('/drinks')
def cat_drink():
    return render_template("katalog.html", items=[{'name': "Медовый лимонад от Бобби", 'image': "honeyy.png", 'price': "от 80 руб", 'description': "Никого - кроме аллергиков - не оставит равнодушным"}
    , {'name': "Имбирно-пряный лимонад от Бобби", 'image': "ginger.png", 'price': "от 80 руб", 'description': "Никого - кроме аллергиков - не оставит равнодушным"}, 
    {'name': "Цитрусовый лимонад от Бобби", 'image': "citruus.png", 'price': "от 80 руб", 'description': "Никого - кроме аллергиков - не оставит равнодушным"}])

@app.route('/lemfru')
def nap_fru():
    return render_template("tovar.html")

@app.route('/about')
def mee():
    return render_template("me.html")

app.run(debug=True)