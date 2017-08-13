import db
import db.adapter
from model import enums
from .order import Order
from .singleton import SingletonMeta
from db import exception


class Shop(metaclass=SingletonMeta):
    _customers_sig = "surname, name, telephone, address"
    _products_sig = "name, count, price"

    def __init__(self):
        self.database = None
        self.order = Order()

    def connect_db(self, db_type, action, data):
        if action is enums.Action.CREATE:
            self.create_db(data, db_type)
        elif action is enums.Action.OPEN:
            self.open_db(data, db_type)

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
        for p in self.order.get_cart():
            print(p)
        self.database.unreserve(
            "products",
            [[x.id, x.count] for x in self.order.get_cart()])
        self.order = Order()
        self.ui_set_order()

    def get_order(self):
        return list(
            self.database.select_by_id(
                "products",
                [x.id for x in self.order.get_cart()])
        )

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
