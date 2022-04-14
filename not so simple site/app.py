from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orm.db'
db = SQLAlchemy(app)
app.secret_key = 'umkns[pdf,b2515vJHR-)~~~~_ jfkldsnf2401'