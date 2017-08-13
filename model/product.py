class Product:

    def __init__(self, from_db):
        self.product_id = from_db[0]
        self.name = from_db[1]
        self.count = from_db[2]
        self.price = from_db[3]
<<<<<<< HEAD
        self.reserve = from_db[4]

    def __str__(self):
    	return """	Id: {}
    	name: {}
    	count: {}
    	price: {}
		reserve: {}""".format(
    		     	self.id,
    		     	self.name,
    		     	self.count,
    		     	self.price,
    		     	self.reserve)
=======
        self.reserved = from_db[4]
>>>>>>> dev
