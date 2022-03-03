import sqlite3

conn = sqlite3.connect("Dasha db (1).db")
cursor = conn.cursor()

cursor.execute("SELECT price AS 'Цена товара с выбранным номером', prod_id FROM Product WHERE prod_id = (SELECT prod_id FROM Order_comp WHERE order_num = (SELECT order_num FROM orders where order_num = 1))")
print(cursor.fetchall())

cursor.execute("SELECT Order_comp.order_num AS 'Номер заказа', Product.price*Order_comp.amount_ordered AS 'Стоимость' FROM Order_comp, Product WHERE Order_comp.prod_id = Product.prod_id")
print(cursor.fetchall())

cursor.execute("SELECT orders.order_num AS 'Номер заказа', The_User.address AS 'Адрес доставки' FROM Orders, The_User WHERE orders.user_id = The_User.user_id AND orders.if_payed = 1")
print(cursor.fetchall())

cursor.execute("SELECT Product.prod_name AS 'Название товара', Product.amount_left AS 'Количество на складе' FROM Product")
print(cursor.fetchall())

cursor.execute("SELECT The_User.username AS 'Имя пользователя', Product.prod_name AS 'Понравившийся товар' FROM The_User, Favorites, Product WHERE (The_User.user_id = Favorites.user_id AND Favorites.prod_id = Product.prod_id)")
print(cursor.fetchall())

conn.close()