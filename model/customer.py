class Customer:

    def __init__(self, from_db):
        self.id = from_db[0]
        self.name = from_db[1]
        self.surname = from_db[2]
        self.telephone = from_db[3]
        self.address = from_db[4]
