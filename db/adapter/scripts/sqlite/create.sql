CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    count INT, 
    price INT check(price >= 0), 
    reserved INT DEFAULT 0,
    CONSTRAINT chk_name_unq UNIQUE (name),
    CONSTRAINT chk_name_len check(name is not null and length(name) <= 50),
    CONSTRAINT chk_count_cor check(count >= 0),
    CONSTRAINT chk_price_cor check(price >= 0),
    CONSTRAINT chk_reserved_cor check(reserved >= 0 and reserved <= count)
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname text, 
    name text , 
    phone text, 
    address text,
    CONSTRAINT chk_surname check(surname is not null and length(surname) <= 30),
    CONSTRAINT chk_name check(name is not null and length(name) <= 30),
    CONSTRAINT chk_phone  check(phone is not null and length(phone) <= 30),
    CONSTRAINT chk_address check(address is not null and length(address) <= 300)
);

CREATE TABLE deals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER, 
    dttm timestamp,
    CONSTRAINT chk_customer_frk FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE INDEX products_ind ON products (name);

CREATE INDEX customers_ind ON customers (id);

CREATE INDEX deals_ind ON customers (id);