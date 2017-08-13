import db
import db.adapter
from .db_description import customers
from .db_description import products
from model import enums
from .order import Order
from .singleton import SingletonMeta
from db import exception


class Shop(metaclass=SingletonMeta):
    
    def __init__(self):
        self.database = None
        self.order = Order()
        self._customers_sig = str([x.name 
            for x in customers.columns[1:]])[1:-1]
        self._products_sig = str([x.name 
            for x in products.columns[1:-1]])[1:-1]

    def connect_db(self, db_type, action, data):
        if action is enums.Action.CREATE:
            self.create_db(data, db_type)
        elif action is enums.Action.OPEN:
            self.open_db(data, db_type)

        self.clear_order()

    def create_db(self, path, db_type):
        if db_type is enums.DbType.SQLITE:
            self.database = db.Manager(db.adapter.Sqlite3(path))
            self.database.create_tables()

    def open_db(self, path, db_type):
        if db_type is enums.DbType.SQLITE:
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

    def to_cart(self, prod_list):
        self.order.to_cart(prod_list)
        self.database.reserve(
            "products",
            [[x.id, x.count] for x in prod_list])
        self.ui_set_order()

    def remove_from_cart(self, prod_list):
        self.order.remove_from_cart(prod_list)
        self.database.unreserve(
            "products",
            [[x.id, x.count] for x in prod_list])
        self.ui_set_order()

    def place_order(self):
        pass

    def clear_order(self):  # TODO: add return of products
        self.database.unreserve(
            "products",
            [[x.id, x.count] for x in self.order.get_cart()])
        self.order = Order()
        self.ui_set_order()

    def get_order(self):
        if self.database is None:
            return list()
        return list(
            self.database.select_by_id(
                "products",
                [x.id for x in self.order.get_cart()])
        )

    def get_from(self, table_name):
        if self.database is None:
            return list()
        return self.database.select_all(table_name)

    def set_customer_id(self, id):
        self.order.set_customer_id(id)

    def add_customer(self, customer):
        self.database.add_row("customers",
                              self._customers_sig,
                              [customer.surname,
                               customer.name,
                               customer.phone,
                               customer.address])

    def ui_set_products(self):
        pass

    def ui_set_order(self):
        pass

    def close_connection(self):
        if self.database is not None:
            self.database.close_connection()
