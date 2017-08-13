import db
from gui.locale import rus as locale

products = db.Table('products')
products.add_column(db.Column('product_id', locale.ID, 1,
                              'INTEGER PRIMARY KEY AUTOINCREMENT'))
products.add_column(db.Column('name', locale.PRODUCT_NAME, 5,
                              'VARCHAR(100) UNIQUE NUT NULL'))
products.add_column(db.Column('count', locale.COUNT, 2,
                              'INT NOT NULL CHECK (count >= 0)'))
products.add_column(db.Column('price', locale.PRICE, 2,
                              'INT CHECK (price >= 0)'))
products.add_column(db.Column('reserved', locale.RESERVED, 3,
                              'INT DEFAULT 0 CHECK (reserved >= 0)'))

customers = db.Table('customers')
customers.add_column(db.Column('customer_id', locale.ID, 1,
                               'INTEGER PRIMARY KEY AUTOINCREMENT'))
customers.add_column(db.Column('surname', locale.SURNAME, 5,
                               'VARCHAR(100) NOT NULL'))
customers.add_column(db.Column('name', locale.CUSTOMER_NAME, 5,
                               'VARCHAR(100) NOT NULL'))
customers.add_column(db.Column('adress', locale.ADRESS, 5,
                               'VARCHAR(200) NOT NULL'))
customers.add_column(db.Column('phone', locale.PHONE, 4,
                               'INT'))
customers.add_column(db.Column('all_sum', locale.ALL_SUM, 3,
                               'INT DEFAULT 0 CHECK (all_sum >= 0)'))

deals = db.Table('deals')
deals.add_column(db.Column('deal_id', locale.ID, 1,
                           'INTEGER PRIMARY KEY AUTOINCREMENT'))
deals.add_column(db.Column('customer_id', locale.CUSTOMER_ID, 2,
                           'INTEGER FOREIGN KEY customers'))
deals.add_column(db.Column('products', locale.BUYS, 6,
                           'some sort of array '))  # TODO: find array
deals.add_column(db.Column('dttm', locale.DTTM, 3,
                           'dttm'))  # TODO: fix date

storage = db.Database('storage')
storage.add_table(products)
storage.add_table(customers)
storage.add_table(deals)

order = db.Table('order')
order.add_column(db.Column('product_id', locale.ID, 1, ''))
order.add_column(db.Column('name', locale.PRODUCT_NAME, 5, ''))
order.add_column(db.Column('price', locale.PRICE, 2, ''))
order.add_column(db.Column('count', locale.COUNT, 2, ''))
