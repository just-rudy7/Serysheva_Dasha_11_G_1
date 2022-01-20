from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orm.db'
db = SQLAlchemy(app)

class the_user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), unique=False)
    reg_data = db.Column(db.DateTime, nullable=True)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.user_id} {self.username}'

class category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.cat_id}{self.cat_name}'

class product(db.Model):
    prod_id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, db.ForeignKey('category.cat_id'), nullable=False)
    prod_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(80))
    amount_left = db.Column(db.Integer, nullable=False)
    price=db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.prod_id}{self.prod_name}{self.price}'

class favorites(db.Model):
    fav_num = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('the_user.user_id'))
    prod_id = db.Column(db.Integer, db.ForeignKey('product.prod_id'))

    def __repr__(self):
        return f'{self.user_id}{self.prod_id}'

class orders(db.Model):
    order_num = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('the_user.user_id'))
    money = db.Column(db.Integer, nullable=False)
    if_payed = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'{self.order_num}{self.user_id}'


class order_comp(db.Model):
    comp_num = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_num'))
    prod_id = db.Column(db.Integer, db.ForeignKey('product.prod_id'))
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.order_id}{self.prod_id}'

db.create_all()
    
Dean = the_user(username = "Dean", password = "Impala67", reg_data = datetime.now(), age=26, address="Kaz")
Sam = the_user(username = "Sammy", password = "lawboi", reg_data = datetime.now(), age=22, address="Kaz")
Peter = the_user(username = "Peter", password = "gr8power", reg_data = datetime.now(), age=16, address="Queens")
lemonade = category(cat_name = "lemonade", description = "time to chill")
shirt = category(cat_name = "t-shirts", description = "time to look cool")
imbir = product(cat_id = 1, prod_name="imbir_medovarius", description = "tasty", amount_left = 59, price=67)
impala = product(cat_id = 2, prod_name="Chevrolet Impala 1967", description = "Baby", amount_left = 1, price=19987)
fav1 = favorites(prod_id = 1, user_id = 3)
fav2 = favorites(prod_id = 2, user_id = 3)
order_dean = orders(user_id = 1, money = 19987, if_payed = True)
order_sam = orders(user_id = 2, money = 134, if_payed = False)
comp_dean = order_comp(order_id = 1, prod_id = 2, amount = 1)
comp_sam = order_comp(order_id = 2, prod_id = 1, amount = 2)

db.session.add(Dean)
db.session.add(Sam)
db.session.add(Peter)
db.session.add(lemonade)
db.session.add(shirt)
db.session.add(imbir)
db.session.add(impala)
db.session.add(fav1)
db.session.add(fav2)
db.session.add(order_dean)
db.session.add(order_sam)
db.session.add(comp_dean)
db.session.add(comp_sam)
db.session.commit()

print(the_user.query.all()[0])
print(category.query.all()[0])
print(product.query.all()[0])
print(favorites.query.all()[0])
print(orders.query.all()[0])
print(order_comp.query.all()[0])
