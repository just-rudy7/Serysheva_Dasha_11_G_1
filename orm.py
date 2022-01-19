from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Dashadb.db'
db = SQLAlchemy(app)

class The_User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.user_id} {self.username}'

db.create_all()
    
Dean = The_User(usename = "Dean",age=26,address="Kaz")
db.session.add(Dean)
db.session.commit()

print(The_User.query.all())
