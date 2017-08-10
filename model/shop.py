import db
import db.adapter
from model import enums
from .order import Order
from .singleton import SingletonMeta


class Shop(metaclass=SingletonMeta):
    _customers_sig = "first_name, second_name, telephone, address"
    _products_sig = "name, count, price"

    def __init__(self):
        self.database = None
        self.order = Order()

    def connect_db(self, db_type, action, data):
        print(db_type, action, data)

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

    def delete_from(self, table_name, id_list):
        self.database.delete(table_name, id_list)

    def to_cart(self, id_list):
        self.order.to_cart(id_list)

    def remove_from_cart(self, id_list):
        self.order.remove_from_cart(id_list)

    def place_order(self):
        pass

    def clear_order(self):
        self.order = Order()
        self.ui_set_products()

    def get_order(self):  # все get - получение list для таблицы
        pass

    def get_from(self, table_name):
        if self.database is None:
            return list()
        return self.database.select_all(table_name)

    def set_customer(self, id):
        self.order.set_customer(id)

    def add_customer(self, customer):
        self.database.add_row("customers",
                              self._customers_sig,
                              [customer.first_name,
                               customer.second_name,
                               customer.telephone,
                               customer.address])

    def ui_set_products(self):
        pass

    def ui_set_order(self):
        pass

    def close_connection(self):
        if self.database is not None:
            self.database.close_connection()
