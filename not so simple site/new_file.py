from flask import *
from flask_sqlalchemy import SQLAlchemy
import datetime
from app import app, db
from orm import favorites, order_comp, orders, otziv, product, the_user


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

@app.route('/sighn-in')
def si():
    return render_template("me.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        try:
            if the_user.query.filter_by(username=name).one().validate(password):
                session['name'] = name
                return redirect(url_for('index'), code=301)
        except:
            pass
    return render_template('login.html', item = session)

@app.route('/logout')
def logout():
    if session.get('name'):
        session.pop('name')
    return redirect('/login', code=302)


@app.route('/firsttry', methods=['GET', 'POST'])
def firsttry():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        address = request.form.get('address')
        age = request.form.get('age')
        db.session.add(the_user(username = name, password = password, age=age, address=address))
        db.session.commit()
        try:
            if the_user.query.filter_by(username=name).one().validate(password):
                session['name'] = name
                return redirect(url_for('index'), code=301)
        except:
            pass
    return render_template('firsttime.html', item = session)

app.run(debug=True)
