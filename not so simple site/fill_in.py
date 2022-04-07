from orm import *
from datetime import datetime

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