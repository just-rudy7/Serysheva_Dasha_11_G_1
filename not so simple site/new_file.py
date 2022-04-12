from orm import otziv, the_user, product, favorites, orders, order_comp
from flask import *
from flask_sqlalchemy import SQLAlchemy
from app import db, app

@app.route('/', methods=['GET', 'POST'])
def mainnn():
    feedback = otziv.query.all()
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        text = request.form.get("text")
        print(name, text)
        if name != '' and text != '' and email!='':
            feedback.reverse()
            f = otziv(name=name, text=text, email=email)
            db.session.add(f)
            db.session.commit()
            feedback.append(f)
            feedback.reverse()
    return render_template('menu.html', feedback=feedback)

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
