import sqlite3
import unittest


class DB():
    def __init__(self, path: str):
        self.__connection = sqlite3.connect(path)
        self.__cursor = self.__connection.cursor()

    def __del__(self):
        self.__connection.close()

    @property
    def get_cursor(self):
        return self.__cursor

    @property
    def conn(self):
        return self.__connection

    def The_User(self, id: int):
        request = 'SELECT username, address, date_of_birth, reg_data FROM The_User WHERE user_id = :id'
        return self.__cursor.execute(request, {'id': id}).fetchall()

    def prod(self, id: int):
        request = 'SELECT prod_name, cat_id, description, amount_left, price FROM Product WHERE prod_id = :id'
        return self.__cursor.execute(request, {'id': id}).fetchall()

    def orders(self, id: int):
        request = 'SELECT user_id, money, if_payed FROM orders WHERE order_num = :id'
        return self.__cursor.execute(request, {'id': id}).fetchall()

    def cat(self, id: int):
        request = 'SELECT cat_name, description FROM Category WHERE cat_id = :id'
        return self.__cursor.execute(request, {'id': id}).fetchall()


class TestDB(unittest.TestCase):
    def setUp(self):
        self.__temp = DB(':memory:')
        self.__temp.get_cursor.executescript(
            '''
            BEGIN TRANSACTION
            CREATE TABLE IF NOT EXISTS "The_User" (
                   "user_id"	INTEGER UNIQUE,
                    "username"	TEXT NOT NULL UNIQUE,
                    "password"	TEXT NOT NULL,
                    "address"	TEXT,
                    "date_of_birth"	DATE NOT NULL DEFAULT '2001-01-01',
                    "reg_data"	TIMESTAMP DEFAULT CURRENT_DATE,
                    PRIMARY KEY("user_id" AUTOINCREMENT)
            );
            INSERT INTO The_User VALUES (1, 'Dean', 'impala67', 'Lawrence, Kansas', '1979-01-24', '2004-07-04');
            INSERT INTO The_User VALUES (2, 'Sam', 'lawboi', 'Lawrence, Kansas', '1983-05-02', '2001-01-01');
            INSERT INTO The_User VALUES (3, 'Dasha', 'Ross_the_Moose', 'Moscow, Russia', '2004-07-25', '2007-06-11');
            INSERT INTO The_User VALUES (4, 'Shaggy', 'scoob', 'Cristal Cave', '1979-01-24', '2001-01-01');
            
            CREATE TABLE IF NOT EXISTS "Product" (
                "prod_id"	INTEGER UNIQUE,
                "cat_id"	INTEGER NOT NULL,
                "prod_name"	TEXT NOT NULL UNIQUE,
                "description"	TEXT,
                "amount_left"	INTEGER NOT NULL,
                "price"	INTEGER NOT NULL,
                FOREIGN KEY("cat_id") REFERENCES "Category"("cat_id"),
                PRIMARY KEY("prod_id" AUTOINCREMENT)
            );
            INSERT INTO Product VALUES (1, 1, 'imbir_medovarius', 'fresh and tasty', 217, 80);
            INSERT INTO Product VALUES (2, 2, 'savin ppl, huntin things, family business', 'super cozy t-shirt', 316, 1104);
            INSERT INTO Product VALUES (3, 2, 'impala', 'fast and furious', 2, 10000000000);
            
            CREATE TABLE IF NOT EXISTS "orders" (
                "order_num"	INTEGER UNIQUE,
                "user_id"	INTEGER,
                "money"	REAL NOT NULL DEFAULT 'SELECT Product.price*Order_comp.amount_ordered FROM Order_comp, Product WHERE Order_comp.prod_id = Product.prod_id',
                "if_payed"	BOOLEAN NOT NULL,
                FOREIGN KEY("user_id") REFERENCES "The_User",
                PRIMARY KEY("order_num" AUTOINCREMENT)
            );
            INSERT INTO orders VALUES (1, 2, 1104.0, 1);
            INSERT INTO orders VALUES (2, 3, 160.0, 0);
            INSERT INTO orders VALUES (3, 1, 1104.0, 1)
            
            CREATE TABLE IF NOT EXISTS "Order_comp" (
                "order_num"	INTEGER NOT NULL,
                "prod_id"	INTEGER NOT NULL,
                "amount_ordered"	INTEGER NOT NULL,
                FOREIGN KEY("prod_id") REFERENCES "Product"("prod_id"),
                FOREIGN KEY("order_num") REFERENCES "orders"("order_num")
            );
            
            INSERT INTO Order_comp VALUES (1, 2, 1);
            INSERT INTO Order_comp VALUES (2, 1, 2);
            INSERT INTO Order_comp VALUES (3, 3, 1);
            INSERT INTO Order_comp VALUES (1, 1, 1);
            
            CREATE TABLE IF NOT EXISTS "Favorites" (
                "user_id"	INTEGER NOT NULL,
                "prod_id"	INTEGER NOT NULL,
                FOREIGN KEY("prod_id") REFERENCES "Product"("prod_id"),
                FOREIGN KEY("user_id") REFERENCES "The_User"("user_id")
            );
            
            INSERT INTO Favorites VALUES (1, 1);
            INSERT INTO Favorites VALUES (2, 2);
            INSERT INTO Favorites VALUES (3, 3);
            INSERT INTO Favorites VALUES (1, 3);
            
            CREATE TABLE IF NOT EXISTS "Category" (
                "cat_id"	INTEGER,
                "cat_name"	TEXT NOT NULL UNIQUE,
                "description"	TEXT,
                PRIMARY KEY("cat_id" AUTOINCREMENT)
            );
            
            INSERT INTO Category VALUES (1, 'lemonade', 'delicious');
            INSERT INTO Category VALUES (2, 't-shirt', 'cool');
            INSERT INTO Category VALUES (3, 'my_dog', 'good_boi');
            COMMIT;
            '''
        )

    def test_user(self):
        for i in range(1, 4 + 1):
            request = self.__temp.The_User(id=i)
            self.assertEqual(1, len(request))

    def test_prod(self):
        for i in range(1, 3 + 1):
            request = self.__temp.prod(id=i)
            self.assertEqual(1, len(request))

    def test_cat(self):
        for i in range(1, 3 + 1):
            request = self.__temp.cat(id=i)
            self.assertEqual(1, len(request))

    def test_orders(self):
        for i in range(1, 3 + 1):
            request = self.__temp.orders(id=i)
            self.assertEqual(1, len(request))

    def tearDown(self):
        self.__temp.conn.close()


if __name__ == '__main__':  # точка входа в программу
    unittest.main(failfast=False)
