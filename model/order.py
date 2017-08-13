class Order:

    def __init__(self):
        self._cart = list()  # list of Products
        self.customer = None  # id
        self.sum = 0

    def to_cart(self, products):  # products = additional list of Product
        for p in products:
            for elem in self._cart:
                if elem.id == p.id:
                    elem.count += p.count
                    break
            self._cart.append(p)


    def set_customer(self, customer_id):
        self.customer = customer_id

    def get_cart(self):
        if not self._cart:
            return []
        else:
            return self._cart

    def remove_from_cart(self, products):
        st = set([x.id for x in products])
        self._cart = [x for x in self._cart if x.id not in st]
