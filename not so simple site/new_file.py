from flask import Flask, render_template

app = Flask(__name__)


@app.route('/abra')
def abra():
    return render_template("katalog.html")


app.run(debug=True)