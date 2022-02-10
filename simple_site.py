from flask import *

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello'

@app.route('/')
def main_page():
    return render_template("menu.html")
    
@app.route('/about')
def mee():
    return render_template("me.html")

@app.route('/drinks')
def drink():
    return render_template("napitki.html")

@app.route('/shirts')
def tshirts():
    return render_template("cool_shirt.html")

@app.route('/imbiir')
def imb_lem():
    return render_template("imb.html")

@app.route('/hoon')
def hon_lem():
    return render_template("hon.html")

@app.route('/fruu')
def fru_lem():
    return render_template("fru.html")

@app.route('/trash')
def trash():
    return render_template("korzina.html")

@app.route('/impala')
def imp_shrt():
    return render_template("impala.html")

@app.route('/cakehole')
def cakehole_shrt():
    return render_template("cakehole.html")

app.run(debug=True)