from . import Order


class Shop:
    def __init__(self):
        self.database = None
        self.order = Order()

    def create_sqlite_db(self, path):
        pass

    def open_sqlite_db(self, path):
        pass

    def add_product(self, product):
        pass

    def delete_product(self, id_list):
        pass

    def to_cart(self, id_list):
        pass

    def remove_from_cart(self, id_list):
        pass

    def place_order(self):
        pass

    def clear_order(self):
        self.order = Order()

    def get_order(self):  # все get - получение list для таблицы
        pass

    def get_products(self):
        pass

    def get_customers(self):
        pass

    def set_customer(self, id):
        pass

    def add_customer(self):
        pass

    def delete_customer(self, id_list):
        pass

    def close_connection(self):  # некие действия перед выключением программ
        pass
