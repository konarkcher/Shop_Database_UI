class Order:
    def __init__(self):
        self._cart = dict()
        self._customer = None
        self._sum = 0

    def to_cart(self, products):
        for p in products:
            if p.id in self._cart:
                self._cart[p.id].count += 1
            else:
                p.count = 1
                self._cart[p.id] = p
        self._sum = sum([x.price * x.count for x in self._cart.values()])

    def set_customer(self, customer):
        self._customer = customer

    def get_cart(self):
        return list(self._cart.values())

    def remove_from_cart(self, products):
        st = set([x.id for x in products])
        self._cart = dict(
            [(x.id, x) for x in self._cart.values() if x.id not in st])
        self._sum = sum([x.price * x.count for x in self._cart.values()])

    def get_initials(self):
        return self._customer.get_initials()

    def get_customer(self):
        return self._customer

    def get_sum(self):
        return self._sum
