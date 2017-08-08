class Order:

    def __init__(self):
        self._cart = list()  # list of Products
        self.customer = None  # id
        self.sum = 0

    def to_cart(self, products):  # products = additional list of Product
        self._cart += products

    def set_customer(self, customer_id):
        self.customer = customer_id

    def get_cart(self):
        if not self._cart:
            return []
        else:
            return self._cart

    def remove_from_cart(self, products_id):
        st = set(products_id)
        self._cart = [x for x in self._cart if x not in st]
