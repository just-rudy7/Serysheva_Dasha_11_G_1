from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def abra():
    return render_template("tovary.html")


app.run(debug=True)