import db
import db.adapter
from datetime import datetime
from .db_description import customers, products, deals
from model import enums
from .order import Order
from .singleton import SingletonMeta
from .check_creator import CheckCreator
from db.exception import *
from .exception import *
from gui.locale import rus
import re


class Shop(metaclass=SingletonMeta):
    def __init__(self):
        self.database = None
        self.order = Order()
        self._check_creator = CheckCreator()
        self._customers_sig = str([x.name
                                   for x in customers.columns[1:]])[1:-1]
        self._products_sig = str([x.name
                                  for x in products.columns[1:-1]])[1:-1]
        self._deals_sig = str([x.name
                               for x in deals.columns[1:-1]])[1:-1]

    def connect_db(self, db_type, action, data):
        if action is enums.Action.CREATE:
            self.create_db(data, db_type)
        elif action is enums.Action.OPEN:
            self.open_db(data, db_type)

        self.ui_display_order()

    def create_db(self, path, db_type):
        if db_type is enums.DbType.SQLITE:
            self.database = db.Manager(
                db.adapter.Sqlite3(path, "id", "reserved", "count"))
            self.database.create_tables()

    def open_db(self, path, db_type):
        if db_type is enums.DbType.SQLITE:
            if self.database is not None:
                self.database.close_connection()
            self.database = db.Manager(
                db.adapter.Sqlite3(path, "id", "reserved", "count"))

    def select_row(self, table_name, id):
        res = list(self.database.select_by_id(table_name, [id]))
        if not res:
            return None
        return res[0]

    def add_product(self, product):
        # print(isinstance(product.name, str), isinstance(product.count, str), isinstance(product.price, str))
        _e = ValidationException("Validation failed", dict())
        if not re.match(rus.PRODUCT_REGX["name"], product.name):
            if (len(product.name) > 30):
                _e.get_dict()["name"] = ConstraintErrorType.TOO_LONG 
            else:
                _e.get_dict()["name"] = ConstraintErrorType.INCORRECT_VALUE
        if not re.match(rus.PRODUCT_REGX["count"], str(product.count)):
            _e.get_dict()["count"] = ConstraintErrorType.INCORRECT_VALUE
        if not re.match(rus.PRODUCT_REGX["price"], str(product.price)):
            _e.get_dict()["price"] = ConstraintErrorType.INCORRECT_VALUE
        if _e.get_dict() != dict():
            raise _e
        try:
            self.database.add_row("products", self._products_sig,
                                  [product.name, product.count, product.price])
        except DbException as e:
            raise e

    def update(self, table_name, column_name, id, value):
        self.database.update(table_name, column_name, id, value)

    def delete_from(self, table_name, id_list):
        self.database.delete(table_name, id_list)

    def to_cart(self, prod_list):
        self.order.to_cart(prod_list)
        self.database.reserve("products", [[x.id, 1] for x in prod_list])
        self.ui_display_order()

    def remove_from_cart(self, prod_list):
        self.order.remove_from_cart(prod_list)
        self.database.unreserve("products",
                                [[x.id, x.count] for x in prod_list])
        self.ui_display_order()

    def place_order(self):
        _now = datetime.now()
        deal_id = self.database.add_row("deals", self._deals_sig,
                                        [self.order.get_customer().id, _now])
        self.database.unreserve("products", [[x.id, x.count] for x in
                                             self.order.get_cart()])
        self.database.decrease("products", [[x.id, x.count] for x in
                                            self.order.get_cart()])
        self._check_creator.write_chck("data/checks/{}.txt".format(deal_id),
                                       self.order, _now)
        self.order = Order()
        self.ui_display_order()

    def clear_order(self):
        if self.database is None:
            self.ui_display_order()
            return
        self.database.unreserve("products", [[x.id, x.count] for x in
                                             self.order.get_cart()])
        self.order = Order()
        self.ui_display_order()

    def get_order(self):
        return self.order.get_cart()

    def get_from(self, table_name):
        if self.database is None:
            return list()
        return self.database.select_all(table_name)

    def set_customer(self, customer):
        self.order.set_customer(customer)

    def add_customer(self, customer):
        _e = ValidationException("Validation failed", dict())
        if not re.match(rus.CUSTOMER_REGX["name"], customer.name):
            if (len(product.name) > 30):
                _e.get_dict()["name"] = ConstraintErrorType.TOO_LONG 
            else:
                _e.get_dict()["name"] = ConstraintErrorType.INCORRECT_VALUE
        if not re.match(rus.CUSTOMER_REGX["surname"], customer.surname):
            if (len(product.name) > 30):
                _e.get_dict()["surname"] = ConstraintErrorType.TOO_LONG 
            else:
                _e.get_dict()["surname"] = ConstraintErrorType.INCORRECT_VALUE
        if not re.match(rus.CUSTOMER_REGX["phone"], str(customer.phone)):
            _e.get_dict()["phone"] = ConstraintErrorType.INCORRECT_VALUE
        if not re.match(rus.CUSTOMER_REGX["address"], str(product.address)):
            if (len(product.address) > 300):
                _e.get_dict()["address"] = ConstraintErrorType.TOO_LONG 
            else:
                _e.get_dict()["address"] = ConstraintErrorType.INCORRECT_VALUE
        if _e.get_dict() != dict():
            raise _e
        try:
            ret_id = self.database.add_row("customers", self._customers_sig,
                                           [customer.surname, customer.name,
                                            customer.phone, customer.address])
            customer.id = ret_id
        except DbException as e:
            arr = e.message.split()
            if arr[0] == 'CHECK':
                raise ConstraintException(
                    e.message, (arr[-1])[4:], ConstraintErrorType.TOO_LONG)
            else:
                raise e

    def ui_display_products(self):
        pass

    def ui_display_order(self):
        pass

    def close_connection(self):
        self.clear_order()
        if self.database is not None:
            self.database.close_connection()
