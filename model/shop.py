import db
import db.adapter
from .order import Order
from .singleton import SingletonMeta


class Shop(metaclass=SingletonMeta):
    _customers_sig = "first_name, second_name, telephone, address"
    _products_sig = "name, count, price"

    def __init__(self):
        self.database = None
        self.order = Order()

    def create_db(self, path):
        self.database = db.Manager(db.adapter.Sqlite3(path))
        self.database.adapter.execute('''CREATE TABLE products
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             name VARCHAR(100), 
             count INT, price INT, 
             reserved INT DEFAULT 0)''')
        self.database.adapter.execute('''CREATE TABLE customers
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             first_name VARCHAR(30), 
             second_name VARCHAR(30), 
             telephone VARCHAR(30), 
             adress VARCHAR(200))''')

    def open_db(self, path):
        if self.database is not None:
            self.database.close_connection()
        self.database = db.Manager(db.adapter.Sqlite3(path))

    def add_product(self, product):
        self.database.add_row("products",
                              self._products_sig,
                              [product.name,
                               product.count,
                               product.price])

    def delete_product(self, id_list):
        self.database.delete("products", id_list)

    def to_cart(self, id_list):
        self.order.to_cart(id_list)

    def remove_from_cart(self, id_list):
        self.order.remove_from_cart(id_list)

    def place_order(self):
        pass

    def clear_order(self):
        self.order = Order()

    def get_order(self):  # все get - получение list для таблицы
        pass

    def get_products(self):
        return list(self.database.select_all("products"))

    def get_customers(self):
        return list(self.database.select_all("customers"))

    def set_customer(self, id):
        self.order.set_customer(id)

    def add_customer(self, customer):
        self.database.add_row("customers",
                              self._customers_sig,
                              [customer.first_name,
                               customer.second_name,
                               customer.telephone,
                               customer.adress])

    def delete_customer(self, id_list):
        self.database.delete("customers", id_list)

    def close_connection(self):  # некие действия перед выключением программ
        self.database.close_connection()
