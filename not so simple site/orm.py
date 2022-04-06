from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db
#УБРАТЬ КАТЕГОРИИ

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
    #картинка

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

class otziv(db.Model):
    ot_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable = False)
    text = db.Column(db.String(80), nullable = False)