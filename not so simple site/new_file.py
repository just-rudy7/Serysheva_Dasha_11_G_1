from orm import otziv, the_user, product, favorites, orders, order_comp
from flask import *
from flask_sqlalchemy import SQLAlchemy
from app import db, app

@app.route('/')
def mainnn():
    if request.method == "POST":
        name_o = request.form.get("name")
        email_o = request.form.get("email")
        text_o = request.form.get("text")
        db.session.add(otziv(name = name_o, email = email_o, text = text_o))
        db.session.commit()
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
