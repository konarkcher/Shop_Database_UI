import model

shop = model.Shop()


#try:
shop.create_db("data/model_test.db", model.Db().SQLITE)	
# except Exception as e:
# 	shop.open_db("data/model_test.db")

products = [[1, "cookie", 42, 1, 0],
            [1, "milk", 15, 2, 0],
            [1, "potatoes", 11, 3, 0],
            [1, "vodka", 11, 4, 0]
            ]

for prod in products:
    shop.add_product(model.Product(prod))

shop.add_customer(model.Customer([0,
                                 "Vasya",
                                 "Pupkin",
                                 "8-800-555-35-35",
                                 "NY, Wall Stret 17, 32 floor"]))


print(shop.get_products())

print(shop.get_order())

shop.to_cart([1, 2, 3])

print(shop.get_order())

shop.remove_from_cart([2])

print(shop.get_order())

shop.to_cart([4])

print(shop.get_order())

shop.remove_from_cart([1,2])



print("=================Customers===============")

print(shop.get_customers())

print("=================Products================")

print(shop.get_products())
