class Product:

    def __init__(self, from_db):  # есть чувство, что это можно написать лучше
        self.id = from_db[0]
        self.name = from_db[1]
        self.count = from_db[2]
        self.price = from_db[3]
        self.reserve = from_db[4]