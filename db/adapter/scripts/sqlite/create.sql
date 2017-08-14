CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE,
    count INT, 
    price INT, 
    reserved INT DEFAULT 0
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname VARCHAR(30), 
    name VARCHAR(30), 
    phone VARCHAR(30), 
    address VARCHAR(200)
);

CREATE TABLE deals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id VARCHAR(30), 
    dttm DATETIME,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE INDEX products_ind ON products (name);

CREATE INDEX customers_ind ON customers (id);

CREATE INDEX deals_ind ON customers (id);