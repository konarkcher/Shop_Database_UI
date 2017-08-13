class Order:

    def __init__(self):
        self._cart = list()  # list of Product's
        self.customer_id = None
        self.sum = 0

    def to_cart(self, products):  # products = additional list of Product
        for p in products:
            for elem in self._cart:
                if elem.product_id == p.product_id:
                    elem.count += p.count
                    break
            self._cart.append(p)


    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_cart(self):
        if not self._cart:
            return []
        else:
            return self._cart

    def remove_from_cart(self, products):
        st = set([x.product_id for x in products])
        self._cart = [x for x in self._cart if x.product_id not in st]
