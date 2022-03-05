from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mainnn():
    return render_template("menu.html")

#пока футболки

@app.route('/shirts')
def cat_shrt():
    return render_template("katalog.html", items=[{'name': "футболка 'Правило'", 'image': "cakehole.jpg", 'price': "2005 руб", 'description': "или за касету Металлики/Нирваны/Моторхеда"}, {'name': "футболка 'Импала'", 'image': "impala.jpg", 'price': "1967 руб", 'description': "Не надо лишних слов: KAZ2Y5"}])

@app.route('/drinks')
def cat_drink():
    return render_template("katalog.html", items=[{'name': "Медовый лимонад от Бобби", 'image': "bhoney.png", 'price': "от 80 руб", 'description': "Никого - кроме аллергиков - не оставит равнодушным"}, {'name': "Имбирно-пряный лимонад от Бобби", 'image': "bginger.png", 'price': "от 80 руб", 'description': "Никого - кроме аллергиков - не оставит равнодушным"}, {'name': "Цитрусовый лимонад от Бобби", 'image': "bcitrus.png", 'price': "от 80 руб", 'description': "Никого - кроме аллергиков - не оставит равнодушным"}])

app.run(debug=True)