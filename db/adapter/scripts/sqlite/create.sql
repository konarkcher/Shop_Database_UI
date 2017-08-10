CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100), 
    count INT, price INT, 
    reserved INT DEFAULT 0
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(30), 
    second_name VARCHAR(30), 
    telephone VARCHAR(30), 
    address VARCHAR(200)
);

CREATE TABLE deals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id VARCHAR(30), 
    deals_dttm DATETIME,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE UNIQUE INDEX products_ind ON products (id);

CREATE UNIQUE INDEX customers_ind ON customers (id);