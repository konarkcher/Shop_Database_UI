import model
from db import exception

shop = model.Shop()

try:
    shop.create_db("data/model_test.db", model.DbType.SQLITE)
except Exception as e:
    shop.open_db("data/model_test.db", model.DbType.SQLITE)

products = [[1, "cookie", 42, 1, 0],
            [2, "milk", 15, 2, 0],
            [3, "potatoes", 11, 3, 0],
            [4, "vodka", 11, 4, 0]
            ]

prodP = []

for prod in products:
    shop.add_product(model.Product(prod))
    prodP.append(model.Product(prod))


customer = model.Customer([0,
                           "Vasya",
                           "Pupkin",
                           "8-800-555-35-35",
                           "NY, Wall Stret 17, 32 floor"])
shop.add_customer(customer)


print(list(shop.get_from("products")))


for p in prodP:
	p.count = 1

shop.to_cart(prodP)

print("=================Products================")

print(list(shop.get_from("products")))

shop.remove_from_cart([prodP[3]])


print("============Products {removed last}=======")

print(list(shop.get_from("products")))


shop.clear_order()

# print(shop.get_order())

# shop.to_cart([1, 2, 3])

# print(shop.get_order())

# shop.remove_from_cart([2])

# print(shop.get_order())

# shop.to_cart([4])

# print(shop.get_order())

# shop.remove_from_cart([1, 2])


print("=================Customers===============")

print(list(shop.get_from("customers")))

print("=================Products================")

print(list(shop.get_from("products")))
