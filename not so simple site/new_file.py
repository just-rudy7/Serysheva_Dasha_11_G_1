from orm import the_user, product, favorites, orders, order_comp
from flask import *
from flask_sqlalchemy import SQLAlchemy
from app import db, app

@app.route('/')
def mainnn():
    return render_template("menu.html")

@app.route('/drinks')
def cat_drink():
    return render_template("katalog.html", items=product.query.all())

@app.route('/lem/', methods = ['GET'])
def which_nap():
    lem_id = int(request.args.get('lem_id', -1))
    return render_template("tovar.html", item=product.query.filter_by(prod_id = lem_id).one())

@app.route('/about')
def mee():
    return render_template("me.html")

app.run(debug=True)

'''{'name': "Медовый лимонад от Бобби", 'image': "honeyy.png", 'price': "от 80 руб", 'description': "Никого - кроме аллергиков - не оставит равнодушным"}
    , {'name': "Имбирно-пряный лимонад от Бобби", 'image': "ginger.png", 'price': "от 80 руб", 'description': "Никого - кроме аллергиков - не оставит равнодушным"}, 
    {'name': "Цитрусовый лимонад от Бобби", 'image': "citruus.png", 'price': "от 80 руб", 'description': "Никого - кроме аллергиков - не оставит равнодушным"}'''