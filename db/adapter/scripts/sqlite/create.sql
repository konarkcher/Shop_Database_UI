CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text UNIQUE check(name is not null and length(name) <= 30),
    count INT check(count >= 0), 
    price INT check(price >= 0), 
    reserved INT DEFAULT 0 check(reserved >= 0 and reserved <= count)
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname text check(surname is not null or length(surname) <= 30), 
    name text check(name is not null or length(name) <= 30), 
    phone text check(phone is not null or length(phone) <= 30), 
    address text check(address is not null or length(address) <= 300)
);

CREATE TABLE deals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER, 
    dttm timestamp,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE INDEX products_ind ON products (name);

CREATE INDEX customers_ind ON customers (id);

CREATE INDEX deals_ind ON customers (id);